#! /bin/bash

PWD=$(pwd)
SCAN_DIR="$PWD/UBD-Docs"
GENF_DIR="$PWD/Generated-Site"

env --chdir="./Reader"              \
    python3 "main.py"               \
            "$SCAN_DIR"             \
            "true"                  \
            "1000000"               \
            "$GENF_DIR"
