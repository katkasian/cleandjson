#!/usr/bin/env python

import json
import argparse


def open_ndjson(ndjson_file):
    with open(ndjson_file, 'r', encoding='utf-8') as file:
        content = file.read()
    return content


def convert_to_json(ndjson_content):
    result = []
    for ndjson_line in ndjson_content.splitlines():
        if not ndjson_line.strip():
            continue  # ignoring empty lines
        json_line = json.loads(ndjson_line)
        result.append(json_line)
    return result


def write_json(json_result, outfile):
    with open(outfile, 'w') as file:
        file.write(json.dumps(json_result))


def main():
    # instantiate argument parser object
    parser = argparse.ArgumentParser(description='Transform NDJSON file produced \
                                                 by Zeeschuimer Firefox extension \
                                                 into a JSON file readable by Tableau')

    # define general options
    helptxt = 'Path to input NDJSON file from Zeeschuimer extension'
    parser.add_argument('-i', '--input-file', required=True, help=helptxt)
    helptxt = 'Path to output JSON file'
    parser.add_argument('-o', '--output-file', required=True, help=helptxt)

    # process provided arguments
    args = parser.parse_args()

    # use functions for file processing defined earlier
    content = open_ndjson(args.input_file)
    processed_content = convert_to_json(content)
    write_json(processed_content, args.output_file)


if __name__ == '__main__':
    main()
