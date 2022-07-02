# Documents Reader

*UBD Documents' Reader* checks validity of [**UBD formatted** documents](https://github.com/ubrant/documents-format) and generates formatted output. It is intended to help (with easy modifications) in feeding data into destination databases or generating any desired format.

> By default HTML pages are generated as output

## Dependencies

It is fully implemented in ***Python***, so you need to have python interpreter installed for using it.

## Usage

Helper scripts are included for easy use:

  * ***run-reader.sh*** for Linux distros; *and*
  * ***run-reader.bat*** for Windows

For basic usage:

1. [Download ***Python***](https://www.python.org/downloads/) and install it (if not already have)
    - Make sure to Check ***"Add Python to PATH"*** while installing

2. [Download ***Reader***](https://github.com/ubrant/documents-reader/archive/refs/heads/main.zip) and unzip it
3. Run ***run-reader*** **.sh / .bat**
4. Write *UBD documents*
    - Put formatted documents in UBD-Docs folder, as it is the base folder that is scanned along-with its internal directories by default
    - To change the default behaviour, update your *.sh / .bat* files or *Python* scripts - command-line arguments are passed-in to the main parser
5. Repeat steps ***3***, ***4*** and ***this*** one
6. Have Fun
