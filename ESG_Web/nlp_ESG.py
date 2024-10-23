from transformers import BertTokenizer, BertForSequenceClassification, pipeline

#https://huggingface.co/nlptown

def nlp_ESG(title):
    finbert = BertForSequenceClassification.from_pretrained('yiyanghkust/finbert-esg-9-categories',num_labels=9)
    tokenizer = BertTokenizer.from_pretrained('yiyanghkust/finbert-esg-9-categories')
    nlp = pipeline("text-classification", model=finbert, tokenizer=tokenizer)
    result = nlp(title)
    return result

#results = nlp('For 2002, our total net emissions were approximately 60 million metric tons of CO2 equivalents for all businesses and operations we have ﬁnancial interests in, based on its equity share in those businesses and operations.')
#print(results) # [{'label': 'Climate Change', 'score': 0.9955655932426453}]