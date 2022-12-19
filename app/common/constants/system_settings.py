import platform
class SystemSettings:
    path_files_videos: str = "videos/"
    path_file_cache:str = "cache/"

    number_screen:int = 1
    active_automatic_updates: bool = False
    type_os: str = platform.system()