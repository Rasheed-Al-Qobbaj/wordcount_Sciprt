import sys
from tqdm import tqdm
from collections import Counter
import re
import os

def get_word_count(filename, case_insensitive=False, exclude_stop_words=False):
    """
    Counts the occurrences of each word in a given text file.

    Args:
        filename (str): The path to the text file to be processed.
        case_insensitive (bool): Whether to count words in a case-insensitive manner.
        exclude_stop_words (bool): Whether to exclude common stop words from the count.

    Returns:
        Counter: A Counter object containing the word counts.
    """
    word_count = Counter()
    total_lines = sum(1 for _ in open(filename, 'r'))

    stop_words = set()
    if exclude_stop_words:
        stop_words = set([
            "the", "and", "is", "in", "to", "of", "a", "that", "it", "on", "for", "with", "as", "was", "at", "by", "an",
            "be", "this", "which", "or", "from", "but", "not", "are", "have", "they", "you", "we", "his", "her", "their",
            "has", "had", "will", "would", "can", "could", "should", "may", "might", "must", "shall"
        ])

    with open(filename, 'r') as file:
        with tqdm(total=total_lines, desc="Processing lines", unit="line") as pbar:
            for line in file:
                words = re.findall(r'\w+', line)
                if case_insensitive:
                    words = [word.lower() for word in words]
                if exclude_stop_words:
                    words = [word for word in words if word not in stop_words]
                word_count.update(words)
                pbar.update(1)

    return word_count

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python script.py <filename> [--case-insensitive] [--exclude-stop-words]")
        sys.exit(1)

    filename = sys.argv[1]
    if not os.path.isfile(filename):
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)

    case_insensitive = '--case-insensitive' in sys.argv
    exclude_stop_words = '--exclude-stop-words' in sys.argv

    word_count = get_word_count(filename, case_insensitive, exclude_stop_words)
    print(f"Total word count: {sum(word_count.values()):,}")
    for word, count in word_count.most_common(10):
        print(f"{word}: {count:,}")
