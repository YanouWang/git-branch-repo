# 数据处理模块 - B3增强版
import csv
import re

def process_data(data):
    """B3数据处理V2"""
    data = str(data).strip()
    return re.sub(r"\s+", " ", data)

def export_csv(data):
    """导出CSV"""
    return ",".join(map(str, data))

def clean_text(text):
    """B3新增：文本清洗"""
    return text.lower().strip()
