
class CommonLetters:
        def __init__(self,first_word = "first",second_word = "second"):
            self.first_word = first_word
            self.second_word = second_word
            self.common_letters = []
            for letter1 in self.first_word:
                for letter2 in self.second_word:
                    if letter1 == letter2 and letter2 not in self.common_letters:
                        self.common_letters.append(letter1)
            self.common_letters.sort()

        def __str__(self):
            s = ""
            for a in self.common_letters:
                s += a            
            return(f"{self.first_word}, {self.second_word} ({s})")

        def set_first_word(self, first_word):
            new = CommonLetters(first_word,self.second_word)
            return new
        
        def set_second_word(self, second_word):
            new = CommonLetters(self.first_word,second_word)
            return new
        
        def get_common_letters(self):
            s = ""
            for a in self.common_letters:
                s += a 
            return s 
                                        
                        


                