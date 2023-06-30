class WordCounter:

    def __init__(self, sentence):
        self.sentence = sentence
    
    def get_word_count(self):   
       wordCount = len(self.sentence.split())
       return wordCount

        # Returns the number of all the words.
    # def get_shortest_word(self): 
    # Returns the length of the shortest word.
    # def get_longest_word(self):  
    # Returns the length of the longest word.
