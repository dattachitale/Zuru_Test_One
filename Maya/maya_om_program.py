"""
This script file is for OM and Commands (Testing Understanding of Maya batch, OM, Commands) assignment:

1. Write some code that performs the following. The code should be able to be run from Terminal/Console
        loads an empty scene
        runs the following python code
        Using maya commands
        Create a cube
        Add an attribute "Show Duplicate" as boolean
        Using the latest Object Model python module
        Get the newly created object
        Duplicate the cube and parent it under the original
        Rename it "CubeB"
        move the CubeB, 10 on X
        add an attribute called "Duplicate" of type boolean
        Connect the "Show Duplicate" attribute, to drve the visibility of CubeB, and the attribute "Duplicate"
        Query thegeometry of CubeB
        Delete the top Face
        Saves the scene
"""

import maya.cmds as cmds
import maya.OpenMaya as om


cmds.file(new=True, force=True)

# Create a cube
cube = cmds.polyCube()[0]

cmds.addAttr(cube, longName="ShowDuplicate", attributeType="bool")

cubeB = cmds.duplicate(cube, name="CubeB")[0]

cmds.rename(cubeB, "CubeB")

cmds.move(10, 0, 0, cubeB, relative=True)

cmds.addAttr(cubeB, longName="Duplicate", attributeType="bool")

# Connect the "Show Duplicate" attribute to drive the visibility of CubeB, and the attribute "Duplicate"
cmds.connectAttr(cube + ".ShowDuplicate", cubeB + ".visibility")
cmds.connectAttr(cube + ".ShowDuplicate", cubeB + ".Duplicate")

# Query the geometry of CubeB
geometry = cmds.ls(cubeB, geometry=True)[0]

# Delete the top Face
cmds.select(geometry + ".f[0]")
cmds.delete()

# Save the scene
cmds.file(rename="path to save scene.ma")
cmds.file(save=True, type="mayaAscii")

######################################################################################################################################


"""
This script file is for OM and Commands (Testing Understanding of Maya batch, OM, Commands) assignment:

2. Write the following code using OM 
        Move Selected object in X by 2
        Move Selected Object in Y by 2
        Move one of the faces of the object outwards by 4
        If undo is triggered, all of these modification should be undone in one undo.
3. Remove all the namespaces in a scene, using OM.
        Namespaces can be nested in this example
        After the code has run all namespaces should no longer exist.
"""

import maya.cmds as cmds
import maya.OpenMaya as om

def move_selected_object_in_x_and_y():
    # Get selected object(s)
    selection = om.MSelectionList()
    om.MGlobal.getActiveSelectionList(selection)

    # Iterate over selected objects
    for i in range(selection.length()):
        # Get DAG path of selected object
        dag_path = om.MDagPath()
        selection.getDagPath(i, dag_path)

        # Move object in X and Y by 2
        transform_fn = om.MFnTransform(dag_path)
        transform_fn.translateBy(om.MVector(2, 2, 0), om.MSpace.kTransform)

def move_face_outwards_by_4():
    # Get selected face
    sel_list = om.MSelectionList()
    om.MGlobal.getActiveSelectionList(sel_list)
    dag_path = om.MDagPath()
    component = om.MObject()

    sel_list.getDagPath(0, dag_path, component)

    # Create iterator for vertices of the face
    iter_vertices = om.MItMeshVertex(dag_path, component)

    # Move each vertex outwards by 4
    while not iter_vertices.isDone():
        vertex_pos = iter_vertices.position(om.MSpace.kTransform)
        new_pos = om.MPoint(vertex_pos.x + 4, vertex_pos.y, vertex_pos.z)
        iter_vertices.setPosition(new_pos, om.MSpace.kTransform)
        iter_vertices.next()

def remove_all_namespaces():
    # Get all namespaces in the scene
    all_namespaces = om.MNamespace.getAllNamespaces()

    # Remove each namespace
    for namespace in all_namespaces:
        om.MNamespace.removeNamespace(namespace)

def main():
    cmds.undoInfo(openChunk=True)
    move_selected_object_in_x_and_y()
    move_face_outwards_by_4()
    remove_all_namespaces()
    cmds.undoInfo(closeChunk=True)

main()