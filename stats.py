def get_num_words(text):
    return len(text.split())

def sort_on(dict):
    return dict["num"]

def get_sorted_dictionaries(dictionaries):
    list = []
    for key in dictionaries:
        new_dict = {}
        new_dict["char"] = key
        new_dict["num"] = dictionaries[key]
        list.append(new_dict)
    list.sort(reverse=True, key=sort_on)
    return list

def get_num_char_apps(text):
    words = text.split()
    appearances = {}
    for word in words:
        for char in word:
            char = char.lower()
            if (not char in appearances):
                appearances[char] = 1
            else:
                appearances[char] += 1
    return appearances
