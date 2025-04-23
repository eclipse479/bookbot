def get_word_count(text_to_use):
    number_of_words = text_to_use.split()
    return len(number_of_words)


def sort_on(dict):
    return dict["count"]

def sort_dictionary(dictionary_to_sort):
    dictionary_list = []
    for entry in dictionary_to_sort:
        temp_dictionary = {"character":entry, "count":dictionary_to_sort[entry]}
        dictionary_list.append(temp_dictionary)

    dictionary_list.sort(reverse=True,key=sort_on)
    return dictionary_list
        

def number_of_characters(text_to_use, key=sort_on):
    character_dictionary = {}
    lowercase_text = text_to_use.lower()

    for character in lowercase_text:
        if character in character_dictionary:
            character_dictionary[character] += 1
        else:
            character_dictionary[character] = 1
    sorted_dictionary = sort_dictionary(character_dictionary)
    return sorted_dictionary
