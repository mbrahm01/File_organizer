import os
import shutil

    
def get_file_category(file_name):
    file_extension = os.path.splitext(file_name)[1].lower()
    document_extensions = ['.txt', '.doc', '.docx', '.pdf']
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    video_extensions = ['.mp4', '.avi', '.mkv', '.mov']
    python_extensions= ['.py']
    # Check the file extension and assign a category
    if file_extension in document_extensions:
        return "Documents"
    elif file_extension in image_extensions:
        return "Images"
    elif file_extension in video_extensions:
        return "Videos"
    elif file_extension in python_extensions:
        return 'Python'
    else:
        return "Other"

def organize_files(source_dir, destination_dir):
    for filename in os.listdir(source_dir):
        source_path = os.path.join(source_dir, filename)
        if os.path.isfile(source_path):
            category = get_file_category(filename)
            category_dir = os.path.join(destination_dir, category)

            if not os.path.exists(category_dir):
                os.makedirs(category_dir)

            shutil.move(source_path, os.path.join(category_dir, filename))

# Example usage
source_directory = "C://Users//Dell//OneDrive//Desktop//expt"
destination_directory = "C://Users//Dell//OneDrive//Desktop//expt//dest"
organize_files(source_directory, destination_directory)
