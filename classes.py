import math
#!#

#stack#
class Stack:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items).replace("]"," <-")

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            raise IndexError("ERROR: The stack is empty!")

    def peek(self):
        try:
            return self.items[-1]
        except IndexError:
            raise IndexError("ERROR: The stack is empty!")
    

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []

    def push_list_from_last(self,a_list):
        a = ""
        for index in range(len(a_list) - 1,-1,-1):
            self.push(a_list[index])

    def pop_two_and_subtract(self):
        try:
            sub1 = self.items[-1]
            sub2 = self.items[-2]
            self.pop()
            self.pop()
            self.push(sub1 - sub2)
        except IndexError:
            raise IndexError("ERROR: The stack is empty!")
#stack#

class ParkingSlot:
    def __init__(self, size=1):
        self.parking_spaces = [ParkingSpace(space_id) for space_id in range(size)]
        
    def get_available(self):
        for space in self.parking_spaces:
            if space.is_available():
                return space
        return None
        
    def check_availability(self):
        return sum(1 for space in self.parking_spaces if space.is_available())
    
    def mark_as_occupied(self):
        available_space = self.get_available()
        if available_space is None:
            print("Sorry, this parking slot is full")
        else:
            available_space.mark_as_occupied()
    
    def __str__(self):
        info = "Parking Slot:\n"
        for space in self.parking_spaces:
            info += str(space) + "\n"
        return info.rstrip("\n")

# Placeholder for the ParkingSpace class implementation
class ParkingSpace:
    def __init__(self, space_id):
        self.space_id = space_id
        self.occupied = False
    
    def is_available(self):
        return not self.occupied
    
    def mark_as_occupied(self):
        self.occupied = True
    
    def __str__(self):
        availability = "available" if not self.occupied else "occupied"
        return f"Parking Space {self.space_id}: {availability}"


#!#



"""#Class11# #Parking#
class ParkingSlot:
    def __init__(self, slot = 1):
        self.list = []
        self.list_full = []
        self.dict = {}
        for index in range(0,slot):
            self.list.append(index)
            self.list_full.append(index)
            self.dict.update({index:0})
        self.slot = slot

        
    def get_available(self):
        for index in self.list:
            if ParkingSpace(index).is_available:
                return ParkingSpace(index)
            else:
                return None
    def check_availability(self):
        self.available = 0
        for index in self.list:
            if ParkingSpace(index).is_available:
                self.available += 1
            else:
                pass
        return self.available

    def mark_as_occupied(self):
        for slots in self.list:
            if ParkingSpace(slots).is_available:
                a = ParkingSpace(slots)
                a.mark_as_occupied()
                self.dict.update({slots:a})
                return
            else:
                return "Sorry, this parking slot is full"     
    
    def __str__(self):
        output = "Parking Slot:"
        for slots in self.list:
            if self.dict[slots] != 0:
                output += "\n" + str(self.dict[slots])
            else:
                output += "\n" + str(ParkingSpace(slots)) 
        return output
            
#Class11# #Parking#

#Class10# #Parking#
class ParkingSpace:
    def __init__(self, space_id = 1):
        self.space_id = space_id
        self.available = True
    def is_available(self):
        if self.available:
            return True
        else:
            return False
    def mark_as_occupied(self):
        self.available = False
    def __str__(self):
        if self.available:
            return(f"Parking Space {self.space_id}: available")
        else:
            return(f"Parking Space {self.space_id}: occupied")

#Class10# #Parking#
"""
#Class9# #Book#
class Book:
    def __init__(self, title):
        self.title = title
        self.authors = []
    def add_author(self,auther):
        self.authors.append(auther)
    def __str__(self):
        stri = ""
        for index in range(0,len(self.authors)):
            if index == 0:
                stri += str(self.authors[index])
            else:
                stri += ", " + str(self.authors[index])
        if self.authors != []:
            return(f"Title: {self.title} by {stri}")
        else:
            return (f"Title: {self.title}")
#Class9# #Book#

#Class8# #Auther#
class Circle:
    def __init__(self, radius=1):
        self.radius = radius

    def get_area(self):
        return 3.14159 * self.radius * self.radius

    def __str__(self):
        return f"A circle with a radius of {self.radius:.2f}cm."

##
class Cone:
    def __init__(self, radius=1, slant_height=1):
        self.radius = radius
        self.slant_height = slant_height
        self.base_circle = Circle(radius)

    def get_total_surface_area(self):
        base_area = self.base_circle.get_area()
        lateral_area = 3.14159 * self.radius * self.slant_height
        return lateral_area + base_area

    def __str__(self):
        return f"A cone with a base circle area of {self.base_circle.get_area():.2f}cm2 and a slant height of {self.slant_height:.2f}cm."

"""class Cone:
    def __init__(self, radius = 1, slant_height = 1):
        Cone.radius = radius
        Cone.slant_height = slant_height
        Cone.base_circle = math.pi * self.radius ** 2
    def __str__(self):
        return(f"A cone with a base circle area of {Cone.base_circle:.2f}cm2 and a slant height of {Cone.slant_height:.2f}cm.")
    def get_total_surface_area(self):
        return math.pi * self.radius * self.slant_height + Cone.base_circle
    #def get_total_surface_area():"""
#Class7# #Cone#


#Class7# #Cone# #!#
 
#Class5# #TicTacToe#
class TicTacToe:
    def __init__(self,line = "         "):
        self.board = []
        for index in range(0,9,3):
            self.board.append(line[index:index + 3])
    def __str__(self):
        return(f"-------\n|{self.board[0][0]}|{self.board[0][1]}|{self.board[0][2]}|\n-------\n|{self.board[1][0]}|{self.board[1][1]}|{self.board[1][2]}|\n-------\n|{self.board[2][0]}|{self.board[2][1]}|{self.board[2][2]}|\n-------\n")
    def check_row_win(self,check):
        for index in range(0,3,):
            if self.board[index][0] == self.board[index][1] == self.board[index][2] == check:
                return True
        else:
            return False
    def check_column_win(self,check):
        for index in range(0,3):
            if self.board[0][index] == self.board[1][index] == self.board[2][index] == check:
                return True
        else:
            return False
    def check_diagonals_win(self,check):
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == check:
            return True
        elif self.board[0][-1] == self.board[1][-2] == self.board[2][-3] == check:
            return True
        else:
            return False
    def check_win(self, check): #!# Check the Result of the diagonals, row and column
        return self.check_column_win(check) or self.check_diagonals_win(check) or self.check_row_win(check)
#Class5# #TicTacToe#


#Class4# #Polygonal Numbers#
class PolygonalNumber:
    def __init__(self,sides = 1,terms = 1):
        self.s = sides
        self.n = terms
        lists = []
        for i in range(1,self.n + 1):
            lists.append(round(((self.s - 2) * (i ** 2) - (self.s - 4) * i) / 2 ))
        self.numbers = lists
    def __str__(self):
        return(f"The polygon numbers are {self.numbers}.")
#Class4# #Polygonal Numbers#

    #Group3# #Comparison symble#
    def __eq__(self,other):
        while isinstance(other,Pyramid) and isinstance(self,Pyramid):
            return (self.length,self.height,self.width) == (other.length,other.height,other.width)
        else:
            return False
    def __lt__(self, other):
        while isinstance(other,Pyramid) and isinstance(self,Pyramid):
            return (self.length,self.height,self.width) < (other.length,other.height,other.width)
        else:
            return False
    def __le__(self, other):
        while isinstance(other,Pyramid) and isinstance(self,Pyramid):
            return (self.length,self.height,self.width) <= (other.length,other.height,other.width)
        else:
            return False
    def __gt__(self, other):
        while isinstance(other,Pyramid) and isinstance(self,Pyramid):
            return (self.length,self.height,self.width) > (other.length,other.height,other.width)
        else:
            return False
    def __ge__(self, other):
        while isinstance(other,Pyramid) and isinstance(self,Pyramid):
            return (self.length,self.height,self.width) >= (other.length,other.height,other.width)
        else:
            return False

    #Group3# #Comparison symble#

#Class2# 
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def translate(self,dx,dy):
        self.x += dx
        self.y += dy
    def __str__(self):
        return f"({self.x},{self.y})"
#Class1# 


#Class2# 
class Square:
    def __init__(self,side_length):
        self.side_length = side_length
    def get_perimeter(self):
        return (self.side_length * 4)
    def __str__(self):
        return(f"{self.side_length} x {self.side_length} Squre")
    def __repr__(self):
        return(f"Square({self.side_length})")
#Class2# 


#Class3# 
class Fraction:
    def __init__(self,numerator = 0,denominator = 1):
        self.numerator = numerator
        self.denominator = denominator
    def __repr__(self):
        return(f"Fraction({self.numerator},{self.denominator})")
    def __str__(self):
        return(f"{self.numerator}/{self.denominator}")
    def __add__(self,other):
        new_num = self.numerator * other.denominator + self.denominator * other.numerator
        new_den = self.denominator * other.denominator
        return Fraction(new_num,new_den)
#Class3#
 
#Class4#
class Pyramid:
    #Group1#
    def __init__(self,base_length = 1,base_width = 1,height = 1):
        self.length = base_length
        self.width = base_width
        self.height = height
    def __repr__(self):
        return(f"Pyramid({self.length}, {self.width}, {self.height})")
    def __str__(self):
        return(f"A pyramid with a base area of {self.length * self.width} and a volume of {(self.length * self.width * self.height / 3):.2f}.")
    #Group1#

    #Group2#
    def get_base_length(self):
        return(self.length)
    def set_base_length(self, base_length):
        if base_length > 0:
            self.length = base_length
        else:
            pass
    def get_base_width(self):
        return(self.width)
    def set_base_width(self, base_width):
        if base_width > 0:
            self.width = base_width
    def get_height(self):
        return(self.height)
    def set_height(self, height):
        if height > 0:
            self.length = height
    def get_base_area(self):
        return(self.length * self.width)
    def get_volume(self):
        return(self.length * self.width * self.height / 3)
    #Group2#



