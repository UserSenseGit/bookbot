def sort_on(item):
    return item[1]

def counting_words(text):
    words = text.split()
    count = len(words)
    return (f"Found {count} total words")  

def counting_characters(text: str) -> dict[str, int]:

    counts: dict[str, int] = {}
    
    for char in text.lower():
        if char in counts:
            counts[char] += 1
        else: 
            counts[char] = 1

    return (counts)

def chars_dict_to_sorted_list(counts):
    results = []
    for ch, n in counts.items():
            results.append((ch,n))
    results.sort(key=sort_on, reverse=True)
    return results
