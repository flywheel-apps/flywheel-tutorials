# Debug BIDS Curation

## Add an ignore rule to a template

The template engine traverses the Flywheel hierarchy, matching and extracting metadata which matches the text strings in the project curation templates. This implementation is very flexible and powerful.   

### Ignore all files in an acquisition container
The `acquisition.label` field is the most common metadata field used in the string matching.  The DICOM and NIfTI files of interest are attached often attached to the acquisition container referenced. Rather than writing "_ignore-BIDS" at the end of each file in the acquisition, one can ignore all files by adding a template rule that looks for "_ignore-BIDS" at the end of `acquisition.label`. Here is an example of ignoring an entire acquisition in the UI.

![ignore_bids_acq.png](pics/add_ignore_rule/ignore_bids_acq.png)

Here is the rule for acquisition containers in the default ReproIn project curation template:
![acquisition-rule.png](pics/add_ignore_rule/acquisition-rule.png)

The rule is executed for every acquisition container.  When recognized, the above "initialize" section says to set the "ignore" property `acquisition.info.BIDS.ignore` based on a match of the given regular expression on the acquisition.label.  `BIDS.ignore` is set to "true" if "ignore-BIDS" or "__dup" is found (the `$regex` allows for different capitalizations for "BIDS" or numbers after "__dup").  The "ignore" flag is a Flywheel metadata value that, when true, prevents all files in the acquisition from being written out in BIDS format.  See [here](Ignore_ses-subj.md) for how to ignore entire subjects and sessions.

### Ignore specific file based on unique characteristics
#### Image Type Example
Instead of ignoring the acquisition container, here is a rule that will ignore specific files if their DICOM tag "ImageType" contains "NORM":
![ignore-norm.png](pics/add_ignore_rule/ignore-norm.png)

This rule, "ignore_norm", reads from top to bottom that whenever a file in an acquisition is a NIfTI or DICOM file and also has the `file.info.ImageType` that contains "NORM", set the "ignore" flag for that file.
   
#### Classification Example
Files can also be ignored based on their Flywheel classification. This example shows that a diffusion file will be ignored if `file.classification.Features includes "Derived".
![ignore-derived.png](pics/add_ignore_rule/ignore-derived.png)

## Debugging an ignore rule
You may have noticed that these rules are not exactly straightforward in the way they are defined.  Also, there are additional features of rule processing that have not been discussed.  

So what do you do when you need to add a new rule?  How do you make sure it is doing exactly what you need it to do?  Answer: step through rule processing using a debugger.

The main loop when curating BIDS is in `curate_bids_tree()` in `curate_bids.py`.  Put a breakpoint there to see how that main loop steps through the Flywheel hierarchy.  Then, take a look at more specifics into how the rules are used in `bidsify_flywheel.process_matching_templates`.  One of the loops in `process_matching_templates` steps through each rule.  Look for `for rule in rules:`.  If you are interested in figuring out how a "where" clause is processed, step into the line that is `if rule.test(context)`.  You can use a conditional breakpoint to stop only when a particular rule.id is being processed.  

Here is an example:
```python
("file" in context) and (rule.id == "wip_file") and ("205 - sWIP T1W_3D_IRCstandard32 SENSE avg" in context["acquisition"].data["label"])
```
The first part makes sure you're dealing with a file, not some container.  The second specifies the rule ID, and the third looks for a specific acquisition label.  Using this condition on that "rule.test" line will let you zoom in to exactly the situation you want to figure out: what happens when a particular acquisition meets a particular rule.  After understanding the "where" part, step along in the code to see what happens when the rule matches the "initialization" part.