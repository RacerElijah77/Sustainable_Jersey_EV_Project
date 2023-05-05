# Collaborative Project for CSC 315 - "Sustainable Jersey"

## Project Contributors:
### Professor: Dr. DeGood
### Developers: Emmanuel Pasteur, Madison Bavosa, EJ Gasataya
### Last Updated: 4/23/23 (for submission on Phase 5b + Added BASH script for simple loading)

## Installation Guide

### Creating Database & Migrating Raw CSV Files into the database
* Prerequisites, ensure that the following packages are installed:
```
# install python pip and psycopg2 packages
sudo pacman -Syu
sudo pacman -S python-pip python-psycopg2

# install flask
pip install flask
# "pip3" for some
```
To run commands and scripts required to create and populate the table, the user must run the following bash command into the terminal:

```
# Make sure that to be in the cab-project-6 directory for this group
bash bash1.sh
```

This allows the CSV contents stored in the data_files sub-directory to be read, and 
stored into the CAB_database based on the DDL amd DML inside the sql scripts. It also opens the UI on the default browser. 
The "typescript" file is a history file containing the DML commands used for this project.
Note: when the PSQL queries pop up in the terminal, press q to scroll down in the command line until the web page opens.

## GUI Guide

### Retrieve Municipality Name from Zip Code
The user can enter a zip code in the field depicted below.
![Zip Code GUI](images/zipCode.png)

After pressing submit, the user will be able to see the zip code they entered as well as the corresponding municipality name and county name.
![Zip Code Results](images/zipResult.png)

### Retrieve Municipalities According to Range of Vehicle Miles Traveled (VMT)
The user can select a minimum value and a maximum value of VMT using the respective slider tools.
![VMT GUI](images/vmtSliders.png)

After pressing submit, the user can view the municipalities that fall within the desired range of VMT.
![VMT Results](images/vmtResults.png)

### Retrieve Municipalities According to Range of Greenhouse Gas (GHG) Emissions
The user can select a minimum value and a maximum value of GHG emissions in metric tons of carbon using the respective slider tools.
![GHG GUI](images/ghgSliders.png)

After pressing submit, the municipalities whose total GHG emissions lie within the desired range of GHG emissions will be listed. 
![GHG Results](images/ghgResults.png)

## Link to open repository in VSCode Extension
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=10765357&assignment_repo_type=AssignmentRepo)
