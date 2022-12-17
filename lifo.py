from queues import Stack

print("\n----- Last In - First Out Queue (Queue Data Type) -----")
lifo = Stack("1st", "2nd", "3rd")
print("\nEnqueueing Process:")
print("Length of queue (initial):", len(lifo))

print("\nPrinting each element, First in-First Out:")
for element in lifo:
    print(element)

print("\nDequeueing Process:")
print("Length of queue (final):", len(lifo))

'''
Paste in the interpreter:
lifo = []

lifo.append("1st")
lifo.append("2nd")
lifo.append("3rd")

lifo.pop()
lifo.pop()
lifo.pop()

-----------------------------------

from queues import Stack
lifo = Stack("1st", "2nd", "3rd")
for element in lifo:
    print(element)
'''