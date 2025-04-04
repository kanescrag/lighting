
#LIGHTING SHELF MODULE - REFLECTOR (BOUNCE) AND FLAG (BLOCKER) TOOLKIT - V001
#------------------------------------

import maya.cmds as cmds
import maya.mel as mel
import os


def blockBounce():
    # ----------LIGHTS FUNCTIONS----------#

    # FLAG----------*
    def flagUtil(*args):
        # check geo selection
        tickCheck = cmds.checkBox(bb, query=True, value = True)
        geoSel = cmds.ls(selection = True)
        for i in geoSel:
            tx = cmds.getAttr(i + ".translateX")
            ty = cmds.getAttr(i + ".translateY")
            tz = cmds.getAttr(i + ".translateZ")
        # grab condtional name
        result = cmds.promptDialog(title='Enter Target Description' ,message='Enter Name:'
                                   ,button=['Square' ,'Disc' ,'Cancel'] ,defaultButton='OK' ,cancelButton='Cancel'
                                   ,dismissString='Cancel')
        if result == 'Cancel':
            pass
        else:
            answer = cmds.promptDialog(query=True, text=True)
            y = str(answer)
            grpList = cmds.ls()
            if len(answer) > 8:
                cmds.confirmDialog( title='Name Error', message='Light descriptor is too long\n\nMaximum 8 letters allowed...', button=['OK'], defaultButton='OK', cancelButton='OK', dismissString='OK' )
            elif len(answer) < 9:
                z = answer + "_flag"
                if z in grpList:
                    cmds.confirmDialog( title='Name Error', message='A light with this name already exists...', button=['OK'], defaultButton='OK', cancelButton='OK', dismissString='OK' )
                else:
                    # create lgt group
                    grpList = cmds.ls()
                    if 'lights' in grpList:
                        pass
                    else:
                        cmds.group( em=True, name='lights')
                    if 'light_utilities' in grpList:
                        pass
                    else:
                        cmds.group( em=True, name='light_utilities')
                        cmds.parent( 'light_utilities', 'lights' )
                    # create card
                    if result == 'Square':
                        cmds.polyPlane(w= 30, h=30, sx = 2 ,sy=2)
                        cmds.rotate( 90, 0, 0, r=True )
                        x = cmds.rename(answer + '_flag')
                        cmds.addAttr( shortName='op', longName='opacity', defaultValue=1, minValue=0, maxValue=1 ,k = True )
                        cmds.move( 0, 50, 0)
                        cmds.parent(x, 'light_utilities')
                        cmds.setAttr (x + ".primaryVisibility", 0)
                        cmds.setAttr (x + ".visibleInReflections", 0)
                        cmds.setAttr (x + ".visibleInRefractions", 0)
                        # assign shader
                        shdname = myShader = cmds.shadingNode('RedshiftMaterial', asShader=True, n = str(x) + "_shd")
                        cmds.setAttr(shdname + ".diffuse_color" ,0, 0, 0,type = "double3" )
                        cmds.setAttr(shdname + ".refl_weight", 0)
                        cmds.select(x)
                        cmds.hyperShade( assign=shdname)
                        cmds.connectAttr (x + ".opacity", shdname + ".opacity_colorR")
                        cmds.connectAttr (x + ".opacity", shdname + ".opacity_colorG")
                        cmds.connectAttr (x + ".opacity", shdname + ".opacity_colorB")
                    elif result == 'Disc':
                        disc = cmds.polyCylinder(n = "discCylinder" ,sx = 30, sz = 1)
                        mel.eval("select -r discCylinder.f[0:59] ;")
                        cmds.delete()
                        cmds.select(disc)
                        mel.eval("move -r 0 0.9999497 0 discCylinder.scalePivot discCylinder.rotatePivot ;")
                        cmds.delete(ch = True)
                        cmds.scale(15 ,15 ,15)
                        cmds.rotate(90 ,0 ,0)
                        cmds.move( 0, 48.928169, 0 )
                        x = cmds.rename(answer + '_flag')
                        cmds.addAttr( shortName='op', longName='opacity', defaultValue=1, minValue=0, maxValue=1 ,k = True )
                        cmds.parent(x, 'light_utilities')
                        cmds.setAttr (x + ".primaryVisibility", 0)
                        cmds.setAttr (x + ".visibleInReflections", 0)
                        cmds.setAttr (x + ".visibleInRefractions", 0)
                        # flag shd
                        shdname = myShader = cmds.shadingNode('RedshiftMaterial', asShader=True, n = str(x) + "_shd")
                        cmds.setAttr(shdname + ".diffuse_color" ,0, 0, 0, type = "double3" )
                        cmds.setAttr(shdname + ".refl_weight", 0)
                        cmds.select(x)
                        cmds.hyperShade( assign=shdname)
                        cmds.connectAttr (x + ".opacity", shdname + ".opacity_colorR")
                        cmds.connectAttr (x + ".opacity", shdname + ".opacity_colorG")
                        cmds.connectAttr (x + ".opacity", shdname + ".opacity_colorB")

                    if geoSel == []:
                        pass
                    elif tickCheck == False:
                        pass
                    else:
                        cmds.setAttr(x + ".translateX" ,tx)
                        cmds.setAttr(x + ".translateY" ,ty)
                        cmds.setAttr(x + ".translateZ" ,tz)

                        # REFLECTOR WHITE----------*
    def reflectorUtilWhite(*args):
        # check geo selection
        tickCheck = cmds.checkBox(bb, query=True, value = True)
        geoSel = cmds.ls(selection = True)
        for i in geoSel:
            tx = cmds.getAttr(i + ".translateX")
            ty = cmds.getAttr(i + ".translateY")
            tz = cmds.getAttr(i + ".translateZ")
        # grab condtional name
        result = cmds.promptDialog(title='Enter Target Description' ,message='Enter Name:'
                                   ,button=['Square' ,'Disc' ,'Cancel'] ,defaultButton='OK' ,cancelButton='Cancel'
                                   ,dismissString='Cancel')
        if result == 'Cancel':
            pass
        else:
            answer = cmds.promptDialog(query=True, text=True)
            y = str(answer)
            grpList = cmds.ls()
            if len(answer) > 8:
                cmds.confirmDialog( title='Name Error', message='Light descriptor is too long\n\nMaximum 8 letters allowed...', button=['OK'], defaultButton='OK', cancelButton='OK', dismissString='OK' )
            elif len(answer) < 9:
                z = answer + "_reflector"
                if z in grpList:
                    cmds.confirmDialog( title='Name Error', message='A light with this name already exists...', button=['OK'], defaultButton='OK', cancelButton='OK', dismissString='OK' )
                else:
                    # create lgt group
                    grpList = cmds.ls()
                    if 'lights' in grpList:
                        pass
                    else:
                        cmds.group( em=True, name='lights')
                    if 'light_utilities' in grpList:
                        pass
                    else:
                        cmds.group( em=True, name='light_utilities')
                        cmds.parent( 'light_utilities', 'lights' )
                    # create card
                    if result == 'Square':
                        cmds.polyPlane(w= 30, h=30, sx = 2 ,sy=2)
                        cmds.rotate( 90, 0, 0, r=True )
                        x = cmds.rename(answer + '_reflector')
                        cmds.addAttr( shortName='op', longName='opacity', defaultValue=1, minValue=0, maxValue=1 ,k = True )
                        cmds.move( 0, 50, 0)
                        cmds.parent(x, 'light_utilities')
                        cmds.setAttr (x + ".primaryVisibility", 0)
                        cmds.setAttr (x + ".visibleInReflections", 0)
                        cmds.setAttr (x + ".visibleInRefractions", 0)
                        # assign shader
                        shdname = myShader = cmds.shadingNode('RedshiftMaterial', asShader=True, n = str(x) + "_shd")
                        cmds.setAttr(shdname + ".diffuse_color" ,0.95, 0.95, 0.95, type = "double3" )
                        cmds.setAttr(shdname + ".refl_weight", 0)
                        cmds.select(x)
                        cmds.hyperShade( assign=shdname)
                        cmds.connectAttr (x + ".opacity", shdname + ".opacity_colorR")
                        cmds.connectAttr (x + ".opacity", shdname + ".opacity_colorG")
                        cmds.connectAttr (x + ".opacity", shdname + ".opacity_colorB")
                    elif result == 'Disc':
                        disc = cmds.polyCylinder(n = "discCylinder" ,sx = 30, sz = 1)
                        mel.eval("select -r discCylinder.f[0:59] ;")
                        cmds.delete()
                        cmds.select(disc)
                        mel.eval("move -r 0 0.9999497 0 discCylinder.scalePivot discCylinder.rotatePivot ;")
                        cmds.delete(ch = True)
                        cmds.scale(15 ,15 ,15)
                        cmds.rotate(90 ,0 ,0)
                        cmds.move( 0, 48.928169, 0 )
                        x = cmds.rename(answer + '_reflector')
                        cmds.addAttr( shortName='op', longName='opacity', defaultValue=1, minValue=0, maxValue=1 ,k = True )
                        cmds.parent(x, 'light_utilities')
                        cmds.setAttr (x + ".primaryVisibility", 0)
                        cmds.setAttr (x + ".visibleInReflections", 0)
                        cmds.setAttr (x + ".visibleInRefractions", 0)
                        # assign shader
                        shdname = myShader = cmds.shadingNode('RedshiftMaterial', asShader=True, n = str(x) + "_shd")
                        cmds.setAttr(shdname + ".diffuse_color" ,0.95, 0.95, 0.95, type = "double3" )
                        cmds.setAttr(shdname + ".refl_weight", 0)
                        cmds.select(x)
                        cmds.hyperShade( assign=shdname)
                        cmds.connectAttr (x + ".opacity", shdname + ".opacity_colorR")
                        cmds.connectAttr (x + ".opacity", shdname + ".opacity_colorG")
                        cmds.connectAttr (x + ".opacity", shdname + ".opacity_colorB")

                    if geoSel == []:
                        pass
                    elif tickCheck == False:
                        pass
                    else:
                        cmds.setAttr(x + ".translateX" ,tx)
                        cmds.setAttr(x + ".translateY" ,ty)
                        cmds.setAttr(x + ".translateZ" ,tz)

    # REFLECTOR GREY----------*
    def reflectorUtilGrey(*args):
        # check geo selection
        tickCheck = cmds.checkBox(bb, query=True, value = True)
        geoSel = cmds.ls(selection = True)
        for i in geoSel:
            tx = cmds.getAttr(i + ".translateX")
            ty = cmds.getAttr(i + ".translateY")
            tz = cmds.getAttr(i + ".translateZ")
        # grab condtional name
        result = cmds.promptDialog(title='Enter Target Description' ,message='Enter Name:'
                                   ,button=['Square' ,'Disc' ,'Cancel'] ,defaultButton='OK' ,cancelButton='Cancel'
                                   ,dismissString='Cancel')
        if result == 'Cancel':
            pass
        else:
            answer = cmds.promptDialog(query=True, text=True)
            y = str(answer)
            grpList = cmds.ls()
            if len(answer) > 8:
                cmds.confirmDialog( title='Name Error', message='Light descriptor is too long\n\nMaximum 8 letters allowed...', button=['OK'], defaultButton='OK', cancelButton='OK', dismissString='OK' )
            elif len(answer) < 9:
                z = answer + "_reflector"
                if z in grpList:
                    cmds.confirmDialog( title='Name Error', message='A utility with this name already exists...', button=['OK'], defaultButton='OK', cancelButton='OK', dismissString='OK' )
                else:
                    # create lgt group
                    grpList = cmds.ls()
                    if 'lights' in grpList:
                        pass
                    else:
                        cmds.group( em=True, name='lights')
                    if 'light_utilities' in grpList:
                        pass
                    else:
                        cmds.group( em=True, name='light_utilities')
                        cmds.parent( 'light_utilities', 'lights' )
                    # create card
                    if result == 'Square':
                        cmds.polyPlane(w= 30, h=30, sx = 2 ,sy=2)
                        cmds.rotate( 90, 0, 0, r=True )
                        x = cmds.rename(answer + '_reflector')
                        cmds.addAttr( shortName='op', longName='opacity', defaultValue=1, minValue=0, maxValue=1 ,k = True )
                        cmds.move( 0, 50, 0)
                        cmds.parent(x, 'light_utilities')
                        cmds.setAttr (x + ".primaryVisibility", 0)
                        cmds.setAttr (x + ".visibleInReflections", 0)
                        cmds.setAttr (x + ".visibleInRefractions", 0)
                        # assign shader
                        shdname = myShader = cmds.shadingNode('RedshiftMaterial', asShader=True, n = str(x) + "_shd")
                        cmds.setAttr(shdname + ".diffuse_color" ,0.187, 0.187, 0.187, type = "double3" )
                        cmds.setAttr(shdname + ".refl_weight", 0)
                        cmds.select(x)
                        cmds.hyperShade( assign=shdname)
                        cmds.hyperShade( assign=shdname)
                        cmds.connectAttr (x + ".opacity", shdname + ".opacity_colorR")
                        cmds.connectAttr (x + ".opacity", shdname + ".opacity_colorG")
                        cmds.connectAttr (x + ".opacity", shdname + ".opacity_colorB")
                    elif result == 'Disc':
                        disc = cmds.polyCylinder(n = "discCylinder" ,sx = 30, sz = 1)
                        mel.eval("select -r discCylinder.f[0:59] ;")
                        cmds.delete()
                        cmds.select(disc)
                        mel.eval("move -r 0 0.9999497 0 discCylinder.scalePivot discCylinder.rotatePivot ;")
                        cmds.delete(ch = True)
                        cmds.scale(15 ,15 ,15)
                        cmds.rotate(90 ,0 ,0)
                        cmds.move( 0, 48.928169, 0 )
                        x = cmds.rename(answer + '_reflector')
                        cmds.addAttr( shortName='op', longName='opacity', defaultValue=1, minValue=0, maxValue=1 ,k = True )
                        cmds.parent(x, 'light_utilities')
                        cmds.setAttr (x + ".primaryVisibility", 0)
                        cmds.setAttr (x + ".visibleInReflections", 0)
                        cmds.setAttr (x + ".visibleInRefractions", 0)
                        shdname = myShader = cmds.shadingNode('RedshiftMaterial', asShader=True, n = str(x) + "_shd")
                        cmds.setAttr(shdname + ".diffuse_color" ,0.187, 0.187, 0.187, type = "double3" )
                        cmds.setAttr(shdname + ".refl_weight", 0)
                        cmds.select(x)
                        cmds.hyperShade( assign=shdname)
                        cmds.connectAttr (x + ".opacity", shdname + ".opacity_colorR")
                        cmds.connectAttr (x + ".opacity", shdname + ".opacity_colorG")
                        cmds.connectAttr (x + ".opacity", shdname + ".opacity_colorB")

                    if geoSel == []:
                        pass
                    elif tickCheck == False:
                        pass
                    else:
                        cmds.setAttr(x + ".translateX" ,tx)
                        cmds.setAttr(x + ".translateY" ,ty)
                        cmds.setAttr(x + ".translateZ" ,tz)

                        # REFLECTOR SQUARE----------*

    # def reflectorSquare(*args):

    # DIFFUSER SQUARE----------*
    # def flagSquare(*args):

    # ---------WINDOW----------*




    if cmds.window("LgtUtilityManager", exists = True):
        cmds.deleteUI("LgtUtilityManager")

    window = cmds.window("LgtUtilityManager", title="Lighting Utility Manager" ,widthHeight=(250, 300) )
    cmds.columnLayout( adjustableColumn=True )
    cmds.separator(h=20)
    cmds.text(l="LIGHT UTILITIES", align = "center")
    cmds.separator(h=20)
    cmds.separator(h=20)
    cmds.text(l="Flags [ blockers ]", align = "center" )
    cmds.separator(h=20)
    cmds.button( label='Flag' ,c = flagUtil, bgc = [0.4 ,0.4 ,0.4])
    cmds.separator(h=20)
    cmds.text(l="Reflectors", align = "center" )
    cmds.separator(h=20)
    cmds.button( label='Reflector [ grey ]' ,c = reflectorUtilGrey, bgc = [0.4 ,0.4 ,0.4])
    cmds.separator()
    cmds.button( label='Reflector [ white ]' ,c = reflectorUtilWhite, bgc = [0.4 ,0.4 ,0.4])
    cmds.separator(h=20)
    # cmds.text(l="Diffuser", align = "center" )
    # cmds.separator(h=20)
    # cmds.button( label='Rim - directional',c = rimDirect, bgc = [0.4,0.4,0.4]  )
    # cmds.separator()
    # cmds.button( label='Diffuser- square',bgc = [0.4,0.4,0.4] )
    # cmds.separator(h=20)
    bb = cmds.checkBox( label='Create utility at selection', align='center' )
    cmds.separator(h=20)
    cmds.showWindow( window )
