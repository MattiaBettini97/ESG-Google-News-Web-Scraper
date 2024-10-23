<!-- ABOUT THE PROJECT -->
## ESG News Scraper & Sentiment Analyzer

This Python program automates the process of gathering news articles related to company ESG (Environmental, Social, and Governance) or sustainability topics from Google News. It analyzes the content using Natural Language Processing (NLP) models to classify ESG-related topics and perform sentiment analysis on both the original language (Italian) and its English translation (it is possible to change the language in translator function).



### Built With

* [![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)




<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites
Make sure you have the following installed:

Python 3.8+
Pip (Python package manager)
You'll also need the following Python libraries:

* Pandas: For handling CSV files.
* BeautifulSoup: For scraping web pages.
* Requests: For making HTTP requests.
* Torch: For using BERT models.
* Transformers: For NLP processing (BERT-based models).
* Googletrans: For translation.

Then:
* Prepare the Companies.csv file: Ensure that your Companies.csv file, which contains the list of company names, is in the root directory. Each company should be listed in a single column (see companies.csv).



### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/MattiaBettini97/ESG-News-Scraper-Sentiment-Analyzer.git
   cd ESG-News-Scraper-Sentiment-Analyzer
   ```
2. Install packages
   ```sh
   pip install beautifulsoup4
   pip install transformers
   pip install googletrans==4.0.0-rc1
   pip install pandas
   pip install torch
   pip install requests
   ```



<!-- USAGE EXAMPLES -->
## Usage

To run the program and start scraping ESG-related news, follow these steps:

Edit the search query: The script is set to look for news using the search query format:

   ```sh
     search_query = f'"{companies.iloc[i, 0]}" ESG OR sustainability'
   ```

You can modify this if you wish to focus on different terms.

### The script will:

* Scrape Google News for ESG-related news for each company listed in Companies.csv.
* Translate article titles (if needed) into English.
* Perform ESG topic classification and sentiment analysis.
### Output two CSV files:
* company_esg_analysis_eng.csv: Results with English titles and translations.
* company_esg_analysis_ita.csv: Results with Italian titles.




<!-- ROADMAP -->
## OutPut

After running the script, two CSV files will be generated:

**1. company_esg_analysis_ita.csv:** Contains the following columns:

* `company_name`: The company the article is about.
* `title`: The article title in Italian.
* `link`: The URL to the news article.
* `date`: The date of the article.
* `ESG topic`: The ESG classification (Environmental, Social, Governance).
* `ESG score`: The confidence score for the classification.
* `sentiment score`: Sentiment score of the article (1–5).

  
**2. company_esg_analysis_eng.csv:** Contains the same columns as above but with the article title translated into English.

## Customization

You can customize the code to:

* Add additional languages.
* Modify the sentiment scoring model.
* Handle additional ESG-related topics.



<!-- CONTACT -->
## Contact

Mattia Bettini - https://www.linkedin.com/in/mattia-bettini-329a22212/



<!-- ACKNOWLEDGMENTS -->
## Future Enhancements

* **Proxy rotation:** To avoid rate-limiting issues while scraping.
* **Error handling improvements:** Adding retry mechanisms for failed requests.
