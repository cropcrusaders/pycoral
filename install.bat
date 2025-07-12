@echo off
echo ================================================================
echo                PyCoral Easy Pip Install
echo ================================================================
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.9+ and try again
    pause
    exit /b 1
)

echo Python found: 
python --version

echo.
echo Starting installation...
echo.

REM Run the Python installation script
python install.py

if errorlevel 1 (
    echo.
    echo ================================================================
    echo                   INSTALLATION FAILED
    echo ================================================================
    echo.
    echo Troubleshooting:
    echo 1. Make sure you're running this from the PyCoral root directory
    echo 2. Check that you have Python 3.9 or newer
    echo 3. Ensure you have internet connection
    echo 4. Try running as administrator if you get permission errors
    echo.
    pause
    exit /b 1
) else (
    echo.
    echo ================================================================
    echo                 INSTALLATION SUCCESSFUL!
    echo ================================================================
    echo.
    echo You can now use PyCoral:
    echo   python -c "import pycoral; print('Version:', pycoral.__version__)"
    echo.
    echo To run examples:
    echo   cd examples
    echo   python classify_image.py --help
    echo.
)

pause
