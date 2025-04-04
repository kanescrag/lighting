'''
-----------------------------------------------------------------------
giant_shotgrid_launch_task
-----------------------------------------------------------------------
Description:   Tool to load selected task pages
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
import maya.OpenMaya as om
import maya.cmds as cmds
from lighting.scripts import sg_creds
from gfoundation import gcontext

# Get scene data
sg = sg_creds.sg_data()
ctx = gcontext.Gcontext.get_from_env()
episode = ctx.episode
project_code = ctx.show 
shot_data = ctx.get_shot()
shot_id = shot_data['id']
task_type = ctx.get_shot_type()

def launch_task_window():
    try:
        # Initialize progress window
        progress_title = "Loading Giant Shotgrid Launch Task"
        progress_message = "Loading Shot Task Launcher..."
        cmds.progressWindow(title=progress_title, progress=0, status=progress_message, isInterruptable=False)

        # Delay for demonstration purposes (simulate loading)
        cmds.progressWindow(edit=True, progress=20, status="Fetching scene data...")

        cmds.progressWindow(edit=True, progress=40, status="Fetching tasks...")

        # Get tasks for the given shot ID
        if task_type == 'Shot':
            filters = [['entity', 'is', {'type': 'Shot', 'id': shot_id}]]
        elif task_type == 'Set':
            filters = [['entity', 'is', {'type': 'Asset', 'id': shot_id}]]
        fields = ['content']
        tasks = sg.find('Task', filters, fields)
        task_list = [task['content'] for task in tasks]

        cmds.progressWindow(edit=True, progress=60, status="Filtering tasks with version uploads...")

        # List only existing task publishes with version uploads
        tasks_with_version_uploads = []
        for task in tasks:
            task_versions = sg.find('Version', [['sg_task', 'is', {'type': 'Task', 'id': task['id']}]], ['id', 'sg_uploaded_movie', 'sg_uploaded_movie_link'])
            if any(version.get('sg_uploaded_movie') or version.get('sg_uploaded_movie_link') for version in task_versions):
                tasks_with_version_uploads.append(task['content'])

        cmds.progressWindow(edit=True, progress=80, status="Creating UI...")

        # Close progress window before creating UI
        cmds.progressWindow(endProgress=True)

        # Create UI after progress window is closed
        create_dropdown_with_tasks(tasks_with_version_uploads)

    except Exception as e:
        cmds.progressWindow(endProgress=True)
        om.MGlobal.displayError(f"Error occurred: {str(e)}")

def create_dropdown_with_tasks(task_names):
    task_window = 'shot_task_launcher'
    
    if cmds.window(task_window, exists=True):
        cmds.deleteUI(task_window)
    
    window = cmds.window(task_window,  title="Shot Task Launcher", iconName='Short Name', widthHeight=(350, 325), tbm=True, s=False)
    cmds.columnLayout(adjustableColumn=True, cat=['both', 20])
    cmds.separator(height=20, style='doubleDash')
    cmds.text('SHOT TASK LAUNCHER')
    cmds.separator(height=30)
    cmds.rowLayout(nc=1, columnWidth1=350, adjustableColumn=True)
    cmds.iconTextButton(style='iconOnly', image1="Z:/studio_tools/pipe2/facility/maya/utilities/shared/icons/SG_small.png", label='sphere', enableBackground=False)
    cmds.setParent('..')  # Return to the column layout
    
    cmds.separator(height=30)
    cmds.text('Task')
    cmds.separator(height=30)
    dropdown = cmds.optionMenu('task_dropdown', label='', width=300)
    for task_name in task_names:
        cmds.menuItem(label=task_name)

    cmds.separator(height=10, style='none')

    def on_button_click(*args):
        selection = cmds.optionMenu(dropdown, query=True, value=True)
        launch_task_page(selection, task_type)
    
    cmds.separator(height=30)
    cmds.button(label='Launch Task Page', command=on_button_click)
    cmds.separator()
    
    cmds.showWindow(task_window)

def launch_task_page(selection, task_type):
    try:
        # Get scene context
        ctx = gcontext.Gcontext.get_from_env()
        episode = ctx.episode
        project_code = ctx.show
        
        # Get active projects
        from lighting.scripts import sg_creds
        sg = sg_creds.sg_data()
        
        # Get project id
        project = sg.find_one('Project', [['name', 'is', project_code]], ['id'])
        project_id = project['id'] if project else None
        
        if task_type == 'Shot':
            # Get task id for shot context
            task = sg.find_one('Task', [['entity', 'is', {'type': 'Shot', 'id': shot_id}], ['content', 'is', selection]], ['id', 'content'])

            if task:
                # Find the latest version of this task
                version = sg.find_one('Version', [['sg_task', 'is', {'type': 'Task', 'id': task['id']}]], ['id', 'code', 'sg_uploaded_movie'], order=[{'field_name': 'created_at', 'direction': 'desc'}])
                
                if version:
                    # Format the URL with the task ID
                    task_url = f"https://giantanimation.shotgunstudio.com/detail/Version/{version['id']}"
                    print(f"Task URL: {task_url}")
                    om.MGlobal.displayInfo(f"Launching shot {selection} task page...")
                    webbrowser.open_new_tab(task_url)
                else:
                    om.MGlobal.displayWarning(f"Version for {selection} task does not exist.")
            else:
                om.MGlobal.displayWarning(f"Task {selection} does not exist for shot {shot_id}.")
        
        elif task_type == 'Set':
            
            # Get task id for asset context
            task = sg.find_one('Task', [['entity', 'is', {'type': 'Asset', 'id': shot_id}], ['content', 'is', selection]], ['id', 'content'])

            if task:
                # Find the latest version of this task
                version = sg.find_one('Version', [['sg_task', 'is', {'type': 'Task', 'id': task['id']}]], ['id', 'code', 'sg_uploaded_movie'], order=[{'field_name': 'created_at', 'direction': 'desc'}])
                
                if version:
                    # Format the URL with the task ID
                    task_url = f"https://giantanimation.shotgunstudio.com/detail/Version/{version['id']}"
                    print(f"Task URL: {task_url}")
                    om.MGlobal.displayInfo(f"Launching asset {selection} task page...")
                    webbrowser.open_new_tab(task_url)
                else:
                    om.MGlobal.displayWarning(f"Version for {selection} asset task does not exist.")
            else:
                om.MGlobal.displayWarning(f"Task {selection} does not exist for asset.")
        
        else:
            om.MGlobal.displayError(f"Unsupported task_type: {task_type}")
    
    except Exception as e:
        om.MGlobal.displayError(f"Error occurred: {str(e)}")

# Call launch_task_window() only once to initiate the process
if __name__ == "__main__":
    launch_task_window()
