import re
from nltk_utils import tokenize
from nltk.tag import pos_tag
from datetime import datetime

def get_current_time():
    t = datetime.now().time()
    return f"{t.strftime('%I')}:{t.strftime('%M')} {t.strftime('%p')}"


def get_asked_word(question:str):
    keyword = ''
    verb_i = 0
    pos = pos_tag(tokenize(question))
    print(pos)
    for i, word in enumerate(pos):
        if word[1] == 'VERB' or word[1] == 'ADP':
            verb_i = i
            break
    while(verb_i< len(pos)-1):
        keyword+=f"{pos[verb_i+1][0]} "
        verb_i+=1
        
    return re.subn('\W', " ", keyword)[0]
