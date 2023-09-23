from Class import *

	
object1 = CommonLetters()
object2 = CommonLetters('hello', 'world')
print(object1)
print(object2)
object1.set_first_word('hello')
print(object1)
object2.set_second_word('bubble')
print(object2)
object3 = CommonLetters('cat', 'banana')
print(object3)
print(CommonLetters('cat', 'dog'))
data = object2.get_common_letters()
print(type(data))
print(data)