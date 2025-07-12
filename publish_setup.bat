@echo off
echo ================================================================
echo           PyCoral Repository Publishing Setup
echo ================================================================
echo.

echo Checking repository status...
git status

echo.
echo Building and testing package...
python prepare_pypi.py

if errorlevel 1 (
    echo.
    echo ================================================================
    echo                    PREPARATION FAILED
    echo ================================================================
    echo Please fix the errors above and try again.
    pause
    exit /b 1
)

echo.
echo ================================================================
echo                  REPOSITORY READY!
echo ================================================================
echo.
echo Your PyCoral repository is now ready for users to install with:
echo.
echo   pip install git+https://github.com/cropcrusaders/pycoral.git
echo.
echo To publish to PyPI (optional):
echo   1. Create account at https://pypi.org
echo   2. Run: twine upload dist/*
echo.
echo Don't forget to:
echo   1. Create a GitHub release/tag (e.g., v2.1.0)
echo   2. Create a GitHub release/tag (e.g., v2.1.0)
echo   3. Push your changes to GitHub
echo.
pause
