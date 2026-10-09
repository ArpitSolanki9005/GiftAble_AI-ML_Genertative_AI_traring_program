#  Create a queue to manage customers waiting for service. Add three customers to the queue, then serve them one by one in FIFO order (First In, First Out).
#  customers = ["Joe", "John", "Mary"]

customers = ["Joe", "John", "Mary","Mac"]

queue = []

# Add customers to the queue
for customer in customers:
    queue.append(customer)

# Serve customers one by one
while queue:
    customer = queue.pop(0)
    print("Serving:", customer)