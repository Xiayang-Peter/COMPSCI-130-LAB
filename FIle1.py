from Class import WordScore,FileScore

file_score1 = FileScore("text.txt")
print(type(file_score1))
print(type(file_score1.get_word_score(0)))
print(file_score1.get_word_score(0))