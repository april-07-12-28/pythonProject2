import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        params = {"path": file_path, "overwrite": "True"}
        headers = {"Authorization": f"OAuth {self.token}"}
        resp = requests.get(url, params=params, headers=headers)
        path_url = resp.json().get('href')
        with open(file_path,'rb') as f:
            response = requests.put(path_url, files={"text": f})


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    file_path = r"C:\Users\petre\PycharmProjects\задача_3\text.txt"
    token = "....."
    uploader = YaUploader(token)
    result = uploader.upload(file_path)