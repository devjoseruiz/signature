#!/usr/bin/env python3

"""! @brief Signature GUI"""

##
# @mainpage Signature GUI
#
# @section description_signature Description
# Signature GUI is a wrapper that brings a graphical interface for Signature.
#
# @section author_signature Author(s)
# - José Ruiz.
#

##
# @file main.py
#
# @brief Main function of the project.
#
# @section description_main Description
# Main function of the project.
#
# @section libraries_main Libraries
# - easygui
#   - EasyGUI is a module for very simple, very easy GUI programming in Python.
#

# Imports
import os
from subprocess import PIPE, run
import tkinter
import easygui as gui

def main():
    # Require the credentials file to get the access token to the workspace
    cert_path = gui.fileopenbox(
            msg="Please, choose the .json file for authentication",
            title="Signature GUI | Choose the .json file",
            default="*.json"
        )
    
    try:
        os.path.exists(cert_path)
    except Exception:
        gui.msgbox(msg="File invalid or not found", title="Signature GUI | Error")
        raise

    # Require the .ods file that contains the users' info
    ods_path = gui.fileopenbox(
            msg="Please, choose the .ods file that contains the users' info",
            title="Signature GUI | Choose the .ods file",
            default="*.ods"
        )

    try:
        os.path.exists(ods_path)
    except Exception:
        gui.msgbox(msg="File invalid or not found", title="Signature GUI | Error")
        raise

    # Require the HTML file that contains the signature template
    template_path = gui.fileopenbox(
            msg="Please, choose the .html file that contains the signature template",
            title="Signature GUI | Choose the .html file",
            default="*.html"
        )
    
    try:
        os.path.exists(template_path)
    except Exception:
        gui.msgbox(msg="File invalid or not found", title="Signature GUI | Error")
        raise

    gui.msgbox(
            msg="Please, be patient until the process finishes. " + \
                "This can take some minutes... Accept to start.",
            title="Please, wait...",
            ok_button="Start"
        )

    # Call the Signature CLI tool
    command = "signature -c {} -u {} -s {}".format(cert_path, ods_path, template_path)
    output = run(
            command,
            stdout=PIPE,
            stderr=PIPE,
            universal_newlines=True,
            shell=True
        )

    # Display the log output
    gui.codebox(msg="Please, check the execution log", title="Signature GUI | Log output", text=output.stdout)

if __name__ == "__main__":
    main()
