import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_upload_url(self, file_name):
        headers = {
            'Authorization': f'OAuth {self.token}'
        }
        params = {
            'path': file_name,
            'overwrite': 'true'
        }
        response = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload', params=params, headers=headers)
        response.raise_for_status()
        return response.json().get('href')

    def upload(self, file_path: str):
        """Метод загружает файл file_path на яндекс диск"""
        # Получаем имя файла
        file_name = file_path.split('/')[-1]

        # Получаем ссылку для загрузки файла
        upload_url = self.get_upload_url(file_name)

        # Загружаем файл на Яндекс.Диск по полученной ссылке
        with open(file_path, 'rb') as f:
            response = requests.put(upload_url, files={'file': f})
        response.raise_for_status()

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = input("Введите путь к файлу: ")
    token = input("Введите OAuth-токен: ")
    uploader = YaUploader(token)
    uploader.upload(path_to_file)