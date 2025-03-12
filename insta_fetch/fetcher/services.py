import requests
import logging

ACCESS_TOKEN = "" #you can add yours
USERNAME = "bbcnews"

def get_instagram_user_id(username):
    
    url = f"https://graph.facebook.com/v18.0/{username}?fields=id&access_token={ACCESS_TOKEN}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json().get("id")
    return None

def fetch_instagram_post():
    try:
        user_id = get_instagram_user_id(USERNAME)
        if not user_id:
            return None

        url = f"https://graph.facebook.com/v18.0/{user_id}/media?fields=caption,media_url&limit=1&access_token={ACCESS_TOKEN}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json().get("data", [])
            if data:
                return {"caption": data[0]["caption"], "image_url": data[0]["media_url"]}
        
        logging.error("Could not fetch Instagram post.")
        return None

    except Exception as e:
        logging.error(f"Error fetching Instagram post: {str(e)}")
        return None