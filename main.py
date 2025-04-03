"""


"""

import shutil
import os
from pathlib import Path
from Classifier import classify_image

# Takes in directory
print("Provide the path leading up to your Testing/ directory. NOTE: Format must be in forward slashes, and must include a slash at the end. Do not include Testing itself.")
print("(You can also probably just input the folder you cloned this repo from)")
print("Ex. C:/Users/econ9/Development/NotHotdog/Code <your testing folder>")
print("C:/Users/sys4dmin/Documents/Development/NotHotDog/Code/")
user_base_directory = input("Path: ")

testing_directory = os.path.join(user_base_directory, "Testing/")
to_sort_directory = os.path.join(testing_directory, "To_Sort/")
hotdog_directory = os.path.join(testing_directory, "Hotdog/")
other_directory = os.path.join(testing_directory, "Other/")


def get_images_from_directory(directory, valid_extensions=(".jpg", ".jpeg", ".png")):
    # Returns a list of image file paths from the specified directory.
    return [os.path.join(directory, f) for f in os.listdir(directory) 
            if f.lower().endswith(valid_extensions)]


def move_image(image_path, destination_folder):
    # Moves an image to the specified folder, creating the folder if needed.
    os.makedirs(destination_folder, exist_ok=True)  # Ensure the folder exists
    shutil.move(image_path, os.path.join(destination_folder, os.path.basename(image_path)))

# Array of paths to the images in the directories
images = get_images_from_directory(to_sort_directory)

# Moves the current image to the appropriate folder
for image in images:
        is_hotdog = classify_image(image) 
            # Classify_image is calling from a function within Classifier.py, 
            # that takes in an image path as an argument, runs it through the model, then returns True 
            # for hotdogs, and False for anything else. Had to do some shaboinkery 
            # to get it to work.
        print("\nClassifier returned: " + str(is_hotdog))
        if is_hotdog == True:
            print(f"Moving {image} to {'Hotdog' if is_hotdog else 'Other'}\n")
            move_image(image, hotdog_directory)
        else:
            print(f"Moving {image} to {'Hotdog' if is_hotdog else 'Other'}\n")
            move_image(image, other_directory)


