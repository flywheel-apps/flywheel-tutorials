# This folder hosts tutorials for python

It hosts a few notebooks that illustrate interactions with a Flywheel instance using the 
[flywheel-sdk](https://flywheel-io.gitlab.io/product/backend/sdk/branches/master/python/index.html).

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gl/flywheel-io%2Fpublic%2Fflywheel-tutorials/master?filepath=python%2FTOC.ipynb)
[![Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/flywheel-apps/flywheel-tutorials/blob/master/python/TOC.ipynb)

## Getting started

Notebooks are files that allow you to create and share documents that contain live code, equations, 
visualizations and narrative text. They run in an open-source web applications such [Jupyter Notebook](https://jupyter.org) 
or [JupyterLab](https://jupyter.org). 


### Requirements

* Access to a Flywheel instance.
* A Flywheel API key. More on how to get yours [here](https://flywheel-io.gitlab.io/product/backend/sdk/branches/master/python/getting_started.html#api-key).

### Using mybinder.org or google collab (easiest, no installation required)  

[Mybinder.org](https://mybinder.org/) turns a git repo into a collection of interactive notebooks. 
Nothing to do. Just click [here to get started](https://mybinder.org/v2/gl/flywheel-io%2Fpublic%2Fflywheel-tutorials/master?filepath=python%2FTOC.ipynb). 

If you have a google account you can also use google collab.  
Nothing to do. Just click [here to get started](https://colab.research.google.com/github/flywheel-apps/flywheel-tutorials/blob/master/python/TOC.ipynb). 

### Using your own Jupyter instance

* Install [Jupyter Notebook](https://jupyter.org) or [JupyterLab](https://jupyter.org).
* Git clone this repo: `git clone https://gitlab.com/flywheel-io/public/jupyter-notebooks.git`.
* Start your jupyter instance and `cd` to the cloned repository to open one of the notebooks.


## Table of contents
| Title        | Description             |
|:-------------|:------------------------|
| [Template](https://gitlab.com/flywheel-io/public/flywheel-tutorials/-/blob/master/python/template.ipynb) | Template notebook to serve as reference for structuring notebooks in this repository|
| [Add subjects to a collection](https://gitlab.com/flywheel-io/public/flywheel-tutorials/-/blob/master/python/add-to-collection-excluding-subjects-in-csv.ipynb)|  <ul><li>Get the project label and collection label (if you have one) you want to edit </li> <li>Parse CSV file that contain Subject Label you want to exclude or any restrain you are looking for </li>|
| [List outdated gear rules and update gear rules for project(s) with latest gear version](https://gitlab.com/flywheel-io/public/flywheel-tutorials/-/blob/master/python/find-outdated-gear-rule-and-update-with-latest-version.ipynb)  | <ul><li> List all project(s) available and gear rules for the project  <br> <li>Functions :<br> a. `get_gear_latest_version(fw, gear_id)` function - To get the latest version of a gear <br> b. `cleanup_rule(rule, project=None)` function - Formulate gear rule by taking a rule input object  |
| [Rename MoCo Series Acquisition Label](https://gitlab.com/flywheel-io/public/flywheel-tutorials/-/blob/master/python/rename-moco-and-acq-label.ipynb) | <ul><li> Rename MoCo series by adding '_moco' and run time <br><li>Functions : <br> a.  `get_scan_moco_label` : Identify the original scan label<br>b.  `modify_acq_name` : Modify Acquisition name based on the session timepoint<br>c.  `update_acq_label` : Update the acquisition label on the FW instances  |
| [ Update Acquisition container timestamp (shown in UI) from Dicom Tag SeriesTime in Dicom file ](https://gitlab.com/flywheel-io/public/flywheel-tutorials/-/blob/master/python/edit-acquisition-timestamp.ipynb) | <ul><li>Update the Acquisition container timestamp (shown in UI) that is incorrect.<br><li>Functions :<br> a.  `get_updated_timestamp` : Get the updated timestamp <br>b.`modify_time` : Comparing the timestamp shows on the Acquisition container and SeriesTime in Dicom file <br>c.`update_container_timestamp` : Update the acquisition timestamp  <br> |
| [Run local analysis and upload back to Flywheel](https://gitlab.com/flywheel-io/public/flywheel-tutorials/-/blob/master/python/local-analysis-notebook-on-ss-ce.ipynb) | Find and download input file from flywheel, process locally, create an analysis container and upload local process outputs to it. <br>|
| [Example calls to REDCap using PyCap](https://gitlab.com/flywheel-io/public/flywheel-tutorials/-/blob/master/python/RedCap_Intergration.ipynb) | <ul><li>An exensive collection of example calls to access various REDCap data using PyCap, in ways that would be useful given the hierarchy of Flywheel Containers. <br> |
| [Full example of adding REDCap data to a Flywheel Container](https://gitlab.com/flywheel-io/public/flywheel-tutorials/-/blob/master/python/add-redcap-data-to-flywheel-container.ipynb) | <ul><li> A real example demonstrating how to access REDCap through PyCap, how to search and view the data, and how to add the data to the appropriate flywheel container </li><br> |
| [Upload data to a new project](https://gitlab.com/flywheel-io/public/flywheel-tutorials/-/blob/master/python/upload-data-to-a-new-project.ipynb) | <ul><li> A simple notebook to create a test project with some dummy data which you can tinker with. Recommeded for novice Flywheel SDK user.</li><br> |
| [Flywheel SDK Example](https://gitlab.com/flywheel-io/public/flywheel-tutorials/-/blob/master/python/Flywheel-SDK-Example.ipynb) | <ul><li> A a real-time example in guiding user how to use Flywheel SDK, adapted from Flywheel SDK Documentation.</li><br> |
| [Batch Run Gears](https://gitlab.com/flywheel-io/public/flywheel-tutorials/-/blob/master/python/batch-run-gears.ipynb) | <ul><li> An overview of the Flywheel Gears and how to run gears as a batch via SDK </li><br> |