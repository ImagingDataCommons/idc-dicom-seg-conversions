# Conversion of PANCREAS_CT collection pancreas annotations from CT images to DICOM SEG

Pancreas annotations based on 81 patients CT scanned were converted from NIFTI format to DICOM SEG objects, aiming to be ingested into NCI Imaging Data Commons.

# Organization of the repository

**pancreas_ct_annotations_conversion_demo.ipynb** and **main_pancreas_ct_annotations_conversion.ipynb** both reflect the conversion process from NIFTI SEG to DICOM SEG of the pancreas annotations. The demo python notebook does not require any authentification or Google Cloud Computing credentials. 

The **data samples** folder contains meta.json file used as SEG metadata input for the dcmqi command itkimage2segimage command.

annotations_nifti and CT_DICOM folder contains samples used in the demo notebook.
