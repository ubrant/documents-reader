@echo off

TITLE UBD Reader

set cwd=%cd%
set recursion_enabled=true
set recursion_depth=1000000
set docs_in_dir=%cwd%\UBD-Docs
set site_out_dir=%cwd%\Generated-Site
set site_base_url=https://ubrant.com/

CD "Reader"
python "main.py"  %docs_in_dir%  %recursion_enabled%  %recursion_depth%  %site_out_dir%  %site_base_url%

PAUSE
