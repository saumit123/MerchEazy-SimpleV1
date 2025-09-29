from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from pymongo import DESCENDING
from typing import Optional
import os
from dotenv import load_dotenv

# Load environment variables for MongoDB credentials
load_dotenv()

def get_mongo_collection(collection_name: str):
    """Establishes a connection to MongoDB and returns a collection."""
    try:
        # Get MongoDB URI from environment variables
        mongo_uri = os.getenv("MONGO_URI")
        if not mongo_uri:
            raise ValueError("MONGO_URI environment variable is not set.")

        client = MongoClient(mongo_uri)
        db = client[os.getenv("DB_NAME", "invoice_items")]
        collection = db[collection_name]
        return collection
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        return None

def save_grocery_list(grocery_list: dict):
    """Saves the structured grocery list (JSON) to a MongoDB collection."""
    collection = get_mongo_collection("grocery_lists")
    if collection is None:
        return

    try:
        # MongoDB is document-based, so you can directly insert the dictionary
        collection.insert_one(grocery_list)
        print("Successfully saved grocery list to MongoDB.")
    except Exception as e:
        print(f"Failed to save data to MongoDB: {e}")

def get_latest_grocery_list() -> Optional[dict]:
    """
    Fetches the most recently saved document from the grocery_lists collection.
    
    Returns:
        dict: The document data, or None if the collection is empty/unavailable.
    """
    collection = get_mongo_collection("grocery_lists")
    if collection is None:
        return None
    
    try:
        # Find the last document inserted by sorting by the MongoDB default _id field (which is time-based)
        latest_doc = collection.find_one(
            {}, 
            sort=[('_id', DESCENDING)]
        )
        return latest_doc
    except Exception as e:
        print(f"Error fetching latest data from MongoDB: {e}")
        return None


if __name__ == "__main__":
    print("--- Testing MongoDB Connection and Data Save ---")
    
    # Define some test data with the new 'qty_num' field
    test_data = {
        "items": [
            {
                "name": "apples", 
                "qty": "1 kg", 
                "qty_num": 1.0, 
                "category": "produce"
            },
            {
                "name": "milk", 
                "qty": "2 bottles", 
                "qty_num": 2.0, 
                "category": "dairy"
            },
        ],
        "source": "test_script"
    }

    # Call the save function with the test data
    save_grocery_list(test_data)

    print("--- Test complete. Check your MongoDB Atlas dashboard for the new data. ---")