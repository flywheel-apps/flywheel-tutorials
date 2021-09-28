# Add user to Flywheel Instance

## Overview

In this section, we will be showing you a simple Python program that allows you to add new users to specified Group and Project with a CSV file as an input. In addition to add user, you also will be able to specify the user roles within the site, Group and Project. 
<br>
_NOTES: We will be using [Project Permission Template](https://docs.flywheel.io/hc/en-us/articles/360049970973) to add users to all projects under the specified Group._
<br>

> To learn more user roles and permissions, feel free to checkout our [documentation](https://docs.flywheel.io/hc/en-us/articles/360033902993) on this topic.

## Requirements
- Makesure Python is installed in your local machine
- Understand User Roles and Permissions and the difference between each roles.
- A CSV file with the following layout:

| First Name | Last Name  |  Email | Group ID | Site-Role | Project Permission |
|---|---|---|---|---|---|
|  testfirst | testlast  | emailtest | test-group-id | User | Read/write |
| testsecond | testperson | email2 | test-group-id-2 | Developer | read only |
| name2 | name3 | email1234 | group123 | User | admin |
> You can also find an example csv file (*user-list-sample.csv*) in this directory.

_NOTES:_
_ 1. For Project Permission, you should put one of the following, **read/write**, **read only**, or **admin**, and it is not case sensitive. The script will not work if the naming of the roles do not match the above._
_ 2. For Site Role, the script will only accept **user**, **developer** and **site admin** as the site-wide role at this moment.


## Instruction

Step 1: Run the following command in your terminal to install required packages
```
pip install -r path/to/requirements.txt 
```
Step 2: Makesure the group(s) has been created. If not, consider to go over [this section](https://gitlab.com/flywheel-io/public/flywheel-tutorials/-/tree/user-creation-script/scripts/add-group-project-to-instance) to learn how to add group(s) and project(s) to your instance via SDK . 

Step 3: Add or modify user permission
```
python path/to/add-user-permission.py --key <your-api-key-here> --file path/to/user-list-sample.csv --email-suffix @somewhere.com
```
