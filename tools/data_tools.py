import pandas as pd
import numpy as np
from pathlib import Path
from typing import Any, Dict, List, Optional

# Data processing tools

def df_from_csv(path: str, **kwargs) -> pd.DataFrame:
    """从 CSV 创建 DataFrame"""
    return pd.read_csv(path, **kwargs)


def df_to_csv(df: pd.DataFrame, path: str, index: bool = False, **kwargs) -> None:
    """DataFrame 写入 CSV"""
    p = Path(path).expanduser().parent
    p.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=index, **kwargs)


def df_head(df: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    """返回前 n 行"""
    return df.head(n)


def filter_df(df: pd.DataFrame, condition: str) -> pd.DataFrame:
    """按表达式过滤 DataFrame"""
    return df.query(condition)


def fillna(df: pd.DataFrame, value: Any = 0) -> pd.DataFrame:
    """填充缺失值"""
    return df.fillna(value)


def array_stats(arr: np.ndarray) -> Dict[str, Any]:
    """返回 numpy 数组统计信息"""
    return {
        "shape": arr.shape,
        "dtype": str(arr.dtype),
        "mean": float(np.mean(arr)),
        "std": float(np.std(arr)),
        "min": float(np.min(arr)),
        "max": float(np.max(arr)),
        "sum": float(np.sum(arr)),
    }


def df_drop_columns(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    """删除列"""
    return df.drop(columns=columns)
