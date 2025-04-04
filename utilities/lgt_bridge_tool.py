'''
    -----------------------------------------------------------------------
    lighting_bridge_tool
    -----------------------------------------------------------------------
    Description:   Quick-launch utility for software from within Maya
    Authors:       Craig Kane
    Email:         craig.kane@giant.ie
    Affiliation:   Giant Animation
    Version:       0.1 - 06/06/2024
    Tested on:     Maya 2022.3
    Updated by:    Craig Kane
    -----------------------------------------------------------------------

    Update History:
    - <Date of Update>: <Description of changes> (Updated by <Your Name>)

    '''

import maya.OpenMaya as om
import maya.cmds as cmds
import subprocess
import os


def nuke_bridge():

    om.MGlobal.displayInfo("Launching Nuke")
    cmds.inViewMessage(amg="Launching Nuke", pos="topCenter", fade=True)

    cmd = ["rez-env", "nuke-14", "nuke_pipeline-0", "-vv", "--", "Nuke14.0"]
    process = subprocess.Popen(cmd, env=os.environ)
    out, err = process.communicate()


    