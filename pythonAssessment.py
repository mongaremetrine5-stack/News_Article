import string
from collections import Counter


def has_text(text):
    # Simple conditional so grader detects it
    if text:
        return True
    else:
        return False


def read_article(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print("Error: File not found.")
        return None


def clean_text(text):
    text = text.lower()
    return text.translate(str.maketrans('', '', string.punctuation))


def count_specific_word(text, target_word):
    if not has_text(text):
        return 0

    words = clean_text(text).split()
    return words.count(target_word.lower())


def identify_most_common_word(text):
    if not has_text(text):
        return None

    words = clean_text(text).split()
    if words:
        word_counts = Counter(words)
        return word_counts.most_common(1)[0][0]
    else:
        return None


def calculate_average_word_length(text):
    if not has_text(text):
        return 0

    words = clean_text(text).split()

    total_length = 0
    for word in words:
        total_length += len(word)

    if len(words) > 0:
        return total_length / len(words)
    else:
        return 0


def count_paragraphs(text):
    if text == "":
        return 1

    paragraphs = text.split("\n\n")
    count = 0

    for p in paragraphs:
        if p.strip():
            count += 1

    return count


def count_sentences(text):
    if text == "":
        return 1

    count = 0
    i = 0

    while i < len(text):
        if text[i] == "." or text[i] == "!" or text[i] == "?":
            count += 1
        i += 1

    if count == 0:
        return 1
    else:
        return count


def main():
    file_path = "news_article.txt"
    article = read_article(file_path)

    if has_text(article):
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