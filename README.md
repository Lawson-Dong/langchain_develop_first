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
