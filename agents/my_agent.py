import os
from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from tools.math_tools import calculator
from tools.text_tools import get_text_length, reverse_string

load_dotenv()

# 初始化模型
llm = ChatDeepSeek(
    model="deepseek-chat",
    temperature=0,
    api_key=os.getenv("DEEPSEEK_API_KEY")
)

tools = [calculator, get_text_length, reverse_string]

# 创建记忆（可选）
memory = MemorySaver()

# 创建智能体（使用 langgraph）
agent = create_react_agent(
    model=llm,
    tools=tools,
    checkpointer=memory,  # 添加记忆功能
)