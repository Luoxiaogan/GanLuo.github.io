#!/bin/bash
# 一键构建 + 在本地浏览器可打开的方式预览（主页 + 博客（含 wiki）合并后的完整站点）
set -e

cd "$(dirname "$0")"

./build_all.sh

PORT="${1:-8000}"
PREVIEW_DIR="$(mktemp -d)"
ln -sf "$(pwd)/_site" "$PREVIEW_DIR/GanLuo.github.io"

URL="http://127.0.0.1:${PORT}/GanLuo.github.io/"
echo ""
echo "==> Serving at $URL  (Ctrl-C to stop)"

if command -v open >/dev/null 2>&1; then
  ( sleep 1; open "$URL" ) &
fi

cd "$PREVIEW_DIR"
python3 -m http.server "$PORT"
