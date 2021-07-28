# put your code here.
 

def count_words(filename):

    word_counts = {}


    for line in filename:
        line = line.strip('\n')
        line = line.split(' ')
        for word in line:
            word = word.lower()
            word = word.strip('?')
            word = word.strip('.')
            word = word.strip(',')
        
            word_counts[word] = word_counts.get(word, 0) + 1
    sorted_by_value = sorted(word_counts.items(), key=lambda x: x[1], reverse = True)
    #return sorted(word_counts)
    return sorted_by_value

print(count_words(open('test.txt')))