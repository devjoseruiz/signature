"""! @brief Module that parses the given arguments to the program."""

##
# @file command_parser.py
#
# @brief Module that parses the given arguments to the program.
#
# @section description_command_parser Description
# Module that parses the given arguments to the program.
#

# Imports
import argparse

def parse():
    """! Define the rules to validate the arguments given to the program.
    @return     List object that contains the arguments as strings.
    """
    parser = argparse.ArgumentParser(
        description='Signature, a tool for updating bunches of email signatures',
        epilog='Copyleft 2021, José Ruiz <joseruiz@keemail.me>'
    )

    parser.add_argument(
        '-u', '--users',
        required=True,
        type=str,
        help='path to a .ods file that contains the users\' data'
    )

    parser.add_argument(
        '-s', '--signature',
        required=True,
        type=str,
        help='path to an .html file that contains the company signature'
    )

    parser.add_argument(
        '-c', '--cert',
        required=True,
        type=str,
        help='path to a .json file that contains the workspace credentials'
    )

    args = parser.parse_args()
    return args
