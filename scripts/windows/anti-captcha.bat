@echo off

set hostsFile=%SYSTEMROOT%\System32\drivers\etc\hosts
set myServer=bcsapi.com
set toRedirect=api.anti-captcha.com

rem -------------------------
rem BestCaptchaSolver captcha gate
rem -------------------------
rem %toRedirect%
rem -------------------------
setlocal EnableDelayedExpansion

if not "%1"=="am_admin" (powershell start -verb runas '%0' am_admin & exit)

echo [+] BestCaptchaSolver captcha gate (hostsfile editor)
echo [+] --------------------------------------------
echo [+] %toRedirect% gate

for /f "tokens=1,2 delims=[]" %%a IN ('ping -n 1 !myServer!') DO (
 if "%%b" NEQ "" set ip=%%b
)
echo [+] IP address %ip%
echo.>>%hostsFile%
echo #bestcaptchasolver gate>>%hostsFile%
echo !ip! %toRedirect%>>%hostsFile%
echo [+] Appended to hosts file: !hostsFile!
echo [+] Check page and make sure you get the message: Captcha gate enabled ^^!
echo [+] --------------------------------------------------------------------------------
timeout /t 10
start "" http://%toRedirect%
pause