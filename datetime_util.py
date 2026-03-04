from datetime import datetime
from log_util import logger

def timestamp_to_datetime_str(timestamp, format_str="%Y-%m-%d %H:%M:%S"):
    """
    Description: 将时间戳转换为指定格式的日期时间字符串
    Author: yangshilin
    Time: 2026-03-04 09:33
    Params: timestamp: 时间戳（int/float/datetime对象）
            format_str: 输出格式（默认"%Y-%m-%d %H:%M:%S"）
    Returns: 格式化后的日期时间字符串（如"2025-03-03 12:00:00"）
    """
    try:
        # 1. 处理时间戳：如果是13位毫秒级，转换为10位秒级
        if isinstance(timestamp, (int, float)):
            # 毫秒级时间戳（如1741000000000）→ 转为秒级
            if len(str(int(timestamp))) == 13:
                timestamp = timestamp / 1000
            # 转换为datetime对象（本地时区）
            dt = datetime.fromtimestamp(timestamp)
        # 2. 如果输入已经是datetime对象，直接格式化
        elif isinstance(timestamp, datetime):
            dt = timestamp
        else:
            logger.error(f"时间戳类型错误，仅支持int/float/datetime，输入类型：{type(timestamp)}")
            return ""
        
        # 3. 格式化输出
        return dt.strftime(format_str)
    
    except ValueError as e:
        # 处理无效时间戳（如超出范围、格式错误）
        logger.error(f"时间戳转换失败：无效的时间戳 {timestamp}，错误：{e}")
        return ""
    except Exception as e:
        # 其他未知异常
        logger.error(f"时间戳转换异常：{e}")
        return ""