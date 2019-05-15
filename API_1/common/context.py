#正则表达式

import re
import configparser
from API_1.common.config import config


class Context:
    loan_id = None


def replace(data):
    p = "#(.*?)#"  #正则表达式
    while re.search(p,data):   #从任意位置开始找，找到第一个就返回match object，如果没有就返回none
        print(data)
        m = re.search(p,data)   #查找匹配合适正则表达式的数据
        g = m.group(1)  #拿到参数化的key，只返回指定组的内容
        try:
            v = config.get('data',g)  #根据key取配置文件里面的值
        except configparser.NoOptionError as e:  #如果配置文件里面没有的时候，去Context里面找
            if hasattr(Context,g):  #判断是否有这个属性，有返回
                v = getattr(Context,g)  #获取类属性的值
            else:
                print("找不到参数化的值")
                raise e

        print(v)
        data = re.sub(p,v,data,count=1)  #替换data中的数据
    return data