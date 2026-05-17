# 数据处理模块 - B3版本
import csv

def process_data(data):
    """B3分支的数据处理"""
    return str(data).strip()

def export_csv(data):
    """B3新增：导出CSV"""
    return ",".join(map(str, data))
