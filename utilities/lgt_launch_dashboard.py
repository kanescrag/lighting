'''
    -----------------------------------------------------------------------
    lighting_shotgrid_launch_project
    -----------------------------------------------------------------------
    Description:   Tool to load the lgt dashboard
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
import maya.OpenMaya as om
from lighting.scripts import sg_creds
from gfoundation import gcontext

def launch_dashboard():  

    #Get scene context
    ctx = gcontext.Gcontext.get_from_env()
    episode = ctx.episode
    episode_lowercase = episode.lower()  
    project_code = ctx.show 
    episode = ctx.episode
    shot_data = ctx.get_shot()
    shot_id = shot_data['id']
    shot_mpco = ctx.get_mpco()
 
    project_code = project_code.upper()

    dashboard_id = 24539
    
    #import sg credentials
    from lighting.scripts import sg_creds
    sg = sg_creds.sg_data()

    # Find the project by its code and get its ID
    project = sg.find_one('Project', [['code', 'is', project_code]], ['id'])
    project_id = project['id'] if project else None
     
    # Format the URL with the project ID
    url = f"https://giantanimation.shotgunstudio.com/page/{dashboard_id}"

    print (f"This is the url: {url}")
    print (f"This is the project_id: {id}")
      
      
    #Feedback return   
    om.MGlobal.displayInfo(f"Url is {url}")
    om.MGlobal.displayInfo(f" -------- ")
    om.MGlobal.displayInfo("Opening Dashboard Page.....")

    #Open the webpage ----------------------------------------------------
    # Path to the Chrome executable
    chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    # Register Chrome as a new browser type
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    # Use the registered Chrome browser to open a URL
    webbrowser.get('chrome').open(url)