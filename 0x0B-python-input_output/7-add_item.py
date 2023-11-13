#!/usr/bin/python3
"""Save argument to a file."""
import sys

if __name__ == "__main__":
    save_file = __import__('5-save_to_json_file').save_to_json_file
    load_json_file = __import__('6-load_from_json_file').load_from_json_file

    args = sys.argv[1:]

    try:
        objects = load_json_file("add_item.json")
    except FileNotFoundError:
        objects = []
    all_objects = objects + args
    save_file(all_objects, "add_item.json")
