# PyCoral API - Updated for Python 3.13

This repository contains an easy-to-use Python API that helps you run inferences
and perform on-device transfer learning with TensorFlow Lite models on
[Coral devices](https://coral.ai/products/).

**🚀 This version has been updated to support Python 3.13 and modern dependencies.**

## Quick Installation

### Install from GitHub (Recommended)

```bash
pip install git+https://github.com/cropcrusaders/pycoral.git
```

### Local Development Install

```bash
git clone https://github.com/cropcrusaders/pycoral.git
cd pycoral
python install.py
```

### Alternative: Install from Built Wheel

```bash
# Clone and build
git clone https://github.com/cropcrusaders/pycoral.git
cd pycoral
python -m build --wheel
pip install dist/pycoral-2.1.0-py3-none-any.whl
```

### Requirements

- Python 3.9, 3.10, 3.11, 3.12, or 3.13
- NumPy >= 1.21.0
- Pillow >= 8.0.0

## What's New in This Version

- ✅ **Python 3.13 Support** - Fully compatible with the latest Python
- ✅ **Modern Dependencies** - Updated NumPy, Pillow, and build system
- ✅ **Easy Installation** - Simple pip install from GitHub
- ✅ **Improved Build System** - Modern packaging with pyproject.toml

## Legacy Installation Notes

The original instructions mentioned installing from apt-get on Debian systems.
This updated version can be installed via pip, but for official Edge TPU drivers,
you may still need to follow [coral.ai/software/](https://coral.ai/software/#pycoral-api)
for the Edge TPU runtime.

**Note:** If you need the exact original Google version, use the official
[coral.ai/software/](https://coral.ai/software/#pycoral-api) instructions.
This repository provides an updated, Python 3.13-compatible version.

## Documentation and examples

To learn more about how to use the PyCoral API, see our guide to [Run inference
on the Edge TPU with Python](https://coral.ai/docs/edgetpu/tflite-python/) and
check out the [PyCoral API reference](https://coral.ai/docs/reference/py/).

Several Python examples are available in the `examples/` directory. For
instructions, see the [examples README](
https://github.com/google-coral/pycoral/tree/master/examples#pycoral-api-examples).


## Compilation

When building this library yourself, it's critical that you have
version-matching builds of
[libcoral](https://github.com/google-coral/libcoral/tree/master) and
[libedgetpu](https://github.com/google-coral/libedgetpu/tree/master)—notice
these are submodules of the pycoral repo, and they all share the same
`TENSORFLOW_COMMIT` value. So just be sure if you change one, you must change
them all.

For complete details about how to build all these libraries, read
[Build Coral for your platform](https://coral.ai/docs/notes/build-coral/).
Or to build just this library, follow these steps:

1.  Clone this repo and include submodules:

    ```
    git clone --recurse-submodules https://github.com/google-coral/pycoral
    ```

    If you already cloned without the submodules. You can add them with this:

    ```
    cd pycoral

    git submodule init && git submodule update
    ```

1.  Run `scripts/build.sh` to build pybind11-based native layer for different
    Linux architectures. Build is Docker-based, so you need to have it
    installed.

1.  Run `make wheel` to generate Python library wheel and then `pip3 install
    $(ls dist/*.whl)` to install it
