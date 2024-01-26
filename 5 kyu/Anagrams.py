def anagrams(word, words):
    isAnagram = []

    for i in words:
        if len(i) == len(word):
            temp = [char for char in i]
            for letter in word:
                if letter in temp:
                    temp.remove(letter)

            if not temp:
                isAnagram.append(i)

    return isAnagram