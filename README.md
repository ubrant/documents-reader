# ***UBD Documents Reader***

*UBD Documents Reader* checks the validity of special [**UBD formatted** documents](https://github.com/ubrant/documents-format) and generates well-formatted output. It is intended to help (with easy modifications) in feeding data into destination databases or generating documents in any desired format.

&nbsp;

> By default HTML pages are generated as output



&nbsp;

## Dependencies

The reader is fully implemented in ***Python*** - without any other dependencies, so you only need to have *Python 3* installed to use it.



&nbsp;

## Usage

Helper scripts are included for easy invokation:

  * You can use ***run-reader.sh*** on Linux distros, *and*
  * ***run-reader.bat*** on Windows

For basic usage:

1. [Download ***Python***](https://www.python.org/downloads/) and install it (if not already have)
    - Make sure to Check "**Add Python to PATH**" while installing on Windows

2. [Download ***Reader***](https://github.com/ubrant/documents-reader/archive/refs/heads/main.zip) and unzip it
3. Run ***run-reader*** **.sh/.bat**
4. Write *UBD* documents
    - Place document files in *UBD-Docs* folder, as it is the base folder that is scanned with internal directories by default
    - To change the default behaviour, update *.sh/.bat* file or *Python* scripts - command-line arguments are passed-in to main parser
5. Repeat steps ***3***, ***4*** and ***this*** one
6. Have Fun
