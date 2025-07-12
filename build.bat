@echo off
echo Building PyCoral for Python 3.13 on Windows...

REM Check if virtual environment exists
if not exist ".venv\Scripts\python.exe" (
    echo Creating virtual environment...
    python -m venv .venv
)

echo.
echo Activating virtual environment...
call .venv\Scripts\activate.bat

echo.
echo Upgrading pip...
python -m pip install --upgrade pip

echo.
echo Installing build dependencies...
pip install --upgrade setuptools wheel build

echo.
echo Installing core dependencies...
pip install "numpy>=1.21.0" "Pillow>=8.0.0"

echo.
echo Building the package...
python -m build

echo.
echo Installing in editable mode...
pip install -e .

echo.
echo Testing installation...
python -c "import pycoral; print('PyCoral version:', pycoral.__version__); import sys; print('Python version:', sys.version)"

echo.
echo Build completed successfully!
echo.
echo The package has been built and installed.
echo Built packages are in the 'dist/' directory.
echo.
pause
