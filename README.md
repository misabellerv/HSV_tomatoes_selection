# Tomato Ripeness Detection Using HSV Color Space Segmentation

This project demonstrates a method for detecting/segmenting ripe tomatoes using HSV (Hue, Saturation, Value) color space segmentation. The segmentation technique helps isolate tomatoes based on their color characteristics, specifically targeting ripe ones for optimal harvesting.

https://github.com/misabellerv/HSV_tomatoes_selection/blob/main/videos/output_video.mp4

## Project Overview

The project involves:

- **Video Processing**: Processing a video feed (or series of images) to identify ripe tomatoes.
- **HSV Color Space**: Converting frames/images to HSV color space to separate color information from brightness.
- **Segmentation**: Creating masks to isolate regions of interest (ripe tomatoes) based on predefined HSV thresholds.
- **Visualization**: Displaying the segmentation results for visual verification.

## Requirements

- Python 3.x
- OpenCV
- NumPy

## Usage

1. Clone the repository:
```bash
git clone https://github.com/misabellerv/HSV_tomatoes_selection.git
```
2. Install dependencies:
### Using pip
```bash
pip install -r requirements.txt
```
### Using conda 
```bash
conda env create -f environment.yml
```
3. Check color space graphs (RGB and HSV). With these graphs, you will set a lower and upper boundaries to HSV as numpy arrays in format `np.array([h, s, v])`:
```bash
python HSV_plot.py
```
### Segmentation rip tomatoes
4. Having your boundaries, you can now run the python segmentation:
```bash
python HSV_segmentation.py --video ${VIDEO_PATH}
```


   

