import requests


class YandexFolderApi:

    def __init__(self, tokken, folder_name):
        self.token = tokken
        self.url = "https://cloud-api.yandex.net/v1/disk/resources"
        self.headers = {'Authorization': self.token}
        self.params = {'path': folder_name}

    def create_folder(self):
        return requests.put(self.url, headers=self.headers, params=self.params).status_code


TOKKEN = 'A**************************'

if __name__ == '__main__':
    print(YandexFolderApi(TOKKEN, '1/2').create_folder())
