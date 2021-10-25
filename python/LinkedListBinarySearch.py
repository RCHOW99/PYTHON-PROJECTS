class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def insert(newItem, head):
    newnode = Node(newItem)
    if head == None:
        head = newnode
        return head
    else:
        current = head
        while current.next is not None:
            current = current.next
        current.next = newnode
        return head


def printSTRUCTURE(currentNode):
    while currentNode is not None:
        print(currentNode.data,end=" ")
        currentNode = currentNode.next


def length(head):
    probe = head
    count = 0
    while probe is not None:
        count += 1
        probe = probe.next
    return count


def traverse(num, searchlist):
    for i in range(num - 1):
        # The range is num - 1 because the loop already starts with one node ahead.
        searchlist = searchlist.next
    return searchlist.data


def linkedlistbinarysearch(searchlist, key):
    high = length(searchlist)
    low = 0
    while high >= low:
        mid = (high + low) // 2
        midv = traverse(mid, searchlist)
        # print("High: ", high, " Low: ", low, " Mid: ", mid, "Mid #: ", midv)
        if key > midv:
            low = mid + 1
        elif key < midv:
            high = mid - 1
        else:
            # print(mid)
            return mid


Array = [2, 3, 6, 7, 9, 13, 45, 78]


head = None
for i in Array:
    head = insert(i, head)

printSTRUCTURE(head)


num = int(input("\nEnter your desired number\n"))
nodenum = linkedlistbinarysearch(head,num)
print(num,"is in node", nodenum)
