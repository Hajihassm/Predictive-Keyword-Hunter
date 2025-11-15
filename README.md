# 🚀 Predictive Keyword Hunter

Yeh ek "Tofani" (powerful) SEO tool hai jo real-time news headlines ka istemal karke aise "future keywords" predict karta hai jin par abhi competition nahi hai.

Yeh script NewsAPI se top tech headlines uthati hai aur Google Gemini AI ka istemal karke un long-tail keywords ki list banati hai jo log agle 24-48 ghanton mein search karne wale hain.

## 🌟 Features (Khususiyat)

* **Real-time Trends:** NewsAPI se fori (instant) top headlines laata hai.
* **AI-Powered Prediction:** Google Gemini (gemma-3n-e2b-it) ka istemal karke search intent ko predict karta hai.
* **Zero-Volume Keywords:** Aapko aise keywords deta hai jin par "Zero Volume" hai, taaki aap sabse pehle rank kar sakein.
* **Secure:** API keys ko code se alag (`.env` file) rakhta hai.

## 🛠️ How It Works (Yeh Kaam Kaise Karta Hai?)

Project ka workflow bohot simple hai:



1.  **Data Collection:** `NewsApiClient` "US" se top "technology" headlines fetch karta hai.
2.  **AI Prompting:** Top headline ko ek "seed topic" ke taur par istemal kiya jaata hai.
3.  **Prediction:** Yeh headline Gemini AI ko ek khaas prompt ke saath bheji jaati hai.
4.  **Output:** AI 15-20 predicted keywords ki ek list return karta hai, jise console par print kar diya jaata hai.

## 💻 Technical Stack (Istemal Shuda Technology)

* **Python 3.9+**
* **Libraries:**
    * `google-generativeai`: Google Gemini API se baat karne ke liye.
    * `newsapi-python`: NewsAPI.org se headlines laane ke liye.
    * `python-dotenv`: API keys ko safely manage karne ke liye.

## 🚀 Setup & Installation (Ise Kaise Chalayein)

Is project ko apne computer par chalane ke liye yeh steps follow karein:

**1. Clone the Repository (Code Download Karein):**
```bash
git clone [https://github.com/AAPKA-USERNAME/Predictive-Keyword-Hunter.git](https://github.com/AAPKA-USERNAME/Predictive-Keyword-Hunter.git)
cd Predictive-Keyword-Hunter