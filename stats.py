def get_num_words(book_text):
    words = book_text.split()
    return len(words)

def get_num_char(book_text):
    counter = {}
    for ch in book_text:
        if ch.lower() in counter:
            counter[ch.lower()] += 1
        else:
            counter[ch.lower()] = 1
    return counter

def sort_dictionary(counter):
    res = []
    for key, value in counter.items():
        new_dict = {"char": key, "num": value}
        res.append(new_dict)
    
    def sort_on(items):
        return items["num"]

    res.sort(reverse=True, key=sort_on)
    return res
