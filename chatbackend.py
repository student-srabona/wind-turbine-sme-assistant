
from langchain_aws import ChatBedrockConverse
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.messages import SystemMessage


def nova_llm():
    llm=ChatBedrockConverse(
        model="amazon.nova-micro-v1:0",
            region_name="us-east-1",
            temperature=0.5,
    )
    
    

    return llm

    
def chat_client():
    llm=nova_llm()
    
    history=[SystemMessage(content="You are  a helpful assistant. Always use the previous conversation history to  answer the users' questions.If the user tells you a fact about themselves ,remembe it and use it later.")]
    
    print("Nova Chatbot")
    print("Type 'exit' to quit.\n")
    
    while True:
        question=input("You: ")
        if question.lower()=="exit":
             print("GoodBye")
             break
             
        history.append(HumanMessage(content=question))
        response=llm.invoke(history)

        print("Nova:",response.content)
        history.append(AIMessage(content=response.content))

if __name__=="__main__":     
    chat_client()
    
        
        
        
    
    


