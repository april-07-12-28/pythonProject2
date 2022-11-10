import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        headers = {"Content-Type": "application/json", "Authorization": f"OAuth {self.token}"}
        params = {"path": file_path, "overwrite": "True"}
        resp = requests.get("https://cloud-api.yandex.net/v1/disk/resources/upload", params=params, headers=headers)
        resp_json = resp.json()
        path_url = resp_json['href']
        with open(file_path, 'rb') as f:
            response = requests.put(path_url, files=f)


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    file_path = "text.txt"
    token = .....
    uploader = YaUploader(token)
    result = uploader.upload(file_path)