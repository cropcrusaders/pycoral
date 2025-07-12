#!/usr/bin/env python3
"""Test script to verify PyCoral imports work correctly."""

import pycoral
print(f'PyCoral version: {pycoral.__version__}')

import pycoral.adapters.common
print('Adapters module imported successfully')

try:
    import pycoral.utils.edgetpu
    print('EdgeTPU utils imported successfully')
except Exception as e:
    print('EdgeTPU utils import failed (expected):', e)

import pycoral.utils.dataset
print('Dataset utils imported successfully')

print('All imports completed successfully!')
