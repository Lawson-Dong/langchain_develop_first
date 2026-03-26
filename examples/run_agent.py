import os
from dotenv import load_dotenv
from agents.my_agent import agent

load_dotenv()

print("示例：智能体工具测试")

# 测试 calculator
resp = agent.invoke({"messages": [("user", "请计算 100 / 4")]} )
print("calculator response:", resp)

# 纯说明：在 agent 中可用已注册工具
# 1) calculator
# 2) get_text_length
# 3) reverse_string
#
# 您可以从此处打开交互会话：
while True:
    query = input("你: ")
    if query.strip().lower() in ["quit", "exit", "q"]:
        print("结束")
        break
    result = agent.invoke({"messages": [("user", query)]})
    print("智能体:", result["messages"][-1].content)
