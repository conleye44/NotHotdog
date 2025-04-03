import shutil
import os
from Classifier import classify_image

Main_dir="C:\\Users\\sys4dmin\\Documents\\Development\\NotHotDog\\Testing"
HD_dir="C:\\Users\\sys4dmin\\Documents\\Development\\NotHotDog\\Testing\\Hotdog"
Other_dir= "C:\Users\sys4dmin\Documents\Development\NotHotDog\Testing\Other"

def get_images_from_directory(directory, valid_extensions=(".jpg", ".jpeg", ".png")):
    #Returns a list of image file paths from the specified directory.
    return [os.path.join(directory, f) for f in os.listdir(directory) 
            if f.lower().endswith(valid_extensions)]


def move_image(image_path, destination_folder):
    #Moves an image to the specified folder, creating the folder if needed.
    os.makedirs(destination_folder, exist_ok=True)  # Ensure the folder exists
    shutil.move(image_path, os.path.join(destination_folder, os.path.basename(image_path)))


images = get_images_from_directory(Main_dir)
print(images)

for image in images:
        is_hotdog = classify_image(image)
        is_hotdog = False  

        # Move the image to the appropriate folder
        if is_hotdog:
            move_image(image, HD_dir)
        else:
            move_image(image, Other_dir)


