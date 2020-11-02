# Flywheel Tutorials/Import Utilities

This folder is dedicated to using Flywheel's SDK to facilitate the import of datasets into Flywheel. Importing structured data and metadata into Flywheel ensures a consistent, reliable, and searchable dataset to share with collaborators.

There are multiple ways to import data into a Flywheel instance. See our [documentation](https://docs.flywheel.io/hc/en-us/articles/360007657833) for other means to accomplish bulk import or ingest. Although these methods can be faster than the following SDK-centric methods, they lack incorporation of subject-specific metadata (e.g. age, pathology, diagnosis) that can be a part of public datasets.

## Data Use Agreements

Many of these tutorials connect to public datasets that require a Data Use Agreement before downloading.  Please respect these constraints, as well as others, when uploading any data to a Flywheel instance.

## Imports

The following ipython Jupyter notebooks import public datasets into a specified Flywheel instance. Ensure you have the proper permissions in your Flywheel instance before attempting.

### [Kaggle Pneumonia Chest X-Ray](kaggle_pneumonia_chestxray.ipynb)

Import data from the [Kaggle RSNA Pneumonia Detection Challenge](https://www.kaggle.com/c/rsna-pneumonia-detection-challenge/).

### [COVID-19 Chest X-Ray Dataset](covid_chestxray_dataset.ipynb)

Import data from the [COVID-19 Chest X-Ray Dataset](https://github.com/ieee8023/covid-chestxray-dataset).
