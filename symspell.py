from symspellpy import SymSpell, Verbosity

# Khởi tạo và tải từ điển một lần
sym_spell = SymSpell()
sym_spell.load_dictionary('dictionary.txt', term_index=0, count_index=1, separator=' ', encoding='utf-8')
sym_spell.load_bigram_dictionary('dictionary_bigram.txt', term_index=0, count_index=1, separator=' ', encoding='utf-8')

def get_correct_text(text):
    suggestions = sym_spell.lookup(text, Verbosity.CLOSEST)
    results = []
    for suggestion in suggestions:
        results.append(suggestion.term)  
    return results

# Hàm này có thể được gọi nhiều lần mà không cần tải lại từ điển
while True:
    print("Nhập văn bản: ")
    input_text = input()
    if input_text.lower() == 'exit':
        break
    correction_results = get_correct_text(input_text)
    for result in correction_results:
        print(result)
