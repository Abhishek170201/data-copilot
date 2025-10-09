from interface import llmInterface
import logging

MEM_SIZE = 5

logger = logging.getLogger(__name__)
class msgManager:
    def __init__(self, system_prompt="You are a helpful assistant."):
        self.conversation = {}
        self.conversation["system"] = system_prompt
        self.conversation["summary"] = ""
        self.conversation["recent_messages"] = []
        # logger.info(f"Initialized conversation with: {self.conversation}")


    def contextUpdate(self):
        if(len(self.conversation["recent_messages"]) > 2 * MEM_SIZE):
            to_summarise = self.conversation["recent_messages"][:2]
            summary_msg = f"Summarise the following conversation between user and assistant in a concise manner, retaining important details:\n{to_summarise}"
            agent = llmInterface()
            summary = agent.query([
                {"role": "system", "content": "You are a summarizer assistant."},
                {"role": "user", "content": summary_msg}
            ])

            self.conversation["summary"] += summary + "\n"
            self.recent_messages = self.recent_messages[2:]

    def addMessage(self, role, content):
        self.conversation["recent_messages"].append({"role":role, "content":content})

    def createMessage(self, role, content):
        return {"role":role, "content":content}
    
    def agentPayload(self, user_input):
        messages = []
        
        messages.append(self.createMessage("system",self.conversation["system"]))

        if self.conversation["summary"]:
            messages.append(self.createMessage("system",f"Summary from the previous conversations given below:\n {self.conversation['summary']}"))

        
        messages.extend(self.conversation["recent_messages"])

        messages.append(self.createMessage("user", user_input))

        return messages
