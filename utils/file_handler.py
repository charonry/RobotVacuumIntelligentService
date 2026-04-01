"""
文件相关操作处理
"""
import os
import hashlib
from utils.logger_handler import logger
from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader, TextLoader

def get_file_md5_hex(filepath: str):
    if not os.path.exists(filepath):
        logger.error(f"{filepath}文件不存在")
        return None
    if not os.path.isfile(filepath):
        logger.error(f"{filepath}不是文件")
        return None

    md5 = hashlib.md5()
    # 4kb分片，避免文件过大爆内存
    chunk_size = 4096
    try:
        with open(filepath,"rb") as f:
            while chunk := f.read(chunk_size):
                md5.update(chunk)
            return md5.hexdigest()
    except Exception as e:
        logger.error(f"{filepath}文件计算md5失败，{str(e)}")
        return None


def listdir_with_allowed_type(path: str, allowed_types: tuple[str]):
    files = []
    if not os.path.isdir(path):
        logger.error(f"{path}不是文件夹")
        return None
    for f in os.listdir(path):
        if f.endswith(allowed_types):
            files.append(os.path.join(path,f))
    # 避免被修改
    return tuple(files)


def pdf_loader(filepath: str, passwd=None) -> list[Document]:
    return PyPDFLoader(filepath,passwd).load()

def txt_loader(filepath: str) -> list[Document]:
    return TextLoader(filepath,encoding='utf-8').load()