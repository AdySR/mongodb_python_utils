from pymongo import *
from bson import ObjectId


def get_documents_by_ids(collection, document_ids):
    """
    Retrieve documents from MongoDB collection based on a list of document IDs.

    Parameters:
    - collection: MongoDB collection object
    - document_ids: List of document IDs to retrieve

    Returns:
    - List of documents matching the provided IDs
    """
    # Convert document IDs to ObjectId
    object_ids = [ObjectId(doc_id) for doc_id in document_ids]

    # Query documents based on ObjectIds
    query = {"_id": {"$in": object_ids}}
    result = collection.find(query)

    # Convert the result to a list and return
    return list(result)




user ='admin'
password = 'admin'

client = MongoClient(f"mongodb+srv://{(user)}:{(password)}@poccluster.sjsfbns.mongodb.net/?retryWrites=true&w=majority")
db = client["poc_db"]  # Replace with your actual database name
your_collection = db["employees"]  # Replace with your actual collection name

# List of document IDs to retrieve
document_ids_to_fetch = ["65beb6cf5784d6fed8e2f73e","65beb6cf5784d6fed8e2f73f","65beb6cf5784d6fed8e2f740"]

# Get documents based on the provided IDs
retrieved_documents = get_documents_by_ids(your_collection, document_ids_to_fetch)

count =0
for document in retrieved_documents:
    print(document)
    count=count+1


print(count)
