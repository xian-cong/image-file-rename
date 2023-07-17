import os

def rename_images(dataset_path, class_names):
    for class_name in class_names:
        class_path = os.path.join(dataset_path, class_name)
        for idx, file_name in enumerate(os.listdir(class_path)):
            if file_name.lower().endswith((".jpg", ".jpeg", ".png")):  # Check for JPG, JPEG, or PNG image
                # Get the file extension from the original file_name
                ext = os.path.splitext(file_name)[1]
                # Generate a new filename based on class name and index with the same extension.
                new_filename = f"{class_name}_{idx}{ext}"
                new_file_path = os.path.join(class_path, new_filename)

                # Handle filename clashes
                counter = 1
                while os.path.exists(new_file_path):
                    new_filename = f"{class_name}_{idx}_{counter}{ext}"
                    new_file_path = os.path.join(class_path, new_filename)
                    counter += 1

                old_file_path = os.path.join(class_path, file_name)
                os.rename(old_file_path, new_file_path)

# Replace 'dataset_path' with the path to your dataset directory.
# Replace class_names with a list of class names in your dataset.
dataset_path = 'C:\\Projects\\new-rpa-poc\\Image Classification Model\\data\\Train'
class_names = ['Nonpopup', 'Popup']

rename_images(dataset_path, class_names)
