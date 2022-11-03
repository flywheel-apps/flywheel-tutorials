# Debug BIDS Curation

## Add a new acquisition type from the BIDS Specification

Adding a whole new type of modality from the BIDS specification is essentially duplicating the work of creating the MRI specification.  For instance, adding Microscopy (see [Section 10-microscopy](https://bids-specification.readthedocs.io/en/stable/04-modality-specific-files/10-microscopy.html) of the Specification), in the "definitions" section of the template, a new "micr_file" would be added that has a "micr/" folder (like "anat/" "func/" etc.), it would have a new "_sample-<label>" element-value pair, and many new modality suffixes (2PE, BF, CARS, CONF, DIC, etc.) and file extensions (png, tif, ome.tif, ome.btf, and ome.zarr) would need to be added.  Additional optional filename entities would also need to be added to the definitions like "stain", "chunk", etc.  Then rules would have to be created to match specific file name conventions (a ReproIn-like convention could be developed), and specific regular expressions would have to be created to find the values for the new entities.  This requires a set of example files for testing and development of the new sections of the project curation template.

Adding new types of anatomical scans, Multi-echo Gradient Recalled Echo (MEGRE) and Multi-echo Spin Echo (MESE) scans, to the existing "anat_file" MRI definition involved only adding two lines  ("MEGRE" and "MESE") to the "enum" list here for the "Modaliy" because the rest of the template was still applicable:

```json
        "Modality": {
          "type": "string",
          "title": "Modality Label",
          "default": "",
          "enum": [
            "angio",
            "defacemask",
            "FLAIR",
            "FLASH",
            "inplaneT1",
            "inplaneT2",
            "MEGRE",
            "MESE",
            "M0map",
            "PD",
            "PDmap",
            "PDT2",
            "R2map",
            "SWImagandphase",
            "T1w",
            "T2w",
            "T1rho",
            "T1map",
            "T2map",
            "T2star"
          ]
        },
```

When adding a new type of acquisition, a lot depends on the file name in addition to the acquisition label.  For MRI, this is mainly handled by `dcm2niix` which was designed to convert DICOMs to NIfTI for BIDS formatting.  For MEGRE and MESE scans, `dcm2niix` creates multiple NIfTI files with names like "anat_MEGRE_acq_T1MEPREINT_e1.nii.gz", "anat_MEGRE_acq_T1MEPREINT_e2.nii.gz", etc.  In BIDS, these are converted into "_echo-1", "_echo-2", etc. elements of the file name.  The "echo" element was already part of the existing "anat_file" definition and initialization so those parts did not need to be added.