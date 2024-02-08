# Zuru_Maya_Project
This includes Maya related assignments. As I do not have maya installed so I have just written python code in two different py files. (Also could not test)

maya_qt.py - this includes first assignment related to Maya QT
maya_om_program.py - this includes the code for OM and Commands assignment - 3 assignments

## maya_qt.py
1. Create a Button that gets the selected object and prints its name [5 points] Testing Understanding of
Maya Qt
This button should be in its own window
Can be docked into the Maya UI

Note: I could solve only one assignment of QT


## maya_om_program.py
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

2. Write the following code using OM 
        Move Selected object in X by 2
        Move Selected Object in Y by 2
        Move one of the faces of the object outwards by 4
        If undo is triggered, all of these modification should be undone in one undo.
3. Remove all the namespaces in a scene, using OM.
        Namespaces can be nested in this example
        After the code has run all namespaces should no longer exist.





