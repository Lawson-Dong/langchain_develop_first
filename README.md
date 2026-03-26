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
项目定义了多个工具函数，按模块分类，使用 `@tool` 装饰器标记（适用于 LangChain 工具）：

**数学工具 (`tools/math_tools.py`)**:
- **`calculator(expression: str) -> str`**
  - 功能：计算数学表达式
  - 示例：`calculator("2+3*4")` 返回 `"计算结果: 14"`
  - 实现：使用 `eval()` 安全计算，支持加减乘除等运算

**文本工具 (`tools/text_tools.py`)**:
- **`get_text_length(text: str) -> str`**
  - 功能：获取文本字符长度
  - 示例：`get_text_length("hello")` 返回 `"文本长度: 5 个字符"`
  - 实现：使用 `len(text)` 计算字符数

- **`reverse_string(text: str) -> str`**
  - 功能：反转字符串
  - 示例：`reverse_string("abc")` 返回 `"反转结果: cba"`
  - 实现：使用切片 `text[::-1]` 反转

**文件工具 (`tools/file_tools.py`)**:
- **`read_file(path, encoding="utf-8") -> str`**: 读取文件内容
- **`write_file(path, content, encoding="utf-8", mode="w") -> None`**: 写入文件
- **`append_file(path, content, encoding="utf-8") -> None`**: 追加写文件
- **`list_dir(path) -> List[str]`**: 列出目录下文件
- **`ensure_dir(path) -> Path`**: 创建目录
- **`read_csv(path, encoding="utf-8") -> List[Dict]`**: 读取 CSV 为字典列表
- **`write_csv(path, rows, headers=None, encoding="utf-8") -> None`**: 写入 Dict 列表到 CSV
- **`read_json(path, encoding="utf-8") -> Any`**: 读取 JSON 文件
- **`write_json(path, data, indent=2, encoding="utf-8") -> None`**: 写入 JSON 文件

**网络工具 (`tools/web_tools.py`)**:
- **`http_get(url, params=None, headers=None, timeout=10) -> Response`**: 发送 GET 请求
- **`http_post(url, data=None, json_data=None, headers=None, timeout=10) -> Response`**: 发送 POST 请求
- **`fetch_html(url, headers=None, timeout=10) -> str`**: 获取页面 HTML 内容
- **`parse_html(html, parser="html.parser") -> BeautifulSoup`**: 解析 HTML
- **`parse_url(url) -> Dict`**: 解析 URL 各部分
- **`url_join(base, path) -> str`**: 拼接相对 URL

**数据工具 (`tools/data_tools.py`)**:
- **`df_from_csv(path, **kwargs) -> DataFrame`**: 从 CSV 创建 DataFrame
- **`df_to_csv(df, path, index=False, **kwargs) -> None`**: DataFrame 写入 CSV
- **`df_head(df, n=5) -> DataFrame`**: 返回前 n 行
- **`filter_df(df, condition) -> DataFrame`**: 按表达式过滤 DataFrame
- **`fillna(df, value=0) -> DataFrame`**: 填充缺失值
- **`array_stats(arr) -> Dict`**: 返回 NumPy 数组统计信息
- **`df_drop_columns(df, columns) -> DataFrame`**: 删除列

#### 3. 智能体创建
- 使用 `create_react_agent` 创建基于 LangGraph 的 ReAct 智能体
- 绑定工具列表：从 `tools` 包导入所有可用工具（目前包括数学、文本、文件、网络、数据处理工具）
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

## 项目文件结构与作用讲解

基于当前 `langchain/` 项目目录，以下是每个文件和目录的详细作用说明：

### 根目录文件

- **`.env`**  
  环境变量配置文件。存储敏感信息如 API 密钥（`DEEPSEEK_API_KEY`），避免硬编码在代码中。使用 `python-dotenv` 库加载。

- **`.gitignore`**  
  Git 忽略文件配置。指定哪些文件/目录不提交到版本控制，如 `__pycache__/`, `.venv`, 临时文件等，保持仓库清洁。

- **`.python-version`**  
  Python 版本指定文件（通常用于 pyenv 或类似工具），确保项目使用特定 Python 版本。

- **`main.py`**  
  项目主入口文件。启动 LangChain 智能体交互程序，导入 `agents.my_agent` 并运行循环对话。

- **`pyproject.toml`**  
  Python 项目配置文件。定义项目元数据、依赖、构建工具等（替代 `setup.py`），支持现代 Python 包管理。

- **`README.md`**  
  项目说明文档。包含安装、运行、使用指南、目录结构、API 说明等，帮助用户快速上手。

- **`uv.lock`**  
  依赖锁定文件。由 `uv` 包管理器生成，确保依赖版本一致性，避免版本冲突。

### 目录

- **`.git/`**  
  Git 版本控制目录。存储仓库历史、分支、提交等信息。

- **`.venv/`**  
  Python 虚拟环境目录。隔离项目依赖，避免全局污染。

- **`agents/`**  
  智能体模块目录。封装 LangChain 智能体的定义、配置和工具绑定。

  - **`__init__.py`**  
    包初始化文件，使 `agents` 成为 Python 包。

  - **`my_agent.py`**  
    智能体核心文件。定义 LangGraph 智能体，加载 LLM（DeepSeek）、工具，并配置记忆（MemorySaver）。

- **`examples/`**  
  示例代码目录。提供使用项目功能的演示脚本。

  - **`run_agent.py`**  
    运行示例。展示如何调用智能体、执行工具调用，并进入交互模式。

- **`tools/`**  
  工具函数模块目录。封装各种实用工具，按功能分类。

  - **`__init__.py`**  
    包初始化文件。统一导出所有工具函数，方便 `from tools import calculator` 等导入。

  - **`data_tools.py`**  
    数据处理工具。包含 Pandas DataFrame 操作、NumPy 数组统计等函数。

  - **`file_tools.py`**  
    文件操作工具。提供文件读写、目录管理、CSV/JSON 处理等功能。

  - **`math_tools.py`**  
    数学计算工具。目前包含 `calculator` 函数，用于表达式计算。

  - **`text_tools.py`**  
    文本处理工具。包含文本长度获取、字符串反转等函数。

  - **`web_tools.py`**  
    网络相关工具。提供 HTTP 请求、HTML 解析、URL 处理等功能。

### 其他

- **`__pycache__/`**（在各包目录下）  
  Python 字节码缓存目录。自动生成，提高模块加载速度，可忽略。

这个项目采用模块化设计：`tools/` 提供基础工具，`agents/` 构建智能体，`main.py` 作为入口，`examples/` 演示用法。适合扩展更多工具或智能体配置。
