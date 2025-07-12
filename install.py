#!/usr/bin/env python3
"""
Easy pip install script for PyCoral
"""
import subprocess
import sys
import os
from pathlib import Path

def main():
    """Simple pip install for PyCoral."""
    print("🚀 Installing PyCoral with pip...")
    
    # Get current directory
    current_dir = Path.cwd()
    
    # Check if we're in the right directory
    if not (current_dir / "setup.py").exists() or not (current_dir / "pycoral").exists():
        print("❌ Error: Please run this script from the PyCoral root directory")
        print("   (The directory containing setup.py and pycoral/)")
        return False
    
    print(f"📁 Installing from: {current_dir}")
    
    # Check Python version
    if sys.version_info < (3, 9):
        print(f"❌ Error: Python 3.9+ required, you have {sys.version}")
        return False
    
    print(f"✅ Python version: {sys.version}")
    
    # Installation commands
    commands = [
        ([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], 
         "Upgrading pip"),
        ([sys.executable, "-m", "pip", "install", "--upgrade", "setuptools", "wheel"], 
         "Installing build tools"),
        ([sys.executable, "-m", "pip", "install", "numpy>=1.21.0", "Pillow>=8.0.0"], 
         "Installing core dependencies"),
        ([sys.executable, "-m", "pip", "install", "-e", "."], 
         "Installing PyCoral in editable mode"),
    ]
    
    # Execute commands
    for cmd, description in commands:
        print(f"\n🔄 {description}...")
        print(f"   Running: {' '.join(cmd)}")
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"✅ {description} - SUCCESS")
        else:
            print(f"❌ {description} - FAILED")
            print(f"   Error: {result.stderr}")
            if result.stdout:
                print(f"   Output: {result.stdout}")
            return False
    
    # Test installation
    print(f"\n🧪 Testing installation...")
    test_result = subprocess.run([
        sys.executable, "-c", 
        "import pycoral; import sys; "
        "print(f'PyCoral {pycoral.__version__} installed successfully!'); "
        "print(f'Python: {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}')"
    ], capture_output=True, text=True)
    
    if test_result.returncode == 0:
        print("✅ Installation test - SUCCESS")
        print(test_result.stdout)
    else:
        print("❌ Installation test - FAILED")
        print(f"   Error: {test_result.stderr}")
        return False
    
    # Success message
    print("\n" + "="*60)
    print("🎉 PyCoral installed successfully! 🎉")
    print("="*60)
    print("\n📋 Quick start:")
    print("   • Test: python -c 'import pycoral; print(pycoral.__version__)'")
    print("   • Examples: cd examples && python classify_image.py --help")
    print("   • Documentation: See README_PYTHON313.md")
    print("\n💡 The package was installed in 'editable' mode.")
    print("   Any changes to the source code will be reflected immediately.")
    
    return True

if __name__ == "__main__":
    try:
        success = main()
        if not success:
            print("\n💡 Troubleshooting tips:")
            print("   • Make sure you're in the PyCoral root directory")
            print("   • Try running with: python install.py")
            print("   • Check that Python 3.9+ is installed")
            print("   • Ensure you have internet connection for downloads")
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n⚠️ Installation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)
