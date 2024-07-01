import os
import glob
for stl_file_name in glob.glob(os.path.join("/Users/ccosmin/Documents/IDC/mri_us_biopsy/stl_files/STLs/*Target*.STL")):
    output_file_name = f"/Users/ccosmin/Documents/IDC/mri_us_biopsy/target_mr_labelmaps_resampled/{stl_file_name.split('/')[-1][:-4]}.nii.gz"
    patID = "-".join(stl_file_name.split("/")[-1].split('-')[0:5])
    serieUID = stl_file_name.split("/")[-1].split("-")[-1][:-4]
    reference_volume_path_lst = glob.glob(os.path.join("/Users/ccosmin/Documents/IDC/mri_us_biopsy/data_in/idc_mr_nrrd_data", f"{patID}_{serieUID}.nrrd"))
    if len(reference_volume_path_lst) == 1: 
        print(f"input STL : {stl_file_name}")
        print(f"output_file_name : {output_file_name}")
        referenceVolumeNode = slicer.util.loadVolume(reference_volume_path_lst[0])
        segmentationNode = slicer.util.loadSegmentation(stl_file_name)
        outputLabelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLabelMapVolumeNode')
        slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(segmentationNode, outputLabelmapVolumeNode, referenceVolumeNode)
        slicer.util.saveNode(outputLabelmapVolumeNode, output_file_name)
        slicer.mrmlScene.RemoveNode(segmentationNode)
        slicer.mrmlScene.RemoveNode(outputLabelmapVolumeNode)
        slicer.mrmlScene.RemoveNode(referenceVolumeNode)
        slicer.mrmlScene.Clear(0)
        assert os.path.exists(output_file_name)
        print("Done...\n")
