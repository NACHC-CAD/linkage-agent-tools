@echo off
echo.
echo.
echo ------
echo Checked out from:
git config --get remote.origin.url
echo.
echo Branch:
git rev-parse --abbrev-ref HEAD
echo ------
echo.
echo.
echo Done.
echo.
echo.


