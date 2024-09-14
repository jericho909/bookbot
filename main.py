def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = word_counter(text)
    print(f"{word_count} words found in document")
    list_of_dicts = dict_to_list(char_count(text))
    sorted_list_of_dicts = sorted(list_of_dicts, key=lambda d: list(d.values())[0], reverse= True)


    for k in sorted_list_of_dicts:
        for key,value in k.items():
            print(f"The {key} character was found {value} times.")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_counter(text):
    word_list = text.split()
    return len(word_list)

def char_count(text):
    lower_text = text.lower()
    char_dict = {

    }
    for char in lower_text:
        if char in char_dict:
            if char.isalpha():
                char_dict[char] += 1
        else:
          char_dict[char] = 1  

    return char_dict

def dict_to_list(dict):
    list_of_dicts = [{key: value} for key, value in dict.items()]
    return list_of_dicts


main()