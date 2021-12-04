# Documents Reader

*UBD Documents Reader* is simply a reader that checks validity of [**UBD** documentation](https://github.com/ubrant/documents-format) files and generates formatted output files. It is intended to help in easy modifications for feeding data into destination databases or generating any desired format.

> Default output is in the form of web pages

## Dependencies

*Reader* is implemented in **Python**. You need to [download](https://www.python.org/downloads/) and install python (if you don't have) for using this reader.

> Make sure to Check "**Add Python to PATH**" while installing

## Documentation Format

Format for documents is maintained in separate [repository](https://github.com/ubrant/documents-format). For using default configuration, put formatted documents in UBD-Docs folder, as it is the base folder that is scanned along-with its internal directories by default. To change the default behaviour, make changes in *.sh/.bat* files; as command-line arguments are passed-in to the main parser.

## Running the Parser

Helper scripts are included in repository:

> * **run-reader.sh** for Linux distros; *and*
> * **run-reader.bat** for Windows

1. [Download](https://www.python.org/downloads/) and install **Python** if not already available.
2. [Download](https://github.com/ubrant/documents-reader/archive/refs/heads/main.zip) this repo
3. Run **run-reader***.sh/.bat*
4. Write *UBD* documents
5. Repeat steps **3**, **4** and **this one**
6. Have Fun
