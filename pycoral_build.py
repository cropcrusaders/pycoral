#!/usr/bin/env python3
"""
Build script for PyCoral with Python 3.13 support
"""
import subprocess
import sys
import os
from pathlib import Path
import argparse

def run_command(cmd, description):
    """Run a command and handle errors."""
    print(f"\n-> {description}")
    print(f"Running: {' '.join(cmd)}")
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"SUCCESS: {description} completed successfully")
        if result.stdout:
            print(result.stdout)
    else:
        print(f"FAILED: {description} failed")
        if result.stderr:
            print(f"Error: {result.stderr}")
        if result.stdout:
            print(f"Output: {result.stdout}")
        return False
    return True

def setup_venv(project_root):
    """Create and setup virtual environment."""
    venv_path = project_root / ".venv"
    python_exe = venv_path / "Scripts" / "python.exe"
    
    if not python_exe.exists():
        print("Creating virtual environment...")
        result = subprocess.run([sys.executable, "-m", "venv", str(venv_path)], 
                               capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Failed to create virtual environment: {result.stderr}")
            return None, None
    
    pip_exe = venv_path / "Scripts" / "pip.exe"
    return python_exe, pip_exe

def install_package(mode="development"):
    """Install the package in different modes."""
    print(f"\nInstalling PyCoral in {mode} mode...")
    
    # Get the project root directory
    project_root = Path(__file__).parent
    os.chdir(project_root)
    
    # Setup virtual environment
    python_exe, pip_exe = setup_venv(project_root)
    if not python_exe:
        return False
    
    # Installation steps based on mode
    if mode == "development":
        steps = [
            ([str(pip_exe), "install", "--upgrade", "pip"], "Upgrading pip"),
            ([str(pip_exe), "install", "--upgrade", "setuptools", "wheel"], "Installing build tools"),
            ([str(pip_exe), "install", "-r", "requirements.txt"], "Installing dependencies"),
            ([str(pip_exe), "install", "-e", "."], "Installing PyCoral in development mode"),
        ]
    elif mode == "build":
        steps = [
            ([str(pip_exe), "install", "--upgrade", "pip"], "Upgrading pip"),
            ([str(pip_exe), "install", "--upgrade", "setuptools", "wheel", "build"], "Installing build tools"),
            ([str(pip_exe), "install", "-r", "requirements.txt"], "Installing dependencies"),
            ([str(python_exe), "-m", "build"], "Building the package"),
            ([str(pip_exe), "install", "dist/*.whl"], "Installing built wheel"),
        ]
    elif mode == "user":
        steps = [
            ([str(pip_exe), "install", "--upgrade", "pip"], "Upgrading pip"),
            ([str(pip_exe), "install", "."], "Installing PyCoral"),
        ]
    
    # Execute installation steps
    for cmd, description in steps:
        if not run_command(cmd, description):
            return False
    
    # Test installation
    test_cmd = [str(python_exe), "-c", 
                "import pycoral; import sys; "
                "print(f'PyCoral {pycoral.__version__} installed successfully!'); "
                "print(f'Python version: {sys.version}')"]
    
    if not run_command(test_cmd, "Testing installation"):
        return False
    
    return True

def main():
    """Main build process."""
    parser = argparse.ArgumentParser(description="PyCoral Build and Install Script")
    parser.add_argument("--mode", choices=["development", "build", "user"], 
                       default="development",
                       help="Installation mode (default: development)")
    parser.add_argument("--clean", action="store_true",
                       help="Clean build artifacts before building")
    
    args = parser.parse_args()
    
    print(f"Building PyCoral for Python 3.13 in {args.mode} mode")
    
    project_root = Path(__file__).parent
    os.chdir(project_root)
    
    # Clean if requested
    if args.clean:
        print("Cleaning build artifacts...")
        for path in ["build", "dist", "*.egg-info"]:
            if Path(path).exists():
                import shutil
                shutil.rmtree(path, ignore_errors=True)
                print(f"Removed {path}")
    
    # Install the package
    success = install_package(args.mode)
    
    if success:
        print("\n" + "="*50)
        print("INSTALLATION COMPLETED SUCCESSFULLY!")
        print("="*50)
        print("\nNext steps:")
        if args.mode == "development":
            print("1. Activate environment: .venv\\Scripts\\activate")
            print("2. Run examples: cd examples && python classify_image.py")
            print("3. Make changes and they'll be reflected immediately")
        elif args.mode == "build":
            print("1. Built packages are in the 'dist/' directory")
            print("2. Install with: pip install dist/*.whl")
            print("3. Distribute the wheel file to others")
        elif args.mode == "user":
            print("1. Package installed in current environment")
            print("2. Import with: import pycoral")
        print("4. Test with: python -c 'import pycoral; print(pycoral.__version__)'")
    else:
        print("\nInstallation failed. Check error messages above.")
    
    return success

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
