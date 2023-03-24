# Debug BIDS Curation

## Solve problems of duplicated BIDS names

As described under "Common errors" in "[BIDS curation tutorial part 5: interpreting the curation report](https://docs.flywheel.io/hc/en-us/articles/4405065304723-BIDS-curation-tutorial-part-5-interpreting-the-curation-report)", there are many reasons why duplicated BIDS names can occur. Use the curation report (the .csv files produced by the BIDS curation gear) to isolate the issue.

As an example, a scanner upgrade can cause multiple acquisitions to be created with similar names.  This situation can occur if the scanner produces a derived or normalized scan from an original scan.  The new acquisition might have files named "anat-T1w" and "anat-T1w_ND". Another example is motion corrected (MOCO) and raw functional scans.  In the "*_nitfis.csv" file of the curation report, these duplicated BIDS names will have "duplicate #" in the final column.  Take a look at the acquisition names and the file names.  If they are different but the difference is not detected by the existing project curation template, then the template can be modified to either detect and add that difference in the "Acq" BIDS entity, or else just ignore one of the two files using the presence or absense of that name difference (as detected by a regex).  Ignoring an acquisition or file is described in [Add_ignore_rule.md](Add_ignore_rule.md). 
