# Word Counter Program

def count_words(sentence):
    """
    Count the number of words in a given sentence.

    Args:
        sentence (str): The input sentence or paragraph.

    Returns:
        int: The number of words in the input.
    """
    # Implement word counting logic here
    words = sentence.split()
    return len(words)

def main():
    # User Input
    user_input = input("Enter a sentence or paragraph: ")

    try:
        # Word Counting Logic
        word_count = count_words(user_input)

        # Output Display
        print(f"Word count: {word_count}")
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
