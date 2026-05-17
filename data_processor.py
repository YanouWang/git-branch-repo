# 数据处理模块 - C4版本
import json

def process_data(data):
    """C4分支的数据处理"""
    if isinstance(data, str):
        return data.upper()
    return json.dumps(data)

def validate_data(data):
    """C4新增：数据验证"""
    return data is not None
