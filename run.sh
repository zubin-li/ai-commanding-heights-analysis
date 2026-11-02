#!/bin/bash
# AI Commanding Heights Strategic Deck Launcher
set -e

cd "$(dirname "$0")"

echo "=========================================================="
echo " 🌐 AI 时代制高点之战：战略分析与实证核查平台"
echo "=========================================================="
PY_BIN="python3"
if [ -x "/opt/homebrew/bin/python3" ]; then
  PY_BIN="/opt/homebrew/bin/python3"
fi

echo "1. 检查 Python 运行环境..."
$PY_BIN --version

echo "2. 校验并重新构建离线数据接口与测试用例..."
$PY_BIN scripts/build_data_assets.py
$PY_BIN tests/validate_project.py

echo "3. 启动本地交互式 Web 研报服务并在浏览器中打开..."
open "http://localhost:8080" 2>/dev/null || open "./index.html" 2>/dev/null || true
$PY_BIN server.py
