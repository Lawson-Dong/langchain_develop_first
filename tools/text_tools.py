from langchain.tools import tool

@tool
def get_text_length(text: str) -> str:
    """获取文本的字符长度"""
    return f"文本长度: {len(text)} 个字符"

@tool
def reverse_string(text: str) -> str:
    """反转字符串"""
    return f"反转结果: {text[::-1]}"