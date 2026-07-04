import traceback

_handlers = {}


def register(event_name, handler):
    _handlers.setdefault(event_name, []).append(handler)
    return handler


def decorator(event_name):
    def deco(handler):
        return register(event_name, handler)

    return deco


def dispatch(event_name, args, default):
    result = default
    for handler in _handlers.get(event_name, ()):
        try:
            value = handler(*args)
        except Exception:
            traceback.print_exc()
            continue
        if value is not None:
            result = value
    return result
