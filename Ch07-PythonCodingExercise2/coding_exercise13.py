def count_word_frequency(sentence):
    words = sentence.split()  # Split the sentence into words
    word_freq = {}  # Dictionary to store word counts
    
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1  # Increment count
    
    return word_freq

# Example usage
print(count_word_frequency("hello world hello"))
print(count_word_frequency("the quick brown fox jumps over the lazy dog"))
