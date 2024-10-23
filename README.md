# ESG-Google-News-Web-Scraper
 This Python program scrapes Google News for ESG or sustainability articles related to companies listed in a CSV file. It uses NLP for ESG classification, sentiment analysis (Italian and English titles), and translation. Results are stored in two CSV files with company name, title, ESG score, sentiment, and more.
ESG News Scraper and Sentiment Analysis
This Python program automates the process of gathering news articles related to company ESG (Environmental, Social, and Governance) or sustainability topics from Google News. It analyzes the content using Natural Language Processing (NLP) models to classify ESG-related topics and perform sentiment analysis on both the original language (Italian) and its English translation.

# Key Features:
# 1 Web Scraping:

Utilizes Google News search for specific companies listed in a CSV file (Companies.csv) to retrieve news articles related to ESG or sustainability.
Implements a fallback mechanism if the initial search query yields no results, by simplifying the search to just the company name.

# 2 Natural Language Processing (NLP):

Uses a custom ESG classifier (nlp_ESG) to detect ESG-related content in news titles.
Sentiment analysis is performed using a pre-trained BERT-based multilingual model (nlptown/bert-base-multilingual-uncased-sentiment) for both the original (Italian) and translated (English) news titles.

# 3 Translation:

Automatically translates Italian news titles to English using the translator module for broader analysis.

# 4 Sentiment Scoring:

The sentiment score (on a scale of 1 to 5) is calculated for both Italian and English news titles using the BERT model.

# 5 Data Output:

The results are stored in two separate CSV files (company_esg_analysis_ita.csv and company_esg_analysis_eng.csv) with columns:
-Company Name
-News Title
-News Link
-Date
-ESG Topic
-ESG Score
-Sentiment Score

# Requirements:
Pandas: For managing company data and storing results in CSV format.
BeautifulSoup (from news module): To parse HTML content from Google News search results.
Transformers (Hugging Face): For sentiment analysis using BERT models.
Torch: For handling BERT model tensor computations.
Translator Module: To translate Italian news titles to English.
# Usage:
Ensure that you have a CSV file named Companies.csv with company names in the first column.
Run the script, and it will scrape the news data, perform ESG classification and sentiment analysis, then output the results into CSV files.
