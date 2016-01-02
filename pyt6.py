# write a function that takes a sentence as a parameter and returns the number of words in the sentence.
# 4.5

def take(sentence):
    s = str(sentence)
    print(s.split())
    print(len(s.split()))

take("jerry likes to eat")
