# 个人主页应用启动器 - solitudo1
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  个人主页应用启动器 - solitudo1" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "正在启动 Flask 应用..." -ForegroundColor Green
Write-Host ""
Write-Host "访问地址: http://127.0.0.1:5000" -ForegroundColor Yellow
Write-Host ""
Write-Host "按 Ctrl+C 停止服务器" -ForegroundColor Red
Write-Host ""

Set-Location $PSScriptRoot
python app.py
