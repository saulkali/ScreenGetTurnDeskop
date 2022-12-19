from app.common.apiData.signage_api_data import SignageApiData
import guid

class SignageBusiness:
    signage_api_data: SignageApiData = None
    def __init__(self):
        self.signage_api_data = SignageApiData()

    def get_signages(self, id_office: guid) -> list[str]:
        return self.signage_api_data.get_signages(id_office)