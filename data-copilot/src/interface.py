import requests
import json
import logging

logger = logging.getLogger(__name__)

class llmInterface:

    def __init__(self, model="gemma3:1b"):
        self.model = model

    def query(self, messages):
        response = requests.post(
            "http://127.0.0.1:11434/api/chat",
            json={"model": self.model, "messages": messages}
        )

        logger.info(f"Received response code :{response.status_code}")
        if response.status_code != 200:
            raise Exception(f"Request failed with status code {response.status_code} : {response.text}")
        
        return self.extractReply(response)  
    
    def extractReply(self, response):
        reply = ""
        for line in response.iter_lines():
            obj = json.loads(line)
            reply += obj["message"]["content"]

        return reply