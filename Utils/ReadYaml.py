import os
import yaml

from Config.Config import Config


class ReadYaml(object):

    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(file=self.filename, mode="r", encoding='utf8', ) as f:
            data = f.read()
        data_yaml = yaml.load(data, Loader=yaml.FullLoader)
        for value in data_yaml:
            # 拼接URL地址
            if value.get("url地址") is not None:
                value["url地址"] = Config.url + value["url地址"]
            # 拼接上传文件的地址
            if value.get("files") is not None:
                value["files"] = Config.test_files_dir + os.path.sep + value["files"]

        return data_yaml


if __name__ == '__main__':
    print(dict(ReadYaml(os.path.join(Config.test_datas_dir, "TestLoginData.yaml")).read()[2])["断言元素定位"])
