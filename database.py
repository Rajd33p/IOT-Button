from pymongo import MongoClient

# Connect to MongoDB


def connect_to_mongodb():
    # Connect to MongoDB
    client = MongoClient("mongodb+srv://appproject:a8CjgbqB4mmTz7VR@app.weapfdj.mongodb.net/?retryWrites=true&w=majority")  
    db = client["CloudHome"]  
    collection = db["Credentials"]  

    return client, collection


def check_credentials(username, password):

    client , collection = connect_to_mongodb()
    
    # Query for the username and password
    query = {
        "username": username,
        "password": password
    }

    result = collection.find_one(query)
    client.close()

    if result:
        return True
    else:
        return False
    


def Check_state(username):
    pass

# Example usage:

# username = "admin"
# password = "admin"
# if check_credentials(username, password):
#     print("Credentials are correct")
# else:   
#     print("Credentials are incorrect")

