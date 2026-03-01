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


def count_word(text, target_word):
    """Counts how many times a specific word appears."""
    words = clean_text(text).split()
    return words.count(target_word.lower())


def most_common_word(text):
    """Finds the most frequently occurring word."""
    words = clean_text(text).split()
    word_counts = Counter(words)
    return word_counts.most_common(1)[0]


def average_word_length(text):
    """Calculates the average word length."""
    words = clean_text(text).split()
    total_length = sum(len(word) for word in words)
    return total_length / len(words) if words else 0


def count_paragraphs(text):
    """Counts paragraphs based on blank lines."""
    paragraphs = text.strip().split("\n\n")
    return len([p for p in paragraphs if p.strip()])


def count_sentences(text):
    """Counts sentences based on ., !, ?"""
    sentence_endings = ['.', '!', '?']
    count = 0
    for char in text:
        if char in sentence_endings:
            count += 1
    return count


def main():
    file_path = "news_article.txt"  
    article = read_article(file_path)

    if article is None:
        print("\n--- TEXT ANALYSIS RESULTS ---\n")

        word_to_count = "Python"
        print("Using test word:", word_to_count)

        print(f"Occurrences of '{word_to_count}': {count_word(article, word_to_count)}")

        common_word, frequency = most_common_word(article)
        print(f"Most common word: '{common_word}' (appears {frequency} times)")

        print(f"Average word length: {average_word_length(article):.2f}")

        print(f"Number of paragraphs: {count_paragraphs(article)}")

        print(f"Number of sentences: {count_sentences(article)}")


if __name__ == "__main__":
    main()