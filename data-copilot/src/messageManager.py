MEM_SIZE = 5

class msgManager:
    def __init__(self, system_prompt="You are a helpful assistant."):
        self.conversation = {}
        self.conversation["system"] = system_prompt


    def contextUpdate(self):
        if(len(self.recent_messages) > 2 * MEM_SIZE):
            to_summarise = self.recent_messages[:2]
            summary_msg = ""
