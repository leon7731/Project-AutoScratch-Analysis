import os
import io
from PIL import Image


def load_image(image_file):
	img = Image.open(image_file)
	return img


def save_uploadedfile(uploadedfile, Save_Path):
    """_summary_: Save Uploaded File to a Folder Directory

	Args:
		uploadedfile (_type_): Uploaded File
		Save_Path (_type_): A Folder Directory Path

	Returns:
		_type_: _description_ : Saved File Path
	"""

    #To read file as bytes:
    img_bytes_data = uploadedfile.getvalue()
    img = Image.open(io.BytesIO(img_bytes_data))
    # img.save(os.path.join(Save_Path ,uploadedfile.name))
    img.save(os.path.join(Save_Path ,"user_scratch_data.jpg"))


def save_multi_uploadedfiles(uploadedfiles, Save_Path):
    Index = 1
    for Image_File in (uploadedfiles):
       #To read file as bytes:
        img_bytes_data = Image_File.getvalue()
        img = Image.open(io.BytesIO(img_bytes_data))
        img.save(os.path.join(Save_Path ,f"user_scratch_data_{Index}.jpg"))
        Index+=1

 
def get_list_full_paths(Directory: str):
    """_summary_: Get All the files "Absolute Path" in a Folder Directory

    Args:
        Directory (_type_): A Folder Directory Path

    Returns:
        _type_: _description_ : List of all the files in the directory
    """
    return [os.path.join(Directory, file) for file in os.listdir(Directory)]


# def Delete_All_Files_in_Folder(Directory: str):
#     """_summary_: Delete All the files in a Folder Directory

#     Args:
#         Directory (str): _description_ : A Folder Directory Path
#     """
#     os.chdir(Directory)
#     all_files = os.listdir()

#     for f in all_files:
#         os.remove(f)

#     # print(os.listdir())