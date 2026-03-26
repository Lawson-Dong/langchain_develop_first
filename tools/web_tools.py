import requests
from bs4 import BeautifulSoup
from typing import Any, Dict
from urllib.parse import urljoin, urlparse, parse_qs

# Web related tools

def http_get(url: str, params: Dict[str, Any] = None, headers: Dict[str, str] = None, timeout: int = 10) -> requests.Response:
    """发送 GET 请求"""
    return requests.get(url, params=params, headers=headers, timeout=timeout)


def http_post(url: str, data: Dict[str, Any] = None, json_data: Any = None, headers: Dict[str, str] = None, timeout: int = 10) -> requests.Response:
    """发送 POST 请求"""
    return requests.post(url, data=data, json=json_data, headers=headers, timeout=timeout)


def fetch_html(url: str, headers: Dict[str, str] = None, timeout: int = 10) -> str:
    """获取页面 HTML 内容"""
    resp = http_get(url, headers=headers, timeout=timeout)
    resp.raise_for_status()
    return resp.text


def parse_html(html: str, parser: str = "html.parser") -> BeautifulSoup:
    """解析 HTML 为 BeautifulSoup 对象"""
    return BeautifulSoup(html, parser)


def parse_url(url: str) -> Dict[str, Any]:
    """解析 URL 各部分"""
    p = urlparse(url)
    return {
        "scheme": p.scheme,
        "netloc": p.netloc,
        "path": p.path,
        "params": p.params,
        "query": p.query,
        "fragment": p.fragment,
        "hostname": p.hostname,
        "port": p.port,
        "username": p.username,
        "password": p.password,
        "query_dict": parse_qs(p.query),
    }


def url_join(base: str, path: str) -> str:
    """拼接相对URL"""
    return urljoin(base, path)
