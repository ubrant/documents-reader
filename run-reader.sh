#! /bin/bash

PWD=$(pwd)
SCAN_DIR="$PWD/UBD-Docs"
GeneratedFiles_DIR="$PWD/Generated-Site"

env --chdir="./Reader"              \
    python3 "main.py"               \
            "$SCAN_DIR"             \
            "true"                  \
            "1000000"               \
            "$GeneratedFiles_DIR"
