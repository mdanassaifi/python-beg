import requests

def fetch_joke_chuck_norris_style():
    url = "https://api.freeapi.app/api/v1/public/randomjokes/joke/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        joke_text = data["data"]["content"]
        return joke_text
    else:
        raise Exception("Failed to fetch joke")

def main():
    try:
        joke = fetch_joke_chuck_norris_style()
        print(f"joke👉 : {joke}")
    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    main()
