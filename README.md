# Documents Reader

It is a simple reader that checks validity of documentation files and generates output files. Easy modifications can be done for feeding data into destination databases or generating any desired format. By default, web pages are generated.

## Dependencies

The reader is implemented in **Python**. You may [download](https://www.python.org/downloads/) and install python if you would like to use this reader.

> Make sure to Check "**Add Python to PATH**" while installing

## Documentation Format

Format for documents is maintained in separate [repository](https://github.com/ubrant/documents-format). To use default configuration, put your formatted documents in UBD-Docs folder, as it is the base folder being processed along-with its internal directories. To change this default path, make changes in simple .sh/.bat files; as this path is provided as a command-line argument to main parser.

## Running the Parser

Two helper scripts are included in repository:

> * **run-reader.sh** for Linux machines
> * **run-reader.bat** for Windows machines

1. First download and install **Python** on your machine.
2. Download this repo
3. Run **run-reader** .sh/.bat
4. Have Fun
