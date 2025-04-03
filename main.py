import shutil
import os
from pathlib import Path
from Classifier import classify_image

# Main_dir="C:<path>NotHotDog/Testing/"
# HD_dir="<path>NotHotDog/Testing/Hotdog/"
# Other_dir= "<path>NotHotDog/Testing/Other/"
print("Provide the path leading up to your Testing/ directory. NOTE: Format must be in forward slashes, and must include a slash at the end. Do not include Testing itself.")
print("(You can also probably just input the folder you cloned this repo from)")
print("Ex. C:/Users/econ9/Development/NotHotdog/ <your testing folder>")
user_base_directory = input("Path: ")

testing_directory = os.path.join(user_base_directory, "Testing/")
to_sort_directory = os.path.join(testing_directory, "To_Sort/")
hotdog_directory = os.path.join(testing_directory, "Hotdog/")
other_directory = os.path.join(testing_directory, "Other/")


def get_images_from_directory(directory, valid_extensions=(".jpg", ".jpeg", ".png")):
    #Returns a list of image file paths from the specified directory.
    return [os.path.join(directory, f) for f in os.listdir(directory) 
            if f.lower().endswith(valid_extensions)]


def move_image(image_path, destination_folder):
    #Moves an image to the specified folder, creating the folder if needed.
    os.makedirs(destination_folder, exist_ok=True)  # Ensure the folder exists
    shutil.move(image_path, os.path.join(destination_folder, os.path.basename(image_path)))


images = get_images_from_directory(to_sort_directory)
print(images)

for image in images:
        is_hotdog = classify_image(image) 

        # Move the image to the appropriate folder
        if is_hotdog == True:
            move_image(image, hotdog_directory)
        else:
            move_image(image, other_directory)


