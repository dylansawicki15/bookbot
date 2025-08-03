def count_words(text):
    return len(text.split())

def count_characters(text):
    counts = {}
    for char in text.lower():
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def map_character_dict(char_dict):
    return_array = []
    for char, num in char_dict.items():
        return_array.append({"char": char, "num": num})
    return return_array
