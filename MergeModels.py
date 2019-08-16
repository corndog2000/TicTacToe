#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Joseph Schroedl
# joe.schroedl@outlook.com
# https://github.com/corndog2000

import argparse
import os
import pickle

from TreeModel import Node

merge_count = 0


def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "dest_path", help="Path to merge destination file", type=str)
    parser.add_argument(
        "source_path", help="Path to data to merge file", type=str)

    return parser.parse_args()


def load_model(path):
    if not os.path.exists(path):
        print("ERROR: File does not exist")
        exit()

    with open(path, "rb") as read_file:
        data = pickle.load(read_file)
        return data


def save_model(path, data):
    with open(path, "wb") as write_file:
        pickle.dump(data, write_file)


def recurse(node1, node2):
    global merge_count

    for n1, n2 in zip(node1.children, node2.children):

        n1.wins += n2.wins
        n1.losses += n2.losses

        merge_count += 1
        #print("Completed node merge", merge_count)

        recurse(n1, n2)


def main(dest_path, source_path):
    dest_data = load_model(dest_path)
    source_data = load_model(source_path)

    recurse(dest_data, source_data)

    save_model(dest_path, dest_data)
    save_model(source_path, source_data)

    print(f"Done. Merged {merge_count} nodes.")


if __name__ == "__main__":
    args = parse_arguments()
    dest_path = args.dest_path
    source_path = args.source_path

    main(dest_path, source_path)
