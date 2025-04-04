'''

AOV Toolkit
AUTHOR - CRAIG KANE - 15/02/22
------------------------------

AOV tool for creating common and custom aovs



------------------------------

'''



#import libraries---------------------

import maya.app.renderSetup.model.override as override
import maya.app.renderSetup.model.selector as selector
import maya.app.renderSetup.model.collection as collection
import maya.app.renderSetup.model.renderLayer as renderLayer
import maya.app.renderSetup.model.renderSetup as renderSetup
import maya.OpenMaya as om
import maya.cmds as cmds
import maya.mel as mel
import json

#import fopr collection wildcard mesh lists ===============================================

json_file_path = r"Z:\studio_tools\pipe2\show\fopr\maya\utilities\lighting\scripts\lists\fopr_mesh_list.json"

with open(json_file_path, 'r') as json_file:
    json_data = json.load(json_file)
    fopr_aov_names = json_data['fopr_aov_names']


#lists
aovs = ['Beauty','Cryptomatte', 'Depth', 'Diffuse Filter','Diffuse Lighting', 'Global Illumination', 'Object-Space Bump Normals',
        'Reflections','Refractions', 'Specular Lighting', 'World Position','Emission','GI'] 

fopr_aov_names = ['eyeringL_msk',
                  'eyeringR_msk',
                  'thinLips_msk',
                  'innerMouth_msk',
                  'pointyLips_msk',
                  'noseEarsBlend_msk',
                  'sheen_refl',
                  'sheen_diffuse',
                  'beard_mouth_msk',
                  'cheek_flap_msk',
                  'beard_msk',
                  'no_beard_skin',
                  #'head_mouth_area_msk',
                  #'SpecularMSK',
                  'l_glowEye',
                  'r_glowEye',
                  'glowMat_msk',
                  'prp_wand',
                  ##'chr_CharName_pointLips_msk_raw_1001',
                  #'broccoli_MSK',
                  'blush_msk',
                  #'puddingstate1',
                  #'puddingstate2',
                  'conjunctionLine_msk',
                  'viozaliamsk ',
                  'ghostPepperEye_aov',
                  'ghostPepperEyeBorder_aov',
                  'hat_mask_aov',
                  'nose_msk ',
                  'goldTeeth_msk',
                  'geoBeard_msk',
                  'saltyLips_MSK',
                  'glow_mask_maceWandirep',
                  'ExtraNeck_Msk' ,
                  'pattyPossum_teeth_msk' ,
                  'lens_msk',
                  'clownTriangles_msk',
                  'mindAngelaGlow_msk',
                  'bike_light_aov',
                  'tv_screen_aov',
                  'clownLips_msk',
                  'clownWhite_msk',
                  'glowStarMat',
                  'pathDev_msk',
                  'teethCurvature_msk'


                  

] 


#functions============================================


#individual aov fuctions------------------------------

def create_beauty_aov():
    
    if cmds.objExists("*rsAov_Beauty*"):
        om.MGlobal.displayInfo("########      Beauty AOV already exists        ########")
    else:
        cmds.rsCreateAov (type = "Beauty")
        cmds.setAttr('rsAov_Beauty.filePrefix',"<BeautyPath>/<BeautyFile>", type = 'string')
        cmds.setAttr ("rsAov_Beauty.allLightGroups", 1)
        cmds.setAttr ("rsAov_Beauty.name", "Beauty",type = 'string')
        om.MGlobal.displayInfo("########      Beauty AOV created        ########")


def create_depth_aov():
                    
    if cmds.objExists('rsAov_Depth'):
        om.MGlobal.displayInfo("########      Depth AOV already exists        ########")
    else:
        cmds.rsCreateAov (type = "Depth") 
        cmds.setAttr ("rsAov_Depth.depthMode", 0)
        cmds.setAttr ("rsAov_Depth.useCameraNearFar", 0)
        cmds.setAttr ("rsAov_Depth.exrCompression", 4)
        cmds.setAttr ("rsAov_Depth.exrBits",32)
        cmds.setAttr ("rsAov_Depth.filterMode",1)  
        om.MGlobal.displayInfo("########      Depth AOV created        ########")


def create_cryptomatte_aov():
            
    if cmds.objExists('rsAov_Cryptomatte'):
        om.MGlobal.displayInfo("########      Cryptomatte AOV already exists        ########")
    else:
        cmds.rsCreateAov (type = "Cryptomatte") 
        cmds.setAttr ("rsAov_Cryptomatte.exrDwaCompressionLevel", 0)
        cmds.setAttr ("rsAov_Cryptomatte.exrCompression", 4)
        cmds.setAttr ("rsAov_Cryptomatte.exrBits",32)
        cmds.setAttr ("rsAov_Cryptomatte.idType",1)  
        cmds.setAttr ("rsAov_Cryptomatte.idType", 0)
        om.MGlobal.displayInfo("########      Cryptomatte AOV created        ########")


def create_object_space_bump_normals_aov():
                    
    if cmds.objExists('rsAov_Object_SpaceBumpNormals'):
        om.MGlobal.displayInfo("########      Object_SpaceBumpNormals AOV already exists        ########")
    else:
        cmds.rsCreateAov (type = "Object-Space Bump Normals")
        cmds.setAttr ("rsAov_Object_SpaceBumpNormals.exrDwaCompressionLevel", 0)
        cmds.setAttr ("rsAov_Object_SpaceBumpNormals.exrCompression", 4)
        cmds.setAttr ("rsAov_Object_SpaceBumpNormals.exrBits",32)  
        om.MGlobal.displayInfo("########      Object_SpaceBumpNormals AOV created        ########")


def create_world_position_aov():
                    
    if cmds.objExists('rsAov_WorldPosition'):
        om.MGlobal.displayInfo("########      World Position AOV already exists        ########")
    else:
        cmds.rsCreateAov (type = "World Position")
        cmds.setAttr ("rsAov_WorldPosition.exrDwaCompressionLevel", 0)
        cmds.setAttr ("rsAov_WorldPosition.exrCompression", 4)
        cmds.setAttr ("rsAov_WorldPosition.scaleZ", -1)
        cmds.setAttr ("rsAov_WorldPosition.exrBits",32)
        om.MGlobal.displayInfo("########      World Position AOV created        ########")      
    

def create_reflections_aov():
                    
    if cmds.objExists('rsAov_Reflections'):
        om.MGlobal.displayInfo("########      Reflections AOV already exists        ########")
    else:
        cmds.rsCreateAov (type = "Reflections")
        om.MGlobal.displayInfo("########      Reflections AOV created        ########")


def create_GI_aov():
                    
    if cmds.objExists('rsAov_GlobalIllumination'):
        om.MGlobal.displayInfo("########      GI AOV already exists        ########")
    else:
        cmds.rsCreateAov (type = "Global Illumination")
        om.MGlobal.displayInfo("########      GI AOV created        ########")


def create_emission_aov():
                    
    if cmds.objExists('rsAov_Emission'):
        om.MGlobal.displayInfo("########      Emission AOV already exists        ########")
    else:
        cmds.rsCreateAov (type = "Emission")
        om.MGlobal.displayInfo("########      Emission AOV created        ########")

                    
def create_refractions_aov():
                    
    if cmds.objExists('rsAov_Refractions'):
        om.MGlobal.displayInfo("########      Refractions AOV already exists        ########")
    else:
        cmds.rsCreateAov (type = "Refractions")
        om.MGlobal.displayInfo("########      Refractions AOV created        ########")


def create_specular_aov():
    if cmds.objExists('rsAov_SpecularLighting'):
        om.MGlobal.displayInfo("########      Specular Lighting AOV already exists        ########")
    else:
        cmds.rsCreateAov (type = "Specular Lighting")
        om.MGlobal.displayInfo("########      Specular Lighting AOV created        ########")


def create_diffuse_filter_aov():
    if cmds.objExists('rsAov_DiffuseFilter'):
        om.MGlobal.displayInfo("########      Diffuse Filter AOV already exists        ########")
    else:
        cmds.rsCreateAov (type = "Diffuse Filter")
        om.MGlobal.displayInfo("########      Diffuse Filter created        ########")


def create_diffuse_lighting_aov():
    if cmds.objExists('rsAov_DiffuseLighting'):
        om.MGlobal.displayInfo("########      Diffuse Lighting AOV already exists        ########")
    else:
        cmds.rsCreateAov (type = "Diffuse Lighting")
        om.MGlobal.displayInfo("########      Diffuse Lighting created        ########")


def create_uv_aov():
    shader_name ='uv_shader'
    shaderSet=shader_name +"_SET"

    #create uv shader

    if cmds.objExists('uv_shader'):
        cmds.delete('uv_shader')
            
    uv_node = cmds.shadingNode("RedshiftState", asShader=True, name=shader_name)
    #cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name=shaderSet)
                
    #get existing aovs
    aov_list = cmds.ls(type='RedshiftAOV')
    aov_name_list = []
    for i in aov_list:
        aov_name = cmds.getAttr(i + '.name')
        aov_name_list.append(aov_name)

    ##check if uv aov exists
    if 'UV' in aov_name_list:
        pass
    else:
        uv_aov = cmds.rsCreateAov(type='Custom')
        cmds.setAttr(uv_aov + '.name', "UV",type = "string")
        #cmds.rename(uv_aov, "uv_aov")

    #make connections
    try:
        cmds.connectAttr(uv_node + '.outUVCoord0', uv_aov + '.defaultShaderR')
        cmds.connectAttr(uv_node + '.outUVCoord1', uv_aov + '.defaultShaderG')
    except:
        pass


    mel.eval("redshiftUpdateActiveAovList()")
    om.MGlobal.displayInfo("########       UV AOV created        ########") 



def create_ao_aov():
    shader_name ='ao_shader'
    shaderSet=shader_name +"_SET"

    #create uv shader

    if cmds.objExists('ao_shader'):
        cmds.delete('ao_shader')
            
    ao_node = cmds.shadingNode("RedshiftAmbientOcclusion", asShader=True, name=shader_name)
    cmds.setAttr (ao_node + ".numSamples", 2048)
    #cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name=shaderSet)
    

                
    #get existing aovs
    aov_list = cmds.ls(type='RedshiftAOV')
    aov_name_list = []
    for i in aov_list:
        aov_name = cmds.getAttr(i + '.name')
        aov_name_list.append(aov_name)

    ##check if uv aov exists
    if 'AO' in aov_name_list:
        pass
    else:
        ao_aov = cmds.rsCreateAov(type='Custom')
        cmds.setAttr(ao_aov + '.name', "AO",type = "string")
        cmds.rename(ao_aov, "AO_aov")

    #make connections
    try:
        cmds.connectAttr(ao_node + '.outColor', 'AO_aov.defaultShader')
    except:
        pass

    #swap colours
    cmds.setAttr (ao_node + ".bright",0 ,0 ,0,type = 'double3' )
    cmds.setAttr (ao_node + ".dark",1 ,1 ,1,type = 'double3' )

    mel.eval("redshiftUpdateActiveAovList()")
    om.MGlobal.displayInfo("########       AO AOV created        ########") 



def create_rsState_aov():
    shader_name ='rsState_shader'
    shaderSet=shader_name +"_SET"
    
        #create uv shader
    
    if cmds.objExists('rsState_shader'):
        cmds.delete('rsState_shader')
                
    state_node = cmds.shadingNode("RedshiftState", asShader=True, name=shader_name)
    
                    
    #get existing aovs
    aov_list = cmds.ls(type='RedshiftAOV')
    x = cmds.ls()
    aov_name_list = []
    for i in aov_list:
        aov_name = cmds.getAttr(i + '.name')
        aov_name_list.append(aov_name)
    
    ##check if uv aov exists
    if 'Normals' in aov_name_list:
        pass
    else:
        state_aov = cmds.rsCreateAov(type='Custom')
        cmds.setAttr(state_aov + '.name', "Normals",type = "string")
        cmds.rename(state_aov, "Normals_aov")
    
        #make connections
        try:
            cmds.connectAttr(state_node + '.outNormal', 'Normals_aov.defaultShader')
        except:
            pass
    
        mel.eval("redshiftUpdateActiveAovList()")
        om.MGlobal.displayInfo("########       Normal State created        ########") 


def create_fopr_character_aovs():

    #get existing aov custom names
    aov_list = cmds.ls(type='RedshiftAOV')
    custom_names = []

    for aov_name in aov_list:
        custom_name_individual = cmds.getAttr(aov_name + ".name")
        custom_names.append(custom_name_individual)

    # check if each name in fopr_aov_names exists in custom_names
    for aov_name in fopr_aov_names:
        if aov_name in custom_names:
            pass
        else:
            ao_aov = cmds.rsCreateAov(type='Custom')
            cmds.setAttr(ao_aov + '.name', aov_name, type='string')

    

    mel.eval("redshiftUpdateActiveAovList()")
    om.MGlobal.displayInfo("########       Character FOPR AOVs created        ########")   


#aov toolkit function----------------------------------


def aov_toolkit():


    def create_aovs(*args):

        #get dropdown state...
        choice = cmds.optionMenu(ltd, q=True, v=True)   
     
        if choice == 'UV':
            create_uv_aov()
            mel.eval("redshiftUpdateActiveAovList()")


        elif choice == 'AO':
            create_ao_aov()
            mel.eval("redshiftUpdateActiveAovList()")


        elif choice == 'Production AOVs':
            create_ao_aov()
            create_beauty_aov()
            create_depth_aov()
            create_cryptomatte_aov()
            create_object_space_bump_normals_aov()
            create_world_position_aov()
            create_reflections_aov()
            create_refractions_aov()
            create_specular_aov()
            create_diffuse_filter_aov()
            create_emission_aov()
            create_GI_aov()
            create_rsState_aov()
            create_diffuse_lighting_aov()
            mel.eval("redshiftUpdateActiveAovList()")


        elif choice == 'FOPR Character AOVs':
            create_fopr_character_aovs()
            mel.eval("redshiftUpdateActiveAovList()")

    
    def delete_all_aovs(*args):
        all_aovs = cmds.ls(type='RedshiftAOV')
        for aov in all_aovs:
            enabled = cmds.getAttr('%s.enabled' % aov)
            if enabled:
                cmds.delete(aov)
                deleted_aovs = True
                om.MGlobal.displayInfo("########       All AOVs deleted        ########")   






    # Make a new window---------------------------------------------------------------------
    if cmds.window("AOVs", exists = True):
        cmds.deleteUI("AOVs")

    window = cmds.window('AOVs', title="AOV Toolkit", iconName='Short Name', widthHeight=(350, 400), tbm = True,s = False )
    cmds.columnLayout( adjustableColumn=True,cat = ['both',20]  )
    cmds.separator(height=20, style='doubleDash')
    cmds.text('AOV TOOLKIT')
    cmds.separator(height=30)
    cmds.iconTextButton( style='iconOnly', image1="Z:/studio_tools/facility/python/maya/lighting/icons/AOV.png", label='sphere')
    cmds.separator(height=30)
    cmds.text('AOV Type')
    cmds.separator(height=5, style = 'none')
    ltd = cmds.optionMenu('choice_menu',label='')
    cmds.menuItem( label='----')
    cmds.menuItem( label='UV')
    #cmds.menuItem( label='AO')
    cmds.menuItem( label='Production AOVs')
    cmds.menuItem( label='FOPR Character AOVs')
    cmds.separator(height=20, style='doubleDash')
    cmds.button( label='Create AOVs',c = create_aovs )
    cmds.separator(height=30)
    cmds.button( label='Delete All AOVs', c = delete_all_aovs,  bgc=(0.7, 0.3, 0.3))
    cmds.separator(height=30)
    cmds.separator(height=5)
    cmds.button( label='Close', command=('cmds.deleteUI(\"' + window + '\", window=True)') )
    cmds.separator()
    cmds.setParent( '..' )
    cmds.showWindow( window )





