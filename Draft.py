from Class import CircularQueue,Stack

try:
    q1 = CircularQueue(4)
    q1.enqueue("A")
    print(q1)
    q1.enqueue("B")
    print(q1)
    print("Dequeued item: ", q1.dequeue())
    print(q1)
    print("Dequeued item: ", q1.dequeue())
    print(q1)
    print("Full?", q1.is_full())
    print("Empty?", q1.is_empty())
except IndexError as err:
    print(err) 