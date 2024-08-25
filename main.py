def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(char_count(text))


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
            char_dict[char] += 1
        else:
          char_dict[char] = 1  

    return char_dict

main()