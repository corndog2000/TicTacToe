#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Joseph Schroedl
#joe.schroedl@outlook.com
#https://github.com/corndog2000

import argparse
import os
import pickle

import colorsys

from PIL import Image
from TreeModel import Node

colors = []

def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument("source_path", help="Path to data to merge file", type = str)

    return parser.parse_args()

def linear_map(value, low, high, newLow, newHigh):
        return newLow + ((value - low) / (high - low)) * (newHigh - newLow)

def hsv2rgb(h,s,v):
        return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))

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

def recurse(node):
    global colors
    
    for n in node.children:

        colors.append(n.rank())

        recurse(n)

def main(source_path):
    source_data = load_model(source_path)

    recurse(source_data)

    print(len(colors))

    img = Image.new("RGB", (1920,1080), "black") # Create new black image
    pixels = img.load() # Create the pixel map

    color_idx = 0
    mapped_rank = 0

    for i in range(img.size[0]):    # For every pixel:
        for j in range(img.size[1]):
            if color_idx >= len(colors):
                break

            #mapped_rank = linear_map(colors[color_idx], 0, 1, 0, 255)
            
            if colors[color_idx] == 0:
                convert_color = hsv2rgb(0, 0, 0)
            else:
                convert_color = hsv2rgb(colors[color_idx], 1, 1)
            #print(colors[color_idx], mapped_rank)
            
            if j % 2 == 0:
                color_idx += 1

            pixels[i,j] = convert_color # Set the colour accordingly

    img.save("out.bmp")
    img.show()

    print("Done")


if __name__ == "__main__":
    args = parse_arguments()
    source_path = args.source_path
    
    main(source_path)