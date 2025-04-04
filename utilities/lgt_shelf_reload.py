'''
    -----------------------------------------------------------------------
    giant_shelf_reload
    -----------------------------------------------------------------------
    Description:   Tool to refresh python shelves in a Maya session
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

# Import libraries
import maya.OpenMaya as om
from lighting.shelf.python_shelf import LGT_TK
import maya.cmds as cmds
import importlib
import sys

def rebuild_shelf():
    try:
        #delete shelf
        cmds.deleteUI('LGT_TK')
        #create shelf
        from lighting.shelf.python_shelf import LGT_TK
        LGT_TK.g_lighting_shelf()
        om.MGlobal.displayInfo("Shelf reloaded successfully")
        cmds.inViewMessage(amg="Shelf reloaded successfully", pos="topCenter", fade=True)

    except:
        om.MGlobal.displayInfo("Shelf failed to reloaded successfully")
        cmds.inViewMessage(amg="Shelf failed to reloaded successfully", pos="topCenter", fade=True)


    
    


