## Contributor license agreement

By submitting code as an individual you agree to the
[individual contributor license agreement](doc/legal/individual_contributor_license_agreement.md).
By submitting code as an entity you agree to the
[corporate contributor license agreement](doc/legal/corporate_contributor_license_agreement.md).

All Documentation content that resides under the [doc/ directory](/doc) of this
repository is licensed under Creative Commons:
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

_This notice should stay as the first item in the CONTRIBUTING.md file._


## Contributor guidelines

We welcome the contribution of tutorials that cover new topics, or expand on existing tutorials.
We strive to provide clear, practical examples that can be easily run by users with even minimal programming skill. (Do we?  Is this true?  Sometimes I Just start typing a sentence not knowing how it's going to end oh god it's happening again.)
To this end, we provide a set of guidelines that we ask all contributors to follow.  The minimal contributor guidelines are the abosolute minimum necessary requirements for a tutorial contribution to be considered for publication on this repository.
If we feel that any of the minimum requirements are not met, our team may ask you to revise the contribution.

Beyond the minimum necessary requirements, we provide a recommended style guide.  Adhering to the recommended style guide increases the chances of the acceptance of your contribution.
It will also likely reduce the amount of time between submission and acceptance, as we may either modify or request changes if we feel that it would singificantly enhance the readibility/clarity of the tutorial.

## Issue labels

The current list of issue labels are [here][https://gitlab.com/flywheel-io/public/flywheel-tutorials/-/labels] and include:


- ~"Bug"  If you find a new bug, please provide as much information as possible to recreate the error.
    The [issue template][link_issue_template] will automatically populate any new issue you open, and contains information we've found to be helpful in addressing bug reports.
    Please fill it out to the best of your ability If you experience the same bug as one already listed in an open issue, please add any additional information that you have as a comment.

- ~"Tutorial Contribution"  If you have your own tutorial notebook to submit for publication in this repository, add this label to your merge request.
    Please ensure that you've read and followed the instructions outlined in this document before submitting.

- ~"Tutorial Request"  If you are unable to contribute yourself, but would like to request a tutorial on a specific topic, please use this tag.  


Outline
Overview of the Repo
About
Purpose of Flywheel-Tutorial


Table of Contents 
Ways to Contribute
Report Bugs/Issues  || Ask Question or Answer Other’s Queries || Typo or Suggestions for Improvement
Guidelines to submit an issue:
Verify that your issue is not being addressed by other issues or PRs
Fulfill our requirements on What to include in the Complete a  bug report
How to submit/make a bug report (Put this as a template file)
Name of the file
Provide a quick summary of the bug/issue
Snapshot of the failing notebook in attachment
What environment was being used (ex: ipynb, Colab or myBinder) and OS they are on if it is being run in the local machine
https://docs.gitlab.com/ee/user/project/description_templates.html

Submit your script notebook - Pull Request
Minimum requirements?:
Python3
pip- installable libraries only
Comments describing flow/execution
All path/file references must be relative to the execution environment (No direct links like ‘/Users/davidparker/Documents/etc…’ that need to be changed manually for execution)
No sensitive information (API-keys, etc)
Should we put a length limit?


What to include in your Notebook/Script 
Prefer to IPYNB notebook
Using ipynb or Google Colab refer to template for the formatting
Summary and/or Purpose of the notebook
Follow PEP-8 guidelines on your code with comments
Checklist to submit a Pull Request/Merge Request
Verify there is no existing notebook
Make sure your code is running properly and has appropriate comments comment out the code accordingly
The script must be in JupyterNotebook format
Provide a helpful Pull Request tile to summarises what your contribution/commit does


Workflow to report a bug or pull request:
Git flow - how to do MR (basic command to include)


https://guides.github.com/introduction/flow/index.html


Notes:
Add Contributing link on README

