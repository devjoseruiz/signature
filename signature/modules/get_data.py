"""! @brief Module that get the files required for the program operations."""

##
# @file get_data.py
#
# @brief Module that get the files required for the program operations.
#
# @section description_get_data Description
# Module that get the files required for the program operations.
#

# Imports
from string import Template
from google.oauth2 import service_account
import pandas as pd

def get_credentials(file_path):
    """! Get the file that contains the Google workspace credentials.
    
    @param file_path    Path to the file.
    @return             Access token.
    """
    scopes = ['https://www.googleapis.com/auth/gmail.settings.basic',
        'https://www.googleapis.com/auth/gmail.settings.sharing']

    try:
        credentials = service_account.Credentials.from_service_account_file(file_path, scopes=scopes)
    except:
        print("No credentials found, so stopping")
        exit(1)
    else:
        return credentials

def get_signature(file_path):
    """! Get the file that contains the signature template.
    
    @param file_path    Path to the file.
    @return             Template content.
    """
    try:
        sig_file = open(file_path, "r")
        sig_template = Template(sig_file.read())
    except:
        print("No signature file found, so stopping")
        exit(1)
    else:
        return sig_template

def get_users(file_path):
    """! Get the file that contains the users' info.
    
    @param file_path      Path to the file.
    @return               List object with users' info.
    """
    try:
        user_data = pd.ExcelFile(file_path, engine="odf")
        df = user_data.parse("livedata")
    except:
        print("No users\' data file found, so stopping")
        exit(1)
    else:
        return df.values
