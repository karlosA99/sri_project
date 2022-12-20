from txt_corpus import txt_corpus
from cran_corpus import cran_corpus
from cisi_corpus import cisi_corpus
from med_corpus import med_corpus
from twenty_news_corpus import twenty_news_corpus
from models import vector_model, boolean_model, fuzzy_model
from document import query
import configparser
from eval import evaluate
# region Reading all settings
config = configparser.ConfigParser()
config.read('source/config.ini')

steamming = config.getboolean('DEFAULT','STEAMMING')
lemmatizing = config.getboolean('DEFAULT','LEMMATIZING')
corp = config['DEFAULT']['CORPUS']
if corp not in ['txt', 'cisi', 'medline', '20news','cranfield']:
    raise Exception('Corpus not allowed. Only TXT, CISI, 20News and Cranfield corpora are allowed')

match corp:
    case 'txt':
        corp = txt_corpus(steamming, lemmatizing)
    case 'cranfield':
        corp = cran_corpus(steamming, lemmatizing)
    case '20news':
        corp = twenty_news_corpus(steamming, lemmatizing)
    case 'cisi':
        corp = cisi_corpus(steamming, lemmatizing)
    case 'medline':
        corp = med_corpus(steamming, lemmatizing)

model = config['DEFAULT']['MODEL']
if model not in ['boolean', 'vector', 'fuzzy']:
    raise Exception('Model not allowed. Only Boolean and Vector models are allowed')

match model:
    case 'boolean':
        model = boolean_model(corp)
    case 'vector':
        model = vector_model(corp)
    case 'fuzzy':
        model = fuzzy_model(corp)
#endregion



q1 : query = query(0,"what similarity laws must be obeyed when constructing aeroelastic models of heated high speed aircraft")
q2 : query = query(1,"(aeroelastic and models) and (heated or high and (speed or aircraft)) and not speed")
q3 : query = query(2,"effects of leading-edge bluntness on the flutter characteristics of some square-planform double-wedge airfoils at mach numbers less than 15.4")

evaluate(corp, model)
"""r = model.exec_query(q1)
q1 : query = query("what similarity laws must be obeyed when constructing aeroelastic models of heated high speed aircraft")
q2 : query = query("(aeroelastic and models) and (heated or high and (speed or aircraft)) and not speed")
q3 : query = query("experimental")
q4 : query = query("models and (speed or not heated)")

r = model.exec_query(q4)
    
for tuple in r:
    print(tuple[0])"""
"""print('***************')
print(x)
print('***************')
print(y)
print('***************')
print(z)
print('***************')"""