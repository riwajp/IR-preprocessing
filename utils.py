import re
import csv
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import defaultdict

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



def build_and_save_inverted_index_csv(input_file, output_file, content_column="Processed"):
    index = defaultdict(lambda: defaultdict(list))

  
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for doc_id, row in enumerate(reader):
            text = str(row.get(content_column, '')).strip()
            if not text:
                continue
            tokens = text.split()
            for pos, token in enumerate(tokens):
                index[token][doc_id].append(pos)

    # Write to CSV
    with open(output_file, 'w', newline='', encoding='utf-8') as f_out:
        writer = csv.writer(f_out)
        writer.writerow(['Term', 'DocID', 'Positions'])  

        for term, positions in index.items():
            for doc_id, positions in positions.items():
                writer.writerow([term, doc_id, ' '.join(map(str, positions))])



# def porter_stem(tokens):
#     def stem(word):
#         suffixes = ['ing', 'ly', 'ed', 'ious', 'ies', 'ive', 'es', 's', 'ment']
#         for suf in suffixes:
#             if word.endswith(suf) and len(word) > len(suf) + 2:
#                 return word[:-len(suf)]
#         return word
#     return [stem(t) for t in tokens]




