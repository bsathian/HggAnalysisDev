import argparse

from helpers import prep_helper

"""
This script writes events to an hdf5 file for BDT/DNN training.
"""

parser = argparse.ArgumentParser()
parser.add_argument(
    "--input",
    help = "path to input ntuple",
    type = str,
)
parser.add_argument(
    "--debug",
    help = "debug level",
    type = int,
    default = 0
)
parser.add_argument(
    "--output",
    help = "name of output hdf5 file",
    type = str,
    default = "test.hdf5"
)

args = parser.parse_args()

prepper = prep_helper.PrepHelper(**vars(args))
prepper.run()
