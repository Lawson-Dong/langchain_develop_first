import os
from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from tools.math_tools import calculator
from tools.text_tools import get_text_length, reverse_string
from tools.web_tools import fetch_webpage_content, search_google, extract_website_info

load_dotenv()

# 初始化模型
llm = ChatDeepSeek(
    model="deepseek-chat",
    temperature=0,
    api_key=os.getenv("DEEPSEEK_API_KEY")
)

# 添加所有工具，包括网络工具以获取实时信息
tools = [
    calculator,
    get_text_length,
    reverse_string,
    fetch_webpage_content,  # 获取网页内容
    search_google,          # 谷歌搜索
    extract_website_info,   # 提取网站信息
]

# 创建记忆（可选）
memory = MemorySaver()

# 创建智能体（使用 langgraph）
agent = create_react_agent(
    model=llm,
    tools=tools,
    checkpointer=memory,  # 添加记忆功能
)