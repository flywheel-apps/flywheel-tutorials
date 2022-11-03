# Debug BIDS Curation

## Add an ignore rule to a template

The way the template engine is implemented makes project curation templates very flexible and powerful.  As the engine traverses the Flywheel hierarchy, the most common metadata field to use to extract text strings is the `acquisition.label`.  This is the text label of the acquisition container where files, usually a DICOM and a NIfTI file, are attached.  One way to ignore all files in an acquisition is to have a rule to the template that looks for "_ignore-BIDS" at the end of that label.  

Here is the rule for acquisition containers in the default ReproIn project curation template:
![acquisition-rule.png](pics/add_ignore_rule/acquisition-rule.png)

The rule is executed for every acquisition container.  When recognized, the above "initialize" section says to set the "ignore" property `acquisition.info.BIDS.ignore` based on a match of the given regular expression on the acquisition.label.  It is set to "true" if "ignore-BIDS" or "__dup" is found (for different capitalizations for "BIDS" or numbers after "__dup").  The "ignore" flag is a Flywheel metadata value that, when true, prevents all files in the acquisition from being written out in BIDS format.  See [here](Ignore_ses-subj.md) for how to ignore entire subjects and sessions
:w

Instead of ignoring the acquisition container, here is a rule that will ignore specific files if their DICOM tag "ImageType" contains "NORM":
![ignore-norm.png](pics/add_ignore_rule/ignore-norm.png)

This says that whenever a file in an acquisition that is a NIfTI or DICOM file and also hase the `file.info.ImageType` that contains "NORM", set the "ignore" flag for that file.

Files can also be ignored based on their Flywheel classification.
![ignore-derived.png](pics/add_ignore_rule/ignore-derived.png)

Here the file will be ignored for diffusion files if `file.classification.Features includes "Derived".

You may have noticed that these rules are not exactly straightforward in the way they are defined.  Also, there are additional features of rule processing that have not been discussed.  So what do you do when you need to add a new rule?  How do you make sure it is doing exactly what you need it to do?  Answer: step through rule processing using a debugger.  The main loop when curating BIDS is in `curate_bids_tree()` in `curate_bids.py`.  Put a breakpoint there to see how that main loop steps through the Flywheel hierarchy.  Then, take a look at more specifics into how the rules are used in `process_matching_templates()` which is in `bidsify_flywheel.py`.  There is a loop in there that steps through each rule.  Look for `for rule in rules:`.  If you are interested in figuring out how a "where" clause is processed, step into the line that is `if rule.test(context)`.  You can use a conditional breakpoint to stop only when a particular rule.id is being processed.  Here is an example:
```python
("file" in context) and (rule.id == "wip_file") and ("205 - sWIP T1W_3D_IRCstandard32 SENSE avg" in context["acquisition"].data["label"])
```
The first part makes sure you're dealing with a file, not some container.  The second specifies the rule ID, and the third looks for a specific acquisition label.  Using this condition on that "rule.test" line will let you zoom in to exactly the situation you want to figure out: what happens when a particular acquisition meets a particular rule.  After understanding the "where" part, step along in the code to see what happens when the rule matches: the "initialization" part.