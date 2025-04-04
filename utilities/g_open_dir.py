"""
-----------------------------------------------------------------------
giant_open_publish_dir
-----------------------------------------------------------------------
Description:   Tool to open the current project publish dir. "Type" arguments == "work", "publish" etc.
Authors:       Craig Kane
Email:         craig.kane@giant.ie
Affiliation:   Giant Animation
Version:       0.1 - 11/07/2024
Tested on:     Maya 2022.3
Updated by:    Craig Kane
-----------------------------------------------------------------------

Update History:
- <DD/MM/YYYY>: <Description of changes> (Updated by <Your Name>)

"""

import webbrowser
import maya.OpenMaya as om
from lighting.scripts import sg_creds
from gfoundation import gcontext
import subprocess
import os

def reveal_directory(directory_type):
    # Get scene data
    sg = sg_creds.sg_data()
    ctx = gcontext.Gcontext.get_from_env()
    department = ctx.department.upper()
    project = ctx.show.upper()
    episode = ctx.episode
    sequence = ctx.sequence
    shot = ctx.shot

    path_pixstor = f"\\\\pixstor\\{project}\\episodes\\{episode}\\{sequence}\\{shot}\\{directory_type}\\{department}"
    path_remotestor = f"S:\\episodes\\{episode}\\{sequence}\\{shot}\\{directory_type}\\{department}"

    # Determine path based on project
    if project == 'FOPR':
        path = os.path.normpath(path_pixstor)
    elif project == 'EGH':
        path = os.path.normpath(path_remotestor)
    else:
        om.MGlobal.displayWarning(f"Unknown project: {project}")
        return

    open_in_explorer(path)

def open_in_explorer(path):
    # Check if the path exists
    if os.path.exists(path):
        # Open the path in Windows Explorer
        om.MGlobal.displayInfo(f"Opening: {path}")
        subprocess.Popen(f'explorer "{path}"')
    else:
        om.MGlobal.displayWarning(f"Path '{path}' does not exist.")