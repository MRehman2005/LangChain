from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

llm = HuggingFaceEndpoint(
    repo_id="MiniMaxAI/MiniMax-M2.5:novita",
    task="conversational",
    temperature=0.2
    
)

model = ChatHuggingFace(llm=llm)
inpt = input("User:")
result = model.invoke(inpt)
print(result.content)