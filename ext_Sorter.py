import os, glob, shutil

# source directory that will be sorted
user_Path = "C:/Users/User/Desktop/source_dir"

# destination directory
path = "C:/Users/User/Desktop/destination_dir"
imgDir = path + "imgs/"
vidDir = path + "vids/"

def sortImages(imgDir, user_Path):
    """
    Looks for .jpg .jpeg and .png extensions
    matches all file extensions in current directory
    and all subdirectories using recursion 
    """
    for i in glob.glob(user_Path+'**/*.jpg', recursive=True) or  glob.glob(user_Path+'**/*.jpeg', recursive=True) or glob.glob(user_Path+'**/*.png', recursive=True):
        print(i)
        shutil.move(i, imgDir) # moves from src to destination folder

def sortVideos(vidDir, user_Path):
    """
    Looks for .mp4 and .avi extensions
    """
    for v in glob.glob(user_Path+'**/*.mp4', recursive=True) or glob.glob(user_Path+'**/*.avi', recursive=True):
        print(v)
        shutil.move(v, vidDir) # moves from src to destination folder

# creates directory and sorts file extensions
try:
    if not os.path.exists(path):
        os.makedirs(imgDir)
        os.makedirs(vidDir)
        print("Directory ", imgDir, " created!\n")
        print("Directory ", vidDir, " created!\n")
        
        print("Starting to copy files into ", imgDir, "\n")
        sortImages(imgDir, user_Path)
        print("\nFinshed copying image files.....")

        print("\nStarting to copy files into ", vidDir, "\n")
        sortVideos(vidDir, user_Path)
        print("\nFinshed copying video files.....")

    else:
        # if directory exists sort file extensions 
        print("\nStarting to copy files into ", imgDir, "\n")
        sortImages(imgDir, user_Path)
        print("\nFinshed copying image files.....")

        print("\nStarting to copy files into ", vidDir, "\n")
        sortVideos(vidDir, user_Path)
        print("\nFinshed copying video files.....")

except FileExistsError:
    print("Error", FileExistsError)