import logging

logger = logging.getLogger()  #建立一个日志收集器
logger.setLevel("DEBUG")  #设定日志收集级别

fmt = "%(name)s-%(levelname)s-%(asctime)s-%(message)s-[%(filename)s:%(lineno)d]"
formatter = logging.Formatter(fmt=fmt)  #设定日志输出格式

console_handler = logging.StreamHandler()  #指定输出到控制台
#吧日志级别放到配置文件里面去配置-- 优化
console_handler.setLevel('DEBUG')   #指定输出级别
console_handler.setFormatter(formatter)

file_handler = logging.FileHandler("case.log")
# 吧日志级别放到配置文件里面去配置
file_handler.setLevel('INFO')
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.info("this is info msg")
logger.debug("this is debug msg")
