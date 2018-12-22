# linkedList.py
# this file provides an example of how to create a
# linked list data structure in python

# classes ===============================
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    # getter and setter class methods for the data field
    def get_data(self): return self.val
    def set_data(self, val): self.val = val
    
    # getter and setter class methods for the next pointer
    def get_next(self): return self.next
    def set_next(self, next): self.next = next


class LinkedList(object):
    def __init__(self, head = None):
        self.head = head  # head node loc
        self.count = 0    # # nodes in list

    def get_count(self):
        return self.count

    # insert items at head of list
    def insertAtHead(self, data):
        new_node = Node(data)
        new_node.set_next(self.head) # first node will have next of None
        self.head = new_node
        self.count += 1

    def find(self, val):
        # start search at head of linked list
        item = self.head
        
        # if you find the search item, return it
        while (item != None):
            if item.get_data() == val:
                return item
            else:
                item = item.get_next()
        
        # if you don't find the search item, return none
        return None

    def deleteAt(self, idx):
        # return None if delete loc is out of linked list range
        if idx > self.count:
            return
        
        # return None if head is only node in list
        if self.head == None:
            return
        
        # delete node idx by removing its linking
        # and leave orphaned mem space for cleaner
        else:
            tempIdx = 0
            node = self.head
            while tempIdx < idx-1:
                node = node.get_next()
                tempIdx += 1
            node.set_next(node.get_next().get_next())
            self.count -= 1

    # print the contents of the linked list
    def dump_list(self):
        tempnode = self.head
        while (tempnode != None):
            print("Node: ", tempnode.get_data())
            tempnode = tempnode.get_next()

# main ==================================
def main():
    # create a linked list and insert some items
    itemlist = LinkedList()
    itemlist.insertAtHead(38)
    itemlist.insertAtHead(49)
    itemlist.insertAtHead(13)
    itemlist.insertAtHead(15)
    
    # look at the contents of the list
    itemlist.dump_list()
    print("Item count: ", itemlist.get_count())
    
    # find loc of items if exist
    print("Finding item: ", itemlist.find(13))
    print("Finding item: ", itemlist.find(78))
    
    # delete an item
    itemlist.deleteAt(3)
    
    # look at the contents of the list again
    itemlist.dump_list()
    print("Item count: ", itemlist.get_count())
    
    # find loc of an item if exists
    print("Finding item: ", itemlist.find(38))
    
    print('Done.')
    
if __name__=='__main__': main()