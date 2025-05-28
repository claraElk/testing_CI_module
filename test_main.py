from main import extract_nifti_data, threshold_data, get_mean
import nibabel as nib
import numpy as np
import os


# Write a test for each function
# You shoudln't upload data on github

def test_extract_nifti_data(tmpdir):
    data = np.ones((32, 32, 15, 100), dtype=np.int16)
    img = nib.Nifti1Image(data, np.eye(4))
    path  = os.path.join(tmpdir, "./test.nii")
    nib.save(img, path)
    loaded_data = extract_nifti_data(path)
    assert np.array_equal(loaded_data, data), "loading is incorrect"

def test_threshold_data():
    data = np.random.rand(4 ,4)
    threshold = 0.1
    thresholded_data = threshold_data(data, threshold)
    assert (thresholded_data > threshold).all(), "thresholding is incorrect"

def test_get_mean():
    data = np.ones((4, 4))
    average = get_mean(data)
    assert average == 1.0, "mean calculation is incorrect"