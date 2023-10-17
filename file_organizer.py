import os
import shutil

    
def get_file_category(file_name):
    file_extension = os.path.splitext(file_name)[1].lower()
    text_documents = ['.txt', '.doc', '.docx', '.rtf']
    spreadsheets = ['.xls', '.xlsx', '.csv']
    presentations = ['.ppt', '.pptx']
    pdf_documents = ['.pdf']
    images = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg']
    video = ['.mp4', '.avi', '.mkv']
    code_files = ['.html', '.css', '.js', '.py', '.java']
    archives = ['.zip', '.rar', '.tar.gz', '.7z']
    databases = ['.sql']
    executables = ['.exe', '.app']
    fonts = ['.ttf', '.otf']
    # Check the file extension and assign a category
    if file_extension in text_documents:
        return "text_documents"
    elif file_extension in spreadsheets:
        return "spreadsheets"
    elif file_extension in presentations:
        return "presentations"
    elif file_extension in pdf_documents:
        return 'pdf_documents'
    elif file_extension in images:
        return 'images'
    elif file_extension in video:
        return 'video'
    elif file_extension in code_files:
        return 'code_files'
    elif file_extension in archives:
        return 'archives'
    elif file_extension in databases:
        return 'databases'
    elif file_extension in executables:
        return 'executables'
    elif file_extension in fonts:
        return 'fonts'
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

# # Example usage
# source_directory = "C:\Users\Dell\OneDrive\Desktop\expt"
# destination_directory = "C:\Users\Dell\OneDrive\Desktop\expt\dest"
# organize_files(source_directory, destination_directory)
