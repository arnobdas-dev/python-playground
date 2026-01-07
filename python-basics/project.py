# Word and Character Counter

def count_words_characters(text):
    """
    Function to count words and characters in a given text
    """
    # Remove leading/trailing spaces
    clean_text = text.strip()
    
    # Count words
    words = clean_text.split()  # splits by spaces
    num_words = len(words)
    
    # Count characters (excluding spaces if you want)
    num_characters = len(clean_text.replace(" ", ""))  # without spaces
    num_characters_with_spaces = len(clean_text)      # including spaces
    
    return num_words, num_characters, num_characters_with_spaces


# ----------- Main Program -------------
print("Welcome to Word & Character Counter!")
text = input("Enter your text: ")

words, chars_no_space, chars_with_space = count_words_characters(text)

print("\nResults:")
print(f"Number of words: {words}")
print(f"Number of characters (excluding spaces): {chars_no_space}")
print(f"Number of characters (including spaces): {chars_with_space}")
