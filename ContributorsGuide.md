## Contributor license agreement

These are just a placeholder copied and pasted from somewhere else.  We need to discuss what we want in this sectin

By submitting code as an individual you agree to the
[individual contributor license agreement](doc/legal/individual_contributor_license_agreement.md).
By submitting code as an entity you agree to the
[corporate contributor license agreement](doc/legal/corporate_contributor_license_agreement.md).

All Documentation content that resides under the [doc/ directory](/doc) of this
repository is licensed under Creative Commons:
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

_This notice should stay as the first item in the CONTRIBUTING.md file._

## Flywheel Tutorials

### Purpose:
The flywheel tutorials repository is a collection of jupyter notebooks intended to be useful demonstrations of how to progamatically interface with flywheel,
 preform tasks, curate/process data, and more, that may otherwise be time-consuming or cumbersome to do manually. These tutorials are designed to be helpful for any user on any instance.  In practice, this means that our tutorials can be easily generalized to multiple use cases, or cover a specific task that is commonly done by users across all instances.

## Contributor guidelines

### General Guidelines:

We welcome the contribution of tutorials that cover new topics, or expand on existing tutorials.  All contributions should be in the spirit of this repositories purpose.  This means that, rather than provide an example of how to do a very specific task to a very specific subset of data, make the example more generalizable.  For example, the following tutorial would not be inline with our purpose:
- Retrieves subject "Sub-45"
- Update metadata field 'birthday' to '01/02/03' using `subject.update_info({"birthday":"01/02/03"})`

While the following would be more in-line:
- Retrieves subjects in a given project based on some sort of customizable query
- Loops through all subjects found in the query, performs checks if necessary
- Creates a dictionary of metadata fields to change (determined by the user)
- Sets the new metadata fields to their desired values, provided by a list or some other source, using: `subject.update_info(update_info_dict)`



We strive to provide clear, practical examples that can be easily run by users with even minimal programming skill. (Do we?  Is this true?  Sometimes I Just start typing a sentence not knowing how it's going to end oh god it's happening again.)
To this end, we provide a set of guidelines that we ask all contributors to follow.  The minimal contributor guidelines are the abosolute minimum necessary requirements for a tutorial contribution to be considered for publication on this repository.
If we feel that any of the minimum requirements are not met, our team may ask you to revise the contribution.

Beyond the minimum necessary requirements, we provide a recommended style guide.  Adhering to the recommended style guide increases the chances of the acceptance of your contribution.
It will also likely reduce the amount of time between submission and acceptance, as we may either modify or request changes if we feel that it would singificantly enhance the readibility/clarity of the tutorial.

### Issue labels

The current list of issue labels are [here](https://gitlab.com/flywheel-io/public/flywheel-tutorials/-/labels) and include:


- ~"Bug"  If you find a new bug, please provide as much information as possible to recreate the error.
    The will automatically populate any new issue you open, and contains information we've found to be helpful in addressing bug reports.
    Please fill it out to the best of your ability If you experience the same bug as one already listed in an open issue, please add any additional information that you have as a comment.

- ~"Tutorial Improvement"  If you have suggestions for how we can improve an existing tutorial by clarifying, expanding, or simply adding content to.

- ~"Tutorial Contribution"  If you have your own tutorial notebook to submit for publication in this repository, add this label to your merge request.
    Please ensure that you've read and followed the instructions outlined in this document before submitting.

- ~"Tutorial Request"  If you are unable to contribute yourself, but would like to request a tutorial on a specific topic, please use this tag.  

- Should I add a tutorial feedback tag?


Guidelines to submit an issue:
Verify that your issue is not being addressed by other issues or PRs
Fulfill our requirements on What to include in the Complete a  bug report
How to submit/make a bug report (Put this as a template file)
Name of the file
Provide a quick summary of the bug/issue
Snapshot of the failing notebook in attachment
What environment was being used (ex: ipynb, Colab or myBinder) and OS they are on if it is being run in the local machine

## Tutorial Contribution

When contributing a new tutorial, we recommend that you familiarize yourself with the [git style workflow](https://guides.github.com/introduction/flow/index.html)

### Contribution Workflow:

- Verify that your contribution is not addressed by other issues or PRs
- Ensure that your contribution meets the minimum contribution requirements
- Provide an informative and appropriate name for the contribution file
- Create a merge request with the ~"Tutorial Contribution" tag and fill out the contribution template


### Minimum contribution requirements:
Your contribution must meet these minimum criteria to be considered for publication:
- Include a brief summary and/or purpose of the notebook
- The notebook should cover material not present in existing notebooks, or with minimal overlap
  - Consider submitting your notebook as an "improvement" to an existing tuturial if there is significant content overlap.
- Code must be python3 executable
- Complete list of library imports, using default python or pip-installable libraries only
- Comments at every major section of code and at the beginning of every function describing what it does.
- All path/file references must be relative to the execution environment (No direct links like ‘/Users/myuser/Documents/etc…’ that need to be changed manually for execution).
- No sensitive information (API-keys, etc)
- Contribution must be in the form of a tutorial (i.e. do not just submit a function that takes a flywheel subject and does some processing.  Include something like a script showing how to find a subject, ensure it will work with the function, run the function, and then check to make sure it worked)


### Recommended style guidelines:
- Prefer a jupyter notebook style contribution
- Follow PEP-8 guidelines
- Extensive comments, in the form of a walkthrough, explaining not only WHAT the code is doing, but WHY (And when appropriate, HOW)


## Bug Report


### Workflow to report a bug or pull request:
- Verify (as best you can) that the bug is code-related.  Review the common support FAQ and ensure your problem isn't covered there
- Generate an issue for the repository and use the ~"Bug" label.
- Populate all fields in the template. 


## Tutorial Improvement

### Tutorial improvement workflow
- Verify (as best you can) that the improvement is not covered in an existing tutorial.
- Create an issue with the label ~"Tutorial Improvement".
- Populate the fields in the template


## Tutorials Request

### Tutorial request workflow
- Verify (as best you can) that the material is not covered in an existing tutorial.
- Create an issue with the lable ~"Tutorial Request"
- Populate the fields in the template


