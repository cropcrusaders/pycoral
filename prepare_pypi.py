#!/usr/bin/env python3
"""
Script to prepare PyCoral for PyPI publishing
"""
import subprocess
import sys
import os
from pathlib import Path
import json

def run_command(cmd, description):
    """Run a command and return success status."""
    print(f"\n→ {description}")
    print(f"  Running: {' '.join(cmd)}")
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"  ✅ SUCCESS")
        if result.stdout.strip():
            print(f"  Output: {result.stdout.strip()}")
        return True
    else:
        print(f"  ❌ FAILED")
        if result.stderr:
            print(f"  Error: {result.stderr}")
        if result.stdout:
            print(f"  Output: {result.stdout}")
        return False

def check_requirements():
    """Check if all required files exist."""
    required_files = [
        "setup.py",
        "pyproject.toml", 
        "pycoral/__init__.py",
        "README.md",
        "LICENSE"
    ]
    
    print("🔍 Checking required files...")
    missing_files = []
    
    for file in required_files:
        if Path(file).exists():
            print(f"  ✅ {file}")
        else:
            print(f"  ❌ {file} - MISSING")
            missing_files.append(file)
    
    return len(missing_files) == 0

def check_version():
    """Check version consistency."""
    print("\n🔍 Checking version consistency...")
    
    # Read version from __init__.py
    init_file = Path("pycoral/__init__.py")
    if init_file.exists():
        content = init_file.read_text()
        for line in content.split('\n'):
            if line.startswith('__version__'):
                version = line.split('=')[1].strip().strip('"\'')
                print(f"  ✅ Found version: {version}")
                return version
    
    print("  ❌ Could not find version in pycoral/__init__.py")
    return None

def build_package():
    """Build the package for distribution."""
    print("\n🏗️ Building package...")
    
    # Clean previous builds
    for path in ["build", "dist", "*.egg-info"]:
        path_obj = Path(path)
        if path_obj.exists():
            import shutil
            shutil.rmtree(path_obj, ignore_errors=True)
            print(f"  🧹 Cleaned {path}")
    
    # Install build tools
    if not run_command([sys.executable, "-m", "pip", "install", "--upgrade", "build", "twine"], 
                      "Installing build tools"):
        return False
    
    # Build the package
    if not run_command([sys.executable, "-m", "build"], "Building package"):
        return False
    
    # Check what was built
    dist_dir = Path("dist")
    if dist_dir.exists():
        files = list(dist_dir.glob("*"))
        print(f"\n📦 Built files:")
        for file in files:
            print(f"  📄 {file.name}")
        return True
    
    return False

def check_package():
    """Check the built package."""
    print("\n🔍 Checking package...")
    
    dist_files = list(Path("dist").glob("*.tar.gz")) + list(Path("dist").glob("*.whl"))
    
    for file in dist_files:
        if not run_command(["twine", "check", str(file)], f"Checking {file.name}"):
            return False
    
    return True

def test_install():
    """Test installation in a temporary environment."""
    print("\n🧪 Testing installation...")
    
    # Find the wheel file
    wheel_files = list(Path("dist").glob("*.whl"))
    if not wheel_files:
        print("  ❌ No wheel file found")
        return False
    
    wheel_file = wheel_files[0]
    
    # Test install
    if not run_command([sys.executable, "-m", "pip", "install", "--force-reinstall", str(wheel_file)], 
                      f"Testing installation of {wheel_file.name}"):
        return False
    
    # Test import
    if not run_command([sys.executable, "-c", "import pycoral; print(f'Version: {pycoral.__version__}')"], 
                      "Testing import"):
        return False
    
    return True

def main():
    """Main preparation process."""
    print("🚀 Preparing PyCoral for PyPI Publishing")
    print("=" * 50)
    
    # Change to project directory
    project_root = Path(__file__).parent
    os.chdir(project_root)
    
    # Check requirements
    if not check_requirements():
        print("\n❌ Missing required files. Please create them first.")
        return False
    
    # Check version
    version = check_version()
    if not version:
        print("\n❌ Version check failed.")
        return False
    
    # Build package
    if not build_package():
        print("\n❌ Package build failed.")
        return False
    
    # Check package
    if not check_package():
        print("\n❌ Package check failed.")
        return False
    
    # Test installation
    if not test_install():
        print("\n❌ Installation test failed.")
        return False
    
    # Success!
    print("\n" + "=" * 50)
    print("🎉 PACKAGE READY FOR PUBLISHING! 🎉")
    print("=" * 50)
    print(f"\n📦 Package version: {version}")
    print(f"📁 Built files in: dist/")
    
    print("\n🚀 Next steps to publish:")
    print("1. Create PyPI account: https://pypi.org/account/register/")
    print("2. Upload to Test PyPI first:")
    print("   twine upload --repository testpypi dist/*")
    print("3. Test install from Test PyPI:")
    print("   pip install --index-url https://test.pypi.org/simple/ pycoral")
    print("4. If everything works, upload to real PyPI:")
    print("   twine upload dist/*")
    
    print("\n🔗 For GitHub installs, users can use:")
    print("   pip install git+https://github.com/cropcrusaders/pycoral.git")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
