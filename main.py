def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dict = count_characters(text)
    char_list = to_list(char_dict)
    char_list.sort(reverse=True, key=sort_on)
    print_report(book_path, num_words, char_list)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_characters(text):
    char_count = {}
    for c in text.lower():
        if c not in char_count:
            char_count[c] = 1
        else:
            char_count[c] += 1
    return char_count

def to_list(dict):
    list = []
    for i in dict:
        if i.isalpha():
            list.append({"char": i,"count": dict[i]})
    return list

def sort_on(dict):
    return dict["count"]

def print_report(path, word_count, char_list):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    for c in char_list:
        char = c["char"]
        count = c["count"]
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")

main()
