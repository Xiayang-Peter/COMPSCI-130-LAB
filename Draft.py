class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    def __str__(self):
        return str(self.data)
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    def set_data(self, new_data):
        self.data = new_data
    def set_next(self, new_next):
        self.next = new_next
    def add_after(self, value):
        current = self.next
        self.next = Node(value)
        self.next.set_next(current)
    def add_list_from_last(self, a_list):
        current_end = self.set_next
        for i in range(len(a_list)):
            self.add_after(a_list[i])
    def get_vowels(self):
        a = ""
        for i in self.data:
            if i in "aeiuo":
                a += i
        return a 
    
def print_node_chain(node):
    if node.next != None:
        print(node,end = " ")
        print_node_chain(node.next)
    else:
        print(node)

def get_reversed(node):
    if node.next == None:
        return [f"{node}"]
    else:
        return get_reversed(node.next) + [f"{node}"]

def get_node_chain(node):
    if node.next == None:
        return [f"{node}"]
    else:
        return [f"{node}"] + get_node_chain(node.next)

def get_all_vowels(node):
    a = get_node_chain(node)
    b = []
    for elements in a:
        c = ""
        for letters in elements:
            if letters in "aeiou":
                c += letters
        b.append(c)
    return b 

def reverse_node_chain(node):
    new_list = get_node_chain(node)
    a = Node(new_list[-1])
    for index in range(0,len(new_list) - 1):
        a.add_after(new_list[index])
    return a 

	
	
node1 = Node(1)
node2 = Node(2)
node1.set_next(node2)
result = reverse_node_chain(node1)
print_node_chain(result)
print_node_chain(node1)