from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

llm =HuggingFaceEndpoint(
    repo_id = "MiniMaxAI/MiniMax-M2.5:novita",
    task = "text-generation"
    
)
model = ChatHuggingFace(llm=llm)
# 1st prompt templete -> detail report
template1 = PromptTemplate(
    template='Write a detail report on black {topic}',
    input_variable = ['topic']
)

# wnd prompt template -> summary
template2 = PromptTemplate(
    template='write 5 lines summary on the following text. /n {tex}',
    input_variables=['text']
)
parser = StrOutputParser()
chain  = template1 | model | parser | template2 | model | parser
result = chain.invoke({'topic':'black hole'})
print(result)
