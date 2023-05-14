import sys
import re
import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
# init lemmatizer
lemmatizer = WordNetLemmatizer()

stopwords=['this','that','and','a','we','it','to','is','of','up','need','i']

def decontracted(phrase):
    # specific
    phrase = re.sub(r"won\'t", "will not", phrase)
    phrase = re.sub(r"can\'t", "can not", phrase)

    # general
    phrase = re.sub(r"n\'t", " not", phrase)
    phrase = re.sub(r"\'re", " are", phrase)
    phrase = re.sub(r"\'d", " would", phrase)
    phrase = re.sub(r"\'ll", " will", phrase)
    phrase = re.sub(r"\'t", " not", phrase)
    phrase = re.sub(r"\'ve", " have", phrase)
    phrase = re.sub(r"\'m", " am", phrase)

    # BeeGFS
    phrase = re.sub(r"helperd", "helper", phrase)

    return phrase

def scrub_words(text):
    """Basic cleaning of texts."""
    
    # remove html markup
    text=re.sub("(<.*?>)","",text)

    # remove _ and - 
    text=re.sub("(-|_)", " ", text)

    # remove single letter word
    text = re.sub(r'\b\w{1}\b', " ", text)
    
    #remove non-ascii and digits
    text=re.sub("(\\W|\\d)"," ",text)
    
    #remove whitespace
    text=text.strip()
    return text

def remove_nouns(text):
    is_noun = lambda pos: pos[:2] == 'NN'
    # do the nlp stuff
    tokenized_ = nltk.word_tokenize(text)
    not_nouns = [word for (word, pos) in nltk.pos_tag(tokenized_) if not is_noun(pos)] 
    output_string = ' '.join([str(e) for e in not_nouns])
    return output_string


def string_preprocessing(input_path, output_path):
    output_file = open(output_path, "w")
    with open(input_path) as fp:
        for line in fp:
            char_needed = False
            output_string = ""
            
            for c in line:
                if char_needed and c != '"':
                    output_string += c.lower()

                if c == '"':
                    if (not char_needed):
                        char_needed = True
                    elif c == '"' and char_needed:
                        output_string += " "
                        char_needed = False

            output_string = output_string.strip()
            output_string = decontracted(output_string)
            s_array = re.split("\\s+", output_string)
            short_s_array = []
            for w in s_array:
                if w not in stopwords:
                    short_s_array.append(w)

            lemmatized_words=[lemmatizer.lemmatize(word=word,pos='v') for word in short_s_array]
            lemmatized_words=[lemmatizer.lemmatize(word=word,pos='n') for word in lemmatized_words]
            
            cleaned_string = [scrub_words(w) for w in lemmatized_words]
            cleaned_string = [scrub_words(w) for w in cleaned_string]
            new_output_string = ' '.join([str(e) for e in cleaned_string if e != ''])
            
            if (not new_output_string.isspace()) and len(new_output_string) > 0:
                output_file.write(new_output_string)
                output_file.write("\n")

# s = ffffa139cab87800
def is_hex(s):
    return re.fullmatch(r'^(0[xX])?[0-9a-fA-F]+$', s or "") is not None

def string_preprocessing_no_quote(input_path, output_path):
    output_file = open(output_path, "w")
    with open(input_path) as fp:
        for line in fp:
            output_string = ""
            
            for c in line:
                output_string += c.lower()

            #output_string = remove_nouns(output_string)

            #print("      ", output_string)
            output_string = output_string.strip()
            output_string = decontracted(output_string)
            s_array = re.split("\\s+", output_string)
            short_s_array = []
            for w in s_array:
                if w.startswith("0x") or w.startswith("@0x") or w.startswith("[0x") or w.startswith("(0x"):
                    continue
                if is_hex(w):
                    continue
                if w not in stopwords:
                    short_s_array.append(w)

            lemmatized_words=[lemmatizer.lemmatize(word=word,pos='v') for word in short_s_array]
            lemmatized_words=[lemmatizer.lemmatize(word=word,pos='n') for word in lemmatized_words]
            
            cleaned_string = [scrub_words(w) for w in lemmatized_words]
            cleaned_string = [scrub_words(w) for w in cleaned_string]
            print("size:", len(cleaned_string), cleaned_string)
            if len(cleaned_string) <= 2:
                continue
            new_output_string = ' '.join([str(e) for e in cleaned_string if e != ''])
            new_output_string = new_output_string.strip()
            
            if (not new_output_string.isspace()) and len(new_output_string) > 0:
                output_file.write(new_output_string)
                output_file.write("\n")

def scrub_words_no_file(text):
    """Basic cleaning of texts."""
    
    # remove html markup
    text=re.sub("(<.*?>)","",text)
    text = re.sub(r'/.*?(\s|\Z)', " ", text)

    # remove _ and - 
    text=re.sub("(-|_)", " ", text)

    # remove single letter word
    text = re.sub(r'\b\w{1}\b', " ", text)

    

    #remove non-ascii and digits
    text=re.sub("(\\W|\\d)"," ",text)
    text=re.sub("blk"," ",text)
    #remove whitespace
    text=text.strip()
    return text

def string_preprocessing_no_file(input_path, output_path):
    output_file = open(output_path, "w")
    with open(input_path) as fp:
        for line in fp:
            char_needed = False
            output_string = ""
            
            for c in line:
                output_string += c.lower()

            #output_string = remove_nouns(output_string)
            output_string = output_string.strip()
            output_string = decontracted(output_string)
            s_array = re.split("\\s+", output_string)
            short_s_array = []
            for w in s_array:
                if w not in stopwords:
                    short_s_array.append(w)

            lemmatized_words=[lemmatizer.lemmatize(word=word,pos='v') for word in short_s_array]
            lemmatized_words=[lemmatizer.lemmatize(word=word,pos='n') for word in lemmatized_words]
            
            cleaned_string = [scrub_words_no_file(w) for w in lemmatized_words]
            cleaned_string = [scrub_words_no_file(w) for w in cleaned_string]
            new_output_string = ' '.join([str(e) for e in cleaned_string if e != ''])
            
            if (not new_output_string.isspace()) and len(new_output_string) > 0:
                output_file.write(new_output_string)
                output_file.write("\n")

if __name__ == '__main__':
    # change the "input_path" to the input file you have
    # change the "output_path" to the output place you want
    string_preprocessing_no_file("input_path", "output_path")
