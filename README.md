# LangChain 工程示例

## 目录结构

```
langchain/
├── .env
├── .gitignore
├── pyproject.toml
├── uv.lock
├── main.py                    # 程序入口
├── tools/                     # 工具函数模块
│   ├── __init__.py
│   ├── math_tools.py         # 数学计算工具
│   ├── text_tools.py         # 文本处理工具
│   ├── file_tools.py         # 文件操作工具
│   ├── web_tools.py          # 网络相关工具
│   └── data_tools.py         # 数据处理工具
├── agents/                   # 智能体定义与配置
│   ├── __init__.py
│   └── my_agent.py           # 智能体构建与工具绑定
└── examples/                 # 运行示例
    └── run_agent.py
```

## 依赖安装

建议使用虚拟环境：

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

如果没有 `requirements.txt`，安装基础依赖：

```bash
pip install python-dotenv langchain-deepseek langgraph requests beautifulsoup4 pandas numpy
```

## 配置

在根目录创建 `.env`：

```
DEEPSEEK_API_KEY=your_api_key_here
```

## 运行主程序

```bash
python main.py
```

## 核心功能说明

### agent_langgraph.py（原始文件）

`agent_langgraph.py` 是项目的核心智能体实现文件，基于 LangChain 和 LangGraph 构建的 AI 智能体。以下是其主要功能：

#### 1. 模型初始化
- 使用 `ChatDeepSeek` 作为底层语言模型
- 配置模型参数：`model="deepseek-chat"`, `temperature=0`
- 从环境变量加载 API 密钥：`DEEPSEEK_API_KEY`

#### 2. 工具定义
文件定义了三个核心工具函数，使用 `@tool` 装饰器标记：

- **`calculator(expression: str) -> str`**
  - 功能：计算数学表达式
  - 示例：`calculator("2+3*4")` 返回 `"计算结果: 14"`
  - 实现：使用 `eval()` 安全计算，支持加减乘除等运算

- **`get_text_length(text: str) -> str`**
  - 功能：获取文本字符长度
  - 示例：`get_text_length("hello")` 返回 `"文本长度: 5 个字符"`
  - 实现：使用 `len(text)` 计算字符数

- **`reverse_string(text: str) -> str`**
  - 功能：反转字符串
  - 示例：`reverse_string("abc")` 返回 `"反转结果: cba"`
  - 实现：使用切片 `text[::-1]` 反转

#### 3. 智能体创建
- 使用 `create_react_agent` 创建基于 LangGraph 的 ReAct 智能体
- 绑定工具列表：`tools = [calculator, get_text_length, reverse_string]`
- 添加记忆功能：`MemorySaver()` 用于保持对话上下文

#### 4. 交互界面
- 提供命令行交互界面
- 支持多轮对话，智能体会根据用户输入调用相应工具
- 会话配置：`{"configurable": {"thread_id": "1"}}` 用于记忆管理
- 退出命令：输入 `quit`, `exit` 或 `q` 结束程序

#### 5. 错误处理
- 捕获工具调用和智能体执行中的异常
- 输出错误信息，帮助调试

### 工具调用流程
1. 用户输入查询
2. 智能体分析查询，决定是否需要调用工具
3. 如果需要，执行相应工具函数
4. 将工具结果结合上下文生成最终回复
5. 输出回复，并保持记忆用于后续对话

## tools 模块说明

- `tools/math_tools.py`
  - `calculator(expression)`
- `tools/text_tools.py`
  - `get_text_length(text)`
  - `reverse_string(text)`
- `tools/file_tools.py`
  - `read_file`, `write_file`, `append_file`, `list_dir`, `ensure_dir`, `read_csv`, `write_csv`, `read_json`, `write_json`
- `tools/web_tools.py`
  - `http_get`, `http_post`, `fetch_html`, `parse_html`, `parse_url`, `url_join`
- `tools/data_tools.py`
  - `df_from_csv`, `df_to_csv`, `df_head`, `filter_df`, `fillna`, `array_stats`, `df_drop_columns`

## agents 模块说明

- `agents/my_agent.py`
  - 创建基于LangGraph的 `agent`，可携带记忆 `MemorySaver`
  - 加载 `tools` 中所有工具

## 示例

`examples/run_agent.py` 里展示了交互模式与工具调用方式。

---

上手后，如需扩展：

- `agents/my_agent.py` 添加更多外部工具或更改 LLM Model 配置
- `tools/*.py` 继续补充 `PDF`, `语义搜索`, `数据库` 等工具
