#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYVER="${PYVER:-$(python3 -c 'import sys; print("%d.%d" % sys.version_info[:2])')}"
OUT="${OUT:-$ROOT/dist/components}"

mkdir -p "$OUT"

echo ">> building 32-bit pyopenmp_native.so against Python $PYVER"
gcc -m32 -shared -fPIC -Wall \
  -I"/usr/include/python${PYVER}" \
  "$ROOT/native/pyopenmp.c" \
  -L/usr/lib -lpython"${PYVER}" \
  -o "$OUT/pyopenmp_native.so"

echo ">> built $OUT/pyopenmp_native.so"
file "$OUT/pyopenmp_native.so"
