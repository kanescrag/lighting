'''
-----------------------------------------------------------------------
giant_mpco_broser
-----------------------------------------------------------------------
Description:   Tool to quickly access MPCO data and pages + hierarchy
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
import urllib.request
import maya.cmds as cmds
import webbrowser
from lighting.scripts import sg_creds
from gfoundation import gcontext
from shared.scripts import giant_shotgrid_data
import importlib

importlib.reload(giant_shotgrid_data)

# Get scene data
sg = sg_creds.sg_data()
ctx = gcontext.Gcontext.get_from_env()
episode = ctx.episode
project_code = ctx.show
task_type = ctx.get_shot_type()
sequence_code = ctx.sequence

# Get the current shot ID from context
current_shot_id = giant_shotgrid_data.get_shot_id()

def mpco_window():

    if task_type == 'Set':
        cmds.warning(f"MPCO can only be run in shot context. Currently in {task_type} context.")
        pass

    else:

        sequence_id = giant_shotgrid_data.get_sequence_id(sequence_code, project_code, sg)
        shot_ids = giant_shotgrid_data.get_shot_id_from_sequence_id(sequence_id, sg)

        def get_shot_info(shot_ids):
            filters = [['id', 'in', shot_ids]]
            fields = ['id', 'code', 'sg_light_rig_parent', 'sg_mpco']
            shots = sg.find('Shot', filters, fields)
            return shots

        shots_info = get_shot_info(shot_ids)

        # Find the current shot's code from the shot IDs
        current_shot_code = None
        for shot in shots_info:
            if shot['id'] == current_shot_id:
                current_shot_code = shot['code']
                break

        def download_image(url, filename):
            try:
                urllib.request.urlretrieve(url, filename)
            except Exception as e:
                print(f"Error downloading image: {e}")

        def create_mpco_browser_gui():
            global shot_dropdown, parent_text_scroll, child_text_scroll, master_shots_scroll, parent_shot_info, parent_shot_label, child_shot_label, master_shot_label, image_box

            # Maya GUI window
            window_name = 'MPCO_Browser'
            if cmds.window(window_name, exists=True):
                cmds.deleteUI(window_name)

            cmds.window(window_name, title="MPCO_Browser", iconName='Short Name', widthHeight=(800, 500), tbm=True, s=False)
            cmds.columnLayout(adjustableColumn=True)

            cmds.separator(height=20, style='doubleDash')
            cmds.text('MPCO Browser')
            cmds.separator(height=30)

            # First row: Select a shot dropdown and master shots scroll box
            cmds.rowLayout(nc=3, adjustableColumn=True, columnWidth3=(200, 100, 300))

            # Column 1: Select a shot dropdown
            cmds.columnLayout(adjustableColumn=True, width=200)
            cmds.text(label="Select a shot:")
            cmds.separator(height=5, style='none')
            shot_dropdown = cmds.optionMenu(cc=update_text_box)

            # Add each shot's code and mpco result to the dropdown
            for shot in shots_info:
                shot_id = shot['id']
                shot_code = shot['code']
                mpco_value = shot.get('sg_mpco', '-')
                label = f"{shot_code} - [{mpco_value}]"
                cmds.menuItem(label=label, parent=shot_dropdown)

            # Set the current shot as the default selection in the dropdown
            if current_shot_code:
                cmds.optionMenu(shot_dropdown, edit=True, value=f"{current_shot_code} - [{shots_info[shot_ids.index(current_shot_id)].get('sg_mpco', '-')}]")

            cmds.setParent('..')  # Return to the row layout

            # Add an empty space (for padding) between the dropdown and the master shots scroll box
            cmds.columnLayout(adjustableColumn=True, width=100)  # This column will act as a spacer
            cmds.setParent('..')  # Return to the row layout

            # Column 2: Master Shots Scroll Box
            cmds.columnLayout(adjustableColumn=True, width=300)
            master_shot_label = cmds.text(label="Master Shots [0]:")
            cmds.separator(height=5, style='none')
            master_shots_scroll = cmds.textScrollList(numberOfRows=2, dcc=open_master_shot_url)  # Use dcc for double-click

            cmds.setParent('..')  # Return to the row layout

            cmds.setParent('..')  # Return to the main column layout

            cmds.separator(height=20, style='doubleDash')

            # Second row: Scroll windows for Parent Shot and Child Shots
            cmds.rowLayout(nc=2, adjustableColumn=True, columnWidth2=(400, 400))

            # Column 1 for Parent Shot Scroll Box
            cmds.columnLayout(adjustableColumn=True, width=400)
            parent_shot_label = cmds.text(label="Parent Shot [0]:")
            cmds.separator(height=5, style='none')
            parent_text_scroll = cmds.textScrollList(numberOfRows=5, dcc=open_shot_url)  # Use dcc for double-click
            cmds.setParent('..')  # Return to the row layout

            # Column 2 for Child Shots Scroll Box
            cmds.columnLayout(adjustableColumn=True, width=400)
            child_shot_label = cmds.text(label="Child Shots [0]:")
            cmds.separator(height=5, style='none')
            child_text_scroll = cmds.textScrollList(numberOfRows=5, allowMultiSelection=False, dcc=open_child_shot_url)  # Use dcc for double-click
            cmds.setParent('..')  # Return to the row layout

            cmds.setParent('..')  # Return to the main column layout

            cmds.separator(height=20, style='doubleDash')

            
            cmds.showWindow(window_name)

            # Populate the initial data based on the current shot
            update_text_box()

        def update_text_box(*args):
            selected_shot_code = cmds.optionMenu(shot_dropdown, query=True, value=True).split(' - ')[0]
            global parent_shot_info

            # Find the selected shot
            selected_shot = None
            for shot in shots_info:
                if shot['code'] == selected_shot_code:
                    selected_shot = shot
                    break
            
            if selected_shot:
                # Update parent text scroll
                light_rig_parent = selected_shot.get('sg_light_rig_parent')
                if light_rig_parent:
                    parent_shot_info = light_rig_parent
                    light_rig_parent_code = light_rig_parent.get('name', 'No parent assigned')
                else:
                    parent_shot_info = None
                    light_rig_parent_code = 'No parent assigned'
                cmds.textScrollList(parent_text_scroll, edit=True, removeAll=True)
                if light_rig_parent_code != 'No parent assigned':
                    cmds.textScrollList(parent_text_scroll, edit=True, append=[light_rig_parent_code])
                cmds.text(parent_shot_label, edit=True, label=f"Parent Shot [{cmds.textScrollList(parent_text_scroll, query=True, numberOfItems=True) if light_rig_parent_code != 'No parent assigned' else 0}]")

                # Update child shots scroll
                child_shots = get_child_shots(selected_shot['id'])
                cmds.textScrollList(child_text_scroll, edit=True, removeAll=True)
                if child_shots:
                    cmds.textScrollList(child_text_scroll, edit=True, append=[shot['code'] for shot in child_shots])
                else:
                    cmds.textScrollList(child_text_scroll, edit=True, append=["No child shots"])
                cmds.text(child_shot_label, edit=True, label=f"Child Shots [{cmds.textScrollList(child_text_scroll, query=True, numberOfItems=True) if child_shots else 0}]")

                # Update master shots scroll
                update_master_shots_scroll()

        def get_child_shots(parent_shot_id):
            child_shots = []
            for shot in shots_info:
                if shot['sg_light_rig_parent'] and shot['sg_light_rig_parent']['id'] == parent_shot_id:
                    child_shots.append(shot)
            return child_shots

        def update_master_shots_scroll():
            master_shots = get_master_shots()
            cmds.textScrollList(master_shots_scroll, edit=True, removeAll=True)
            if master_shots:
                cmds.textScrollList(master_shots_scroll, edit=True, append=[shot['code'] for shot in master_shots])
            else:
                cmds.textScrollList(master_shots_scroll, edit=True, append=["No master shots"])
            cmds.text(master_shot_label, edit=True, label=f"Master Shots [{cmds.textScrollList(master_shots_scroll, query=True, numberOfItems=True) if master_shots else 0}]")

        def get_master_shots():
            master_shots = []
            for shot in shots_info:
                if shot.get('sg_mpco') == 'Master':
                    master_shots.append(shot)
            return master_shots

        def open_shot_url(*args):
            global parent_shot_info
            if parent_shot_info:
                entity_type = parent_shot_info.get('type')
                entity_id = parent_shot_info.get('id')
                if entity_type == 'Shot':
                    url = f"https://giantanimation.shotgunstudio.com/detail/Shot/{entity_id}"
                elif entity_type == 'Asset':
                    url = f"https://giantanimation.shotgunstudio.com/detail/Asset/{entity_id}"
                webbrowser.open(url)

        def open_child_shot_url(*args):
            selected_child = cmds.textScrollList(child_text_scroll, query=True, selectItem=True)
            if selected_child:
                child_shot_code = selected_child[0]
                # Find shot ID from shot code
                child_shot_id = None
                for shot in shots_info:
                    if shot['code'] == child_shot_code:
                        child_shot_id = shot['id']
                        break
                if child_shot_id:
                    url = f"https://giantanimation.shotgunstudio.com/detail/Shot/{child_shot_id}"
                    webbrowser.open(url)

        def open_master_shot_url(*args):
            selected_master = cmds.textScrollList(master_shots_scroll, query=True, selectItem=True)
            if selected_master:
                master_shot_code = selected_master[0]
                # Find shot ID from shot code
                master_shot_id = None
                for shot in shots_info:
                    if shot['code'] == master_shot_code:
                        master_shot_id = shot['id']
                        break
                if master_shot_id:
                    url = f"https://giantanimation.shotgunstudio.com/detail/Shot/{master_shot_id}"
                    webbrowser.open(url)

        create_mpco_browser_gui()
