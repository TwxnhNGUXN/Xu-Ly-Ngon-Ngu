import json
from symspellpy import SymSpell, Verbosity

def load_single_characters(filename="vietnam74K.txt"):
    single_characters = set()
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                word = line.strip().lower()
                single_characters.add(word)
    except Exception as e:
        print(f"Error loading file {filename}: {e}")
    return single_characters

def initialize_symspell():
    sym_spell = SymSpell()
    dictionary_path = 'dictionary.txt'
    bigram_dictionary_path = 'dictionary_bigram.txt'

    try:
        if not sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1, separator=' ', encoding='utf-8'):
            raise RuntimeError(f"Failed to load dictionary file: {dictionary_path}")
        if not sym_spell.load_bigram_dictionary(bigram_dictionary_path, term_index=0, count_index=1, separator=' ', encoding='utf-8'):
            raise RuntimeError(f"Failed to load bigram dictionary file: {bigram_dictionary_path}")
    except Exception as e:
        print(f"Error initializing SymSpell: {e}")

    return sym_spell

# Cài đặt biến toàn cục cho hiệu suất tối ưu
single_characters = load_single_characters()
sym_spell = initialize_symspell()

def get_wrong_text(text):
    words = text.lower().split()
    wrong_text = [word for word in words if word not in single_characters]
    return wrong_text

def get_correct_text(word):
    suggestions = sym_spell.lookup(word, Verbosity.CLOSEST, max_edit_distance=2, include_unknown=True)
    return [suggestion.term for suggestion in suggestions]
