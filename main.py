from agents.my_agent import agent

# 主函数
def main():
    print("=" * 50)
    print("LangChain 智能体已启动（支持互联网访问）！")
    print("现在可以获取实时信息")
    print("输入 'quit' 退出")
    print("=" * 50)
    
    # 显示可用工具
    print("\n可用工具:")
    from agents.my_agent import tools
    for tool in tools:
        print(f"  • {tool.name}: {tool.description}")
    
    print("\n示例问题:")
    print("  'Google搜索Python官网'")
    print("  '获取GitHub主页内容'")
    print("  '计算2+3*4是多少'")
    print("  '翻转这个字符串: hello'\n")

    # 配置会话 ID（用于记忆）
    config = {"configurable": {"thread_id": "1"}}

    while True:
        user_input = input("\n你: ")
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("再见！")
            break

        try:
            # 调用智能体
            response = agent.invoke(
                {"messages": [("user", user_input)]},
                config=config
            )
            # 获取最后一条消息（智能体的回复）
            last_message = response["messages"][-1]
            print(f"\n智能体: {last_message.content}")
        except Exception as e:
            print(f"\n错误: {e}")

if __name__ == "__main__":
    main()
