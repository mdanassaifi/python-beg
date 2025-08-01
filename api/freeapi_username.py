import requests

def fetch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()


    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        password = user_data["login"]["password"]
        dob = user_data["dob"]
        return username, country, password, dob
    else:
        raise Exception("Failed to fetch user data from FreeAPI")
    
def main():
    try:
        username, country, password, dob = fetch_random_user_freeapi()
        print(f"username: {username} \ncountry: {country} \npassword: {password} \ndob: {dob}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
