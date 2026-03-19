@echo off
echo Starting AI Reminder System...

:: 启动 FastAPI
start cmd /k "cd /d %~dp0 && py -m uvicorn main:app --reload"

:: 启动 Reminder Checker
start cmd /k "cd /d %~dp0 && py reminder_checker.py"

:: 启动前端服务器
start cmd /k "cd /d %~dp0 && py -m http.server 5500"

echo All services started!
pause