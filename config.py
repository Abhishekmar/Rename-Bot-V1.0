import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "21414727")

API_HASH = os.environ.get("API_HASH", "b4135f6b8cd476d931e78787a0cb77c1")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6511248244:AAFrpZ6J_ZwEzEVbs9jwM7S1_9jb-O5_oWI") 

FORCE_SUB = os.environ.get("FORCE_SUB", "Movilious") 

DB_NAME = os.environ.get("AbhiRename_Bot","")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://Abhishekq76:84078042@cluster0.s3319zt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/Rename-Bot-01-15")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6796937630').split()]

PORT = os.environ.get("PORT", "8080")
