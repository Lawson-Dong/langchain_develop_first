"""
展示智能体的网络访问能力
"""
import sys
sys.path.insert(0, '.')

from agents.my_agent import agent

def main():
    print("=" * 60)
    print("LangChain 智能体 - 网络访问演示")
    print("=" * 60)
    print("\n智能体现在可以:")
    print("  ✓ 搜索最新信息（Google搜索）")
    print("  ✓ 获取网页内容")
    print("  ✓ 提取网站信息")
    print("  ✓ 执行本地计算")
    print("  ✓ 处理文本操作")
    print("\n输入 'quit' 退出\n")
    print("=" * 60 + "\n")
    
    # 配置会话 ID（用于记忆）
    config = {"configurable": {"thread_id": "web_demo"}}
    
    # 演示问题列表
    demo_queries = [
        "请从百度首页提取最新的新闻标题",
        "搜索Python最新版本信息",
        "计算: 2 + 3 * 4",
        "获取GitHub的主页内容并提取其中关于功能的信息"
    ]
    
    print("自动运行演示查询...")
    for i, query in enumerate(demo_queries[:2], 1):  # 运行前2个演示
        print(f"\n【演示 {i}】")
        print(f"问题: {query}")
        print("-" * 60)
        
        try:
            response = agent.invoke(
                {"messages": [("user", query)]},
                config=config
            )
            last_message = response["messages"][-1]
            content = str(last_message.content)[:500]  # 限制显示长度
            print(f"智能体: {content}...")
        except Exception as e:
            print(f"错误: {e}")
    
    # 交互模式
    print("\n" + "=" * 60)
    print("进入交互模式（输入问题与智能体对话）")
    print("=" * 60 + "\n")
    
    while True:
        user_input = input("你: ").strip()
        if user_input.lower() in ['quit', 'exit', 'q', '退出']:
            print("再见！")
            break
        
        if not user_input:
            continue
        
        try:
            response = agent.invoke(
                {"messages": [("user", user_input)]},
                config=config
            )
            last_message = response["messages"][-1]
            print(f"\n智能体: {last_message.content}\n")
        except Exception as e:
            print(f"\n错误: {e}\n")

if __name__ == "__main__":
    main()
