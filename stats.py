def getBookText(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents
        # print(file_contents)

def word_count(file_contents):
    number_of_words = len(file_contents.split())
    return number_of_words

def character_count(file_contents):
    char_count = {}
    for char in file_contents.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def print_report(file_contents):
    word_c = word_count(file_contents)
    char_count = character_count(file_contents)
    sorted_char_count = dict(sorted(char_count.items(), key=lambda item: item[1], reverse=True))
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at file given")
    print("----------- Word Count ----------")
    print(f"Found {word_c} total words")
    print("--------- Character Count -------")
    for char in sorted_char_count:
        if char.isalpha() == True:
            value = sorted_char_count[char]
            print(f"{char}: {value}")
    print("============= END ===============")

