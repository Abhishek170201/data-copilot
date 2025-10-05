import os
import pandas as pd

class DataLoader:
    """Minimal CSVLoader placeholder."""

    def __init__(self, path: str):
        self.path = path

    def fileTypeFinder(self):
        _, file_extension = os.path.splitext(self.path)
        return file_extension.lower()
    
    def load(self):
        fileType = self.fileTypeFinder()
        if fileType == ".csv":
            print(f"Loading CSV file from: {self.path}")
            df = pd.read_csv(self.path)
        elif fileType in [".xls", ".xlsx"]:
            print(f"Loading Excel file from: {self.path}")
            df = pd.read_excel(self.path)
        else:
            raise ValueError("Unsupported file type. Please provide a CSV or Excel file.")

        print("Data loaded successfully.")
        return df