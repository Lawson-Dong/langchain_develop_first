import csv
import json
import os
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

# File operation tools

def read_file(path: Union[str, Path], encoding: str = "utf-8") -> str:
    """读取文件内容"""
    with open(path, "r", encoding=encoding) as f:
        return f.read()


def write_file(path: Union[str, Path], content: str, encoding: str = "utf-8", mode: str = "w") -> None:
    """写入文件（覆盖或追加）"""
    parent = Path(path).expanduser().parent
    parent.mkdir(parents=True, exist_ok=True)
    with open(path, mode, encoding=encoding) as f:
        f.write(content)


def append_file(path: Union[str, Path], content: str, encoding: str = "utf-8") -> None:
    """追加写文件"""
    write_file(path, content, encoding=encoding, mode="a")


def list_dir(path: Union[str, Path]) -> List[str]:
    """列出目录下文件"""
    return [str(p) for p in Path(path).expanduser().iterdir()]


def ensure_dir(path: Union[str, Path]) -> Path:
    """创建目录（如果不存在）"""
    p = Path(path).expanduser()
    p.mkdir(parents=True, exist_ok=True)
    return p


def read_csv(path: Union[str, Path], encoding: str = "utf-8") -> List[Dict[str, Any]]:
    """读取 CSV 为字典列表"""
    with open(path, newline="", encoding=encoding) as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]


def write_csv(path: Union[str, Path], rows: List[Dict[str, Any]], headers: Optional[List[str]] = None, encoding: str = "utf-8") -> None:
    """写入 Dict 列表到 CSV"""
    parent = Path(path).expanduser().parent
    parent.mkdir(parents=True, exist_ok=True)
    if not headers and rows:
        headers = list(rows[0].keys())
    with open(path, "w", newline="", encoding=encoding) as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers or [])
        writer.writeheader()
        writer.writerows(rows)


def read_json(path: Union[str, Path], encoding: str = "utf-8") -> Any:
    """读取 JSON 文件"""
    with open(path, "r", encoding=encoding) as f:
        return json.load(f)


def write_json(path: Union[str, Path], data: Any, indent: int = 2, encoding: str = "utf-8") -> None:
    """写入 JSON 文件"""
    parent = Path(path).expanduser().parent
    parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding=encoding) as f:
        json.dump(data, f, ensure_ascii=False, indent=indent)
