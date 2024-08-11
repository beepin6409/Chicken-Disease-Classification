import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')
#Info means logging onlly information log
#format , it will get asci time and logging message you want to put

#defining project name
project_name = "cnnClassifier"



list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",    # for implementing mlops tools
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

#Windows use backslash and here we are using forward , so handling it is required.

#  What this Path does ?
#  It will authomatically convert and returns the Windows Path

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)  # returns two things i.e. folder and filename


    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory ;{filedir} for the file : {filename}")


    if (not os.path.exists(filepath) or os.path.getsize(filepath) == 0):    # if file doesnt exist then
         with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file : {filepath}")
    else:
        logging.info(f"{filename} is already existed")


