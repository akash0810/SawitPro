import cv2
import numpy as np
import os

def save_detected_objects(image_path, save_folder, lower_color_bound, upper_color_bound, min_object_area):
    image = cv2.imread(image_path)

    # Convert the image to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_bound = np.array(lower_color_bound)
    upper_bound = np.array(upper_color_bound)
    mask = cv2.inRange(hsv_image, lower_bound, upper_bound)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Save each detected object as a separate image
    os.makedirs(save_folder, exist_ok=True)
    for i, contour in enumerate(contours):
        x, y, w, h = cv2.boundingRect(contour)
        object_area = w * h
        if object_area >= min_object_area:
            object_image = image[y:y + h, x:x + w]
            object_filename = os.path.join(save_folder, f"color_{i}.png")
            cv2.imwrite(object_filename, object_image)

if __name__ == '__main__':
    
    # Replace 'image_path' with the path to your image file like classify.jpg
    image_path = 'C:\\Users\\Akash Verma\\Dropbox\\PC\\Downloads\\classify.jpeg'
    

    # Define the lower and upper bounds for the color range to detect
    lower_red_bound = [160, 153, 153]  
    upper_red_bound = [180, 255, 255]
    lower_yellow_bound = [22, 93, 0]  
    upper_yellow_bound = [45, 255, 255]
    lower_green_bound = [36, 25, 25]  
    upper_green_bound = [70, 255, 255]
    min_object_area = 1000
    
    save_detected_objects(image_path, 'red_objects', lower_red_bound, upper_red_bound, min_object_area)
    save_detected_objects(image_path, 'yellow_objects', lower_yellow_bound, upper_yellow_bound, min_object_area)
    save_detected_objects(image_path, 'green_objects', lower_green_bound, upper_green_bound, min_object_area)
