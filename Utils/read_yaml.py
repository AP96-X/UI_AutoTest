import os

import yaml

root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class ReadFileData:

    @staticmethod
    def load_data(file_path, path="ApiData"):
        try:
            data_file_path = os.path.join(root_path, path, file_path)
            with open(data_file_path, encoding='utf-8') as f:
                data_content = yaml.safe_load(f)
        except Exception as ex:
            print(ex)
        else:
            return data_content

    @staticmethod
    def load_config(file_path):
        try:
            data_file_path = os.path.join(root_path, "Config", file_path)
            with open(data_file_path, encoding='utf-8') as f:
                data_content = yaml.safe_load(f)
        except Exception as ex:
            print(ex)
        else:
            return data_content

    @staticmethod
    def write_data(file_path, keyword, data):
        try:
            data_file_path = os.path.join(root_path, "ApiData", file_path)
            write_data = {
                "%s" % keyword: data
            }
            with open(data_file_path, "w", encoding="utf-8") as f:
                yaml.dump(data=write_data, stream=f, allow_unicode=True)
        except Exception as ex:
            print(ex)


read_data = ReadFileData

if __name__ == '__main__':
    pass
