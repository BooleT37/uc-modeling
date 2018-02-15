@echo off
call :check_Permissions

cd %~dp0
jupyter notebook


:check_Permissions
    net session >nul 2>&1
    if not %errorLevel% == 0 (
        echo You need to run this script with administrative rights
        pause
        exit
    )