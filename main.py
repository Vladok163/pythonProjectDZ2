import requests
from bs4 import BeautifulSoup

url = "https://akabab.github.io/superhero-api/api/all.json"
response = requests.get(url)
response = response.json()

name = {}

def get_key(url,hero_list):
    best_hero = ''
    best_brain = 0
    for name in hero_list:
        for item in response:
            if 'Hulk' == item['name'] and best_brain < item['powerstats']:
                best_hero = item["name"]
                best_brain = item["powerstats"]
                return f'{best_hero}, {best_brain}'






# See PyCharm help at https://www.jetbrains.com/help/pycharm/
class YaUploader:
    def __init__(self, token: str):
        self.token = token

 def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files?limit=1000'
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        return response.json()

 def _get_upload_link(self, disk_file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()


if __name__ == '__main__':
path_to_file = ""
token = ""
uploader = YaUploader(token)
result = uploader.upload(path_to_file)
