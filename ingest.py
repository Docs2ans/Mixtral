from langchain.document_loaders import PDFMinerLoader 
from langchain.text_splitter import RecursiveCharacterTextSplitter 
from langchain.embeddings import SentenceTransformerEmbeddings 
from langchain.vectorstores import Chroma 
import os 
from constants import CHROMA_SETTINGS
from langchain.text_splitter import MarkdownHeaderTextSplitter
from langchain.document_loaders import UnstructuredMarkdownLoader

persist_directory = "db"

def main():
    document_list=[]
    for root, dirs, files in os.walk("docs"):
        for file in files:
            print(file)
            #Execute the following 2 lines if you want to remove .yaml files if present
            # if file.endswith(".yaml"):
            #       os.remove(os.path.join(root, file))
            if file.endswith(".md"):
                            print(file)
                            loader = UnstructuredMarkdownLoader(os.path.join(root, file))
                            document = loader.load()
                            document_list.append(document)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=500)
    texts=[]
    for i in range(len(document_list)):
          text = text_splitter.split_documents(documents=document_list[i])
          texts.append(text)
    #create embeddings here
    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    #create vector store here
    for j in texts:
          db = Chroma.from_documents(j, embeddings, persist_directory=persist_directory, client_settings=CHROMA_SETTINGS)
          db.persist()
          db=None 

if __name__ == "__main__":
    main()