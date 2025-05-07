import sys
import yaml
from ines_tools_mathprog import read_mathprog_model_structure
from ines_tools_mathprog import read_mathprog_model_data
from pathlib import Path


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit("You need to provide the following arguments 1. settings file 2. url of the target Spine database 3. file name for the osemosys data")

    with open(sys.argv[1], 'r') as yaml_file:
        settings = yaml.safe_load(yaml_file)
    url_db = settings["target_db"]
    if len(sys.argv) > 2:
        url_db = sys.argv[2]
    code_file_name = str(Path(__file__).parent / "mathprog_files" / settings["model_code"])
    if len(sys.argv) > 3:
        data_file_name = sys.argv[3]
    param_dimens_file = str(Path(__file__).parent / "mathprog_files" / 'param_dimens.yaml')

    read_mathprog_model_structure.read_mathprog_structure(settings, url_db, code_file_name, param_dimens_file)
    print("Added model structure")
    read_mathprog_model_data.read_mathprog_data(settings, url_db, data_file_name, param_dimens_file)
    print("Added model data")
