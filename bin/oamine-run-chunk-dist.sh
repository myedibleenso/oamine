#!/usr/bin/env bash

# FIXME: make this a Python script w/ argparse

CPT_DIR=/path/to/preprocess/pkl
OUTPUT_DIR=/path/to/output

python launch_chunk.py --cpt_dir $CPT_DIR --output_dir $OUTPUT_DIR
