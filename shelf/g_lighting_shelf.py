
##Lighting Shelf - Redshift - Craig Kane - 12/10/2021
########################################################
#------------------------------------------------------


# IMPORT LIBRARIES
import maya.cmds as cmds
import maya.mel as mel
import logging
import importlib
from gfoundation import gcontext
from shared.scripts import giant_wiki_launcher


# Get context of current environment
ctx = gcontext.Gcontext.get_from_env()
project = ctx.show
dept = ctx.department
dept_lower = dept.lower()
task_type = ctx.get_shot_type()
render_engine = ctx.showspec['renderer']
show = ctx.show



# ------------------------------ SHELF TEMPLATE ------------------------------

def _null(*args):
    pass

class _shelf_template:

    def __init__(self, name="LGT_TK", icon_path="Z:/studio_tools/pipe2/facility/maya/utilities/lighting/icons/"):
        self.name = name
        self.icon_path = icon_path
        self.label_background = (0, 0, 0, 0)
        self.label_colour = (.9, .9, .9)
        self._clean_old_shelf()
        cmds.setParent(self.name)
        self.build()

    def build(self):
        '''This method should be overwritten in derived classes to actually build the shelf
        elements. Otherwise, nothing is added to the shelf.'''
        pass
    
    def add_button(self, label, annotation, icon, myEbg, command=_null, double_command=_null,noDefaultPopup=True):
        '''Adds a shelf button with the specified label, command, double click command and image.'''
        cmds.setParent(self.name)
        return cmds.shelfButton(width=37, height=37, image=icon, l=label, ann=annotation,
            command=command, dcc=double_command, imageOverlayLabel=label,
            olb=self.label_background, olc=self.label_colour,ndp = noDefaultPopup,ebg = myEbg
        )

    def add_menu_item(self, parent, label, sub_menu=0, command=_null, icon=None, divider=0):
        '''Adds a menu item with the specified label, command, and image to the specified parent.'''
        if icon:
            icon = self.icon_path + icon
        return cmds.menuItem(p=parent, l=label, c=command, i=icon, d=divider, sm=sub_menu)

    def add_sub_menu(self, parent, label, icon=None):
        '''Adds a sub-menu item with the specified label and icon to the specified parent popup menu.'''
        if icon:
            icon = self.icon_path + icon
        return cmds.menuItem(p=parent, l=label, i=icon, subMenu=1)

    def radio_menu_item(self, parent, label, source_type, collection=None, command=_null):
        return cmds.menuItem(p=parent, l=label, stp=source_type, cl=collection, c=command)

    def _clean_old_shelf(self):
        '''Checks if the shelf exists and empties it if it does or creates it if it does not.'''
        if cmds.shelfLayout(self.name, ex=1):
            if cmds.shelfLayout(self.name, q=1, ca=1):
                for each in cmds.shelfLayout(self.name, q=1, ca=1):
                    cmds.deleteUI(each)
        else:
            cmds.shelfLayout(self.name, p="ShelfLayout")


# ------------------------------ SHELF FUNCTIONS ------------------------------

# -------- Show Bible -------- #

def giant_project_bible_global(*args):
    from shared.scripts import giant_project_bibles
    importlib.reload(giant_project_bibles)
    giant_project_bibles.generate_project_urls(project,"global")

def giant_project_bible_overview(*args):
    from shared.scripts import giant_project_bibles
    importlib.reload(giant_project_bibles)
    giant_project_bibles.generate_project_urls(project,"overview")

def giant_project_bible_episodes(*args):
    from shared.scripts import giant_project_bibles
    importlib.reload(giant_project_bibles)
    giant_project_bibles.generate_project_urls(project,"episodes")

def giant_project_bible_characters(*args):
    from shared.scripts import giant_project_bibles
    importlib.reload(giant_project_bibles)
    giant_project_bibles.generate_project_urls(project,"characters")

def giant_project_bible_sets(*args):
    from shared.scripts import giant_project_bibles
    importlib.reload(giant_project_bibles)
    giant_project_bibles.generate_project_urls(project,"sets")

def giant_project_bible_department(*args):
    from shared.scripts import giant_project_bibles
    importlib.reload(giant_project_bibles)
    giant_project_bibles.generate_project_urls(project,dept_lower)





# -------- Giant wiki -------- #

#creative--------#

def giant_wiki_planning_button(*args):
    from shared.scripts import giant_wiki_launcher
    importlib.reload(giant_wiki_launcher)
    giant_wiki_launcher.open_wiki_page("lighting-dept","lgt-creative-workflow","lgt_planning")

def giant_wiki_prelighting_button(*args):
    from shared.scripts import giant_wiki_launcher
    importlib.reload(giant_wiki_launcher)
    giant_wiki_launcher.open_wiki_page("lighting-dept","lgt-creative-workflow","lgt_pre-lighting")

def giant_wiki_asset_lighting_button(*args):
    from shared.scripts import giant_wiki_launcher
    importlib.reload(giant_wiki_launcher)
    giant_wiki_launcher.open_wiki_page("lighting-dept","lgt-creative-workflow","lgt_asset_lighting")

def giant_wiki_shot_lighting_button(*args):
    from shared.scripts import giant_wiki_launcher
    importlib.reload(giant_wiki_launcher)
    giant_wiki_launcher.open_wiki_page("lighting-dept","lgt-creative-workflow","lgt_shot_lighting")

#technical-------#

def giant_wiki_lgt_scene_build_button(*args):
    from maya_animation.scene_builds import light_scene_build
    light_scene_build.arnss_build()
    #from shared.scripts import giant_wiki_launcher
    #importlib.reload(giant_wiki_launcher)
    #giant_wiki_launcher.open_wiki_page("lighting-dept","lighting-technical-workflow","lgt_build")
                                       
def giant_wiki_lgt_scene_publish_button(*args):
    from shared.scripts import giant_wiki_launcher
    importlib.reload(giant_wiki_launcher)
    giant_wiki_launcher.open_wiki_page("lighting-dept","lighting-technical-workflow","lgt_publish")
                                       
def giant_wiki_pipe_overview_button(*args):
    from shared.scripts import giant_wiki_launcher
    importlib.reload(giant_wiki_launcher)
    giant_wiki_launcher.open_wiki_page("lighting-dept","lighting-technical-workflow","lgt_pipe_overview")
                                       
def giant_wiki_lgt_shelf_button(*args):
    from shared.scripts import giant_wiki_launcher
    importlib.reload(giant_wiki_launcher)
    giant_wiki_launcher.open_wiki_page("lighting-dept","lighting-technical-workflow","lgt_shelf")
                                       
def giant_wiki_shot_lgt_naming_button(*args):
    from shared.scripts import giant_wiki_launcher
    importlib.reload(giant_wiki_launcher)
    giant_wiki_launcher.open_wiki_page("lighting-dept","lighting-technical-workflow","lgt_naming-conventions")

def giant_wiki_shot_triage_button(*args):
    from shared.scripts import giant_wiki_launcher
    importlib.reload(giant_wiki_launcher)
    giant_wiki_launcher.open_wiki_page("lighting-dept","lighting-technical-workflow","lgt_shot_triage")


#-----------------  shotgrid pages -----------------#


def shotgun_launch_dashboard_page(*args):
    from lighting.scripts import lgt_shotgrid_launch_dashboard
    importlib.reload(lgt_shotgrid_launch_dashboard)
    lgt_shotgrid_launch_dashboard.launch_dashboard()

def shotgun_launch_project_page(*args):
    from shared.scripts import giant_shotgrid_launch_project
    importlib.reload(giant_shotgrid_launch_project)
    giant_shotgrid_launch_project.launch_project_page()

def shotgun_launch_episode_page(*args):
    from shared.scripts import giant_shotgrid_launch_episode
    importlib.reload(giant_shotgrid_launch_episode)
    giant_shotgrid_launch_episode.launch_episode_page()

def shotgun_launch_shot_page(*args):
    from shared.scripts import giant_shotgrid_launch_shot
    importlib.reload(giant_shotgrid_launch_shot)
    giant_shotgrid_launch_shot.launch_shot_page()

def shotgun_launch_current_task_page(*args):
    import importlib
    from shared.scripts import giant_shotgrid_launch_current_task
    importlib.reload (giant_shotgrid_launch_current_task)
    giant_shotgrid_launch_current_task.launch_current_task_page()

def shotgun_launch_task_page(*args):
    from shared.scripts import giant_shotgrid_launch_task
    importlib.reload(giant_shotgrid_launch_task)
    giant_shotgrid_launch_task.launch_task_window()

def shotgun_open_shot_by_name_button(*args):
    from shared.scripts import giant_open_shot_page
    importlib.reload(giant_open_shot_page)
    giant_open_shot_page.shot_open()

def giant_scene_context_button(*args):
    from shared.scripts import giant_scene_context
    importlib.reload(giant_scene_context)
    giant_scene_context.show_scene_context_confirm_dialog()


# -------- IT-------#

def giant_it_support_issue_button(*args):
    from shared.scripts import giant_it_support
    importlib.reload(giant_it_support)
    giant_it_support.launch_it_support("issue")                                

def giant_it_support_request_button(*args):
    from shared.scripts import giant_it_support
    importlib.reload(giant_it_support)
    giant_it_support.launch_it_support("request")          




#-----------------  lighting in/out -----------------#
 
def scene_build_button(*args):
    if show == 'fopr':
        from lighting.scripts import lgt_scene_build
        importlib.reload(lgt_scene_build)
        lgt_scene_build.context_build()
    elif show == 'egh':
        from maya_animation.scene_builds import light_scene_build
        light_scene_build.arnss_build()


def giant_load_button(*args):
    from maya_pipeline.io_tools.file_driver import MayaFileDriver
    from qt_gui_lib.io_tools.file_load_ui import FileLoadUI
    flwin = FileLoadUI(MayaFileDriver())
    flwin.show()
   

def context_switcher_button(*args):
    from gcontextswitcher.drivers.mayacontextdriver import MayaContextDriver
    from gcontextswitcher.contextswitcher import ContextSwitcher
    cswin = ContextSwitcher(MayaContextDriver())
    cswin.show()

def giant_save_button(*args):
    from maya_pipeline.io_tools.file_driver import MayaFileDriver
    from qt_gui_lib.io_tools.file_save_ui import FileSaveUI
    flwin = FileSaveUI(MayaFileDriver())
    flwin.show()

def giant_publish_button(*args):
    from maya_animation.publish import lgt_shot_rig_publish_ui
    lgt_shot_rig_publish_ui.launch_ui()

def asset_browser_button(*args):
    from maya_pipeline.io_tools.file_driver import MayaFileDriver
    import gasset_browser.ui.browser as asset_browser
    browser = asset_browser.GiantAssetBrowser.launch(context=MayaFileDriver().context, file_driver=MayaFileDriver())


# ---------------- time logs --------------------#

def giant_shotgrid_task_status_button(*args):
    from shared.scripts import giant_shotgrid_task_status
    importlib.reload(giant_shotgrid_task_status)
    giant_shotgrid_task_status.open_task_status_window()

def giant_shotgrid_set_time_log(*args):
    from shared.scripts import giant_shotgrid_task_status
    importlib.reload(giant_shotgrid_task_status)
    giant_shotgrid_task_status.open_task_status_window()

#----------------- review tools -----------------#

def hiero_launch_button(*args):
    from lighting.scripts import lgt_hiero_launch
    importlib.reload(lgt_hiero_launch)
    lgt_hiero_launch.hiero_launcher()

def rv_launch_button(*args):
    from shared.scripts import giant_rv_launch
    importlib.reload(giant_rv_launch)
    giant_rv_launch.rv_sequence_review()

def mpco_browser_button(*args):
    from lighting.scripts import lgt_mpco_browser
    importlib.reload(lgt_mpco_browser)
    lgt_mpco_browser.mpco_window()


def explorer_open_work_dir(*args):
    from shared.scripts import giant_open_dir
    importlib.reload(giant_open_dir)
    giant_open_dir.reveal_directory("work")

def explorer_open_publish_dir(*args):
    from shared.scripts import giant_open_dir
    importlib.reload(giant_open_dir)
    giant_open_dir.reveal_directory("publish")

    

# -------- Render Farm -------- # 

def deadline_button(*args):
    from shared.scripts import giant_deadline_submitter
    importlib.reload(giant_deadline_submitter)
    giant_deadline_submitter.submit_window()
    
def giant_wiki_render_farm_button(*args):
    from shared.scripts import giant_wiki_launcher
    importlib.reload(giant_wiki_launcher)
    giant_wiki_launcher.open_wiki_page("rendering","rd_submitter","")

                      

# -------- Render Tools -------- # 

def render_layer_toolkit_button(*args):
    from lighting.scripts import egh_lgt_render_layer_toolkit, egh_lgt_render_layer_library
    importlib.reload(egh_lgt_render_layer_toolkit)
    importlib.reload(egh_lgt_render_layer_library)
    egh_lgt_render_layer_toolkit.render_layer_toolkit()

def aov_toolkit_button(*args):
    from lighting.scripts import lgt_aovs
    importlib.reload(lgt_aovs)
    lgt_aovs.aov_toolkit()

def open_renderer_window(*args):
    from shared.scripts import giant_open_render_window
    importlib.reload(giant_open_render_window)
    giant_open_render_window.launch_render_window()



# -------- Scene Update -------- #


def scene_update_anm_button(*args):
    from maya_animation.scene_builds import light_scene_build
    light_scene_build.arnss_update_animation()
    #from maya_animation.scene_builds import light_scene_build
    #light_scene_build.update_animation()

def scene_update_assets_button(*args):
    from maya_pipeline.utils import gui
    gui.launch_scene_updater()
    #from lighting.scripts import lgt_update_assets
    #lgt_update_assets.context_update()


def giant_shelf_reload(*args):
    from lighting.scripts import lgt_shelf_reload
    importlib.reload(lgt_shelf_reload)
    lgt_shelf_reload.rebuild_shelf()


# --------- Lighting Toools -------- #m


def light_button(*args):
    from lighting.scripts import lgt_light_toolkit
    importlib.reload(lgt_light_toolkit)
    lgt_light_toolkit.launch_lighting_toolkit()

def list_lights(*args):
    mel.eval('callPython "maya.app.renderSetup.lightEditor.views.editorUI" "createLightEditorWindow" {}')

def light_linking(*args):
    mel.eval('LightCentricLightLinkingEditor')

def character_light_rig_button(*args):
    from lighting.scripts import fopr_character_light_rig
    importlib.reload(fopr_character_light_rig)
    fopr_character_light_rig.character_light_rig_tool()

def render_submitter():
    from maya_pipeline.render_submit import submitter_ui
    submitter_ui.launch_ui()

def card_toolkit_button(*args):
    from lighting.scripts import lgt_card_toolkit_dev
    importlib.reload(lgt_card_toolkit_dev)
    lgt_card_toolkit_dev.launch_card_toolkit()

def matte_card_toolkit_button(*args):
    from lighting.scripts import lgt_matte_card_toolkit
    importlib.reload(lgt_matte_card_toolkit)
    lgt_matte_card_toolkit.launch_matte_card_toolkit()


def bridge_button(*args):
    from lighting.scripts import lgt_bridge_tool
    importlib.reload(lgt_bridge_tool)
    lgt_bridge_tool.nuke_bridge()


def giant_renderer_documentation_button(*args):
    from lighting.scripts import lgt_renderer_documentation
    importlib.reload(lgt_renderer_documentation)
    lgt_renderer_documentation.launch_documentation_page()






def rapid_render_button(*args):
    from lighting.scripts import lgt_render_settings
    importlib.reload(lgt_render_settings)
    lgt_render_settings.apply_json_data('low')

def mpco_render_settings_button(*args):
    from lighting.scripts import lgt_render_settings
    importlib.reload(lgt_render_settings)
    lgt_render_settings.apply_json_data('production')

def mpco_render_setup_button(*args):
    from lighting.modules import g_mpco_render_setup_apply
    g_mpco_render_setup_apply.grab_render_setup()


def lens_button(*args):
    from lighting.modules import g_lensToolkit
    g_lensToolkit.lens_toolkit()

def motion_blur_button(*args):
    from lighting.modules import g_motion_blur_toolkit
    g_motion_blur_toolkit.motion_blur_toolkit()

def volume_button(*args):
    from lighting.modules import g_volumeToolkit
    g_volumeToolkit.volume_toolkit()

def tesselation_button(*args):
    import importlib
    from lighting.scripts import TesselationManager
    importlib.reload(TesselationManager)
    TesselationManager.create_TMUI()

def eyelid_fix(*args):
    from lighting.scripts import fopr_character_eyelid_fix
    importlib.reload(fopr_character_eyelid_fix)
    fopr_character_eyelid_fix.fixEyes()

def overrides_button(*args):
    pass

def materials_button(*args):
    import importlib
    from lighting.scripts import fopr_reassignShadersFromLk
    importlib.reload(fopr_reassignShadersFromLk)
    fopr_reassignShadersFromLk.fixShaders()

def fopr_force_cleanup_button(*args):
    try:
        from lighting.scripts import fopr_forceCleanLk
        importlib.reload(fopr_forceCleanLk)
        fopr_forceCleanLk.forceCleanLk()
    except IndexError as e:
        cmds.confirmDialog(
            title='Error', message='\nSelect your geometry first! \n',
            button=['OK'], defaultButton='OK', cancelButton='OK', dismissString='OK'
        )

def fopr_rebuild_set_button(*args):
    try:
        import importlib
        from lighting.scripts import fopr_rebuildSet
        importlib.reload(fopr_rebuildSet)
        fopr_rebuildSet.rebuildSet()
    except IndexError as e:
        cmds.confirmDialog(
            title='Error', message='\nSelect your geometry first! \n',
            button=['OK'], defaultButton='OK', cancelButton='OK', dismissString='OK'
        )

def light_rig_to_camera_button(*args):
    import importlib
    from lighting.scripts import fopr_lightRigRotationOffset
    importlib.reload(fopr_lightRigRotationOffset)
    fopr_lightRigRotationOffset.createCamOffsetRig()

def frame(*args):
    import importlib
    import frame
    importlib.reload(frame)
    frame.create()

def giant_wiki_button(section,subsection):
    from shared.scripts import giant_wiki_launcher
    importlib.reload(giant_wiki_launcher)
    print(f"Debug: Section: {section}, Subsection: {subsection}")
    giant_wiki_launcher.launch_page(section,subsection)

def camera_culling_tool():
    from maya_pipeline.tools import camera_culling_tool
    camera_culling_tool.run_camera_culling_tool()
        
def lmc_toolkit():
    from lighting.scripts import lgt_utils
    importlib.reload(lgt_utils)
    lgt_utils.lgt_matte_champion()

# ------------------------------ SHELF BUILD ------------------------------

class g_lighting_shelf(_shelf_template):


    def build(self):
        

        # -------- Show Bible -------- #

        cmds.separator(style="none",w=10)
        show_bible_button = self.add_button(label ="", annotation = "Show Bible", myEbg=False, icon = self.icon_path + "lgt_bible.png", noDefaultPopup=True, command=_null)
        show_bible_menu = cmds.popupMenu(parent=show_bible_button,button=3)

        cmds.menuItem(divider=1)
        cmds.menuItem(parent=show_bible_menu, label = "Show Bible Pages", enable=False, boldFont=True)
        cmds.menuItem(divider=1)
        self.add_menu_item(parent=show_bible_menu, label="Project Bible", command=giant_project_bible_global)
        self.add_menu_item(parent=show_bible_menu, label="Overview", command=giant_project_bible_overview)
        self.add_menu_item(parent=show_bible_menu, label="Episodes", command=giant_project_bible_episodes)
        self.add_menu_item(parent=show_bible_menu, label="Characters", command=giant_project_bible_characters)
        self.add_menu_item(parent=show_bible_menu, label="Sets", command=giant_project_bible_sets)
        cmds.menuItem(divider=1)
        cmds.menuItem(parent=show_bible_menu, label = "Show Bible Pages", enable=False, boldFont=True)
        cmds.menuItem(divider=1)
        self.add_menu_item(parent=show_bible_menu, label=f"{dept} Department", command=giant_project_bible_department)




        

        # --- Giant Wiki --- #
        
        giant_wiki_button = self.add_button(label ="", annotation = "Giant Wiki", myEbg=False, icon = self.icon_path + "lgt_wiki.png", noDefaultPopup=True, command=_null)
        giant_wiki_menu = cmds.popupMenu(parent=giant_wiki_button,button=3)

        cmds.menuItem(divider=1)
        cmds.menuItem(parent=giant_wiki_menu, label = "Creative Workflow", enable=False, boldFont=True)
        cmds.menuItem(divider=1)
        self.add_menu_item(parent=giant_wiki_menu, label="Planning", command=giant_wiki_planning_button)
        self.add_menu_item(parent=giant_wiki_menu, label="Pre-Lighting", command=giant_wiki_prelighting_button)
        self.add_menu_item(parent=giant_wiki_menu, label="Asset Lighting", command=giant_wiki_asset_lighting_button)
        self.add_menu_item(parent=giant_wiki_menu, label="Shot Lighting", command=giant_wiki_shot_lighting_button)
        cmds.menuItem(divider=1)
        cmds.menuItem(parent=giant_wiki_menu, label = "Production Workflow", enable=False, boldFont=True)
        cmds.menuItem(divider=1)
        self.add_menu_item(parent=giant_wiki_menu, label="Placeholder", command=giant_wiki_planning_button)
        cmds.menuItem(divider=1)
        cmds.menuItem(parent=giant_wiki_menu, label = "Technical Workflow", enable=False, boldFont=True)
        cmds.menuItem(divider=1)
        self.add_menu_item(parent=giant_wiki_menu, label="LGT Build", command=giant_wiki_lgt_scene_build_button)
        self.add_menu_item(parent=giant_wiki_menu, label="LGT Publish", command=giant_wiki_lgt_scene_publish_button)
        self.add_menu_item(parent=giant_wiki_menu, label="LGT Pipeline Overview", command=giant_wiki_pipe_overview_button)
        self.add_menu_item(parent=giant_wiki_menu, label="LGT Shelf Reference", command=giant_wiki_lgt_shelf_button)
        self.add_menu_item(parent=giant_wiki_menu, label="LGT Naming Conventions", command=giant_wiki_shot_lgt_naming_button)        
        cmds.menuItem(divider=1)
        cmds.separator(style="none",w=10)


        # ----- Shotgrid ----- #

        shotgrid_button = self.add_button(label ="", annotation = "Shotgrid Pages", myEbg=False, icon = self.icon_path + "lgt_flow.png", noDefaultPopup=True, command=_null)
        shotgrid_menu = cmds.popupMenu(parent=shotgrid_button,button=3)
        cmds.menuItem(divider=1)
        cmds.menuItem(parent=shotgrid_menu, label = "Shotgrid", enable=False, boldFont=True)
        cmds.menuItem(divider=1)
        self.add_menu_item(parent = shotgrid_menu, label = "Dashboard", command=shotgun_launch_dashboard_page)
        cmds.menuItem(divider=1)
        self.add_menu_item(parent = shotgrid_menu, label = "Open Current Project Page", command=shotgun_launch_project_page)
        self.add_menu_item(parent = shotgrid_menu, label = "Open Current Episode Page", command=shotgun_launch_episode_page)
        self.add_menu_item(parent = shotgrid_menu, label = "Open Current Shot/Asset Page", command=shotgun_launch_shot_page)
        cmds.menuItem(divider=1)
        self.add_menu_item(parent = shotgrid_menu, label = "Open Current Task Version Page", command=shotgun_launch_current_task_page)
        self.add_menu_item(parent = shotgrid_menu, label = "Open a Task Version Page", command=shotgun_launch_task_page)
        cmds.menuItem(divider=1)
        self.add_menu_item(parent = shotgrid_menu, label = "Open Shot Page By Name", command=shotgun_open_shot_by_name_button)
        cmds.menuItem(divider=1)
        self.add_menu_item(parent = shotgrid_menu, label = "View Scene Context", command=giant_scene_context_button)
        cmds.separator(style = "single")


        # ----- scene I/O ----- #

        self.add_button(label="", annotation="Scene Build",command = scene_build_button, myEbg=False, icon = self.icon_path + "lgt_build.png")
        cmds.separator(style="none",w=10)
        self.add_button(label="", annotation="Scene Load",command = giant_load_button, myEbg=False, icon = self.icon_path + "lgt_file_open.png")
        cmds.separator(style="none",w=10)
        self.add_button(label="", annotation="Context Switcher",command = "from gcontextswitcher.drivers.mayacontextdriver import MayaContextDriver;from gcontextswitcher.contextswitcher import ContextSwitcher;cswin = ContextSwitcher(MayaContextDriver()); cswin.show()", myEbg=False, icon = self.icon_path + "lgt_file_switch.png")
        cmds.separator(style="none",w=10)
        self.add_button(label="", annotation="Scene Save",command = giant_save_button, myEbg=False, icon = self.icon_path + "lgt_file_save.png")
        cmds.separator(style="none",w=10)
        self.add_button(label="", annotation="Scene Publish",command = giant_publish_button, myEbg=False, icon = self.icon_path + "lgt_publish.png")
        cmds.separator(style="none",w=10)
        self.add_button(label="", annotation="Asset Browser",command = asset_browser_button, myEbg=False, icon = self.icon_path + "lgt_load_asset3.png")
        cmds.separator(style = "single")

        # -------- Timelogs -------- # 
        
        timelog_button = self.add_button(label ="", annotation = "Timelogs", myEbg=False, icon = self.icon_path + "lgt_timelogs.png", noDefaultPopup=True, command=_null)
        timelog_menu = cmds.popupMenu(parent=timelog_button,button=3)

        self.add_menu_item(parent = timelog_menu, label = "Set Status", command=giant_shotgrid_task_status_button)
        self.add_menu_item(parent = timelog_menu, label = "Personal Timelog (placeholder)", command=_null)
        cmds.menuItem(divider=1)
        self.add_menu_item(parent = timelog_menu, label = "Tickets", command=_null)
        
        cmds.separator(style = "single")

        # -------- Notes -------- # 

        notes_button = self.add_button(label ="", annotation = "Notes (placeholder)", myEbg=False, icon = self.icon_path + "lgt_notes2.png", noDefaultPopup=True, command=_null)
        notes_menu = cmds.popupMenu(parent=notes_button,button=3)

        cmds.menuItem(divider=1)
        cmds.menuItem(parent=notes_menu, label = "Notes Pages", enable=False, boldFont=True)
        cmds.menuItem(divider=1)
        self.add_menu_item(parent = notes_menu, label = "Shot Notes", command=_null)
        self.add_menu_item(parent = notes_menu, label = "Episodic Launch", command=_null)
        self.add_menu_item(parent = notes_menu, label = "Colour Scripts", command=_null)
        self.add_menu_item(parent = notes_menu, label = "Master Lighting", command=_null)
        cmds.separator(style = "none",  w = 10)

        # ----- Review Tools ----- #

        review_button = self.add_button(label ="", annotation = "Update", myEbg=False, icon = self.icon_path + "review.png", noDefaultPopup=True, command=_null)
        review_menu = cmds.popupMenu(parent=review_button,button=3)
        cmds.menuItem(divider=1)
        cmds.menuItem(parent=review_menu, label = "Players", enable=False, boldFont=True)
        cmds.menuItem(divider=1)     
        self.add_menu_item(parent = review_menu, label = "Hiero Review", command=hiero_launch_button)
        self.add_menu_item(parent = review_menu, label = "RV Review", command=rv_launch_button)
        cmds.menuItem(divider=1)
        #cmds.menuItem(parent=review_menu, label = "Tools", enable=False, boldFont=True)
        #cmds.menuItem(divider=1)   
        #self.add_menu_item(parent = review_menu, label = "MPCO Browser", command=mpco_browser_button)
        #cmds.menuItem(divider=1)
        cmds.menuItem(parent=review_menu, label = "Windows Explorer", enable=False, boldFont=True)
        cmds.menuItem(divider=1)
        self.add_menu_item(parent = review_menu, label = "Open Work Directory", command=explorer_open_work_dir)
        self.add_menu_item(parent = review_menu, label = "Open Publish Directory", command=explorer_open_publish_dir)
        self.add_menu_item(parent = review_menu, label = "Open Latest Renders Directory", command=explorer_open_publish_dir)
        cmds.separator(style = "none",  w = 10)


        # -------- MPCO Tools -------- #
        mpco_button = self.add_button(label ="", annotation = "MPCO Tools", myEbg=False, icon = self.icon_path + "lgt_mpco.png", noDefaultPopup=True, command=mpco_browser_button)
        cmds.separator(style = "single")




        # -------- Reload and Update and Modify -------- #
        reload_button = self.add_button(label ="", annotation = "Review Tools", myEbg=False, icon = self.icon_path + "lgt_updates.png", noDefaultPopup=True, command=_null)
        reload_menu = cmds.popupMenu(parent=reload_button,button=3)
        cmds.menuItem(divider=1)
        cmds.menuItem(parent=reload_menu, label = "Update Tools", enable=False, boldFont=True)
        cmds.menuItem(divider=1)     
        self.add_menu_item(parent = reload_menu, label = "Update Animation Caches", command=scene_update_anm_button)
        self.add_menu_item(parent = reload_menu, label = "Update Scene Asset", command=scene_update_assets_button)
        #self.add_menu_item(parent = reload_menu, label = "Update Scene Shaders", command=scene_update_assets_button)
        cmds.menuItem(divider=1)
        self.add_menu_item(parent = reload_menu, label = "Reload Shelf", command=giant_shelf_reload)
        cmds.separator(style = "none",  w = 10)

        camera_button = self.add_button(label ="", annotation = "Camera Tools", myEbg=False, icon = self.icon_path + "lgt_camera.png", noDefaultPopup=True, command=camera_culling_tool)
        camera_menu = cmds.popupMenu(parent=camera_button,button=3)
        cmds.menuItem(divider=1)
        cmds.menuItem(parent=camera_menu, label = "Camera Tools", enable=False, boldFont=True)
        cmds.menuItem(divider=1)     
        self.add_menu_item(parent = camera_menu, label = "Camera Culling Tool", command=scene_update_anm_button)

        cmds.separator(style = "single")


        # ----- Lightbag menu ----- #

        lightbag_button = self.add_button(label ="", annotation = "Light Bag", myEbg=False, icon = self.icon_path + "lgt_bulb3.png", noDefaultPopup=True, command=light_button)
        cmds.separator(style = "none",  w = 10)
        card_button = self.add_button(label ="", annotation = "Card Toolkit", myEbg=False, icon = self.icon_path + "lgt_card_toolkit3.png", noDefaultPopup=True, command=card_toolkit_button)
        card_menu = cmds.popupMenu(parent=card_button,button=3)
        cmds.menuItem(divider=1)
        cmds.menuItem(parent=card_menu, label = "Card Tools", enable=False, boldFont=True)
        cmds.menuItem(divider=1)     
        self.add_menu_item(parent = card_menu, label = "Light Blockers", command=card_toolkit_button)
        self.add_menu_item(parent = card_menu, label = "Light Reflectors", command=card_toolkit_button)
        self.add_menu_item(parent = card_menu, label = "Matte Cards", command=matte_card_toolkit_button)
        #self.add_button(label ="", annotation = "Card Toolkit", myEbg=False, icon = self.icon_path + "lgt_card_toolkit3.png", noDefaultPopup=True, command=light_button)
        cmds.separator(style = "none",  w = 10)
     #  self.add_button(label ="", annotation = "Matte Toolkit", myEbg=False, icon = self.icon_path + "lgt_matte.png", noDefaultPopup=True, command=card_button)
      # cmds.separator(style = "none",  w = 10)
        self.add_button(label ="", annotation = "Light Lister", myEbg=False, icon = self.icon_path + "lgt_list.png", noDefaultPopup=True, command=list_lights)
        cmds.separator(style = "none",  w = 10)
        self.add_button(label ="", annotation = "Light Linker", myEbg=False, icon = self.icon_path + "lgt_linking.png", noDefaultPopup=True, command=light_linking)
        cmds.separator(style = "none",  w = 10)
        self.add_button(label ="", annotation = "Bridge", myEbg=False, icon = self.icon_path + "lgt_bridge.png", noDefaultPopup=True, command=bridge_button)
        cmds.separator(style = "single")
        
        
  
        
        # --- Render Tools --- #

        render_tools_button = self.add_button(label ="", annotation = "Render Layer Toolkit", myEbg=False, icon = self.icon_path + "lgt_layers.png", noDefaultPopup=True, command=render_layer_toolkit_button)
        cmds.separator(style = "none",  w = 10)
        #render_tools_menu = cmds.popupMenu(parent=render_tools_button,button=3)
        #self.add_menu_item(parent=render_tools_menu, label="Render Layer Toolkit", command=render_layer_toolkit_button)
        #self.add_menu_item(parent=render_tools_menu, label="AOV Toolkit", command=aov_toolkit_button)
        #self.add_menu_item(parent=render_tools_menu, label="Redshift Render Window", command=open_renderer_window)

        self.add_button(label ="", annotation = "AOV Toolkit", myEbg=False, icon = self.icon_path + "lgt_aov3.png", noDefaultPopup=True, command=aov_toolkit_button)
        cmds.separator(style = "none",  w = 10)
        self.add_button(label ="", annotation = "Renderer Window", myEbg=False, icon = self.icon_path + "lgt_window.png", noDefaultPopup=True, command=open_renderer_window)
        cmds.separator(style = "none",  w = 10)


        # --- Rendering and Render Settings --- #

        render_settings_button = self.add_button(label ="", annotation = "LMC Toolkit", myEbg=False, icon = self.icon_path + "lgt_render_settings.png", noDefaultPopup=True, command=lmc_toolkit)
                                                         #render_settings_button = self.add_button(label ="", annotation = "Render Settings", myEbg=False, icon = self.icon_path + "lgt_render_settings.png", noDefaultPopup=True, command=_null)
        #render_settings_menu = cmds.popupMenu(parent=render_settings_button,button=3)
        #cmds.menuItem(divider=1)
        #cmds.menuItem(parent=render_settings_menu, label = "Render Setting Profiles", enable=False, boldFont=True)
        #cmds.menuItem(divider=1)     
        #self.add_menu_item(parent=render_settings_menu, label="Rapid Render Settings", command=rapid_render_button)
        #cmds.menuItem(divider=1)
        #self.add_menu_item(parent=render_settings_menu, label="Production Render Settings", command=mpco_render_settings_button)
        #cmds.menuItem(divider=1)
        #self.add_menu_item(parent=render_settings_menu, label="MPCO Render Settings", command=mpco_render_setup_button)
        #cmds.separator(style = "single")


       
        # --- Render Farm --- #

        render_farm_button = self.add_button(label ="", annotation = "Farm Submitter", myEbg=False, icon = self.icon_path + "lgt_render_farm2.png", noDefaultPopup=True, command=deadline_button)
        farm_menu = cmds.popupMenu(parent=render_farm_button,button=3)
        self.add_menu_item(parent=farm_menu, label="Render Submitter Documentation", command=giant_wiki_render_farm_button)
        cmds.separator(style = "single")

        
        # --- Support --- #

        troubleshooting_button = self.add_button(label ="", annotation = "Troubleshooting", myEbg=False, icon = self.icon_path + "lgt_help2.png", noDefaultPopup=True, command=_null)
        troubleshooting_menu = cmds.popupMenu(parent=troubleshooting_button,button=3)
        cmds.menuItem(divider=1)
        cmds.menuItem(parent=troubleshooting_menu, label = "Documentation", enable=False, boldFont=True)
        cmds.menuItem(divider=1)     
        self.add_menu_item(parent=troubleshooting_menu, label="LGT Triage", command=giant_wiki_shot_triage_button)
        self.add_menu_item(parent=troubleshooting_menu, label="LGT QC", command=giant_wiki_planning_button)
        self.add_menu_item(parent = troubleshooting_menu, label = "Noise Control", command=giant_wiki_shot_triage_button)
        self.add_menu_item(parent = troubleshooting_menu, label = "Render Engine Documentation", command=giant_renderer_documentation_button)
        cmds.separator(style = "none",  w = 10)

        it_support_button = self.add_button(label ="", annotation = "Tickets", myEbg=False, icon = self.icon_path + "lgt_ticket3.png", noDefaultPopup=True, command=_null)
        it_support_menu = cmds.popupMenu(parent=it_support_button,button=3)
        cmds.menuItem(divider=1)
        cmds.menuItem(parent=it_support_menu, label = "Systems", enable=False, boldFont=True)
        cmds.menuItem(divider=1)
        self.add_menu_item(parent=it_support_menu, label="Report An Issue", command=giant_it_support_issue_button)
        self.add_menu_item(parent=it_support_menu, label="Request A Service", command=giant_it_support_request_button)
        cmds.menuItem(divider=1)
        cmds.menuItem(parent=it_support_menu, label = "Pipeline", enable=False, boldFont=True)
        self.add_menu_item(parent=it_support_menu, label="Request A Feature", command=giant_it_support_request_button)
        cmds.menuItem(divider=1)
        self.add_menu_item(parent=it_support_menu, label="Pitch A Tool Idea", command=giant_it_support_request_button)
        cmds.separator(style = "single")

        if task_type == "Set":
            self.add_button(label ="", annotation = f"{project} : Asset", myEbg=False, icon = self.icon_path + "asset_icon.png", noDefaultPopup=True, command=_null)
        elif task_type == "Shot":
            self.add_button(label ="", annotation = f"{project} : Shot", myEbg=False, icon = self.icon_path + "shot_icon.png", noDefaultPopup=True, command=_null)

        #self.add_button(annotation="Creates scene environment and animates lights", icon="LGT_scene_anim.png", script_syntax=scene_build_anim_button)
        #self.add_button(label="Scene Update", annotation="Updates lighting in current scene", icon="LGT_update.png", script_syntax=scene_update_button)
        #self.add_button(label="Giant Save", annotation="Saves file using custom save window", icon="Giant_save.png", script_syntax=giant_save_button)
        #self.add_button(label="Giant Load", annotation="Loads file using custom load window", icon="Giant_load.png", script_syntax=giant_load_button)
        #self.add_button(label="Giant Publish", annotation="Publishes the current file", icon="Giant_publish.png", script_syntax=giant_publish_button)
        #self.add_button(label="Lighting Toolkit", annotation="Opens the lighting toolkit", icon="LGT_toolkit.png", script_syntax=light_button)
        #self.add_button(label="List Lights", annotation="Lists all lights in the scene", icon="LGT_list_lights.png", script_syntax=list_lights)
        #self.add_button(label="Light Linking", annotation="Opens the light linking editor", icon="LGT_light_linking.png", script_syntax=light_linking)
        #self.add_button(label="Character Light Rig", annotation="Builds character light rig", icon="LGT_char_light_rig.png", script_syntax=character_light_rig_button)
        #self.add_button(label="Render Submitter", annotation="Opens the render submission tool", icon="render_submitter.png", script_syntax=render_submitter)
        #self.add_button(label="Card Toolkit", annotation="Opens the card toolkit", icon="card_toolkit.png", script_syntax=card_button)
        #self.add_button(label="Layer Toolkit", annotation="Opens the render layer toolkit", icon="render_layer_toolkit.png", script_syntax=layer_button)
        #self.add_button(label="AOVs Toolkit", annotation="Opens the AOVs toolkit", icon="AOVs_toolkit.png", script_syntax=aov_button)
        #self.add_button(label="Redshift Render View", annotation="Opens the Redshift render view", icon="RS_render_view.png", script_syntax=rs_window)
        #self.add_button(label="Rapid Render", annotation="Applies low quality render settings", icon="rapid_render.png", script_syntax=rapid_render_button)
        #self.add_button(label="MPCO Render Settings", annotation="Applies production render settings", icon="mpco_render_settings.png", script_syntax=mpco_render_settings_button)
        #self.add_button(label="MPCO Render Setup", annotation="Grabs the current render setup for later use", icon="mpco_render_setup.png", script_syntax=mpco_render_setup_button)
        
        #self.add_button(label="Lens Toolkit", annotation="Opens the lens toolkit", icon="lens_toolkit.png", script_syntax=lens_button)
        #self.add_button(label="Motion Blur Toolkit", annotation="Opens the motion blur toolkit", icon="motion_blur_toolkit.png", script_syntax=motion_blur_button)
        #self.add_button(label="Volume Toolkit", annotation="Opens the volume toolkit", icon="volume_toolkit.png", script_syntax=volume_button)
        #self.add_button(label="Tesselation Manager", annotation="Opens the tesselation manager", icon="tesselation_toolkit.png", script_syntax=tesselation_button)
        #self.add_button(label="Eyelid Fix", annotation="Fixes the eyelids of characters", icon="eyelid_fix.png", script_syntax=eyelid_fix)
        #self.add_button(label="Reassign Shaders", annotation="Reassigns shaders from legacy lighting scenes", icon="reassign_shaders.png", script_syntax=reassign_shaders_from_lk)
        #self.add_button(label="Force Cleanup", annotation="Forces cleanup of legacy lighting scenes", icon="force_cleanup.png", script_syntax=fopr_force_cleanup_button)
        #self.add_button(label="Rebuild Set", annotation="Rebuilds the current set from templates", icon="rebuild_set.png", script_syntax=fopr_rebuild_set_button)
        #self.add_button(label="Light Rig to Camera", annotation="Creates a camera offset rig for light rigs", icon="camera_offset.png", script_syntax=light_rig_to_camera_button)
        #self.add_button(label="Context Switcher", annotation="Switches context in the current environment", icon="context_switcher.png", script_syntax=context_switcher_button)
        #self.add_button(label="Documentation", annotation="Opens the shotgun documentation", icon="SG_doc.png", script_syntax=shotgun_button)
        #self.add_button(label="Giant Wiki", annotation="Opens the Giant Wiki", icon="Giant_wiki.png", script_syntax=giant_wiki_button)
        #self.add_button(label="Redshift Documentation", annotation="Opens the Redshift Documentation", icon="RS_doc.png", script_syntax=redshift_doc_button)


def build_shelf():
    if dept == "LGT":
        g_lighting_shelf()
