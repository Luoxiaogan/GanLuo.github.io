#!/bin/bash
# 一键构建 Jekyll 主页 + Astro 博客（含 wiki），产物合并到 _site/（结构与 GitHub Actions 部署一致）
set -e

export PATH="/opt/homebrew/opt/ruby@3.1/bin:$PATH"
export SDKROOT="/Library/Developer/CommandLineTools/SDKs/MacOSX26.sdk"
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8

cd "$(dirname "$0")"

echo "==> Building Jekyll homepage..."
bundle exec jekyll build

echo "==> Building Astro blog..."
(cd blog && bun run build)

echo "==> Merging blog output into _site/blog ..."
mkdir -p _site/blog
cp -r blog/dist/* _site/blog/

echo "==> Done. Output in ./_site"
