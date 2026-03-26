import requests
import os
from bs4 import BeautifulSoup
from typing import Any, Dict
from urllib.parse import urljoin, urlparse, parse_qs
from langchain.tools import tool
import re

# 导入Tavily搜索API
try:
    from tavily import TavilyClient
    HAS_TAVILY = True
except ImportError:
    HAS_TAVILY = False

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


@tool
def fetch_webpage_content(url: str) -> str:
    """
    获取网页内容并提取主要文本。
    
    Args:
        url: 网页URL地址
    
    Returns:
        网页的主要文本内容（清除HTML标签）
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, timeout=10, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 移除script和style标签
        for script in soup(['script', 'style']):
            script.decompose()
        
        # 获取文本内容
        text = soup.get_text()
        
        # 清理多余的空白
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = ' '.join(chunk for chunk in chunks if chunk)
        
        # 限制长度
        if len(text) > 2000:
            text = text[:2000] + "...(内容太长已截断)"
        
        return text if text else "无法获取网页内容"
    except Exception as e:
        return f"获取网页失败: {str(e)}"


@tool
def search_google(query: str) -> str:
    """
    🌐 使用Tavily搜索API获取实时互联网信息
    
    Tavily是为AI设计的搜索引擎，能快速获取相关信息。
    
    Args:
        query: 搜索关键词
    
    Returns:
        搜索结果（标题、链接、内容摘要）
    """
    if not query or not isinstance(query, str):
        return "搜索关键词无效"
    
    try:
        # 获取Tavily API密钥
        api_key = os.getenv("TAVILY_API_KEY")
        
        if not api_key or api_key == "your_tavily_api_key_here":
            return "错误：未配置Tavily API密钥。请访问 https://tavily.com 获取API密钥，然后在.env中配置TAVILY_API_KEY"
        
        if not HAS_TAVILY:
            return "错误：Tavily库未安装。请运行: pip install tavily-python"
        
        # 使用Tavily搜索
        client = TavilyClient(api_key=api_key)
        response = client.search(query=query, max_results=5, include_answer=True)
        
        # 格式化搜索结果
        results = []
        
        # 如果有直接答案，先显示
        if "answer" in response and response["answer"]:
            results.append(f"【直接回答】\n{response['answer']}\n")
        
        # 显示搜索结果
        if "results" in response and response["results"]:
            results.append("【搜索结果】")
            for i, result in enumerate(response["results"], 1):
                title = result.get("title", "无标题")
                url = result.get("url", "无链接")
                content = result.get("content", "无摘要")
                
                # 限制内容长度
                if len(content) > 200:
                    content = content[:200] + "..."
                
                results.append(f"\n{i}. 标题：{title}\n   链接：{url}\n   内容：{content}")
            
            return "\n".join(results)
        else:
            return "未找到相关搜索结果"
    
    except Exception as e:
        return f"搜索失败: {str(e)}"


@tool
def extract_website_info(url: str, keywords: str = None) -> str:
    """
    从网站提取信息，可选按关键词过滤。
    
    Args:
        url: 网站URL
        keywords: 要提取的关键词（用逗号分隔），为空时返回所有内容
    
    Returns:
        提取的信息
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, timeout=10, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 移除脚本和样式
        for script in soup(['script', 'style']):
            script.decompose()
        
        # 获取标题
        title = soup.title.string if soup.title else "无标题"
        
        # 获取主要内容
        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = ' '.join(chunk for chunk in chunks if chunk)
        
        if keywords:
            # 按关键词过滤
            keywords_list = [k.strip().lower() for k in keywords.split(',')]
            filtered_text = []
            for sentence in text.split('。'):
                if any(keyword in sentence.lower() for keyword in keywords_list):
                    filtered_text.append(sentence)
            text = '。'.join(filtered_text)
        
        # 限制长度
        if len(text) > 2000:
            text = text[:2000] + "...(内容已截断)"
        
        return f"网页标题: {title}\n\n内容:\n{text}" if text else "无法提取内容"
    except Exception as e:
        return f"信息提取失败: {str(e)}"
