import json
import keyword
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
APIDOCS = ROOT / "third_party" / "open.mp-capi" / "apidocs"
OUT = ROOT / "pyopenmp" / "generated"

ENTITY_GROUPS = {
    "Actor": "Actor",
    "Player": "Player",
    "Vehicle": "Vehicle",
    "Object": "Object",
    "Pickup": "Pickup",
    "GangZone": "GangZone",
    "Menu": "Menu",
    "TextDraw": "TextDraw",
    "TextLabel": "TextLabel",
    "NPC": "Npc",
    "Class": "Class",
}

SKIP_GROUPS = {"Component", "Event"}

VOID_PARAM_CLASS = {
    "player": "Player",
    "targetplayer": "Player",
    "forplayer": "Player",
    "issuer": "Player",
    "killer": "Player",
    "damager": "Player",
    "vehicle": "Vehicle",
    "targetvehicle": "Vehicle",
    "actor": "Actor",
    "targetactor": "Actor",
    "object": "Object",
    "targetobject": "Object",
    "pickup": "Pickup",
    "gangzone": "GangZone",
    "menu": "Menu",
    "textdraw": "TextDraw",
    "textlabel": "TextLabel",
    "npc": "Npc",
    "class": "Class",
}

SCALARS = {
    "int": "c_int",
    "uint8_t": "c_uint8",
    "uint16_t": "c_uint16",
    "uint32_t": "c_uint32",
    "uint64_t": "c_uint64",
    "float": "c_float",
    "bool": "c_bool",
}


def snake(name):
    out = []
    chars = list(name)
    for i, c in enumerate(chars):
        if c.isupper():
            prev = chars[i - 1] if i > 0 else ""
            nxt = chars[i + 1] if i + 1 < len(chars) else ""
            boundary = False
            if prev:
                if prev.islower() or prev.isdigit():
                    boundary = True
                elif prev.isupper() and nxt and nxt.islower():
                    boundary = True
            if boundary:
                out.append("_")
            out.append(c.lower())
        else:
            out.append(c)
    return "".join(out)


def sanitize(name):
    if keyword.iskeyword(name) or name in ("None", "True", "False"):
        return name + "_"
    return name


def is_out(ty):
    return ty.endswith("*") and ty not in ("void*", "const char*")


def ctype_of(ty):
    base = ty.rstrip("*").strip()
    return "ctypes." + SCALARS[base]


def argtype_expr(ty):
    if ty == "void*":
        return "ctypes.c_void_p"
    if ty == "const char*":
        return "ctypes.c_char_p"
    if ty == "CAPIStringView*":
        return "ctypes.POINTER(_capi.CAPIStringView)"
    if ty == "CAPIStringBuffer*":
        return "ctypes.POINTER(_capi.CAPIStringBuffer)"
    if is_out(ty):
        return "ctypes.POINTER(%s)" % ctype_of(ty)
    return ctype_of(ty)


def restype_expr(ret):
    if ret == "void*":
        return "ctypes.c_void_p"
    return ctype_of(ret)


def method_field(group, fname):
    prefix = group + "_"
    return fname[len(prefix):] if fname.startswith(prefix) else fname


def emit_native(func):
    name = snake(func["name"])
    params = func["params"]
    ret = func["ret"]

    argtypes = [argtype_expr(p["type"]) for p in params]
    sig = []
    pre = []
    call = []
    outs = []

    for p in params:
        rn = sanitize(snake(p["name"]))
        ty = p["type"]
        if is_out(ty):
            if ty == "CAPIStringView*":
                pre.append("%s = _capi.CAPIStringView()" % rn)
                call.append("ctypes.byref(%s)" % rn)
                outs.append(("_capi.read_view(%s)" % rn, True))
            elif ty == "CAPIStringBuffer*":
                pre.append("%s = _capi.OutBuffer()" % rn)
                call.append("ctypes.byref(%s.raw)" % rn)
                outs.append(("%s.value()" % rn, True))
            else:
                pre.append("%s = %s()" % (rn, ctype_of(ty)))
                call.append("ctypes.byref(%s)" % rn)
                outs.append(("%s.value" % rn, False))
        elif ty == "const char*":
            sig.append(rn)
            call.append("_capi.enc(%s)" % rn)
        else:
            sig.append(rn)
            call.append(rn)

    lines = []
    lines.append("import ctypes")
    lines.append("")
    lines.append("from pyopenmp import _capi")
    lines.append("")
    lines.append(
        '_fn = _capi.lazy("%s", %s, [%s])'
        % (func["name"], restype_expr(ret), ", ".join(argtypes))
    )
    lines.append("")
    lines.append("")
    lines.append("def %s(%s):" % (name, ", ".join(sig)))
    for stmt in pre:
        lines.append("    " + stmt)

    call_expr = "_fn(%s)" % ", ".join(call)
    if not outs:
        lines.append("    return " + call_expr)
    else:
        lines.append("    __ret = " + call_expr)
        values = [e for (e, _) in outs]
        tuple_expr = values[0] if len(values) == 1 else "(" + ", ".join(values) + ")"
        if ret == "bool":
            lines.append("    if __ret:")
            lines.append("        return " + tuple_expr)
            lines.append("    return None")
        elif ret in ("int", "uint8_t", "uint16_t", "uint32_t", "uint64_t") and all(
            s for (_, s) in outs
        ):
            lines.append("    return " + tuple_expr)
        else:
            lines.append("    return (" + ", ".join(["__ret"] + values) + ")")

    signature = "%s(%s)" % (name, ", ".join(sig))
    return name, "\n".join(lines) + "\n", signature


def emit_entity_method(group, func):
    params = func["params"]
    has_self = bool(params) and params[0]["type"] == "void*"
    native = snake(func["name"])
    py_name = sanitize(snake(method_field(group, func["name"])))

    inputs = [p for p in params if not is_out(p["type"])]
    input_names = [sanitize(snake(p["name"])) for p in inputs]

    lines = []
    if has_self:
        rest = input_names[1:]
        lines.append("    def %s(%s):" % (py_name, ", ".join(["self"] + rest)))
        args = ["self.ptr"] + rest
        lines.append("        return natives.%s(%s)" % (native, ", ".join(args)))
    else:
        lines.append("    @classmethod")
        lines.append("    def %s(%s):" % (py_name, ", ".join(["cls"] + input_names)))
        wrap = py_name in ("create", "from_id") and func["ret"] == "void*"
        if wrap:
            lines.append(
                "        result = natives.%s(%s)" % (native, ", ".join(input_names))
            )
            lines.append(
                "        ptr = result[0] if isinstance(result, tuple) else result"
            )
            lines.append("        return cls(ptr) if ptr else None")
        else:
            lines.append(
                "        return natives.%s(%s)" % (native, ", ".join(input_names))
            )
    return py_name, "\n".join(lines) + "\n"


def event_arg(ty, name):
    if ty == "void*":
        cls = VOID_PARAM_CLASS.get(name.lower())
        return ("entities.%s(_capi.deref_handle(list_, %%d))" % cls) if cls else "_capi.deref_handle(list_, %d)"
    if ty == "int":
        return "_capi.deref_int(list_, %d)"
    if ty == "float":
        return "_capi.deref_float(list_, %d)"
    if ty == "bool":
        return "_capi.deref_bool(list_, %d)"
    if ty == "CAPIStringView":
        return "_capi.deref_view(list_, %d)"
    raise SystemExit("unmapped event arg type: " + ty)


def clean_dir(path):
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True)


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)


def main():
    api = json.loads((APIDOCS / "api.json").read_text())
    events = json.loads((APIDOCS / "events.json").read_text())

    clean_dir(OUT)
    (OUT / "__init__.py").write_text("")

    natives_dir = OUT / "natives"
    natives_dir.mkdir()

    md_api = []
    top_imports = []
    fn_count = 0

    for group in sorted(api):
        if group in SKIP_GROUPS:
            continue
        funcs = sorted(api[group], key=lambda f: f["name"])
        mod = sanitize(snake(group))
        group_dir = natives_dir / mod
        group_dir.mkdir()
        names = []
        md_fns = []
        for func in funcs:
            name, code, signature = emit_native(func)
            write(group_dir / ("%s.py" % name), code)
            names.append(name)
            fn_count += 1
            md_fns.append("`%s`: `%s`" % (func["name"], signature))
        init = "".join("from .%s import %s\n" % (n, n) for n in names)
        init += "\n__all__ = [%s]\n" % ", ".join('"%s"' % n for n in names)
        write(group_dir / "__init__.py", init)
        top_imports.append("from .%s import *" % mod)
        md_api.append((group, md_fns))

    write(natives_dir / "__init__.py", "\n".join(top_imports) + "\n")

    emit_entities(api)
    md_events = emit_events(events)
    write_generated_md(md_api, md_events, fn_count)

    print("generated %d functions and %d events" % (fn_count, len(md_events)))


def emit_entities(api):
    lines = ["from pyopenmp.generated import natives", "", ""]
    class_names = []
    for group in ENTITY_GROUPS:
        cls = ENTITY_GROUPS[group]
        class_names.append(cls)
        lines.append("class %s:" % cls)
        lines.append("    def __init__(self, ptr):")
        lines.append("        self.ptr = ptr")
        lines.append("")
        funcs = sorted(api.get(group, []), key=lambda f: f["name"])
        for func in funcs:
            _, code = emit_entity_method(group, func)
            lines.append(code)
        lines.append("")
    lines.append("__all__ = [%s]" % ", ".join('"%s"' % c for c in class_names))
    write(OUT / "entities.py", "\n".join(lines) + "\n")


def emit_events(events):
    all_events = []
    for group in events:
        all_events.extend(events[group])
    all_events.sort(key=lambda e: e["name"])

    lines = [
        "import ctypes",
        "",
        "from pyopenmp import _capi",
        "from pyopenmp import event",
        "from pyopenmp.generated import entities",
        "",
        "_EVENT_CB = ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.POINTER(_capi.EventArgs_Common))",
        "_trampolines = []",
        "",
        "",
    ]

    table = []
    decorators = []
    md = []

    for ev in all_events:
        name = ev["name"]
        method = snake(name)
        tramp = "_tramp_%s" % method
        badret = ev["badret"]
        default = {"none": "True", "true": "False", "false": "True"}[badret]

        decode = []
        call_args = []
        for i, arg in enumerate(ev["args"]):
            expr = event_arg(arg["type"], arg["name"]) % i
            rn = sanitize(snake(arg["name"]))
            decode.append("    %s = %s" % (rn, expr))
            call_args.append(rn)

        lines.append("def %s(args):" % tramp)
        lines.append("    list_ = args.contents.list")
        lines.extend(decode)
        lines.append(
            '    return event.dispatch("%s", (%s), %s)'
            % (name, ", ".join(call_args) + ("," if len(call_args) == 1 else ""), default)
        )
        lines.append("")
        lines.append("")

        decorators.append('%s = event.decorator("%s")' % (method, name))
        table.append('    ("%s", %s),' % (name, tramp))
        md.append((name, "%s%s" % (method, _md_event_sig(ev, badret))))

    lines.append("_TABLE = [")
    lines.extend(table)
    lines.append("]")
    lines.append("")
    lines.append("")
    lines.extend(decorators)
    lines.append("")
    lines.append("")
    lines.append("def register_all():")
    lines.append("    lib = _capi.load()")
    lines.append("    add = lib.Event_AddHandler")
    lines.append("    add.restype = ctypes.c_bool")
    lines.append(
        "    add.argtypes = [ctypes.c_char_p, ctypes.c_int, ctypes.c_void_p]"
    )
    lines.append("    _trampolines.clear()")
    lines.append("    for name, func in _TABLE:")
    lines.append("        cb = _EVENT_CB(func)")
    lines.append("        _trampolines.append(cb)")
    lines.append(
        "        add(name.encode(), _capi.EVENT_PRIORITY_DEFAULT, ctypes.cast(cb, ctypes.c_void_p))"
    )
    lines.append("")
    lines.append(
        "__all__ = [%s]"
        % ", ".join(['"register_all"'] + ['"%s"' % snake(e["name"]) for e in all_events])
    )
    write(OUT / "events.py", "\n".join(lines) + "\n")
    return md


def _md_event_sig(ev, badret):
    args = ", ".join(sanitize(snake(a["name"])) for a in ev["args"])
    ret = " -> bool" if badret != "none" else ""
    return "(%s)%s" % (args, ret)


def write_generated_md(md_api, md_events, fn_count):
    lines = ["# Generated bindings", ""]
    lines.append("Produced by `python tools/codegen.py`.")
    lines.append("")
    lines.append(
        "**Totals:** %d functions across %d groups, %d events."
        % (fn_count, len(md_api), len(md_events))
    )
    lines.append("")
    lines.append("## Functions")
    lines.append("")
    for group, fns in sorted(md_api):
        lines.append("### %s (%d)" % (group, len(fns)))
        lines.append("")
        for f in fns:
            lines.append("- " + f)
        lines.append("")
    lines.append("## Events")
    lines.append("")
    for name, sig in md_events:
        lines.append("- `%s`: `%s`" % (name, sig))
    lines.append("")
    write(ROOT / "GENERATED.md", "\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
