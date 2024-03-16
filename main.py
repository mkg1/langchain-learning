from langchain.document_loaders import TextLoader
from dotenv import load_dotenv

load_dotenv()

# langchain includes various loaderes for different file types, including loading files from amazon s3 buckets
# langchain file loaders return a document with at least 2 properties: page_content & metadata

loader = TextLoader("facts.txt")
docs = loader.load()

print(docs)
