from news import news
import pandas as pd
from urllib.parse import quote
from nlp_ESG import nlp_ESG
from translator import translator
#from soup_test import soup_test
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

root = "https://www.google.com/"
link = "https://www.google.com/search?q=ABB+ESG&tbm=nws&source=lnt&tbs=sbd:1&sa=X&ved=0ahUKEwjAvsKDyOXtAhXBhOAKHXWdDgcQpwUIKQ&biw=1604&bih=760&dpr=1.2"

companies = pd.read_csv('Companies.csv')
companies = pd.DataFrame(companies)

tokenizer = AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

df_eng = []
df_ita = []

for i in range(len(companies)):
    
    search_query = f'"{companies.iloc[i, 0]}" ESG OR sustainability'
    #search_query = search_query.replace(" ","+")
    search_query = quote(search_query)
    #tbs=sbd:1 to sort results by date, showing the latest news first
    link = f"https://www.google.com/search?q={search_query}&tbm=nws&source=lnt&tbs=sbd:1&sa=X"
    soup = news(link)
    
    #soup = soup_test()
    
    if not soup or not soup.find_all('div', attrs={'class': 'SoaBEf'}):
        search_query = f'"{companies.iloc[i, 0]}"'
        search_query = quote(search_query)
        link = f"https://www.google.com/search?q={search_query}&tbm=nws&source=lnt&tbs=sbd:1&sa=X"
        soup = news(link)
        
    if not soup or not soup.find_all('div', attrs={'class': 'SoaBEf'}):
        print(f"No results for {companies.iloc[i, 0]}. Retrying...")
        continue
        
    #print(search_query)
    #print(soup)
    #print("------------------------------------------------------------------------------------------------")
    for item in soup.find_all('div',attrs = {'class':'SoaBEf'}):
     # Extract the title from the nested div with the desired class
        #print(item)
        title_div = item.find('div', attrs={'class': 'n0jPhd ynAwRc MBeuO nDgy9d'}) #BNeawe vvjwJb AP7Wnd
        date_div = item.find('div', attrs={'class': 'OSrXXb rbYSKb LfVVr'})
        link_a = item.find('a',attrs = {'class':'WlydOe'})

        if title_div:
           title = title_div.get_text()
           #print(title)
           
        if date_div:
            date_span = date_div.find('span')
            if date_span:
               date = date_span.get_text()
            #print("Extracted date:", date)
        if link_a:
           link_news = link_a['href']
           #print(link_news)

        esg_label_score_ita = nlp_ESG(title)
        esg_label_ita = esg_label_score_ita[0]['label']
        esg_score_ita = esg_label_score_ita[0]['score']        
        
        title_eng = translator(title)
        
        esg_label_score_eng = nlp_ESG(title_eng)
        esg_label_eng = esg_label_score_eng[0]['label']
        esg_score_eng = esg_label_score_eng[0]['score']
        
        tokens_ita = tokenizer.encode(title , return_tensors='pt')
        result_ita = model(tokens_ita) 
        sentiment_score_ita = int(torch.argmax(result_ita.logits)) + 1 # from 1 to 5
        
        tokens_eng = tokenizer.encode(title_eng , return_tensors='pt')
        result_eng = model(tokens_eng) 
        sentiment_score_eng = int(torch.argmax(result_eng.logits)) + 1 # from 1 to 5
        
        
        #TO DO. Add sentiment analysis
        df_ita.append({'company_name': companies.iloc[i, 0],'title': title,'link': link_news,'date': date,'ESG topic':esg_label_ita,'ESG score':esg_score_ita,'sentiment score':sentiment_score_ita})
        df_eng.append({'company_name': companies.iloc[i, 0],'title': title_eng,'link': link_news,'date': date,'ESG topic':esg_label_eng,'ESG score':esg_score_eng,'sentiment score':sentiment_score_eng})          
        

# Convert the results to a DataFrame
news_df_ita = pd.DataFrame(df_ita)
news_df_eng = pd.DataFrame(df_eng)

# Save the results to a CSV file
news_df_ita.to_csv('company_esg_analysis_ita.csv', index=False)
news_df_eng.to_csv('company_esg_analysis_eng.csv', index=False)

#print("News data saved to 'company_news_results.csv'")
          