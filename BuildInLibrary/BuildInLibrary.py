import random
import re
import time


class BuildInLibrary:
    glob_parameter = {}  # 存全局变量

    def set_glob_parameter(self, key, value):
        """把value的值放入变量名 key 中，"""
        # 1.提取 key   ##{{first_phone}}
        parameter_key = re.fullmatch(r'{{(\w+)}}', key).group(1)
        # 2.保存参数
        self.glob_parameter[parameter_key] = value
        return self.glob_parameter.get(parameter_key)

    def get_glob_parameter(self, key):
        self.glob_parameter['timestamp'] = str(int(time.time() * 1000))
        self.glob_parameter["timetime"] = str(int(time.time()))
        self.glob_parameter['random_phone'] = "1" + \
                                              str(random.randint(3, 9)) + \
                                              str(random.randint(0, 9)) + \
                                              time.strftime('%d%H%M%S')
        return self.glob_parameter.get(key)

    def replace_parameter(self, value):
        """替换参数--> 可以替换多个~,满足{{$参数}}规则的会被替换"""
        parameter_key = re.findall(r'{{\$(\w+)}}', value)
        for param in parameter_key:
            value = self.get_glob_parameter(param)
            to = rf"{value}"
            value = re.sub(rf'{{{{\${param}}}}}', lambda m: to, value)
        return value


if __name__ == "__main__":
    bl = BuildInLibrary()
    bl.set_glob_parameter("{{username}}", "admin")
    bl.set_glob_parameter("{{password}}", "123456")
    username = bl.get_glob_parameter("username")
    password = bl.get_glob_parameter("password")
    text = "{{$username}} + {{$password}} + {{$timetime}}"
    t = bl.replace_parameter(text)
    print(t)
