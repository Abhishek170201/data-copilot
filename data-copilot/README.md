# data-copilot

DataCopilot: AI-Powered Data Analyst Assistant

Description:
DataCopilot is an intelligent AI assistant that allows users to interact with datasets naturally — just like consulting a human data analyst. By combining Python, Pandas, and large language models (LLMs), DataCopilot can summarize datasets, answer complex analytical questions, generate insights, and even suggest visualizations — all through natural language prompts.

Users can upload datasets (CSV, Excel, or Google Sheets), and DataCopilot automatically performs exploratory data analysis (EDA) to generate a structured summary of the data. This summary is then used as context for the LLM to provide accurate, insightful, and data-driven responses.

Key Features:

Dynamic Dataset Interaction: Upload any dataset and ask questions in plain English.

Exploratory Data Analysis (EDA): Automatically summarizes columns, data types, missing values, numeric statistics, and categorical distributions.

Natural Language Queries: Users can ask complex questions like:

“Which regions had the highest revenue growth last quarter?”

“Find anomalies in transaction volume and explain possible causes.”

(IN PROGRESS)
RAG (Retrieval-Augmented Generation): The AI decides when to query the dataset and retrieves relevant information before answering, reducing hallucinations.

Agentic Behavior: The model can decide whether to run queries, summarize data, or generate plots, enabling intelligent decision-making.

Modular Design: Clear separation between data ingestion, EDA, LLM interaction, and visualization tools.

Optional Visualization: Generate plots for trends, distributions, or correlations using Python libraries.

Local & Cloud-Compatible: Supports running LLMs locally (Ollama, Gemma3) or via cloud APIs (OpenAI, LlamaIndex, LangChain).

Design:
flowchart TD
    A[User Interface] <--> B[Chat Manager / Conversation Layer] <--> C[Agent / RAG Layer]
    C --> D[LLM Integration]
    D --> E[Data / Tools Layer]


Usage

Start chat:
1. Place the dataset (CSV/Excel) in the data folder
2. Run the following cmd to trigger the chat
    python src/main.py  --path data/sample.csv
