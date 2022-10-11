# method to create a queue 
# initialize all information in the queue dictionary
def createQueue(queue, capacity):
    if type(queue) is not type(dict()):
            print('CreateQueue method expected queue argument')
            return
    if capacity is None:
            print('CreateQueue method expected capacity argument')
            return 
    queue['Queue'] = []
    queue['Capacity'] = capacity
    queue['IsEmptyQueue'] = None
    queue['IsFullQueue'] = None
    queue['RetValue'] = None
    queue['FirstValue'] = None

# method to check whether the queue is emtpy or not
def isEmptyQueue(queue):
    if type(queue) is not type(dict()):
            print('IsEmptyQueue method expected queue argument')
            return
    queue['IsEmptyQueue'] = len(queue['Queue']) == 0
    
# method to check whether the queue is full or not
def isFullQueue(queue):
    if type(queue) is not type(dict()):
            print('IsFullQueue method expected queue argument')
            return
    
    queue['IsFullQueue'] = len(queue['Queue']) == queue['Capacity']

# method to dequeue the first value in the stack
def dequeue(queue):
    if type(queue) is not type(dict()):
        print('Dequeue method expected queue argument')
        return
    isEmptyQueue(queue)
    if queue['IsEmptyQueue']:
        print("Queue is empty")
        return 
    else:
        queue['RetValue'] = queue['Queue'].pop(0)

# method to enqueue a value into the queue
def enqueue(queue, value):
    if type(queue) is not type(dict()):
        print('Enqueue method expected queue argument')
        return
    if value is None:
        print('Enqueue method expected value argument')
        return
    isFullQueue(queue)
    if queue['IsFullQueue']:
        print("Queue is full")
        return 
    else:
        queue['Queue'].append(value)

# method to get the first value of the queue
def getFirstValue(queue):
    if type(queue) is not type(dict()):
        print('GetFirstValue method expected stack argument')
        return
    isEmptyQueue(queue)
    if queue['IsEmptyQueue']:
        print("Queue is empty")
        return
    else: 
        queue['FirstValue'] = queue['Queue'][0]

def simQueue(method_name, queue=None, capacity=None, value=None):
    if method_name == "CreateQueue":
       createQueue(queue, capacity)

    elif method_name == "IsEmptyQueue":
        isEmptyQueue(queue)

    elif method_name == "IsFullQueue":
        isFullQueue(queue)

    elif method_name == "Dequeue":
        dequeue(queue)
    elif method_name == "Enqueue":
        enqueue(queue, value)

    elif method_name == "GetFirstValue":
        getFirstValue(queue)
    
    else:
        print(f"{method_name} is not support")
        
queue1 = {
    'Queue' : [],
    'Capacity' : None,
    'IsEmptyQueue' : None,
    'IsFullQueue' : None,
    'RetValue' : None,
    'FirstValue' : None
}

simQueue(queue=queue1, method_name="CreateQueue", capacity=5)

# queue1.enqueue(1)
simQueue(queue=queue1, method_name="Enqueue", value=1)

# queue1.enqueue(2)
simQueue(queue=queue1, method_name="Enqueue", value=2)

# print(queue1.IsFullQueue())
simQueue(queue=queue1, method_name="IsFullQueue")
print(queue1["IsFullQueue"])

# print(queue1.front())
simQueue(queue=queue1, method_name="GetFirstValue")
print(queue1["FirstValue"])

# print(queue1.dequeue())
simQueue(queue=queue1, method_name="Dequeue")
print(queue1["RetValue"])

# print(queue1.front())
simQueue(queue=queue1, method_name="GetFirstValue")
print(queue1["FirstValue"])

# print(queue1.dequeue())
simQueue(queue=queue1, method_name="Dequeue")
print(queue1["RetValue"])

# print(queue1.IsEmptyQueue())
simQueue(queue=queue1, method_name="IsEmptyQueue")
print(queue1["IsEmptyQueue"])


#output: False
          #1
          #1
          #2
          #2
        #True
