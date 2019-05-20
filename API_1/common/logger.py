import logging
from API_1.common import contants
from API_1.common.config import config


def get_logger(name):

    logger = logging.getLogger(name)  #建立一个日志收集器
    logger.setLevel("DEBUG")  #设定日志收集级别

    fmt = "%(name)s - %(levelname)s - %(asctime)s - %(message)s - [%(filename)s:%(lineno)d]"
    formatter = logging.Formatter(fmt=fmt)  #设定日志输出格式

    console_handler = logging.StreamHandler()  #指定输出到控制台
    #吧日志级别放到配置文件里面去配置-- 优化
    gather = config.get('log','gather_log')
    console_handler.setLevel(gather)   #指定输出级别
    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(contants.log_dir + "/case.log")
    # 吧日志级别放到配置文件里面去配置
    output = config.get('log','output_log')
    file_handler.setLevel(output)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    return logger

if __name__ == '__main__':
    logger = get_logger('case')
    logger.debug("测试开始")
    logger.info("测试报错")
    logger.error("测试数据")
    logger.warning("测试结果")
    logger.critical("测试结束")