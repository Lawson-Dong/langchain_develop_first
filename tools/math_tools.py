from langchain.tools import tool

@tool
def calculator(expression: str) -> str:
    """计算数学表达式，例如 '2+3*4'"""
    try:
        result = eval(expression)
        return f"计算结果: {result}"
    except Exception as e:
        return f"计算错误: {str(e)}"