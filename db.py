from astrapy import DataAPIClient
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

ENDPOINT = os.getenv("ASTRA_ENDPOINT")
TOKEN = os.getenv("Astra_DB_Application_Token")

@st.cache_resource
def get_db():
    client = DataAPIClient(token=TOKEN)
    db = client.get_database_by_api_endpoint(ENDPOINT)
    return db

db = get_db()
collections = ["personal_data", "notes"]

for collection in collections:
    try:
        db.create_collection(collection)
    except:
        pass


personal_data_collection = db.get_collection("personal_data")
notes_collection = db.get_collection("notes")