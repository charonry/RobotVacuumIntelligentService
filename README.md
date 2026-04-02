# 智扫通机器人智能客服Demo

基于 ReAct 架构的扫地机器人智能客服系统，支持 RAG 检索增强、工具调用和个性化报告生成。

## 功能特性

- **智能对话**：基于 ReAct 架构，具备思考-行动-观察的自主决策能力
- **RAG 检索**：从向量数据库检索扫地机器人专业知识、使用指南和故障处理方案
- **工具调用**：集成天气查询、用户定位、使用记录获取等多种工具
- **报告生成**：支持生成个性化的扫地机器人使用报告
- **流式响应**：支持 SSE 流式输出，提升用户体验

## 技术栈

- **框架**：LangChain + LangGraph
- **模型**：通义千问 (Qwen3-Max)
- **向量数据库**：ChromaDB
- **嵌入模型**：DashScope Text-Embedding-V4
- **前端**：Streamlit
- **配置管理**：YAML

## 项目结构

```
.
├── agent/                  # Agent 核心模块
│   ├── react_agent.py     # ReAct Agent 实现
│   └── tools/             # 工具集
│       ├── agent_tools.py # 工具函数定义
│       └── middleware.py  # 中间件（监控、日志、提示词切换）
├── config/                # 配置文件
│   ├── agent.yml          # Agent 配置
│   ├── rag.yml            # RAG 模型配置
│   ├── chroma.yml         # 向量数据库配置
│   └── prompts.yml        # 提示词路径配置
├── data/                  # 数据目录
├── db/                    # 数据库/向量存储
├── logs/                  # 日志目录
├── model/                 # 模型工厂
│   └── factory.py         # 模型创建工厂
├── prompts/               # 提示词模板
│   ├── main_prompt.txt    # 主提示词
│   ├── rag_summarize.txt  # RAG 摘要提示词
│   └── report_prompt.txt  # 报告生成提示词
├── rag/                   # RAG 模块
│   ├── rag_service.py     # RAG 服务
│   └── vector_store.py    # 向量存储管理
├── utils/                 # 工具类
│   ├── config_handler.py  # 配置加载
│   ├── file_handler.py    # 文件处理
│   ├── logger_handler.py  # 日志管理
│   ├── path_tool.py       # 路径工具
│   └── prompt_loader.py   # 提示词加载
├── app.py                 # Streamlit 前端入口
└── demo.ipynb             # 演示 Notebook
```

## 快速开始

### 1. 环境要求

- Python 3.10+
- 阿里云 DashScope API Key

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 配置环境变量

```bash
export DASHSCOPE_API_KEY="your-api-key"
```

### 4. 启动服务

```bash
# 启动 Web 界面
python -m streamlit run app.py
```

## 核心组件说明

### ReAct Agent

位于 `agent/react_agent.py`，是系统的核心决策引擎：

- 支持多轮工具调用
- 内置中间件机制（监控、日志、提示词切换）
- 流式响应输出

### 工具集

| 工具名 | 功能描述 |
|--------|----------|
| `rag_summarize` | 从向量库检索扫地机器人专业知识 |
| `get_weather` | 获取指定城市天气信息 |
| `get_user_location` | 获取用户所在城市 |
| `get_user_id` | 获取当前用户 ID |
| `get_current_month` | 获取当前月份 |
| `fetch_external_data` | 获取用户历史使用记录 |
| `fill_context_for_report` | 触发报告生成上下文注入 |

### RAG 检索

位于 `rag/rag_service.py`，实现基于向量数据库的检索增强：

- 使用 ChromaDB 存储文档向量
- 支持语义相似度检索
- 自动摘要和答案生成

## 配置说明

### RAG 配置 (`config/rag.yml`)

```yaml
chat_model_name: qwen3-max          # 聊天模型名称
embedding_model_name: text-embedding-v4  # 嵌入模型名称
```

### ChromaDB 配置 (`config/chroma.yml`)

```yaml
collection_name: robot_docs         # 集合名称
persist_directory: ./db/chroma      # 持久化目录
embedding_model: text-embedding-v4  # 嵌入模型
```

## 使用示例

### 基本对话

```python
from agent.react_agent import ReActAgent

agent = ReActAgent()
for chunk in agent.execute_stream("小户型适合什么扫地机器人？"):
    print(chunk, end="", flush=True)
```

### 生成使用报告

```python
from agent.react_agent import ReActAgent

agent = ReActAgent()
for chunk in agent.execute_stream("给我生成我的使用报告"):
    print(chunk, end="", flush=True)
```


