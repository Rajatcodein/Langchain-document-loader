from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.output_parsers import StrOutputParser

loader = PyPDFLoader('dl-curriculum.pdf')

docs = loader.load()
parser = StrOutputParser()

splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0,
    separator=''
)

result = splitter.split_documents(docs) 

#print(parser.invoke(result))
print(result)