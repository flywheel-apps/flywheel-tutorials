# DICOM and NIfTI
What are Dicom files and NIfTI files? Clinical imaging data is often stored in the DICOM format, but neuroimaging is often shared in the NIfTI format.  This section explores the differences as well as conversion strategies


## DICOM
DICOM (digital imaging and communications in medicine) is a standard developed by the American College of Radiology [1,2]. DICOM was developed to hold multiple imaging sets as well as patient and image specific information in one file.  DICOM's consist of a header that has patient information, parameters for the imaging study, image attributes (size, etc.), and machine specific information [2].  After the header, there are multiple image sets containing intensity data that can be
reconstructed _along_ with the information in the header [2].  The DICOM format stresses the idea that the imaging data cannot be separated from the metadata [1,2].

An important limitation of the DICOM format is that data is essentially 2D where 3D information is represented by many slices of 2D data. Additionally, DICOM headers can contain _private fields_ which are manufacturer specific and are not documented [2].

DICOM is a very technical standard which also defines image compression and network transfer protocols [3].  DICOM requires significant development effort, and is therefore not always supported in a research environment [3].

## NIfTI
The NIfTI format is based off an older format called Analyze that was built specifically for post-processing [2].  The NIfTI file has a more technical structure that can be represented as a C structure.  The header has a predictable length and the NIfTI format can store images with non-integer intensity values natively (whereas DICOM uses a scale factor to scale values to integers) [2].  

NIfTI is generally thought of as a much simpler file format.  Additionally, there are multiple open source libraries supporting reading and writing NIfTI files.  Because of this many processing tools have been built to support NIfTI files [3].


## Conversion
Converting from DICOM to NIfTI is often necessary to do processing on clinical imaging data.  Clinical imaging comes in the DICOM file format whereas most processing libraries are written to support NIfTI files.

### Challenges



[1] M. Larobina, L. Murino, "Medical Image File Formats," _J. Digit. Imaging_, vol. 27, no. 2, pp. 200-206, 2014. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3948928/

[2] D. R. Varma, "Managing DICOM images: Tips and tricks for the radiologist," _Indian J. Radiol. Imaging_, vol. 22, no. 1, pp. 4-13, 2012.

[3] X. Li, P. S. Morgan, et al. "The first step for neuroimaging data analysis: DICOM to NIfTI conversion," _J. Neuro. Meth._, vol. 264, pp. 47-56, 2016. https://www.sciencedirect.com/science/article/pii/S0165027016300073

[x] K. J. Gorgolewski, T. Auer, et al., "The brain imaging data structure, a format for organizing and describing outputs of neuroimaging experiments," _Sci. Dat._, no. 3, vol. 160044, 2016. https://www.nature.com/articles/sdata201644


