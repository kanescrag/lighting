'''
    -----------------------------------------------------------------------
    giant_lighting_toolkit
    -----------------------------------------------------------------------
    Description:   Lighting toolkit. Small conditiona-based script to manage light creation and assign common light attributes such as light group name,
    outliner structure and modify several default values when created to make it easier to work with
    lights upon creation. Appends lights under a 'set lights' group when created within the set task context, and under 'shot lights' within a shot context

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

import maya.cmds as cmds
import maya.mel as mel
import json
import os
from gfoundation import gcontext

# Get Shotgun task context
context = gcontext.Gcontext.get_from_env()
giant_context = context.get_shot_type()
shot_code = context.shot

# Get scene renderer
render_engine = context.showspec['renderer']

def launch_lighting_toolkit():

    # JSON IMPORT --------

    # Path to the JSON file
    file_path = r"Z:/studio_tools/pipe2/facility/maya/utilities/lighting/scripts/profiles/lgt_renderer_configurations.json"

    # Read the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Extract outliner structures
    naming_conventions = data.get('naming_conventions', {})

    # Extract data for renderer based on context
    render_engine_data = data.get('renderers', {}).get(render_engine, {})

    # Extract outliner structure names
    lights_group_name = naming_conventions.get('lights_group_name', 'Lights')
    set_lights_group_name = naming_conventions.get('set_lights_group_name', 'set_lights')
    shot_lights_group_name = naming_conventions.get('shot_lights_group_name', 'shot_lights')
    set_lights_utility_group_name = naming_conventions.get('shot_lights_group_name', 'shot_utilities')
    sht_lights_utility_group_name = naming_conventions.get('shot_lights_group_name', 'shot_utilities')
    light_suffix = naming_conventions.get('light_suffix', '_light')

    def create_outliner_structure(selected_category):
        """Create master and subgroup in Outliner based on the context and selected category."""

        # Create the master light group if it doesn't exist
        if not cmds.objExists(lights_group_name):
            cmds.group(em=True, name=lights_group_name)

        # Create the appropriate subgroup based on the giant_context
        if giant_context == 'Set':
            subgroup_name = set_lights_group_name
        else:
            subgroup_name = shot_lights_group_name

        if not cmds.objExists(subgroup_name):
            cmds.group(em=True, name=subgroup_name, parent=lights_group_name)

        # Create the selected category group within the subgroup
        if selected_category == 'primary':
            target_group_name = f"{subgroup_name}_primary"
            if not cmds.objExists(target_group_name):
                cmds.group(em=True, name=target_group_name, parent=subgroup_name)
            return target_group_name
        elif selected_category == 'secondary':
            target_group_name = f"{subgroup_name}_secondary"
            if not cmds.objExists(target_group_name):
                cmds.group(em=True, name=target_group_name, parent=subgroup_name)
            return target_group_name
        else:
            raise ValueError("Invalid category selected")

    def create_light(*args):
        """Create the light based on the user input and add it to the appropriate Outliner group."""
        selected_light_type = cmds.optionMenu(light_type_menu, query=True, value=True)
        custom_name = cmds.textField(light_name_field, query=True, text=True)
        light_category = cmds.optionMenu(light_category_menu, query=True, value=True)

        # Ensure a valid light category is selected
        if light_category == 'Select Category':
            cmds.confirmDialog(title="Selection Error", message="Please select a light category before creating a light.", button=["OK"], defaultButton="OK")
            return

        # Default to 'default_light' if no custom name is provided
        base_light_name = custom_name if custom_name else "default_light"

        # Concatenate light name and suffix
        if giant_context == "Set":
            light_name = f"{shot_code}_{base_light_name}{light_suffix}"
        elif giant_context == "Shot":
            light_name = f"{base_light_name}{light_suffix}"

        # Check if a light with the same name already exists
        if cmds.objExists(light_name):
            cmds.confirmDialog(title="Light Name Exists", message=f"A light with the name '{light_name}' already exists. Please choose a different name.", button=["OK"], defaultButton="OK")
            return

        # Create the Outliner structure and get the correct subgroup based on selected category
        target_group = create_outliner_structure(light_category)

        # Create Light
        created_light = cmds.createNode(selected_light_type)

        # Identify the transform node (root node) of the newly created light
        transform_node = cmds.listRelatives(created_light, parent=True)[0]

        # Rename the transform node to the desired light name
        new_light = cmds.rename(transform_node, light_name)

        # Parent the created light under the appropriate subgroup
        cmds.parent(new_light, target_group)

        # Set additional attributes
        aov_attribute_name = render_engine_data.get('aov_attribute_name', 'aov')
        if aov_attribute_name:
            cmds.setAttr(f'{light_name}.{aov_attribute_name}', light_name, type="string")

    def update_light_types(render_engine):
        """Update the light types in the option menu based on the renderer."""
        light_list = render_engine_data.get('lights', [])

        cmds.optionMenu(light_type_menu, edit=True, deleteAllItems=True)
        for light in light_list:
            cmds.menuItem(parent=light_type_menu, label=light)
        print(f"Updated light types for renderer: {render_engine}")

    def lighting_toolkit():
        # Create the UI
        if cmds.window("Lighting_Toolkit", exists=True):
            cmds.deleteUI("Lighting_Toolkit")

        window = cmds.window('Lighting_Toolkit', title="Lighting Toolkit", iconName='Short Name', widthHeight=(350, 450), tb=True, s=False)
        cmds.columnLayout(adjustableColumn=True, cat=['both', 20])
        cmds.separator(height=20, style='doubleDash')
        cmds.text('LIGHTING TOOLKIT')
        cmds.separator(height=30)
        cmds.iconTextButton(style='iconOnly', image1="Z:/studio_tools/pipe2/facility/maya/utilities/lighting/icons/lgt_bulb3.png", label='sphere')
        cmds.separator(height=30)
        cmds.text(f'Renderer: {render_engine}')
        cmds.separator(height=30)

        cmds.text('Light Type')
        global light_type_menu
        cmds.separator(height=5, style='none')
        light_type_menu = cmds.optionMenu()
        update_light_types(render_engine)  # Use the renderer from context

        cmds.separator(height=20)
        cmds.text('Light Category')
        global light_category_menu
        cmds.separator(height=5, style='none')
        light_category_menu = cmds.optionMenu()
        # Add a placeholder item
        cmds.menuItem(label='Select Category', enable=False)
        cmds.menuItem(label='primary')
        cmds.menuItem(label='secondary')

        cmds.separator(height=20)
        cmds.text('Custom Light Name')
        global light_name_field
        cmds.separator(height=5, style='none')
        light_name_field = cmds.textField(text="")  # Initialize as blank

        cmds.separator(height=20)
        cmds.button(label='Create Light', command=create_light)
        cmds.separator(height=5)
        cmds.button(label='Close', command=lambda *args: cmds.deleteUI(window, window=True))
        cmds.separator()

        cmds.setParent('..')
        cmds.showWindow(window)

    # Run the toolkit
    lighting_toolkit()
