# PyCoral Installation Guide

## Quick Install (Recommended)

### For Windows Users:
Simply double-click `install.bat` or run in Command Prompt:
```cmd
### From Source (Development)
```bash
git clone https://github.com/cropcrusaders/pycoral.git
cd pycoral
python install.py
```l.bat
```

### For All Platforms:
```bash
python install.py
```

## Manual Installation Options

### Option 1: Standard pip install (Development Mode)
```bash
# Install core dependencies
pip install --upgrade pip setuptools wheel
pip install numpy>=1.21.0 Pillow>=8.0.0

# Install PyCoral in editable mode
pip install -e .
```

### Option 2: Using the enhanced build script
```bash
# Development mode (recommended for development)
python build.py --mode development

# Build mode (creates distributable packages)
python build.py --mode build

# User mode (simple installation)
python build.py --mode user

# Clean build (removes old artifacts first)
python build.py --mode development --clean
```

### Option 3: Build and install wheel
```bash
# Build wheel package
pip install build
python -m build

# Install the built wheel
pip install dist/*.whl
```

## Installation Verification

After installation, test with:
```bash
python -c "import pycoral; print('PyCoral version:', pycoral.__version__)"
```

Expected output:
```
PyCoral version: 2.1.0
```

## System Requirements

- **Python**: 3.9, 3.10, 3.11, 3.12, or 3.13
- **Operating System**: Windows, Linux, or macOS
- **Dependencies**:
  - NumPy >= 1.21.0
  - Pillow >= 8.0.0
- **Optional**: Edge TPU runtime (for hardware acceleration)

## Installation Modes Explained

### Development Mode (`-e` or `--editable`)
- **Best for**: Active development, testing changes
- **How it works**: Creates a link to your source code
- **Benefits**: Changes to source code are immediately available
- **Command**: `pip install -e .`

### Standard Installation
- **Best for**: End users, production deployment
- **How it works**: Copies files to Python's site-packages
- **Benefits**: Clean, isolated installation
- **Command**: `pip install .`

### Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv pycoral_env

# Activate it
# Windows:
pycoral_env\Scripts\activate
# Linux/Mac:
source pycoral_env/bin/activate

# Install PyCoral
python install.py

# When done, deactivate
deactivate
```

## Troubleshooting

### Common Issues

**1. Python Version Error**
```
Error: Python 3.9+ required
```
**Solution**: Install Python 3.9 or newer from python.org

**2. Permission Denied**
```
Permission denied when installing
```
**Solution**: 
- Use virtual environment (recommended)
- Or run as administrator (Windows) / sudo (Linux/Mac)
- Or use `pip install --user .`

**3. NumPy Installation Fails**
```
Failed building wheel for numpy
```
**Solution**:
- Update pip: `pip install --upgrade pip`
- Install pre-compiled wheel: `pip install --only-binary=numpy numpy`

**4. Import Error After Installation**
```
ModuleNotFoundError: No module named 'pycoral'
```
**Solution**:
- Check you're using the same Python that you installed to
- Activate virtual environment if using one
- Reinstall: `pip uninstall pycoral && pip install -e .`

**5. Edge TPU Not Detected**
```
Edge TPU runtime not found
```
**Solution**: Install Edge TPU runtime separately from Google Coral documentation

### Getting Help

1. **Check installation**: `pip list | grep pycoral`
2. **Check Python path**: `python -c "import sys; print(sys.path)"`
3. **Reinstall clean**: 
   ```bash
   pip uninstall pycoral
   pip install -e .
   ```

## Advanced Installation

### From Source (Development)
```bash
git clone https://github.com/google-coral/pycoral.git
cd pycoral
python install.py
```

### Custom Build Options
```bash
# With specific Python version
/path/to/python3.13 install.py

# Clean install
python build.py --mode development --clean

# Build distribution packages
python build.py --mode build
```

### Docker Installation
```dockerfile
FROM python:3.13-slim

WORKDIR /app
COPY . .

RUN pip install --upgrade pip && \
    pip install -e .

CMD ["python", "-c", "import pycoral; print('PyCoral ready!')"]
```

## Next Steps After Installation

1. **Run Examples**:
   ```bash
   cd examples
   python classify_image.py --help
   ```

2. **Read Documentation**:
   - `README_PYTHON313.md` - Updated features
   - `docs/` - Full documentation
   - `examples/` - Working code samples

3. **Install Edge TPU Runtime** (for hardware acceleration):
   - Follow Google's Coral Edge TPU setup guide
   - Test with Edge TPU examples

4. **Development Setup**:
   ```bash
   pip install pytest black isort ruff  # Development tools
   pytest tests/                       # Run tests
   black .                            # Format code
   ```

## Support

- **GitHub Issues**: Report bugs and feature requests
- **Examples**: Check `examples/` directory for working code
- **Documentation**: See `docs/` directory
- **Community**: Google Coral community forums
