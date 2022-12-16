from queues import Queue

print("\n----- First In - First Out Queue (Queue Data Type) -----")

fifo = Queue("1st", "2nd", "3rd")
print("\nEnqueueing Process:")
print("Length of queue (initial):", len(fifo))

print("\nPrinting each element, First in-First Out:")
for element in fifo:
    print(">> ", element)
print("\nDequeueing Process:")
print("Length of queue (final):", len(fifo))