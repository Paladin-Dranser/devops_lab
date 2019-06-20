def is_one_row(word: str, row: tuple) -> bool:
    for letter in word:
        if letter.lower() not in row:
            return False
    else:
        return True


top_row = tuple('qwertyuiop')
middle_row = tuple('asdfghjkl')
bottom_row = tuple('zxcvbnm')

words = list(input().split())

one_row_words = list()
for word in words:
    if (
            is_one_row(word, top_row) or
            is_one_row(word, middle_row) or
            is_one_row(word, bottom_row)
       ):
        one_row_words.append(word)

print(*one_row_words)
