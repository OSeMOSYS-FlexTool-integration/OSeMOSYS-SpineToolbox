# OSeMOSYS-SpineToolbox
Allows using Spine Toolbox for OSeMOSYS scenario and workflow management

## Installation 

### Simple installation

    Load and extract two zip files. 
    The first contains the contents of this repository.
    
    The second file contains the Spine Toolbox with an executable for starting the toolbox. 
    https://github.com/spine-tools/Spine-Toolbox/releases/download/0.9.6/Spine-Toolbox-win-0.9.6.zip
    These will only work with Windows 10 and Windows 11.

### Installation with terminal

    Install git.
    Git clone this repository:

    ```
    git clone https://github.com/OSeMOSYS-FlexTool-integration/OSeMOSYS-SpineToolbox
    ```

    Install Spine-Toolbox 

    Follow the instructions in https://github.com/spine-tools/Spine-Toolbox
    You can install it with pipx or git.
        

## Use

    Start Spine Toolbox either by the executable or from terminal depending on the installation.
    Go to File -> New project. Find the folder OSeMOSYS-SpineToolbox that you extracted. You will see the toolbox symbol next to it.

    The Toolbox takes in ready made osemosys files. This is the file you would pass to the OSeMOSYS.
    
    1. Click Osemosys_data. Add file path by clicking the green plus symbol. Find your input file.
    2. Click Read_OSeMOSYS. Remove the old path from the third argument by clicking it and the red minus symbol. Drag the new path from the available resources as the new third argument.
    3. Run Read_OSeMOSYS.
    4. The Osemosys__data database should now contain your data. You can create new scenarios by:

        - Create a new alternative
        - Create a new scenario
        - Add the base scenario and the new alternative to this new scenario. The lower alternatives in the list override higher ones.
        - Add data to this new alternative by adding rows to the data but using the new alternative in the alternative name column. Check from the data format from the base 
        -  Commit changes
    6. Choose the new scenario from the filter selection. Running multiple scenarios at the same time is not supported.
    7. Run Write_OSeMOSYS. This creates a new osemosys input file. The filename can be changed from the osemosys settings.
    8. Run Run_OSeMOSYS. Alternatively you can pass this input file to solver of your choice.

## Contents

This repository contains:

- glpsol_files: The solver glpsol and its dependencies
- mathprog_files: Contains Osemosys mathprog file model.mod. (https://github.com/OSeMOSYS/OSeMOSYS) 
    The param_dimens.yaml is temporary file that is used in the transformations
- ines_tools_mathprog: Contains mathprog transformation files from ines-tools (https://github.com/ines-tools/ines-tools)
- data: contains example files
- .spinetoolbox contains the Spine toolbox workflow files. 
- python files that handle the transformation
