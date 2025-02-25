import os
import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# MongoDB connection
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB")
COLLECTIONS = os.getenv("MONGO_COLLECTIONS").split(",")  # List of collection names
EXCEL_FILES = os.getenv("EXCEL_FILES").split(",")  # List of corresponding Excel file paths

# Ensure collections and files match
if len(COLLECTIONS) != len(EXCEL_FILES):
    raise ValueError("⚠️ Mismatch: The number of collections and Excel files must be the same.")

# Connect to MongoDB
try:
    client = MongoClient(MONGO_URI)
    db = client[MONGO_DB]
    print(f"✅ Connected to MongoDB database: {MONGO_DB}")
except Exception as e:
    print(f"❌ Error connecting to MongoDB: {e}")
    exit(1)

# Upload each Excel file to its corresponding collection
for collection_name, excel_file in zip(COLLECTIONS, EXCEL_FILES):
    try:
        # Read Excel file
        df = pd.read_excel(excel_file, dtype=str)  # Read as string to prevent data type issues
        data = df.to_dict(orient="records")  # Convert DataFrame to list of dictionaries

        if not data:
            print(f"⚠️ No data found in {excel_file}, skipping...")
            continue

        # Insert data into MongoDB
        collection = db[collection_name]
        collection.insert_many(data)
        print(f"🚀 Successfully inserted {len(data)} records into {collection_name} from {excel_file}")
    except Exception as e:
        print(f"❌ Error processing {excel_file}: {e}")

# Close MongoDB connection
client.close()
print("✅ All data uploaded successfully!")
