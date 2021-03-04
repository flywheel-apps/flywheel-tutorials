# Add Group and Project to your Flywheel Instance
## Overview

In this section, we will be showing you a simple Python program that allows you to create new group(s) and project(s) with a CSV file as an input.

## Requirements
- Understand what is Group and Project in Flywheel. *Feel free to check out our docs to learn more about [Group](https://docs.flywheel.io/hc/en-us/articles/360015173694) and [Project](https://docs.flywheel.io/hc/en-us/articles/360037869114)*
- Makesure Python is installed in your local machine
- A CSV file with the following layout:

| Group Name  | Group ID  |  Project Label |
|---|---|---|---|---|
|  test-group-name | test-group-id  | test-project-label | 
> You can also find an example csv file (*group-project-list-sample.csv*) in this directory.

## Instruction

Step 1: Run the following command in your terminal to install required packages

```
pip install -r path/to/requirements.txt 
```
Step 2: Update your CSV file with groups and projects that you would like to create on your Instance.

Step 3: Run the Python Script to create new groups and projects.
```
python path/to/create-group-project.py --key <your-api-key-here> --file path/to/group-project-list-sample.csv
```