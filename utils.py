import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


# Set stop words list
STOP_WORDS = set(stopwords.words('english'))

lemmatizer = WordNetLemmatizer()



def clean_text(text):
    text = text.lower()
    text = re.sub(r'https?://\S+', '', text)  # remove URLs
    text = re.sub(r'\b[\w.-]+?@\w+?\.\w+?\b', '', text)  # remove emails
    text = re.sub(r'[^a-z\s]', '', text)  # remove punctuation/numbers
    return text

def tokenize(text):
    return text.split()

def remove_stopwords(tokens):
    return [t for t in tokens if t not in STOP_WORDS]

def lemmatize(tokens):
    return [lemmatizer.lemmatize(token) for token in tokens]






# def porter_stem(tokens):
#     def stem(word):
#         suffixes = ['ing', 'ly', 'ed', 'ious', 'ies', 'ive', 'es', 's', 'ment']
#         for suf in suffixes:
#             if word.endswith(suf) and len(word) > len(suf) + 2:
#                 return word[:-len(suf)]
#         return word
#     return [stem(t) for t in tokens]




