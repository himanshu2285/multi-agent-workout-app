from .db import personal_data_collection, notes_collection

def get_value(_id):
    return {
        "_id": _id,
        "general": {
            "name": "",
            "age": 30,
            "weight": 70,
            "height": 170,
            "gender": "Male",
            "fitness_level": "Beginner",
            "activity_level": "Sedentary"
        },
        "goals": ["Weight Loss"],
        "nutrition": {
            "colaries":2000,
            "protein":150,
            "carbs":150,
            "fats":30
        },
    }
    
def create_profile(_id):
    profile_values = get_value(_id)
    result = personal_data_collection.insert_one(profile_values)
    return result.inserted_id, result

def get_profile(_id):
    return personal_data_collection.find_one({"_id": {"$eq": _id}})

def get_notes(_id):
    return list(notes_collection.find({"user_id": {"$eq": _id}  }))