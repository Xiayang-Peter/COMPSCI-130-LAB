from classes import Stack

def simple_balanced_brackets(text):
    a = Stack()
    #b = Stack()
    try:
        for i in range(0,len(text),):
            if text[i] == "(":
                a.push("(")
            elif text[i] == ")":
                a.pop()
        if a.is_empty():
            return True
        else: return False
    except:
        return False
        

print(simple_balanced_brackets('(x)(())()'))

"""    for i in range(0,len(text),1):
        if text[i] == "(" or text[i] == "'":
            a.push(text[i])
    print(a)
    for i in range(0,len(text),1):
        if text[i] == ")" or text[i] == "'":
            b.push(text[i])
    print(b)
"""

