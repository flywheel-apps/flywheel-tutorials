# Flywheel Public Jupyter Notebooks

Hosts a few notebooks that illustrate interactions with a Flywheel instance using the 
[flywheel-sdk](https://flywheel-io.gitlab.io/product/backend/sdk/branches/master/python/index.html).

## Table of content 


|     | Title        | Description             |
| --- |:-------------|:------------------------|
| 0 | [Template](https://gitlab.com/flywheel-io/public/jupyter-notebooks/-/blob/master/template.ipynb) | Template notebook to serve as reference for structuring notebooks in this repository |
| 1 | [Add subjects to a collection](https://gitlab.com/flywheel-io/public/jupyter-notebooks/-/blob/master/add-to-collection-excluding-subjects-in-csv.ipynb )|  <ul><li>Get the project label and collection label (if you have one) you want to edit </li> <li>Parse CSV file that contain Subject Label you want to exclude or any restrain you are looking for </li>|
| 2 | [List outdated gear rules and update gear rules for project(s) with latest gear version](https://gitlab.com/flywheel-io/public/jupyter-notebooks/-/blob/master/find-outdated-gear-rule-and-update-with-latest-version.ipynb)  | <ul><li> List all project(s) available and gear rules for the project  <br> <li>Functions :<br> a. `get_gear_latest_version(fw, gear_id)` function - To get the latest version of a gear <br> b. `cleanup_rule(rule, project=None)` function - Formulate gear rule by taking a rule input object  |

## Getting started

Notebooks are files that allow you to create and share documents that contain live code, equations, 
visualizations and narrative text. They run in an open-source web applications such [Jupyter Notebook](https://jupyter.org) 
or [JupyterLab](https://jupyter.org). 

### Requirements

* Access to a Flywheel instance.
* A Flywheel API key. More on how to get yours [here](https://flywheel-io.gitlab.io/product/backend/sdk/branches/master/python/getting_started.html#api-key).

### Using mybinder.org (easiest, no installation required)

[Mybinder.org](https://mybinder.org/) turns a git repo into a collection of interactive notebooks. 
Nothing to do. Just click [here to get started](https://mybinder.org/v2/gl/flywheel-io%2Fpublic%2Fjupyter-notebooks/master). 

### Using your own Jupyter instance

* Install [Jupyter Notebook](https://jupyter.org) or [JupyterLab](https://jupyter.org).
* Git clone this repo: `git clone https://gitlab.com/flywheel-io/public/jupyter-notebooks.git`.
* Start your jupyter instance and `cd` to the cloned repository to open one of the notebooks.