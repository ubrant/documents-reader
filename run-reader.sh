#! /bin/bash

PWD=$(pwd)
Scan_DIR="$PWD/UBD-Docs"
GeneratedFiles_DIR="$PWD/Generated-Site"

env --chdir="./Reader"              \
    python3 "main.py"               \
            "$Scan_DIR"             \
            "true"                  \
            "1000000"               \
            "$GeneratedFiles_DIR"
