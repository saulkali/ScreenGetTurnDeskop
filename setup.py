import PyInstaller.__main__
import shutil
from helper import getFile

path_base: str = "dist/main/"

def copy_cache_folder():
    try:
        folder_name: str = "cache"
        shutil.copytree(
            src=getFile(folder_name),
            dst= path_base + folder_name
        )
    except Exception as e:
        print(f"Error: {e}")
    else:
        print(f"Create file /{folder_name}")

def copy_logs_folder():
    try:
        folder_name: str = "logs"
        shutil.copytree(
            src=getFile(folder_name),
            dst= path_base + folder_name
        )
    except Exception as e:
        print(f"Error: {e}")
    else:
        print(f"Create file /{folder_name}")

def copy_staticfiles_folder():
    try:
        folder_name: str = "staticfiles"
        shutil.copytree(
            src=getFile(folder_name),
            dst= path_base + folder_name
        )
    except Exception as e:
        print(f"Error: {e}")
    else:
        print(f"Create file /{folder_name}")

def copy_res_folder():
    try:
        folder_name: str = "app/res"
        shutil.copytree(
            src=getFile(folder_name),
            dst= path_base + folder_name
        )
    except Exception as e:
        print(f"Error: {e}")
    else:
        print(f"Create file /{folder_name}")

def copyfiles():
    copy_cache_folder()
    copy_logs_folder()
    copy_staticfiles_folder()
    copy_res_folder()

def main():
    #commands pyinstaller
    commands = [
        getFile("setup.spec")
    ]

    PyInstaller.__main__.run(commands,)
    copyfiles()

main()