@echo off

TITLE UB Documentsreader

set cwd=%cd%
set docs_dir=%cwd%\UBD-Docs
set site_dir=%cwd%\Generated-Site

CD "Reader"
python "main.py"  %docs_dir% "true" "1000000" %site_dir%

PAUSE