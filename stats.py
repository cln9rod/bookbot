def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_char_counts(char_counts):
    # Create a list of dictionaries for alpha characters only
    filtered_list = [
        {"char": char, "num": count}
        for char, count in char_counts.items()
        if char.isalpha()
    ]
    
    # Sort the list by 'num' descending
    filtered_list.sort(key=lambda x: x['num'], reverse=True)
    
    return filtered_list