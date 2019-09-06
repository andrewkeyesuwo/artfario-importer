
import requests



class MetAPI(object):
    FULL_COLLECTION_URL = '/public/collection/v1/objects'

    def __init__(self, met_api_url):
        #https://collectionapi.metmuseum.org
        self.met_api_url = met_api_url

    def get_full_collection(self):
        try:
            full_collection_url = self.met_api_url + self.FULL_COLLECTION_URL
            data = requests.get(full_collection_url)
            return data
        except requests.RequestException as e:
            print(e)
            raise e
        