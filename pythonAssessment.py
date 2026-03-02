import string
from collections import Counter


def read_article(file_path):
    """Reads and returns the content of a text file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print("Error: File not found.")
        return None


def clean_text(text):
    """Converts text to lowercase and removes punctuation."""
    text = text.lower()
    return text.translate(str.maketrans('', '', string.punctuation))


# ---------------- REQUIRED FUNCTIONS FOR TESTS ---------------- #

def count_specific_word(text, target_word):
    """Counts how many times a specific word appears."""
    if not text:
        return 0

    words = clean_text(text).split()
    return words.count(target_word.lower())


def identify_most_common_word(text):
    """Finds the most frequently occurring word."""
    if not text:
        return None

    words = clean_text(text).split()
    if not words:
        return None

    word_counts = Counter(words)
    return word_counts.most_common(1)[0][0]


def calculate_average_word_length(text):
    """Calculates the average word length."""
    if not text:
        return 0

    words = clean_text(text).split()
    if not words:
        return 0

    total_length = 0
    for word in words:  
        total_length += len(word)

    return total_length / len(words)


def count_paragraphs(text):
    """Counts paragraphs based on blank lines."""
    if not text.strip():
        return 0

    paragraphs = text.strip().split("\n\n")
    count = 0

    for p in paragraphs:  
        if p.strip():
            count += 1

    return count


def count_sentences(text):
    """Counts sentences based on ., !, ?"""
    if not text:
        return 0

    sentence_endings = ['.', '!', '?']
    count = 0
    i = 0

    
    while i < len(text):
        if text[i] in sentence_endings:  
            count += 1
        i += 1

    return count


# ---------------- MAIN PROGRAM ---------------- #

def main():
    file_path = "news_article.txt"
    article = read_article(file_path)

    if article is not None:  
        print("\n--- TEXT ANALYSIS RESULTS ---\n")

        word_to_count = "Python"
        print("Using test word:", word_to_count)

        print(f"Occurrences of '{word_to_count}': {count_specific_word(article, word_to_count)}")

        common_word = identify_most_common_word(article)
        print(f"Most common word: '{common_word}'")

        print(f"Average word length: {calculate_average_word_length(article):.2f}")

        print(f"Number of paragraphs: {count_paragraphs(article)}")

        print(f"Number of sentences: {count_sentences(article)}")


if __name__ == "__main__":
    main()