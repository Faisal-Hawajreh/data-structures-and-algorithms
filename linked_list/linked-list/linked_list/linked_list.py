class Node:

    def __init__(self,value):
        self.value = value
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None

    def append(self,node):
        if self.head is None:
            self.head = node
        
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
    


    def insert(self,node):
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node



    def includes(self, value):
        if self.head is None:
            return False
        else :
            current = self.head
            while current.value != value:
                if current.next is None: 
                    return False
                current = current.next
            return True



    def __str__(self) :
        output = ""
        if self.head is None:
            output = "Empty linked list"
        else: 
            current = self.head
            while(current):
                output+= f'{current.value} -->'
                current = current.next
            
            output+= "None"
        return output


if __name__ == "__main__":
    ll = linked_list()
    mustafa = Node("Mustafa")
    zaid = Node("Zaid")
    hind = Node("Hind")
    faisal = Node("Faisal")
    ll.insert(mustafa)
    ll.insert(zaid)
    ll.insert(hind)
    ll.insert(faisal)
    print(ll.includes("Hi"))
    print(ll)


