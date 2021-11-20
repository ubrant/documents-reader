@echo off

TITLE UB Documentsreader

set cwd=%cd%
set do_recursion=true
set recursion_depth=1000000
set docs_dir=%cwd%\UBD-Docs
set site_dir=%cwd%\Generated-Site
set base_url=https://ubrant.com/

CD "Reader"
python "main.py"  %docs_dir%  %do_recursion%  %recursion_depth%  %site_dir%  %base_url%

PAUSE