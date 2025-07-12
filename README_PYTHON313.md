# PyCoral - Updated for Python 3.13

This is an updated version of Google's PyCoral library that has been modernized to work with Python 3.13 and the latest dependencies.

## What's Updated

### Python Support
- ✅ **Python 3.13.5** - Fully compatible with the latest Python version
- ✅ **Python 3.9+** - Supports Python 3.9, 3.10, 3.11, 3.12, and 3.13
- ❌ Dropped support for Python 3.6, 3.7, 3.8 (EOL versions)

### Dependencies Updated
- **NumPy**: Updated to `>=1.21.0` (from 1.16.0)
- **Pillow**: Updated to `>=8.0.0` (from 4.0.0)
- **Build System**: Modernized with `pyproject.toml`
- **Development Tools**: Added modern linting and formatting tools

### Package Structure
- Added `pyproject.toml` for modern Python packaging
- Updated `setup.py` with current Python version support
- Created comprehensive `requirements.txt`
- Added automated build scripts for Windows

## Quick Start

### Installation

#### Option 1: Using the provided build script (Windows)
```bash
.\build.bat
```

#### Option 2: Manual installation
```bash
# Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
# or
source .venv/bin/activate  # Linux/Mac

# Install dependencies
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

# Install PyCoral in development mode
pip install -e .
```

### Verification
```bash
python -c "import pycoral; print('PyCoral version:', pycoral.__version__)"
```

## Key Features Maintained

All original PyCoral functionality has been preserved:
- Edge TPU inference support
- TensorFlow Lite model compatibility
- Image classification and object detection
- Model training and adaptation utilities
- Pipeline processing capabilities

## Project Structure

```
pycoral/
├── pycoral/           # Main package code
├── examples/          # Example scripts
├── tests/            # Test suite
├── docs/             # Documentation
├── build.py          # Python build script
├── build.bat         # Windows build script
├── pyproject.toml    # Modern packaging config
├── requirements.txt  # Dependency list
└── setup.py          # Legacy setup script
```

## Development

### Running Examples
```bash
cd examples
python classify_image.py --help
```

### Running Tests
```bash
pip install pytest
pytest tests/
```

### Code Formatting
```bash
pip install black isort ruff
black .
isort .
ruff check .
```

## Compatibility Notes

- **TensorFlow Lite**: The project now uses the standalone TensorFlow package instead of the deprecated `tflite-runtime`
- **Edge TPU**: Edge TPU drivers need to be installed separately (see Google's Coral documentation)
- **Model Files**: All existing `.tflite` model files remain compatible

## License

This project maintains the original Apache 2.0 license from Google's PyCoral.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes with proper testing
4. Run the code formatting tools
5. Submit a pull request

## Troubleshooting

### Common Issues

**Import Error**: Make sure you're using Python 3.9+ and have activated the virtual environment.

**Edge TPU Not Found**: Install the Edge TPU runtime from Google's Coral documentation.

**Model Loading Issues**: Ensure your model files are compatible with the latest TensorFlow Lite version.

For more help, check the `examples/` directory for working code samples.
