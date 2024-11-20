import requests
import json

def internet_search(query):
    # Your Bing API or other search API key goes here
    subscription_key = 'YOUR_BING_API_KEY'  # Replace with your Bing API key
    search_url = "https://api.bing.microsoft.com/v7.0/search"
    
    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    params = {"q": query, "textDecorations": True, "textFormat": "HTML"}
    
    response = requests.get(search_url, headers=headers, params=params)
    
    if response.status_code == 200:
        search_results = response.json()
        # Grab the top snippet from the results (you can refine this to get better results)
        if search_results.get("webPages"):
            return search_results["webPages"]["value"][0]["snippet"]
        else:
            return "Sorry, I couldn't find relevant information."
    else:
        return "There was an error with the search request."