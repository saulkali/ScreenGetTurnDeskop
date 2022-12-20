from helper import singleton, getFile
import pickle
from app.common.constants.system_settings import SystemSettings
from app.common.constants.api_settings import ApiSettings

@singleton
class GlobalSystemSettings:

    api_settings:ApiSettings = ApiSettings()
    system_settings:SystemSettings = SystemSettings()

    def __init__(self):
        self.__read_files_pickles()

    def __load_api_settings(self):
        try:
            name_file = "api_settings"
            api_settings = open(getFile(self.system_settings.path_file_cache+name_file), "rb")
            self.api_settings = pickle.load(api_settings)
            print("settings api settings loaded")
        except Exception as error:
            print(error)
            print("settings api settings not found")

    def __load_system_settings(self):
        try:
            name_file = "api_settings"
            system_settings = open(getFile(self.system_settings.path_file_cache+name_file), "rb")
            self.system_settings = pickle.load(system_settings)
            print("settings api settings loaded")
        except Exception as error:
            print(error)
            print("settings api settings not found")
    def __read_files_pickles(self):
        self.__load_api_settings()

    def save(self):
        with open(getFile(self.system_settings.path_file_cache+"system_settings"), "wb") as system_settings_pickle_in:
            pickle.dump(self.system_settings, system_settings_pickle_in)
            print("save system settings")

        with open(getFile(self.system_settings.path_file_cache+"api_settings"), "wb") as api_settings_pickle_in:
            pickle.dump(self.api_settings, api_settings_pickle_in)
            print("save api settings")
        print("save all settings success")