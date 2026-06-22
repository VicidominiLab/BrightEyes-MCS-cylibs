@echo off
setlocal
cd /d "%~dp0"

if not exist .venv\Scripts\python.exe (
    python -m venv .venv
    if errorlevel 1 goto :error
)

call .venv\Scripts\activate.bat
if errorlevel 1 goto :error

python -m pip install --upgrade pip setuptools wheel build Cython numpy pytest
if errorlevel 1 goto :error

python setup.py build_ext --inplace
if errorlevel 1 goto :error

python -m pip install -e .
if errorlevel 1 goto :error

python -m pytest tests
if errorlevel 1 goto :error

python -m build --wheel
if errorlevel 1 goto :error

echo.
echo Build completed. Wheel files are in the dist folder.
exit /b 0

:error
echo.
echo Build failed.
exit /b 1
