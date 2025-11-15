# 🚀 Predictive Keyword Hunter

This is a powerful SEO tool that leverages real-time news headlines to predict "future keywords"—search terms that currently have little to no competition.

The script fetches top technology headlines from **NewsAPI** and uses **Google's Gemini AI** to generate a list of long-tail keywords and questions poised to trend within the next 24-48 hours.

## 🌟 Features

* **Real-time Trends:** Fetches instant top headlines from NewsAPI.
* **AI-Powered Prediction:** Uses Google Gemini (e.g., `gemma-3n-e2b-it`) to analyze search intent and predict queries.
* **Zero-Volume Keywords:** Generates keywords that currently have "Zero Volume," allowing you to rank first.
* **Secure:** Keeps API keys separate and safe from the main code using a `.env` file.

## 🛠️ How It Works

The project workflow is straightforward:



1.  **Data Collection:** The `NewsApiClient` fetches the top "technology" headlines from the "US".
2.  **AI Prompting:** The top headline is used as a "seed topic".
3.  **Prediction:** This headline is sent to the Gemini AI with a specialized prompt.
4.  **Output:** The AI returns a list of 15-20 predicted keywords, which are then printed to the console.

## 💻 Technical Stack

* **Python 3.9+**
* **Libraries:**
    * `google-generativeai`: To interact with the Google Gemini API.
    * `newsapi-python`: To fetch headlines from NewsAPI.org.
    * `python-dotenv`: To safely manage API keys.

## 🚀 Setup & Installation

Follow these steps to run this project on your local machine:

**1. Clone the Repository:**
```bash
git clone [https://github.com/Hajihassm/Predictive-Keyword-Hunter.git](https://github.com/Hajihassm/Predictive-Keyword-Hunter.git)
cd Predictive-Keyword-Hunter