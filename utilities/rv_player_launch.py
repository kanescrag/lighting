from PySide2 import QtWidgets, QtCore
import maya.OpenMaya as om
import maya.cmds as cmds
from lighting.scripts import sg_creds
from gfoundation import gcontext
import re
import subprocess

sg = sg_creds.sg_data()
ctx = gcontext.Gcontext.get_from_env()
episode = ctx.episode
project_code = ctx.show
task_type = ctx.get_shot_type()


def rv_sequence_review():
    if task_type == "Set":
        om.MGlobal.displayWarning(f"This action can only be run in Shot context. Currently in Set/Asset context: {episode}")
    else:

        class RVLauncherDialog(QtWidgets.QDialog):
            def __init__(self, parent=None):
                super(RVLauncherDialog, self).__init__(parent)
                self.setWindowTitle("RV Launcher")
                self.setMinimumWidth(400)

                # Create widgets
                self.launch_button = QtWidgets.QPushButton("Launch RV")
                self.launch_button.clicked.connect(self.launch_rv)

                # Progress bar
                self.progress_bar = QtWidgets.QProgressBar()
                self.progress_bar.setMinimum(0)
                self.progress_bar.setMaximum(100)

                # Layout
                layout = QtWidgets.QVBoxLayout()
                layout.addWidget(self.launch_button)
                layout.addWidget(self.progress_bar)
                self.setLayout(layout)

            def get_shot_sequence_id(self, sequence_code, project_code):
                # Initialize Shotgun session
                sg = sg_creds.sg_data()

                # Get project ID
                project_get = sg.find("Project", [['code', 'is', project_code]], fields=['id'])
                if not project_get:
                    raise ValueError(f"No project found with code {project_code}")
                project_id = project_get[0]['id']

                # Get all sequences in the project
                sequences = sg.find("Sequence", filters=[['project', 'is', {'type': 'Project', 'id': project_id}]], fields=["code", "id"])

                # Find the sequence with the given sequence_code
                sequence_data = next((item for item in sequences if item["code"] == sequence_code), None)
                if not sequence_data:
                    raise ValueError(f"No sequence found with code {sequence_code} in project {project_code}")
                
                # Return the sequence ID
                return sequence_data['id']

            def list_shot_ids_in_sequence(self, sequence_id):
                # Initialize Shotgun session
                sg = sg_creds.sg_data()

                # Get all shots in the sequence
                shots = sg.find("Shot", filters=[['sg_sequence', 'is', {'type': 'Sequence', 'id': sequence_id}]], fields=["id"])

                # Extract shot IDs
                shot_ids = [shot['id'] for shot in shots]
                
                return shot_ids

            def rv_launcher(self, latest_versions):
                # Path to the RV executable
                rv_path = r"C:\Program Files\ShotGrid\RV-2022.3.0\bin\rv.exe"

                # Initialize an empty list for media files
                media_files = []

                # Function to extract sequence and shot numbers from the file path
                def extract_sequence_shot(filename):
                    match = re.search(r'_sq(\d+)_sh(\d+)_', filename)
                    if match:
                        sequence = int(match.group(1))
                        shot = int(match.group(2))
                        return sequence, shot
                    return None, None

                # Create a list of (sequence, shot) tuples from latest_versions keys
                shots_to_launch = [(sequence_code, shot_id) for shot_id in latest_versions.keys()]

                # Sort shots_to_launch based on (sequence, shot) for consistent ordering
                shots_to_launch.sort()

                # Generate media file paths based on latest_versions
                for sequence, shot_id in shots_to_launch:
                    version_info = latest_versions[shot_id]
                    if version_info:
                        file_path = version_info['file_path']
                        media_files.append(file_path)

                # Sort media files based on sequence and shot numbers
                sorted_media_files = sorted(media_files, key=lambda f: extract_sequence_shot(f))

                # Construct the command to launch RV with the sorted media files
                command = [rv_path] + sorted_media_files

                # Launch the RV process
                try:
                    subprocess.Popen(command)
                    print("RV launched successfully with the sequence")
                except Exception as e:
                    print(f"Failed to launch RV: {e}")

            def launch_rv(self):
                try:
                    
                    # Get context data
                    ctx = gcontext.Gcontext.get_from_env()
                    episode = ctx.episode
                    project_code = ctx.show
                    sequence_code = ctx.sequence

                    # Get sequence ID
                    sequence_id = self.get_shot_sequence_id(sequence_code, project_code)

                    # Get shot IDs in sequence
                    shot_ids = self.list_shot_ids_in_sequence(sequence_id)

                    # Check if shot_ids is None or empty
                    if shot_ids is None or len(shot_ids) == 0:
                        raise ValueError(f"No shots found in sequence {sequence_code}")

                    # Populate latest_versions dictionary
                    latest_versions = {}

                    # Calculate progress bar increments
                    increment = 100.0 / len(shot_ids)

                    for idx, shot_id in enumerate(shot_ids):
                        # Update progress bar
                        progress_value = int((idx + 1) * increment)
                        self.progress_bar.setValue(progress_value)
                        QtWidgets.QApplication.processEvents()  # Refresh the GUI

                        # Initialize Shotgun session (if not already done)
                        sg = sg_creds.sg_data()

                        # Query versions associated with the current shot
                        filters = [['entity', 'is', {'type': 'Shot', 'id': shot_id}]]
                        fields = ['id', 'code', 'entity', 'sg_version_number', 'created_at', 'sg_path_to_movie']

                        versions = sg.find('Version', filters, fields, order=[{'field_name': 'sg_version_number', 'direction': 'desc'}])

                        if versions:
                            latest_version = versions[0]  # Assuming versions are sorted by version number in descending order
                            latest_versions[shot_id] = {
                                'version_number': latest_version['sg_version_number'],
                                'file_path': latest_version['sg_path_to_movie']
                            }
                        else:
                            # Handle case where no versions are found
                            latest_versions[shot_id] = None

                    # Launch RV with the latest version paths
                    self.rv_launcher(latest_versions)

                    # Close window
                    self.close()

                except ValueError as e:
                    om.MGlobal.displayError(str(e))
                    self.progress_bar.setValue(0)

        # Function to show the dialog
        def show_rv_launcher_dialog():
            dialog = RVLauncherDialog()
            dialog.exec_()

        # Show the dialog
        show_rv_launcher_dialog()
