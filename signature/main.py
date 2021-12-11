#!/usr/bin/env python3

"""! @brief Signature"""

##
# @mainpage Signature
#
# @section description_signature Description
# Signature is a tool for updating bunches of corporate email signatures.
#
# @section author_signature Author(s)
# - José Ruiz.
#

##
# @file main.py
#
# @brief Main function of the program.
#
# @section description_main Description
# Main function of the program.
#
# @section libraries_main Libraries
# - argparse
#   - Facilitates the development of parsers for CLI applications.
# - google.oauth2
#   - Allows authentication using Google services credentials.
# - googleapiclient
#   - Facilitates the interaction with the Google API.
# - pandas
#   - Optimized library for operating with data structures.
#

# Imports
import time
from modules.command_parser import *
from modules.get_data import *
from modules.update_data import *

def main():
    # Parse the arguments given to the application.
    args = parse()
    # Get the Google workspace credentials.
    credentials = get_credentials(args.cert)
    # Get the HTML template for signatures.
    signature = get_signature(args.signature)
    # Get the users' info.
    users = get_users(args.users)

    # Read the users' data contained in the document.
    for datarow in users:
        email_addr = datarow[0]
        try:
            # Updates the signature for each user.
            update_user_sig(credentials, datarow, signature)
        except (RefreshError, TransportError) as e:
            print(f"Error encountered for: {email_addr}. Error was: {e}")
            continue
        except Exception as e:
            raise

if __name__ == "__main__":
    main()
