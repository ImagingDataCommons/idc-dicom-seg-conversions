# Prostate_mri_us_biopsy_dcm_conversion
Provides examples for converting prostate MRI-US-Biopsy collection STL prostate and lesion surfaces to DICOM SEG and DICOM STL. 

# Conversion to DICOM process

## Conversion to DICOM SEG
1) STL to labelmap -- Utils folder
2) labelmap to SEG DICOM -- see DEMO_Conversion_STL_TO_DICOM.ipynb

## Conversion to DICOM STL
1) STL to DICOM STL -- see DEMO_Conversion_STL_TO_DICOM.ipynb

# Repository organization

## Data samples folder
The folder contains STL and labelmaps samples for prostate and lesion surfaces, used for conversion showcase.
We include the already computed labelmaps from Slicer conversion, since we cannot showcase it inside Google Colab.

## metadata folder
Contains segments metadata.json files used as input for conversion to DICOM SEG, for both lesion and prostate surfaces.

## Utils folder
Contains example of slicer script used to convert STL files into labelmaps with reference T2W images.

The conversion Slicer script is also available in our demo github repository, [here](https://github.com/ImagingDataCommons/prostate_mri_us_biopsy_dcm_conversion/blob/main/utils/convert_STL_labelmap_slicer_script.py).

The terminal command run over the Slicer-based python script is provided below as an example:

`<path to Slicer executable> --no-splash --no-main-window --python-script "<root-folder-path-to-script>/convert_STL_labelmap_slicer_script.py.py"`

The script has pre-defined paths for the location of the STL files and the output labelmaps files, so please change these paths inside the script itself.

Mentioned scripts iterates over the STL files and finds the reference T2W image **.nrrd** file, used as a reference node for the output labelmap segmentations. Resulting labelmaps have the same geometry and orientation as the segmented MRI T2W image.

## Notebooks

[main_stl_seg_to_dcm.ipynb](https://github.com/ImagingDataCommons/prostate_mri_us_biopsy_dcm_conversion/blob/main/main_stl_seg_to_dcm.ipynb) notebook gives an overview of the conversion steps and how to reproduce the results.

[demo_conversion_stl_to_dicom.ipynb](https://github.com/ImagingDataCommons/prostate_mri_us_biopsy_dcm_conversion/blob/main/demo_conversion_stl_to_dicom.ipynb) is supporting the implementation of the M3D DICOM modality in [QIICR](https://github.com/QIICR/QuantitativeReporting) for [Slicer3D](https://www.slicer.org/) use.

# Conversion tools used

- STL To labelmap : Slicer3D
- labelmap to SEG DICOM : dcmqi 1.2.4
- STL to DICOM STL : dicom3tools 

# Collection information : Prostate-MRI-US-Biopsy

Please see [TCIA website](https://wiki.cancerimagingarchive.net/pages/viewpage.action?pageId=68550661) and [Imaging Data Commons](https://portal.imaging.datacommons.cancer.gov/explore/) for additional details/visualization of the T2W MRI images considered for annotations conversion. 


# Where to download the DICOM SEG/STL objects

A zenodo publication will follow shortly, where 1017 prostate annotations and 1311 lesions were converted from STL to DICOM SEG/STL and publicly available.
A final step will be the publication of these annotations in the [Imaging Data Commons platform](https://portal.imaging.datacommons.cancer.gov/).
