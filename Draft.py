from Class import WordScore

def selection_sort(word_scores):
    for pass_num in range(len(word_scores)-1, 0, -1):
        position_largest = 0
        for i in range(1,pass_num+1):
            if word_scores[i]>word_scores[position_largest]:
                position_largest=i
        word_scores[i],word_scores[position_largest]=word_scores[position_largest],word_scores[i]
        a = ""
        for elements in word_scores:
            a += f"{elements} "
        print(a)



a_list = [WordScore('trees')]
selection_sort(a_list)
for word_score in a_list:
    print(word_score, end = ' ')
print("DONE")