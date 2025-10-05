import pandas as pd
from ydata_profiling import ProfileReport
import os
import logging

logger = logging.getLogger(__name__)

class EDA:
    """Minimal EDA class placeholder."""

    def __init__(self, df=None):
        self.df = df

    def basicEDA(self):
        details = {}
        details["row"] = self.df.shape[0]
        details["column"] = self.df.shape[1]
        details["summary"] = {}
        details["summary"]["mean"] = self.df.describe().iloc["mean"].to_dict()
        details["summary"]["median"] = self.df.descirbe().iloc["50%"].to_dict()
        details["dataTypes"] = {}
        details["dataTypes"]["numeric"] = self.df.select_dtypes(include=["number"]).columns.tolist()
        details["dataTypes"]["categorical"] = self.df.select_dtypes(include=["object"]).columns.tolist()
        details["missingValues"] = ((self.df.isnull().sum()/len(self.df))*100).to_dict()

        return details
    
    def generateEDAReport(self, output_file="../reports/eda_report.html"):
        os.makedirs(os.path.dirname(output_file),exist_ok=True)
        report = ProfileReport(self.df, title="EDA Report", explorative=True)
        report.to_file(output_file)
        logger.info(f"EDA report generated and saved to {output_file}")