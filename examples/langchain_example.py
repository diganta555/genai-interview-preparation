# Optional: uv sync --extra frameworks
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.language_models.fake_chat_models import FakeListChatModel
from langchain_core.output_parsers import StrOutputParser
prompt = ChatPromptTemplate.from_messages([
    ('system','Summarize supported evidence. Say unknown if missing.'),
    ('human','Question: {question}\nEvidence: {evidence}')])
model = FakeListChatModel(responses=['Fixture answer: refunds within 14 days.'])
chain = prompt | model | StrOutputParser()
if __name__ == '__main__':
    print(chain.invoke({'question':'Refund period?', 'evidence':'14 days.'}))
    print('The fake model is a protocol test, not a quality demonstration.')
