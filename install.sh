#!/bin/bash
python -m build
python -m pip install ./dist/ConcurrentImageRead-0.0.12.tar.gz
