# PyCoral Installation Options

## 🎯 **For End Users - How to Install**

### Option 1: Install from GitHub (Recommended)
```bash
# Latest version from main branch
pip install git+https://github.com/cropcrusaders/pycoral.git

# Specific version/tag
pip install git+https://github.com/cropcrusaders/pycoral.git@v2.1.0

# Development version from specific branch
pip install git+https://github.com/cropcrusaders/pycoral.git@development
```

### Option 2: Install from PyPI (When Available)
```bash
pip install pycoral
```

### Option 3: Local Development Install
```bash
# Clone the repository
git clone https://github.com/cropcrusaders/pycoral.git
cd pycoral

# Install in development mode
pip install -e .

# Or use our easy installer
python install.py
```

## 🛠️ **For Repository Owner - What You Need to Do**

### 1. Prepare Your Repository

Your repo already has:
- ✅ `setup.py` (updated for Python 3.13)
- ✅ `pyproject.toml` (modern packaging)
- ✅ `requirements.txt` (dependencies)
- ✅ `install.py` (easy installer)
- ✅ Proper version in `pycoral/__init__.py`

### 2. Create a Release on GitHub

1. **Tag your version**:
   ```bash
   git tag v2.1.0
   git push origin v2.1.0
   ```

2. **Create GitHub Release**:
   - Go to your GitHub repo
   - Click "Releases" → "Create a new release"
   - Choose tag `v2.1.0`
   - Title: "PyCoral v2.1.0 - Python 3.13 Support"
   - Description: List of changes

### 3. Optional: Publish to PyPI

To allow `pip install pycoral`:

1. **Install twine**:
   ```bash
   pip install twine
   ```

2. **Build distribution**:
   ```bash
   python -m build
   ```

3. **Upload to PyPI**:
   ```bash
   twine upload dist/*
   ```

## 📋 **Repository Checklist**

Before users can install from your repo, ensure:

- ✅ `setup.py` with correct metadata
- ✅ `pyproject.toml` with build configuration  
- ✅ `__init__.py` with `__version__`
- ✅ `requirements.txt` with dependencies
- ✅ `README.md` with installation instructions
- ✅ Proper Git tags for versions
- ✅ GitHub releases for major versions

## 🎯 **Recommended Installation Instructions for Users**

Add this to your README.md:

```markdown
## Installation

### Quick Install
pip install git+https://github.com/cropcrusaders/pycoral.git

### Development Install
git clone https://github.com/cropcrusaders/pycoral.git
cd pycoral
python install.py

### Requirements
- Python 3.9+
- NumPy >= 1.21.0
- Pillow >= 8.0.0
```
