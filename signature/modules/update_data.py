"""! @brief Module that updates the signatures."""

##
# @file update_data.py
#
# @brief Module definition.
#
# @section description_update_data Description
# Module definition.
#

# Imports
from googleapiclient.discovery import build
from googleapiclient.errors import *
from google.auth.exceptions import *

def update_user_sig(credentials, user_data, sig_template):
    """! Update the users' signature.

    @param credentials      Google workspace credentials.
    @param user_data        Users' data.
    @param sig_template     Signature template.
    """
    username    = user_data[0]
    first_name  = user_data[1]
    last_name   = user_data[2]
    full_name   = "%s %s" % (first_name, last_name)
    job_title   = user_data[3]
    telephone   = user_data[4]

    # Insert the user data into the custom template.
    sig = sig_template.substitute(full_name=full_name, job_title=job_title,
                                  telephone=telephone, email=username)
    # Get access using credentials.
    credentials_delegated = credentials.with_subject(username)
    gmail_service = build("gmail", "v1", credentials=credentials_delegated)
    addresses = gmail_service.users().settings().sendAs().list(userId='me',
                        fields='sendAs(isPrimary,sendAsEmail)').execute().get('sendAs')
    # Search for the main email address of the user.
    address = None
    for address in addresses:
        if address.get('isPrimary'):
            break
    # Update the signature.
    if address:
        rsp = gmail_service.users().settings().sendAs().patch(userId='me',
                    sendAsEmail=address['sendAsEmail'],
                    body={'signature':sig}).execute()
        print(f"Signature changed for: {username}")
    else:
        print(f"Could not find primary address for: {username}")
