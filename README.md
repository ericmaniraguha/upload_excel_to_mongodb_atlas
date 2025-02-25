# 🗂️ MongoDB Excel Uploader

A Python script to dynamically upload multiple Excel files with varying columns to **MongoDB Atlas**. Uses environment variables for secure configuration.

---

## 🌟 Features
- ✅ **Multi-file Support**: Upload multiple Excel files to different collections
- ✅ **Dynamic Schema Handling**: Automatically adapts to varying Excel column structures
- ✅ **Secure Configuration**: Uses `.env` file for MongoDB credentials
- ✅ **Error Handling**: Robust validation for missing files/credentials
- ✅ **Data Type Conversion**: Handles Excel dates/numbers → MongoDB compatible formats

---

## ⚙️ Setup

### **1️⃣ Prerequisites**
- Python 3.8+
- MongoDB Atlas cluster ([setup guide](https://www.mongodb.com/docs/atlas/getting-started/))

### **2️⃣ Install Dependencies**
```bash
pip install pandas pymongo python-dotenv openpyxl
```
### **3️⃣ Configuration**

Create `.env file`:

### **MongoDB Atlas Connection**
`MONGO_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net
MONGO_DB=your_database_name`

### Collections & Files Mapping (comma-separated)
`MONGO_COLLECTIONS=users,products
EXCEL_FILES=./data/users.xlsx,./data/products.xlsx`

Place Excel `files in /data directory (or modify paths in .env)`

### **🚀 Usage**
`python upload_multiple_excels.py`

### **Sample Output:**

✅ Successfully connected to MongoDB Atlas!
📁 Processing 2 file(s)...

📄 users.xlsx → Collection 'users'
   ✔️ Inserted 150 documents
   
📄 products.xlsx → Collection 'products' 
   ✔️ Inserted 857 documents

🎉 All files uploaded successfully!

### **📂 Project Structure**
MongoDB-Excel-Uploader/
├── data/                   # Excel files directory
│   ├── users.xlsx
│   └── products.xlsx
├── upload_multiple_excels.py  # Main script
├── .env                    # Environment variables
└── README.md               # This documentation

### **🛠️ Troubleshooting**
#### **🔗 Connection Issues**
##### **Verify MongoDB `URI format:`*

`mongodb+srv://<USERNAME>:<PASSWORD>@cluster-name.mongodb.net`
`Whitelist IP in Atlas → Network Access`

##### **📄 File Not Found**

###### Check file paths
`ls ./data/users.xlsx ./data/products.xlsx`

#### 🐍 Python Errors

#### Ensure all dependencies are installed
`pip install -r requirements.txt`

### **📜 License**
MIT License - Modify and use freely. Attribution appreciated!
