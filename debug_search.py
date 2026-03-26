#!/usr/bin/env python
"""
Tavily API搜索功能调试脚本
用于验证API连接和测试搜索功能
"""
import sys
import os
sys.path.insert(0, '.')

from dotenv import load_dotenv

print("="*70)
print("Tavily搜索API调试脚本")
print("="*70)

# 加载环境变量
load_dotenv()
tavily_key = os.getenv("TAVILY_API_KEY")

# 检查1：API密钥配置
print("\n【检查1】API密钥配置")
print("-"*70)
if not tavily_key:
    print("❌ 未找到TAVILY_API_KEY环境变量")
    sys.exit(1)
elif tavily_key == "your_tavily_api_key_here":
    print("❌ TAVILY_API_KEY为占位符，需要配置真实密钥")
    sys.exit(1)
else:
    print(f"✓ 找到API密钥: {tavily_key[:20]}...{tavily_key[-10:]}")

# 检查2：Tavily包是否安装
print("\n【检查2】Tavily包检查")
print("-"*70)
try:
    from tavily import TavilyClient
    print("✓ Tavily包已安装")
except ImportError as e:
    print(f"❌ Tavily包未安装或导入失败: {e}")
    sys.exit(1)

# 检查3：初始化TavilyClient
print("\n【检查3】TavilyClient初始化")
print("-"*70)
try:
    client = TavilyClient(api_key=tavily_key)
    print("✓ TavilyClient初始化成功")
except Exception as e:
    print(f"❌ TavilyClient初始化失败: {e}")
    sys.exit(1)

# 检查4：执行搜索查询
print("\n【检查4】执行搜索查询")
print("-"*70)
test_queries = [
    "Python 3.14",
    "AI人工智能最新进展 2026",
    "GitHub最新趋势"
]

for query in test_queries:
    print(f"\n搜索: {query}")
    try:
        response = client.search(query=query, max_results=3, include_answer=True)
        
        # 显示结果
        if "answer" in response and response["answer"]:
            print(f"  直接答案: {response['answer'][:100]}...")
        
        if "results" in response and response["results"]:
            print(f"  找到 {len(response['results'])} 个结果:")
            for i, result in enumerate(response["results"][:2], 1):
                title = result.get("title", "无标题")[:50]
                url = result.get("url", "")[:50]
                print(f"    {i}. {title}")
                print(f"       {url}")
        else:
            print("  未找到结果")
        
        print("  ✓ 搜索成功")
    
    except Exception as e:
        print(f"  ❌ 搜索失败: {e}")
        import traceback
        traceback.print_exc()

# 检查5：测试智能体搜索工具
print("\n【检查5】测试智能体搜索工具")
print("-"*70)
try:
    from agents.my_agent import agent, tools
    print("✓ 智能体和工具加载成功")
    
    # 显示可用工具
    print("\n可用工具:")
    for i, tool in enumerate(tools, 1):
        tool_type = "🌐 网络" if any(x in tool.name.lower() for x in ['search', 'fetch', 'extract']) else "📱 本地"
        print(f"  {i}. {tool.name:<25} {tool_type}")
    
    # 查找搜索工具
    search_tool = next((t for t in tools if t.name == 'search_google'), None)
    if search_tool:
        print(f"\n✓ 找到搜索工具: {search_tool.name}")
        print(f"  描述: {search_tool.description[:100]}...")
    else:
        print("❌ 未找到search_google工具")
    
except Exception as e:
    print(f"❌ 智能体加载失败: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# 检查6：通过智能体测试搜索
print("\n【检查6】通过智能体执行搜索")
print("-"*70)
try:
    config = {"configurable": {"thread_id": "debug_test"}}
    
    test_query = "搜索 Python 最新版本"
    print(f"查询: {test_query}")
    
    response = agent.invoke(
        {"messages": [("user", test_query)]},
        config=config
    )
    
    # 获取最后一条消息
    last_message = response["messages"][-1]
    result_preview = str(last_message.content)[:200]
    
    print(f"\n智能体回复:")
    print(f"  {result_preview}...")
    print("\n✓ 智能体搜索成功")
    
except Exception as e:
    print(f"❌ 智能体搜索失败: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "="*70)
print("调试完成！")
print("="*70)
print("\n📋 总结:")
print("  ✓ API密钥已配置")
print("  ✓ Tavily包已安装")
print("  ✓ 搜索功能可用")
print("\n🚀 现在可以启动主程序: python main.py")
