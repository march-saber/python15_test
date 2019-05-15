import configparser
from API_1.common import contants

class ReadConfig:
    """
    完成配置文件的读取
    """

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(contants.global_file,encoding='utf-8') #先加载global_file
        switch = self.config.getboolean('switch','on')  #返回的为布尔值，on的值
        if switch:  #开关打开的时候，使用online的配置
            self.config.read(contants.online_file, encoding='utf-8')
        else:
            self.config.read(contants.test_file, encoding='utf-8')

    def get(self,section,option):   #创建一个get方法，用于config调用，
        return self.config.get(section,option)

config = ReadConfig()

# if __name__ == '__main__':
#     config = ReadConfig()
#     print(config.get('api','pre_url'))
