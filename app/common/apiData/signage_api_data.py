import app.common.constants.api_settings as ApiSettings
import requests
import guid
import json

class SignageApiData:

    def __init__(self):
        pass

    def get_signages(self,id_office:guid) -> list[str]:
        list_signages: list[str] = []
        try:
            http_response = requests.get(
                ApiSettings.host_base + ApiSettings.signage_by_office_endpoint + str(id_office),
                verify= False
            )
            if http_response.status_code == 200:
                json_response = http_response.json()
                if json_response is not None:
                    for signage in json_response:
                        signage_split = signage.split("/")
                        list_signages.append(signage_split[len(signage_split)-1])
        except Exception as error:
            print(error)
        return  list_signages