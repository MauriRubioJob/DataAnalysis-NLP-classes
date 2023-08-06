# Create a Python program to remove all punctuation from a sentence.

sentence = "'Then the Dormouse shall!' they both cried. 'Wake up, Dormouse!' And they pinched it on both sides at once."


punctuation = ",.:;-!?'"
for symbol in punctuation:
    sentence = sentence.replace(symbol, "")

print(sentence)