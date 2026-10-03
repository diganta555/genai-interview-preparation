# Optional: uv sync --extra frameworks. No API key required.
from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.types import interrupt, Command
class State(TypedDict, total=False):
    question: str
    approved: bool
    answer: str
def approval(state: State):
    approved = interrupt({'action':'answer fixture question','question':state['question']})
    return {'approved': bool(approved)}
def answer(state: State):
    return {'answer': 'Approved fixture response.' if state['approved'] else 'Declined.'}
builder = StateGraph(State)
builder.add_node('approval',approval)
builder.add_node('answer',answer)
builder.add_edge(START,'approval')
builder.add_edge('approval','answer')
builder.add_edge('answer',END)
graph = builder.compile(checkpointer=InMemorySaver())
if __name__ == '__main__':
    config = {'configurable':{'thread_id':'demo-thread'}}
    paused = graph.invoke({'question':'Refund period?'},config)
    print('Paused:',paused)
    print('Resumed:',graph.invoke(Command(resume=True),config))
