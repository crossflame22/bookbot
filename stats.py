def get_num_words(string):
    count = 0
    for word in string.split():
        count += 1
    return count
def get_char_count(string):
    counts = {}
    for character in string:
        char = character.lower()
        if char not in counts:
            counts[char] = 1
        else:
            counts[char] += 1
    return counts
def sort_dictionary(counts):
    items = list(counts.items())
    items.sort(key=lambda item: item[1], reverse=True)
    return items