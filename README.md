# Lighting Utilities

A collection of tools used for production with the Maya animation DCC

## Utilities

- shelf: A structured, Python-based shelf designed to organise and host lighting utilities within the Maya DCC application. The shelf is rebuilt cleanly upon each launch of the software. An visual demonstration of the shelf and tools can be found here: https://vimeo.com/manage/videos/1072359364

-----

- g_shotgrid_launch_task: Tool to load selected task pages

- g_load_websites: Context-aware tool leveraging the Giant API and Shotrgrid database to load specific websites based on conditions within the current scene context

- hiero_player_launch: A module that launches the Hiero media player from within the Maya DCC environment, preloaded with review videos for the current shot context. It also provides options to view outputs from preceding and succeeding departments for comparative evaluation.

- lgt_aovs: A tool for generating sets of common AOV (Arbitrary Output Variable) data layers, eliminating the need for manual creation through a structured GUI that allows quick assigment to render outputs.

- lgt_bridge_tool: A work-in-progress bridge tool for opening the Nuke DCC application from directly within Maya. The intetion is to have it refere to the existing scene context to open the Nuke DCC with the correct task environment

- lgt_card_toolkit: A tool for generating utility objects for creative lighting, including bounce, reflector, and blocker (flag) card geometry. The tool automatically creates the cards, assigns the appropriate shaders, intelligently names both the geometry and shaders, and organizes the assets into a structured, named group, making them ready for positioning.

- lgt_launch_dashboard: A context-aware quick-access function to launch the Shorgrid production management dashboard page for artists to access their personal worksheets and assigments 

- lgt_light_toolkit: A compact and full-featured condition-based tool designed to manage light asset creation and assign common attributes, such as light group names, outliner structure, and modifications to default values, simplifying light management upon creation. It places lights under a 'set lights' group when created within the set task context, and under a 'shot lights' group in the shot context.

- lgt_mpco_browser: Text-only GUI tool that provides dropdown lists of the shot hierarchy relationship for the current sequence context. Shot strings data can be double-clicked to launch a browser page on the related shot and task

- lgt_shelf_reload: Tool to refresh python shelves in a Maya DCC session

- rv_player_launch: A module that launches the Hiero media player from within the Maya DCC environment, preloaded with review videos for the current shot context. It also provides options to view outputs from preceding and succeeding departments for comparative evaluation.

- g_open_dir: Open the scene context output directroy in explorer

- g_project_bibles: Pop-open function for project bibles and documentation


## Requirements

- Python
- ShotGrid API + key
- gfoundation (Giant proprietary API)