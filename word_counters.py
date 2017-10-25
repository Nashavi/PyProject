from collections import defaultdict

def word_counter(sentences):
    word_dict  = defaultdict(int)
    for word in sentences.split():
        word_dict[word] +=1
    return print(word_dict)

word_counter("My Name is Avinash is my name")



from collections import Counter

print(Counter("My Name is Avinash is my name".split()))
