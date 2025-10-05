import argparse
import logging
from utils import DataLoader
from eda import EDA
from messageManager import msgManager
from interface import llmInterface


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")

logger = logging.getLogger(__name__)

class DataCopilotCLI:

    def __init__(self, path: str = "../data/sample.csv"):
        self.path = path

    def run(self):
        parser = argparse.ArgumentParser(description="Data Copilot CLI")
        parser.add_argument(
            "--path", type=str, default=self.path, help="Path to the CSV file"
        )
        args = parser.parse_args()
        logger.info(f"Loading data from: {args.path}")

        data_loader = DataLoader(args.path)
        df = data_loader.load()
        logger.info(f"Data saved in dataframe with shape: {df.shape}")

        eda = EDA(df)
        df_details = eda.basicEDA()
        logger.info("Basic EDA completed.")

        eda.generateEDAReport()

        system_prompt = f'''
        You are DataCopilot — an intelligent data science assistant that helps analyze datasets and answer analytical questions using statistical reasoning and programming.

        Below is a summary of the dataset currently in context in json format:

        {df_details}

        ======================
        🧠 YOUR ROLE & RULES
        ======================
        1. You have access only to the above dataset summary.
        2. You must answer user questions **strictly based on the data** described above.
        3. When applicable, provide the **Python (pandas) code** required to compute or verify the answer.
        4. When describing insights, use **clear and concise English** explanations.
        5. Always refer to column names **exactly as they appear** in the dataset.
        6. If a question cannot be answered based on the available summary, respond:
        "I don't have enough detail in the provided dataset summary to answer this precisely."
        7. Do not hallucinate values or assume missing data.
        8. When performing reasoning, explicitly describe your logic.
        9. For comparison or aggregation questions, specify what operation would be used (e.g., mean, sum, groupby, count).
        10. Always aim to be **educational, accurate, and transparent** in your answers.

        ======================
        💡 OUTPUT FORMATS
        ======================
        - For analytical questions → provide concise English + Python code snippet.
        - For descriptive questions → provide clear insights.
        - For follow-up questions → maintain logical continuity with previous responses.

        Now wait for the user's question.
        '''

        manager = msgManager(system_prompt)

        user_input1 = "Give a short summary of the dataset"

        manager.contextUpdate()
        messages = manager.agentPayload(user_input1)

        agent = llmInterface()

        reply = agent.query(messages)
        
        logger.info(f"Reply from the agent: {reply}")

        manager.addMessage("user",user_input1)
        manager.addMessage("assistant",reply)


        