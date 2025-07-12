# 🚀 PyCoral Pip Install - Quick Reference

## One-Line Install Commands

### Super Easy (Windows)
```cmd
install.bat
```

### Cross-Platform
```bash
python install.py
```

### Standard pip (if you know what you're doing)
```bash
pip install -e .
```

## What Gets Installed

- ✅ **PyCoral 2.1.0** - Updated for Python 3.13
- ✅ **NumPy ≥1.21.0** - Latest compatible version
- ✅ **Pillow ≥8.0.0** - Modern image processing
- ✅ **All dependencies** automatically handled

## Installation Verification

```bash
python -c "import pycoral; print('Version:', pycoral.__version__)"
```

Expected output: `Version: 2.1.0`

## Quick Start After Install

```bash
# Test basic functionality
python -c "import pycoral"

# Run examples
cd examples
python classify_image.py --help

# Check what's installed
pip list | grep pycoral
```

## Installation Options

| Method | Command | Best For |
|--------|---------|----------|
| **Easy Install** | `install.bat` | Windows users, beginners |
| **Python Script** | `python install.py` | All platforms, with feedback |
| **Direct pip** | `pip install -e .` | Experienced users |
| **Build Script** | `python build.py` | Advanced options |

## File Structure After Install

```
pycoral/
├── install.py          ← Easy install script
├── install.bat         ← Windows batch installer  
├── build.py           ← Advanced build script
├── INSTALL.md         ← Detailed install guide
├── requirements.txt   ← Dependencies list
├── pyproject.toml     ← Modern packaging config
└── setup.py          ← Traditional setup file
```

## Development vs Production

### Development Install (Editable)
```bash
pip install -e .
```
- ✅ Changes to code take effect immediately
- ✅ Good for development and testing
- ✅ Easy to update and modify

### Production Install
```bash
pip install .
```
- ✅ Clean, isolated installation
- ✅ Good for deployment
- ✅ No source code dependencies

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Python too old | Install Python 3.9+ |
| Permission denied | Use virtual environment |
| Import fails | Check Python environment |
| Dependencies fail | Update pip first |

## Next Steps

1. **✅ Install**: Use one of the methods above
2. **🧪 Test**: Run verification command
3. **📖 Learn**: Check `examples/` directory
4. **🚀 Build**: Start your Coral AI project!

---
**Need help?** See `INSTALL.md` for detailed instructions.
