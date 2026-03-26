# 快速开始指南

## 智能体互联网能力已启用 ✅

### 快速启动
```bash
python main.py
```

### 可用工具

#### 网络工具（新增）
1. **search_google**: 搜索互联网
   ```
   例: "搜索最新的AI新闻"
   例: "查找Python官方网站信息"
   ```

2. **fetch_webpage_content**: 获取网页内容
   ```
   例: "获取GitHub主页的内容"
   例: "抓取CNN首页的文章"
   ```

3. **extract_website_info**: 提取网站信息（支持关键词过滤）
   ```
   例: "从Wikipedia提取关于Python的信息"
   例: "从Tesla官网提取产品信息，关键词: 电动汽车, 技术"
   ```

#### 本地工具
4. **calculator**: 数学计算
   ```
   例: "计算 100 * 0.15"
   例: "365 * 24 = ?"
   ```

5. **get_text_length**: 文本长度
   ```
   例: "这句话有多少个字符"
   ```

6. **reverse_string**: 反转文本
   ```
   例: "反转 'hello'"
   ```

## 使用示例

### 例1: 获取实时信息
**用户**: 搜索最新的Python 3.14版本发布信息  
**智能体**: [使用search_google搜索] → 返回最新信息

### 例2: 网站内容分析  
**用户**: 从GitHub Python主题页面提取热门项目  
**智能体**: [使用fetch_webpage_content] → 提取和分析内容

### 例3: 综合应用
**用户**: 搜索2026年全球GDP数据，然后帮我计算日均增长  
**智能体**:
1. [使用search_google找到数据]
2. [使用calculator计算: 总额/365]
3. 返回结果

## 常见问题

**Q: 网络请求很慢？**  
A: 网络请求需要5-30秒，这是正常的。请耐心等待。

**Q: 某些网站无法访问？**  
A: 可能是网站的反爬虫机制。可以尝试其他网站。

**Q: 如何获得最佳搜索结果？**  
A: 使用具体的关键词，避免模糊表述。

## 环境要求

- Python 3.14+
- requests 2.32.0+
- beautifulsoup4 4.14.0+
- 稳定的网络连接

## 文件结构

```
langchain/
├── main.py                 # 主程序
├── agents/
│   └── my_agent.py        # 智能体核心（已启用网络工具）
├── tools/
│   ├── math_tools.py      # 数学工具
│   ├── text_tools.py      # 文本工具
│   ├── web_tools.py       # 网络工具（新增3个工具）
│   └── ...
├── examples/
│   └── web_agent_demo.py  # 网络功能演示脚本
├── INTERNET_FEATURES.md   # 详细功能文档
└── pyproject.toml         # 项目配置
```

## 功能验证

运行以下命令验证智能体已正确配置：

```bash
python -c "from agents.my_agent import tools; print([t.name for t in tools])"
```

预期输出：
```
['calculator', 'get_text_length', 'reverse_string', 'fetch_webpage_content', 'search_google', 'extract_website_info']
```

---

**状态**: ✅ 已启用所有功能  
**最后更新**: 2026年3月26日
