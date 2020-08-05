bloop
## Contributor license agreement

By submitting code to this notebook, you agree to the [MIT license agreement](https://opensource.org/licenses/MIT).


## Flywheel Tutorials

### Purpose:
The Flywheel tutorials repository is a collection of Jupyter notebooks intended to be useful demonstrations of how to programmatically interface with Flywheel, preform tasks, curate & process data, and more, that may otherwise be time-consuming or cumbersome to do manually. These tutorials are designed to be helpful for any user on any instance. In practice, this means that our tutorials can be easily generalized to multiple use cases, or cover a specific task commonly done by users across all instances. This goes beyond simple SDK "examples," which may show the correct syntax used to call a function and strives to provide a more detailed story about where and how these functions might be used. We hope to demonstrate the potential and ease of interfacing with Flywheel utilizing the SDK, to empower users to tackle potentially tricky problems with confidence, and to inspire users to see new use-cases they may not have otherwise considered.

## Contributor guidelines

### General Guidelines:

We welcome the contribution of tutorials that cover new topics, or expand on existing tutorials.  All contributions should be in the spirit of this repository's purpose.  This means that, rather than provide an example of how to do a very specific task to a very specific subset of data, make the example more generalizable.  For example, the following tutorial would not be inline with our purpose:
- Retrieves subject "Sub-45"
- Update metadata field 'birthday' to '01/02/03' using `subject.update_info({"birthday":"01/02/03"})`

While the following would be more inline:
- Retrieves subjects in a given project based on some sort of customizable query
- Loops through all subjects found in the query, performs checks if necessary
- Creates a dictionary of metadata fields to change (determined by the user)
- Sets the new metadata fields to their desired values, provided by a list or some other source, using: `subject.update_info(update_info_dict)`



We strive to provide clear, practical examples that can be easily run by users with even minimal programming skill. 


To this end, we provide a set of guidelines that we ask all contributors to follow.  The minimal contributor guidelines are the absolute minimum necessary requirements for a tutorial contribution to be considered for publication on this repository.

Beyond the minimum necessary requirements, we provide a recommended style guide.  Adhering to the recommended style guide increases the chances of the acceptance of your contribution.
It will also likely reduce the amount of time between submission and acceptance, as we may either modify or request changes if we feel that it would significantly enhance the readability/clarity of the tutorial.

### Issue labels

The current list of issue labels are [here](https://gitlab.com/flywheel-io/public/flywheel-tutorials/-/labels) and include:


- ~"Bug"  If you find a new bug, please provide as much information as possible to recreate the error.
    The will automatically populate any new issue you open, and contains information we've found to be helpful in addressing bug reports.
    Please fill it out to the best of your ability If you experience the same bug as one already listed in an open issue, please add any additional information that you have as a comment.

- ~"Tutorial Improvement"  If you have suggestions for how we can improve an existing tutorial by clarifying, expanding, or simply adding content to.

- ~"Tutorial Contribution"  If you have your own tutorial notebook to submit for publication in this repository, add this label to your merge request.
    Please ensure that you've read and followed the instructions outlined in this document before submitting.

- ~"Tutorial Request"  If you are unable to contribute yourself, but would like to request a tutorial on a specific topic, please use this tag.  


## Tutorial Contribution

When contributing a new tutorial, we recommend that you familiarize yourself with the [git style workflow](https://guides.GitLab.com/introduction/flow/index.html)

### Contribution Workflow:

- Verify that your contribution is not addressed by other issues or PRs
- Fork the tutorials repository and begin work on new feature branch
- Ensure that your contribution meets the [minimum contribution requirements](minimum-contribution-requirements)
- Provide an informative and appropriate name for the contribution file
- Create a merge request with the ~"Tutorial Contribution" tag and fill out the contribution template

### Forking and developing
The preferred way to contribute to flywheel tutorials is to fork the main repository on GitLab, then submit a “merge request” (MR).

In the first few steps, we explain how to locally install flywheel tutorials, and how to set up your git repository:

***Create an account on GitLab if you do not already have one.***

***Fork the project repository:***

click on the ‘Fork’ button near the top right of the page. This creates a copy of the code under your account on the GitLab user account. For more details on how to fork a repository see this guide.

***Clone your fork of the flywheel tutorials repo from your GitLab account to your local disk:***

```bash
$ git clone git@gitlab.com:your-login/flywheel-tutorials.git 
$ cd flywheel-tutorials
```

***Add the upstream remote:*** 

This saves a reference to the main flywheel tutorials repository, which you can use to keep your repository synchronized with the latest changes:

```bash
$ git remote add upstream https://gitlab.com/flywheel-io/public/flywheel-tutorials.git
```

You should now have a working installation of flywheel tutorials, and your git repository properly configured. The next steps now describe the process of modifying code and submitting a MR:

***Synchronize your master branch with the upstream master branch***

```bash
$ git checkout master
$ git pull upstream master
```

***Create a feature branch to hold your development changes (replacing MY_FEATURE with a descriptive name for the feature you are contributing; e.g., accessing-project-metadata):***

```bash
$ git checkout -b MY_FEATURE
```
and start making changes. Always use a feature branch. PROTIP: It’s good practice to never work on the master branch!

Develop the feature on your feature branch on your computer, using Git to do the version control. When you’re done editing, add changed files using git add and then git commit:

```bash
$ git add modified_files
$ git commit
```
to record your changes in Git, then push the changes to your GitLab account with:

```bash
$ git push -u origin MY_FEATURE
```
Follow these instructions to create a merge request from your fork. This will send an email to the committers. You may want to consider sending an email to the mailing list for more visibility.


#### Learning git:

The Git documentation and http://try.github.io are excellent resources to get started with git, and understanding all of the commands shown here.

#### Merge request checklist
Before an MR can be merged, it needs to be approved by two core developers. Please prefix the title of your merge request with [MRG] if the contribution is complete and should be subjected to a detailed review. An incomplete contribution – where you expect to do more work before receiving a full review – should be prefixed [WIP] (to indicate a work in progress) and changed to [MRG] when it matures. WIPs may be useful to indicate you are working on something to avoid duplicated work, request a broad review of functionality or API, or seek collaborators. WIPs often benefit from the inclusion of a task list in the MR description.

In order to ease the reviewing process, we recommend that your contribution complies with the [minimum submission requirements](minimum-contribution-requirements). 


### Minimum contribution requirements:
Your contribution must meet these minimum criteria to be considered for publication:
- Include a brief summary and/or purpose of the notebook
- The notebook should cover material not present in existing notebooks, or with minimal overlap
  - Consider submitting your notebook as an "improvement" to an existing tutorial if there is significant content overlap.
- Code must be python3 executable
- Complete list of library imports, using only default python or pip-installable libraries
- All path/file references must be relative to the execution environment (No direct links like ‘/Users/myuser/Documents/etc…’ that need to be changed manually for execution).
- No sensitive information (API-keys, PHI, protected data, etc.)
- Contribution must be in the form of a tutorial (i.e. do not just submit a function that takes a flywheel subject and does some processing.  Include something like a script showing how to find a subject, ensure it will work with the function, run the function, and then check to make sure it worked)


### Recommended style guidelines:
- Prefer a jupyter notebook style contribution
- Follow [PEP-8](https://www.python.org/dev/peps/pep-0008/) guidelines. For the most part, [Black](https://pypi.org/project/black/), a code formatter, will get you there.
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
- Create an issue with the label ~"Tutorial Request"
- Populate the fields in the template


