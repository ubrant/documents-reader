# Documents Reader

*UBD Documents Reader* is simply a reader that checks validity of [**UBD** formatted documentation](https://github.com/ubrant/documents-format) files and generates formatted output. It is intended to help (with easy modifications) in feeding data into destination databases or generating any desired format.

> Default output is in the form of HTML pages

## Dependencies

*Reader* is fully implemented in **Python**. You need to have python interpreter installed for using this reader.

## Running

Helper scripts are included in repository:

> * **run-reader.sh** for Linux distros; *and*
> * **run-reader.bat** for Windows


1. [Download **Python**](https://www.python.org/downloads/) and install it (if not already available)
    - Make sure to Check "**Add Python to PATH**" while installing

2. [Download **Reader's** ZIP](https://github.com/ubrant/documents-reader/archive/refs/heads/main.zip) and unzip it
3. Run **run-reader***.sh/.bat*
4. Write *UBD* documents
    - Put formatted documents in UBD-Docs folder, as it is the base folder that is scanned along-with its internal directories by default
    - To change the default behaviour, make changes in *.sh/.bat* files, as command-line arguments are passed-in to the main parser
5. Repeat steps **3**, **4** and **this one**
6. Have Fun
