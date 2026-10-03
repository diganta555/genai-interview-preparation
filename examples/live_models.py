"""Optional paid/network integration. Never invoked by offline tests.

Configure GENAI_MODEL and GENAI_PROVIDER, plus provider-specific credentials.
Install the corresponding LangChain provider package, then run this module.
"""
import os
from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage, HumanMessage

def create_model():
    return init_chat_model(os.environ['GENAI_MODEL'],
                           model_provider=os.environ['GENAI_PROVIDER'])
if __name__ == '__main__':
    model = create_model()
    response = model.invoke([
        SystemMessage(content='Summarize only the supplied evidence; use one sentence.'),
        HumanMessage(content='Evidence: retrieval adds source documents to model context.')])
    print(response.content)
    print(response.usage_metadata)
