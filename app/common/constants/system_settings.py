import platform
import app.common.values.strings as Strings


class SystemSettings:
    path_files_videos: str = "videos/"
    path_file_cache: str = "cache/"

    number_screen: int = 1
    active_automatic_updates: bool = False
    type_os: str = platform.system()

    def is_windows(self) -> bool:
        return self.type_os is Strings.type_os_windows

    def is_unix(self) -> bool:
        return self.type_os in Strings.type_os_unix
