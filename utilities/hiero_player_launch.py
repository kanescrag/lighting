import os
import pathlib
import subprocess
import maya.OpenMaya as om
import maya.cmds as cmds
from lighting.scripts import sg_creds
from gfoundation import gcontext
import re

# Get scene data
sg = sg_creds.sg_data()
ctx = gcontext.Gcontext.get_from_env()
episode = ctx.episode
project_code = ctx.show
shot_data = ctx.get_shot()
shot_id = shot_data['id']

def hiero_launcher():

    def hiero_player_launch(path):
        nukeExe = r"C:\Program Files\Nuke14.0v4\Nuke14.0.exe"
        subprocess.Popen('"' + nukeExe + '" --player ' + path)

    def latest_version_list():
        # Initialize progress window
        progress_title = "Loading Giant Shotgrid Launch Task"
        progress_message = "Loading Shot Task Launcher..."
        cmds.progressWindow(title=progress_title, progress=0, status=progress_message, isInterruptable=False)
        
        # Define fields and filters for the ShotGrid query
        fields = ['id', 'code', 'sg_path_to_movie', 'created_at']
        filters = [['entity', 'is', {'type': 'Shot', 'id': shot_id}]]

        # Sort by creation date (descending) to get the latest version first
        sort = [{'field_name': 'created_at', 'direction': 'desc'}]

        # Query ShotGrid for versions associated with the shot, sorted by creation date
        versions = sg.find('Version', filters, fields, sort)

        # Update progress
        cmds.progressWindow(edit=True, progress=20, status="Fetching versions from ShotGrid...")

        # Extract file paths from versions and keep track of the highest versions
        highest_versions = {}
        has_polish_version = False

        # Updated pattern to match v###, v##, V###, and V##
        version_pattern = re.compile(r'_(v\d{2,3})\.', re.IGNORECASE)

        total_versions = len(versions)
        progress_increment = 80 / total_versions if total_versions else 1

        for i, version in enumerate(versions):
            path = version['sg_path_to_movie']
            if not path:
                continue

            match = version_pattern.search(path)
            if not match:
                continue

            version_number = match.group(1)
            base_name = path[:match.start()]

            # Convert version_number to lowercase to ensure consistent comparison
            version_number = version_number.lower()

            # Check if this version has "polish" in its name
            if 'polish' in path.lower():
                has_polish_version = True

            # Exclude files with "block" in their name if polish version exists
            if 'block' in path.lower() and has_polish_version:
                continue

            # Compare version numbers and keep the highest one
            if base_name not in highest_versions or version_number > highest_versions[base_name][1]:
                highest_versions[base_name] = (path, version_number)
            
            # Update progress
            cmds.progressWindow(edit=True, progress=20 + (i + 1) * progress_increment, status="Processing versions...")


        # Concatenate paths so Hiero opens all shots in 1 session
        file_paths_concatenated = " ".join([info[0] for info in highest_versions.values()])

        # End progress window
        cmds.progressWindow(endProgress=1)

        return file_paths_concatenated

    path = latest_version_list()
    hiero_player_launch(path)
