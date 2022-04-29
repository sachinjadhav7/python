#!/usr/bin/env python3

import os
import shutil
import webbrowser
from shutil import make_archive
from colorama import init, Fore
import configparser as MCP
import configparser as RCP


# Intializing the Colorama package
init(autoreset=True)

Spec_gen_Msg = Fore.BLUE + '''Interface specification generation is in progress ...'''
Success_Msg = Fore.GREEN + 'Interface specification is ready '
errorMsg = Fore.RED + 'Exited from zip file creation of Interface spec release...'
successMsg_open = Fore.BLUE + 'Opening interface spec file is in progress ...'
successMsg = Fore.GREEN + ' Interface spec release zip generated successfully'

Git_Credentials = {}

# create index page of the interface spec
def generateIndexPage(currentworkingdir, dictvalue, changlogdict):
    indexstring = '/*!\n\mainpage\n <table>\n<tr><th>Service <th>Current version' \
                  '	<th>Changes from last delivery\n '
    tablerow_string = ""
    # creating the reference in the index
    for key, value in dictvalue.items():
        for changelogkey, changelogvalue in changlogdict.items():

            if key == changelogkey:
                # Finding the services repo fix version to manipulate the mainpage
                fixversion = BCP.getServiceRepoTag(key)
                if 0 == len(fixversion):  # service repo tag version is empty then look for master services tag version
                    fixversion = MCP.getMasterServiceRepoTag(key)
                else:
                    fixversion = BCP.getServiceRepoTag(key)

                tablerow_string = '<tr><td><a href="' + value + '">' + key + '</a>' + '<td>' + fixversion.strip() \
                                  + ' <td>' + changelogvalue + '\n'
                break
        indexstring += tablerow_string
    indexpagefile = util.getreleasePath(currentworkingdir) + "/Mainpage.dox"

    # creating documentation main page with index content to generate index
    with open(indexpagefile, "w") as file:
        indexstring += "</table>\n*/"
        file.write(indexstring)
        file.close()


