#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYVER="${PYVER:-$(python3 -c 'import sys; print("%d.%d" % sys.version_info[:2])')}"
OUT="${OUT:-$ROOT/dist/components}"
PTR="$(python3 -c 'import struct; print(struct.calcsize("P"))')"

mkdir -p "$OUT"

echo ">> building 32-bit pyopenmp_native.so against Python $PYVER"
if [ "$PTR" = "4" ]; then
  CFLAGS="$(python3-config --includes)"
  LDFLAGS="$(python3-config --ldflags --embed 2>/dev/null || python3-config --ldflags)"
  gcc -m32 -shared -fPIC -Wall $CFLAGS \
    "$ROOT/native/pyopenmp.c" \
    $LDFLAGS \
    -o "$OUT/pyopenmp_native.so"
else
  gcc -m32 -shared -fPIC -Wall \
    -I"/usr/include/python${PYVER}" \
    "$ROOT/native/pyopenmp.c" \
    -L/usr/lib -lpython"${PYVER}" \
    -o "$OUT/pyopenmp_native.so"
fi

echo ">> built $OUT/pyopenmp_native.so"
file "$OUT/pyopenmp_native.so" || true
