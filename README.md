# OSeMOSYS-SpineToolbox
Allows using Spine Toolbox for OSeMOSYS scenario and workflow management

## Installation 

### Simple installation

Load and extract two zip files. 
The first contains the contents of this repository.
https://github.com/OSeMOSYS-FlexTool-integration/OSeMOSYS-SpineToolbox/archive/refs/tags/1.0.2.zip

The second file contains the Spine Toolbox with an executable for starting the toolbox. 
https://github.com/spine-tools/Spine-Toolbox/releases/download/0.9.3/Spine-Toolbox-win-0.9.3.zip
These will only work with Windows 10 and Windows 11. The zip installed Toolbox is slightly slower than the other option, but it is easier to set up and you will not have to spend time on setting up environments.

### Installation with terminal

Install git.
Git clone this repository to a directory of your choosing:

```
git clone https://github.com/OSeMOSYS-FlexTool-integration/OSeMOSYS-SpineToolbox
```

Install Spine-Toolbox 

Follow the instructions in https://github.com/spine-tools/Spine-Toolbox
You can install it with pipx or git.
        

## Use

Start Spine Toolbox either from the executable or from terminal depending on the installation.
Go to File -> Open project. Find the folder OSeMOSYS-SpineToolbox that you extracted. You will see the toolbox symbol next to it.

The Toolbox takes in ready made osemosys text files. This is the file you would pass to the OSeMOSYS.

1. Click Osemosys_data. Add file path by clicking the green plus symbol. Find your input file.

    ![add_file](./docs/add_file.png)
2. Click Read_OSeMOSYS. Remove the old path from the third argument by clicking it and the red minus symbol. Drag the new path from the available resources as the new third argument.
    
    ![remove_file](./docs/remove_file.png)
    ![drag_file](./docs/drag_file.png)
3. Run Read_OSeMOSYS.
4. The Osemosys__data database should now contain your data. You can create new scenarios by:

    + Create a new alternative
    + Create a new scenario
    + Add the base scenario and the new alternative to this new scenario. The lower alternatives in the list override higher ones.
    
    ![Scenario](./docs/scenario.png)
    
    + Add data to this new alternative by adding rows to the data but using the new alternative in the alternative name column. Check from the data format from the base
    
    ![new data](./docs/new_data.png)

    +  Commit changes
6. Choose the new scenario from the filter selection. Running multiple scenarios at the same time is currentle not supported.

    ![Filter](./docs/filter.png)
7. Run Write_OSeMOSYS. This creates a new osemosys input file. The filename can be changed from the osemosys settings.
8. Run Run_OSeMOSYS. Alternatively you can pass this input file to solver of your choice.


### Settings
The file settings_OSeMOSYS.yaml contains the following settings for the user:

- model_code: The osemosys mathprog file name.
- new_model_name: The name of the new input file.
- target_db: (optional, does not do anything when used in toolbox workflow)
- solution_file: OSeMOSYS solution file name
- alternative_name: The alternative name that the imported data uses.
- purge: True/False. Purge the database before writing new data, if false, change the alternative name between runs


## Contents

This repository contains:

- glpsol_files: The solver Glpsol and its dependencies
- mathprog_files: Contains Osemosys mathprog file model.mod. (https://github.com/OSeMOSYS/OSeMOSYS) 
    The param_dimens.yaml is temporary file that is used in the transformations
- ines_tools_mathprog: Contains mathprog transformation files from ines-tools (https://github.com/ines-tools/ines-tools)
- data: contains example files
- .spinetoolbox contains the Spine toolbox workflow files. 
- python files that handle the transformation
