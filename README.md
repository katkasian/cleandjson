# Clean NDJSON tool

Transform your NDJSON file into a standard JSON format. 
This tool was developed to be used in a workflow combining [Zeeschuimer](https://github.com/digitalmethodsinitiative/zeeschuimer) scraper and Tableau.

## Installation

Download the cleandjson.py script.

Next, if you don't already have a Python virtual environment set up, make a new one ad-hoc:

```
virtualenv env
source env/bin/activate
```
Optionally, make the script executable if you are using a UNIX environment. This way, you do not have to specify `python` in your command every time you run the script.

```
chmod +x cleandjson.py
```

## Usage

### Viewing Built-in Documentation
To view help info text on how to run the script and available options, run it with the `-h` flag:

```
python ./cleandjson.py -h
```

### Basic Usage
The script requires the `-i/--input-file` option to specify the NDJSON file you want to transform into regular JSON. 
The output file must be also provided using the `-o/--output-file` option.

Example command:

```
python ./cleandjson.py -i INPUT_FILE_HERE -o OUTPUT_FILE_HERE
```

### Issues

If you encounter any problem using the tool, please submit an issue to this repository. Cheers!