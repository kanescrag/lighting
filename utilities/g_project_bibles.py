'''
    -----------------------------------------------------------------------
    giant_project_bibles
    -----------------------------------------------------------------------
    Description:   Tool to load projet bible pages
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


import os
import webbrowser
from lighting.scripts import sg_creds
from gfoundation import gcontext

#Get scene context
ctx = gcontext.Gcontext.get_from_env()
episode = ctx.episode
episode_lowercase = episode.lower()  
project_code = ctx.show 
episode = ctx.episode
shot_data = ctx.get_shot()
shot_id = shot_data['id']
shot_mpco = ctx.get_mpco()


# url paths

def generate_project_urls(project_code, url_type):
    base_url = f"https://sites.google.com/giant.ie/wiki/main/animation-dept/{project_code}-bible"
        
    urls = {
        "global": base_url,
        "overview": f"{base_url}/{project_code}_overview",
        "episodes": f"{base_url}/{project_code}_episodes",
        "characters": f"{base_url}/{project_code}_characters",
        "sets": f"{base_url}/{project_code}_sets"
    }
    
    url = urls.get(url_type)
    webbrowser.open_new_tab(url)

    