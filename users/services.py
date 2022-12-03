import json


class FileReadWriteService:
    _filee_name = None

    @classmethod
    def load_users(cls):
        try:
            with open(cls._filee_name) as file:
                return json.load(file)
        except (Exception,):
            return []

    @classmethod
    def save_users(cls, data):
        try:
            with open(cls._filee_name, 'w') as file:
                json.dump(data, file)
        except Exception as err:
            return str(err)

