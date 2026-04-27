@echo off
echo ========================================
echo   个人主页应用启动器 - solitudo1
echo ========================================
echo.
echo 正在启动 Flask 应用...
echo.
echo 访问地址: http://127.0.0.1:5000
echo.
echo 按 Ctrl+C 停止服务器
echo.

cd /d "%~dp0"
python app.py

pause
