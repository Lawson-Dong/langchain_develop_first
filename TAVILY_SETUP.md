# Tavily搜索API配置指南

## 📝 概述

智能体已升级为使用 **Tavily搜索API** 来获取互联网信息。Tavily是专门为AI应用设计的搜索引擎，比传统爬虫更可靠。

## ✅ 快速配置步骤

### 第1步：获取Tavily API密钥

1. 访问 **https://tavily.com**
2. 点击 "Sign Up" 或 "Get Started"
3. 使用邮箱注册账户
4. 验证邮箱后登录
5. 进入API Dashboard
6. 复制你的 **API Key**

预计时间：2-3分钟

### 第2步：配置API密钥

编辑项目根目录的 `.env` 文件，找到这一行：

```env
TAVILY_API_KEY=your_tavily_api_key_here
```

替换为你的实际API密钥：

```env
TAVILY_API_KEY=tvly-xxxxxxxxxxxxxxxxxxxxxx
```

### 第3步：启动智能体

```bash
python main.py
```

现在你可以使用搜索功能了！

## 🔍 使用示例

### 搜索最新新闻
```
你: 搜索最新的AI人工智能发展趋势

智能体: [使用Tavily API搜索] → 返回最新信息
```

### 搜索网站信息
```
你: 搜索Python官方网站

智能体: [使用Tavily API] → 返回python.org和相关信息
```

### 查找特定内容
```
你: 搜索ChatGPT最新功能 2026

智能体: [使用Tavily] → 返回ChatGPT最近更新内容
```

## 🎯 Tavily API的优势

| 优势 | 说明 |
|------|------|
| **为AI优化** | 专门为AI应用设计，返回结构化数据 |
| **直接答案** | 提供可信的直接回答，不仅仅是链接 |
| **实时信息** | 获取最新、最热、最相关的信息 |
| **可靠性** | 企业级API，比爬虫更稳定 |
| **易整合** | Python库易用，与LangChain兼容 |
| **无需代理** | 不需要配置代理或反爬虫规避 |

## 📊 策略对比

### 旧策略（DDGS + Bing爬虫）
- ❌ 爬虫易被检测和阻止
- ❌ HTML结构频繁变化
- ❌ LLM不知道何时调用
- ✅ 不需要API密钥

### 新策略（Tavily API）
- ✅ API调用可靠稳定
- ✅ 返回结构化数据
- ✅ 易于集成和使用
- ✅ 为AI应用专门设计
- ⚠️ 需要API密钥

## ⚙️ 技术细节

### 使用的库
```python
from tavily import TavilyClient

client = TavilyClient(api_key="your_key")
response = client.search(
    query="search term",
    max_results=5,
    include_answer=True
)
```

### 返回数据格式
```python
{
    "answer": "直接的、经过验证的答案",
    "results": [
        {
            "title": "网页标题",
            "url": "https://example.com",
            "content": "网页摘要内容",
            "score": 0.95  # 相关性评分
        },
        # ... 更多结果
    ]
}
```

## 🐛 故障排查

### 错误：API密钥未配置
```
错误：未配置Tavily API密钥。请访问 https://tavily.com 获取API密钥
```

**解决方案**：
1. 检查 `.env` 文件中是否有 `TAVILY_API_KEY`
2. 确保不是 `your_tavily_api_key_here` 的占位符

### 错误：搜索失败
```
搜索失败: Invalid API key
```

**解决方案**：
1. 验证API密钥是否正确复制
2. 访问 https://tavily.com 确认密钥是否有效
3. 检查网络连接

### 错误：Tavily库未安装
```
错误：Tavily库未安装。请运行: pip install tavily-python
```

**解决方案**：
```bash
pip install tavily-python
```

## 📱 在其他项目中使用Tavily

如果你想在其他Python项目中使用Tavily：

```python
from tavily import TavilyClient
import os

# 从环境变量读取API密钥
api_key = os.getenv("TAVILY_API_KEY")
client = TavilyClient(api_key=api_key)

# 执行搜索
response = client.search(query="your query", max_results=5)

# 处理结果
for result in response["results"]:
    print(f"标题: {result['title']}")
    print(f"链接: {result['url']}")
    print(f"内容: {result['content']}\n")
```

## 🔗 相关链接

- **Tavily官网**：https://tavily.com
- **API文档**：https://tavily.com/api
- **Python库文档**：https://github.com/tavily-ai/tavily-python
- **定价页面**：https://tavily.com/pricing

## 💡 提示

1. **免费额度**：Tavily提供免费额度，足够开发使用
2. **计费模式**：按API调用次数计费
3. **速率限制**：免费用户可能有调用限制
4. **安全**：API密钥不要公开分享或提交到Git

## 📝 文件修改记录

- `pyproject.toml`：替换 `ddgs>=9.0.0` 为 `tavily-python>=0.7.0`
- `tools/web_tools.py`：使用TavilyClient替换DDGS和Bing爬虫
- `.env`：添加 `TAVILY_API_KEY` 配置

---

**下一步**：按照"快速配置步骤"完成API密钥设置，然后运行 `python main.py` 即可开始使用！
