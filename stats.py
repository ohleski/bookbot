def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return f"{file_contents}"

def get_num_words(text):
    num_words = len(text.split())
    return num_words

def get_num_chars(text):
    text = text.lower()
    char_map = {}
    for chr in text:
        if chr in char_map:
            char_map[chr] = char_map[chr] + 1
        else:
            char_map[chr] = 1
    return char_map

def sort_char_count(char_dict):
    char_list = []
    for key, value in char_dict.items():
        char_list.append({"char": key, "num": value})
    char_list.sort(key=lambda item: item["char"])
    return char_list

def sort_char_list_by_num(char_list):
    char_list.sort(reverse=True, key=lambda item: item["num"])
    return char_list
