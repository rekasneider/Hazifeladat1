class Node:
    def __init__(self, data):
        self.data=data
        self.next=None


class LinkedList:
    head=None
    def appendFront(self, data):
        new_e=Node(data)
        new_e.next=self.head
        self.head=new_e


    def appendBack(self, data):
        new_e=Node(data)
        if self.head is None:
            self.head=new_e
        else:
            current_item=self.head
            while current_item.next is not None:
                current_item=current_item.next
            current_item.next=new_e


    def removedata(self, element):
        tmp=self.head
        previous=None
        while tmp is not None:
            if tmp.data==element:
                if previous is None:
                    self.head=self.head.next
                else:
                    previous.next=tmp.next
            previous=tmp
            tmp=tmp.next


    def append(self, data, afterthis):
        new_e=Node(data)
        tmp=self.head
        afterthis=Node(data)
        while tmp is not None:
            if tmp.data==afterthis:
                new_e.next=afterthis.next
                afterthis.next=new_e
            tmp=tmp.next



    def show(self):
        tmp=self.head
        print('A lista elemei')
        while tmp is not None:
            print(tmp.data, '->', end="")
            tmp=tmp.next
        print('None')



s=LinkedList()
s.appendBack(22)
s.appendBack(23)
s.appendBack(24)
s.append(25,22)

s.show()