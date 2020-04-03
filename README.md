# Flywheel Public Jupyter Notebooks

Hosts a few notebooks that illustrate interactions with Flywheel using the flywheel-sdk.


|     | Title       | Description   |
| --- |:-------------|:------------------------|
| 1 | [Add subjects to a collection](https://gitlab.com/flywheel-io/public/jupyter-notebooks/-/blob/master/add-to-collection-excluding-subjects-in-csv.ipynb )|  <ul><li>Get the project label and collection label (if you have one) you want to edit </li> <li>Parse CSV file that contain Subject Label you want to exclude or any restrain you are looking for </li>|
| 2 | [List outdated gear rules and update gear rules for project(s) with latest gear version](https://gitlab.com/flywheel-io/public/jupyter-notebooks/-/blob/master/find-outdated-gear-rule-and-update-with-latest-version.ipynb)  | <ul><li> List all project(s) available and gear rules for the project  <br> <li>Functions :<br> a. `get_gear_latest_version(fw, gear_id)` function - To get the latest version of a gear <br> b. `cleanup_rule(rule, project=None)` function - Formulate gear rule by taking a rule input object  |

**Links to Local Jupyter Notebook/Collab**

1. [Jupyter Notebook](https://hub.gke.mybinder.org/user/flywheel-io-pub-pyter-notebooks-tmv68n53/tree)
2. [Google Colab](https://drive.google.com/a/flywheel.io/file/d/1QP_ZcXmhtHVbV0-1wvTkhVAQeSuV6Whw/view?usp=sharing)