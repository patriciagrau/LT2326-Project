import string
import re

def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
    
def processing_wiki_data(data_wiki):
    """
    Processes the data from the WSC_data.txt file.
    It gets rid of things between parenthesis -because it's
    mostly dates- numbers and things that follow the pattern
    number-number. 
    We only keep sentences with size bigger or equal to 9, 
    because the smallest size in the WSC dataset is 9.
    """
    
    f = open(data_wiki, 'r')
    l = f.readlines()
    j = []
    
    checking = string.punctuation + '||'

    for x in l:

        # remove \t and \n
        x = x.strip()

        # remove stuff in parenthesis
        x = re.sub("[\(\[].*?[\)\]]", "", x)

        # repeating pattern
        pattern1 = re.compile("([0-9]-[0-9])")
        pattern2 = re.compile("([0-9]:[0-9][0-9])")

        if '. ' in x:
            # separating sentences
            sentences = x.split('. ')
            for sent in sentences:
                copy = []
                words = sent.split()
                for w in words:
                    w = w.strip()
                    w = w.strip(';/),.(:"-')
                    # remove punctuation standing alone or numbers
                    if w in checking or any(i.isdigit() for i in w):
                        pass
                    # removing the repeating pattern
                    elif pattern1.match(w) or pattern2.match(w):
                        pass
                    else:
                        copy.append(w.lower()) # old w.strip(string.punctuation)

                if len(copy) > 8:
                    j.append(' '.join(copy))
        else:
            copy = []
            words = x.split()
            for w in words:
                w = w.strip(';/),.(-:"')
                # remove punctuation standing alone or numbers
                if w in checking or any(i.isdigit() for i in w):
                    pass
                # removing the repeating pattern
                elif pattern1.match(w) or pattern2.match(w):
                    pass
                else:
                    copy.append(w.lower()) # old w.strip(string.punctuation)
            if len(copy) > 8:
                j.append(' '.join(copy))

    g = open('wiki_sent.csv', 'w')
    for element in j:
        g.write(element + '\n')
#         if element[-1] in string.punctuation:
#             g.write(element + "\n")
#         else:
#             g.write(element + ".\n")
    f.close()
    g.close()

def data_to_csv(data):
    with open(data) as f:
        with open('wiki_sent.csv', 'w') as g:
            for line in f:
                g.write(line.lower())
                
    
if __name__ == '__main__':
    data_wiki = '/home/gusgraupa@GU.GU.SE/MLNLP2/LT2326-Project/data/WSC_data.txt'
    processing_wiki_data(data_wiki)
    
    
