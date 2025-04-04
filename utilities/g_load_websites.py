'''
    -----------------------------------------------------------------------
    giant_load_websites
    -----------------------------------------------------------------------
    Description:   Tool to load specific websites based on conditions
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


import webbrowser
from maya import cmds
from gfoundation import gcontext
from lighting.scripts import sg_creds
import re
import os



#Get scene context
ctx = gcontext.Gcontext.get_from_env()
episode = ctx.episode
episode_lowercase = episode.lower()  
project_code = ctx.show 
episode = ctx.episode
shot_data = ctx.get_shot()
shot_id = shot_data['id']
shot_mpco = ctx.get_mpco()


def launch_project_project_page(project_code):  
    
    project_code = project_code.upper()
    
    #get active projects
    from lighting.scripts import sg_creds
    sg = sg_creds.sg_data()
    projects = sg.find("Project", filters=[["sg_status", "is", "Active"]], fields=["code", "name", "id", "tank_name"])

    # Find the project by its code and get its ID
    for project in projects:
        if project.get('code') == project_code:
            project_id = project.get('id')
            break  # Exit the loop once the project is found
    else:
        return None
     
    # Format the URL with the project ID
    url = f"https://giantanimation.shotgunstudio.com/page/project_overview?project_id={project_id}"
      
      
    #Open the webpage    
    webbrowser.open_new_tab(url)
    





def launch_shot_page(shot_id):
    url = f"https://giantanimation.shotgunstudio.com/detail/Shot/{shot_id}"
    os.system(f"start \"\" \"{url}\"")