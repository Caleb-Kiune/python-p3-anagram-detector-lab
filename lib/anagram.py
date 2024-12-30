# your code goes here!


class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        # This will hold the matched anagrams
        matches = []

        # Sort the original word's letters for comparison
        sorted_word = sorted(self.word)

        # Iterate over the list of possible anagrams
        for candidate in word_list:
            # Sort the candidate word's letters
            if sorted(candidate) == sorted_word:
                # If the sorted letters match, it's an anagram
                matches.append(candidate)

        return matches
