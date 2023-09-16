class CircularQueue:
    def __init__(self, empty_value = 8):
        self.item = [None] * empty_value
        self.capacity = empty_value
        self.count = 0        
        self.front = 0                                  #front and back index value
        self.back = self.capacity - 1
    def is_empty(self):
        if  self.back > self.front:
            return True
        else:
            for i in self.item:
                if i == None:
                    pass
                else:
                    return False
            return True
    def is_full(self):
        return None not in self.item
    def show_contents(self):
        return(f"{self.item}, front:{self.front}, back:{self.back}, count:{self.count}")
    
    def enqueue(self, item):
        if self.is_full():
            raise IndexError("ERROR: The queue is full.")
        else:
            self.back = (self.back + 1) % self.capacity
            self.item[self.back] = item
            self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("ERROR: The queue is empty.")
        else:
            dequeue_item = self.item[self.front]
            self.front = (self.front + 1) % self.capacity
            self.count -= 1
        return dequeue_item
        


    def __str__(self):
        print(self.item)
        print(self.front)
        print(self.back)
        a = "-> |"
        for i in range(self.back,self.front - 1,-1):
            if (i != self.front) and self.item[i] != None:
                a += f"{self.item[i]}, "
            elif self.item[i] != None:
                a += f"{self.item[i]}"
            else:
                pass
        a += "| ->"
        return a



class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0, item)                
    def dequeue(self):
        if self.is_empty():
            raise IndexError("ERROR: The queue is empty!")
        else:
            return self.items.pop()  
    def peek(self):
        if self.is_empty():
            raise IndexError("ERROR: The queue is empty!")
        else:
            return self.items[len(self.items) - 1]
    def size(self):
        return len(self.items)   
    def clear(self):
        self.items = []

    def enqueue_list_from_last(self, a_list):
        for i in range(len(a_list) - 1,-1,-1):
            self.enqueue(f"{a_list[i]}")

    def __str__(self):
        st = str(self.items)
        a = st.replace("[","-> |").replace("]","| -> ")
        return a

    


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


""" OLD
class CircularQueue:
    def __init__(self, empty_value = 8):
        self.item = [None] * empty_value
        self.capacity = empty_value
        self.count = 0        
        self.front = 0                                  #front and back index value
        self.back = self.capacity - 1
    def is_empty(self):
        for i in self.item:
            if i == None:
                pass
            else:
                return False
        return True
    def is_full(self):
        return None not in self.item
    def show_contents(self):
        return(f"{self.item}, front:{self.front}, back:{self.back}, count:{self.count}")
    
    def enqueue(self, item):
        if self.is_full():
            raise IndexError("ERROR: The queue is full.")
        else:
            self.back = (self.back + 1) % self.capacity
            self.item[self.back] = item
            self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("ERROR: The queue is empty.")
        else:
            dequeue_item = self.item[self.front]
            self.front = (self.front + 1) % self.capacity
            self.count -= 1
        return dequeue_item

    def __str__(self):
        a = "-> |"
        for i in range(self.back,self.front - 1,-1):
            if (i != self.front) and self.items[(self.front + i) % self.capacity] != None:
                a += f"{self.items[(self.front + i) % self.capacity]}, "
            elif self.item[i] != None:
                a += f"{self.items[(self.front + i) % self.capacity]}"
            else:
                pass
        a += "| ->"
        return a



"""