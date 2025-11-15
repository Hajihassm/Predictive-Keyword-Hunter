import os
import google.generativeai as genai
from newsapi import NewsApiClient
from dotenv import load_dotenv

# Step 1: .env file se API keys load karein
load_dotenv()
NEWS_API_KEY = os.getenv('NEWS_API_KEY')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# Check karein ki keys load hui hain ya nahi
if not NEWS_API_KEY or not GEMINI_API_KEY:
    print("Error: API keys .env file mein nahi milin.")
    print("Check karein ki .env file ka naam sahi hai aur usmein keys maujood hain.")
    exit()

# --- MODULE 1: NewsAPI se Data Fetch Karna ---
def get_top_headline():
    try:
        newsapi = NewsApiClient(api_key=NEWS_API_KEY)
        top_headlines = newsapi.get_top_headlines(
                                                category='technology',
                                                language='en',
                                                country='us'
                                              )
        
        if top_headlines['status'] == 'ok' and top_headlines['totalResults'] > 0:
            # Sirf pehli headline return karein
            first_headline = top_headlines['articles'][0]['title']
            return first_headline
        else:
            return None
    except Exception as e:
        print(f"NewsAPI Error: {e}")
        return None

# --- MODULE 3: Gemini AI se Keywords Generate Karna ---
# --- MODULE 3: Gemini AI se Keywords Generate Karna ---
def get_predicted_keywords(headline):
    try:
        # Gemini API ko configure karein
        genai.configure(api_key=GEMINI_API_KEY)
        
        # --- YAHAN BADLAAV KIYA GAYA HAI ---
        # Humne 'gemini-pro' ko 'gemini-1.5-flash' se badal diya hai
        # Yeh naya aur tez model hai
        model = genai.GenerativeModel('gemma-3n-e2b-it') 
        # --- END BADLAAV ---
        
        # Hamara "Tofani" Prompt
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
        
        # AI se response generate karwayein
        response = model.generate_content(prompt)
        return response.text
        
    except Exception as e:
        print(f"Gemini AI Error: {e}")
        return None

# --- Main Program ko Run Karein ---
print("🚀 Predictive Keyword Hunter chal raha hai...")

print("Step 1: NewsAPI se top headline laa raha hai...")
headline = get_top_headline()

if headline:
    print(f"\n🔥 Top Headline Mili: {headline}")
    
    print("\nStep 2: Gemini AI se keywords predict karwa raha hai...")
    keywords = get_predicted_keywords(headline)
    
    if keywords:
        print("\n--- 🤖 Predicted Keywords List ---")
        print(keywords)
    else:
        print("Gemini AI se keywords nahi mil sake.")
else:
    print("NewsAPI se koi headline nahi mili.")