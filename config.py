import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "10355467"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "d86087c1892f818da03d68c3eaba765c")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://sarab9968:XSXhVMVLFJ47Q9am@cluster0.ljeycyu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
