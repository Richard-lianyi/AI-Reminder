@echo off
echo Stopping all services...

:: 关闭 uvicorn (8000端口)
for /f "tokens=5" %%a in ('netstat -ano ^| findstr :8000') do taskkill /PID %%a /F

:: 关闭前端服务器 (5500端口)
for /f "tokens=5" %%a in ('netstat -ano ^| findstr :5500') do taskkill /PID %%a /F

:: 关闭 checker（通过 python 进程名，简单粗暴）
taskkill /IM python.exe /F

echo All services stopped!
pause