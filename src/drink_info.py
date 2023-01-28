import requests


def get_drink(a):
    api_url = "https://www.thecocktaildb.com/api/json/v1/1/search.php?s="

    get_data = requests.get(api_url + a).json()

    if get_data["drinks"] == None:
        return False
    else:
        return get_data

def get_drink_tags(a):
    api_url = "https://www.thecocktaildb.com/api/json/v1/1/search.php?s="

    get_data = requests.get(api_url + a).json()

    if get_data["drinks"][0]["strTags"] == None:
        return False
    else:
        return get_data["drinks"][0]["strTags"]

def get_instruction(lang, a):
    api_url = "https://www.thecocktaildb.com/api/json/v1/1/search.php?s="
    if lang == "EN".lower():
        get_data = requests.get(api_url + a).json()

        if get_data["drinks"][0]["strInstructions"] == None:
            return False
        else:
            return get_data["drinks"][0]["strInstructions"]
    elif lang == "ES".lower():
        get_data = requests.get(api_url + a).json()

        if get_data["drinks"][0]["strInstructionsES"] == None:
            return False
        else:
            return get_data["drinks"][0]["strInstructionsES"]
    elif lang == "DE".lower():
        get_data = requests.get(api_url + a).json()

        if get_data["drinks"][0]["strInstructionsDE"] == None:
            return False
        else:
            return get_data["drinks"][0]["strInstructionsDE"] 
    elif lang == "IT".lower():
        get_data = requests.get(api_url + a).json()

        if get_data["drinks"][0]["strInstructionsIT"] == None:
            return False
        else:
            return get_data["drinks"][0]["strInstructionsIT"] 
    elif lang == "FR".lower():
        get_data = requests.get(api_url + a).json()

        if get_data["drinks"][0]["strInstructionsFR"] == None:
            return False
        else:
            return get_data["drinks"][0]["strInstructionsFR"]
    else:
        return False
        
        
