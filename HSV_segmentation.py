import cv2
import numpy as np
import argparse

# Argument parser for command-line options
parser = argparse.ArgumentParser(description="HSV masking for tomatoes selection.")

# Command-line arguments
parser.add_argument('--video', default=None, help='Path to the video file.')

args = parser.parse_args()

# HSV limits (you should check it manually using HSV_space.ipynb)
LOWER_BOUND = np.array([0, 100, 100])
UPPER_BOUND = np.array([10, 255, 255])

# Resize video
WIDTH = 700
HEIGHT = 500

# Open video
VIDEO_PATH = args.video

cap = cv2.VideoCapture(VIDEO_PATH)

while True:
    ret, frame = cap.read()
    
    if not ret:
        break
    
    frame = cv2.resize(frame, (WIDTH, HEIGHT))
    
    # Convert frame to csv
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Create mask given the HSV interval
    mask = cv2.inRange(hsv_frame, LOWER_BOUND, UPPER_BOUND)
    
    # Apply binary mask to original image
    apply_mask = cv2.bitwise_and(frame, frame, mask=mask)
    
    # Colored mask
    colored_mask = np.zeros_like(frame)
    colored_mask[mask > 0] = [255, 0, 0]
    
    # Masked original frame 
    masked_frame = cv2.addWeighted(frame, 1, colored_mask, 0.5, 0)

    combined_frame = np.hstack((frame, apply_mask, masked_frame))
    cv2.imshow(f'Tomatoes Harvesting Selection Using HSV Segmentation', combined_frame)
    
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
