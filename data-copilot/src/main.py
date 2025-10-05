import argparse
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")

logger = logging.getLogger(__name__)

class DataCopilotCLI:
    """Minimal CLI class placeholder."""

    def __init__(self, path: str = "../data/sample.csv"):
        self.path = path



    def run(self):
        parser = argparse.ArgumentParser(description="Data Copilot CLI")
        parser.add_argument(
            "--path", type=str, default=self.path, help="Path to the CSV file"
        )
        args = parser.parse_args()
        logger.info(f"Loading data from: {args.path}")