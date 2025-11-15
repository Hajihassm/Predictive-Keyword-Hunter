import os
import google.generativeai as genai
from newsapi import NewsApiClient
from dotenv import load_dotenv

load_dotenv()
NEWS_API_KEY = os.getenv('NEWS_API_KEY')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

if not NEWS_API_KEY or not GEMINI_API_KEY:
    print("Error: API keys not found in .env file.")
    print("Check that the .env file exists and contains your keys.")
    exit()

def get_top_headline():
    try:
        newsapi = NewsApiClient(api_key=NEWS_API_KEY)
        top_headlines = newsapi.get_top_headlines(
                                                category='technology',
                                                language='en',
                                                country='us'
                                              )
        
        if top_headlines['status'] == 'ok' and top_headlines['totalResults'] > 0:
            first_headline = top_headlines['articles'][0]['title']
            return first_headline
        else:
            return None
    except Exception as e:
        print(f"NewsAPI Error: {e}")
        return None

def get_predicted_keywords(headline):
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        
        model = genai.GenerativeModel('gemma-3n-e2b-it') 
        
        prompt = f"""
        Headline: "{headline}"

        Based on this new trending headline, generate a list of 15 "long-tail keywords" and "user questions" that people will search for on Google in the next 24-48 hours.

        Focus on these categories:
        1.  Informational (What is/How to)
        2.  Problems (Bugs/Errors/Not working)
        3.  Availability (Release date/Download)
        4.  Reviews (Worth it/Review)

        Format the output as a simple list.
        """
        
        response = model.generate_content(prompt)
        return response.text
        
    except Exception as e:
        print(f"Gemini AI Error: {e}")
        return None

print("🚀 Predictive Keyword Hunter is running...")

print("Step 1: Fetching top headline from NewsAPI...")
headline = get_top_headline()

if headline:
    print(f"\n🔥 Top Headline Found: {headline}")
    
    print("\nStep 2: Predicting keywords with Gemini AI...")
    keywords = get_predicted_keywords(headline)
    
    if keywords:
        print("\n--- 🤖 Predicted Keywords List ---")
        print(keywords)
    else:
        print("Could not get keywords from Gemini AI.")
else:
    print("No headline received from NewsAPI.")