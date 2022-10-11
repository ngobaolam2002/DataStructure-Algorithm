# method to create a stack 
# initialize all information in the stack dictionary
def createStack(stack, capacity):
    if type(stack) is not type(dict()):
            print('createStack method expected stack argument')
            return
    if capacity is None:
            print('CreateStack method expected capacity argument')
            return 
    stack['Stack'] = []
    stack['Capacity'] = capacity
    stack['TopIdx'] = -1
    stack['IsEmptyStack'] = None
    stack['IsFullStack'] = None
    stack['RetValue'] = None
    stack['TopValue'] = None

# method to check whether the stack is emtpy or not
def isEmptyStack(stack):
    if type(stack) is not type(dict()):
            print('IsEmptyStack method expected stack argument')
            return
    if stack['TopIdx'] == -1:
        stack['IsEmptyStack'] = True
    else:
        stack['IsEmptyStack'] = False

# method to check whether the stack is full or not
def isFullStack(stack):
    if type(stack) is not type(dict()):
            print('IsFullStack method expected stack argument')
            return
    if stack['TopIdx'] == stack['Capacity']-1:
        stack['IsFullStack'] = True
    else:
        stack['IsFullStack'] = False

# method to pop the top value in the stack
def popStack(stack):
    if type(stack) is not type(dict()):
        print('PopStack method expected stack argument')
        return
    isEmptyStack(stack)
    if stack['IsEmptyStack']:
        print("Stack is empty")
        return 
    else:
        stack['RetValue'] = stack['Stack'].pop()
        stack['TopIdx'] -= 1

# method to push a value into the stack
def pushStack(stack, value):
    if type(stack) is not type(dict()):
        print('PushStack method expected stack argument')
        return
    if value is None:
        print('PushStack method expected value argument')
        return
    isFullStack(stack)
    if stack['IsFullStack']:
        print("Stack is full")
        return 
    else:
        if stack['IsEmptyStack']: stack['Stack'].append(value)
        stack['TopIdx'] += 1

# method to get the top value of the stack
def getTopValue(stack):
    if type(stack) is not type(dict()):
        print('GetTopValue method expected stack argument')
        return
    isEmptyStack(stack)
    if stack['IsEmptyStack']:
        print("Stack is empty")
        return
    else: 
        stack['TopValue'] = stack['Stack'][stack['TopIdx']]

def simStack(method_name, stack=None, capacity=None, value=None):
    if method_name == "CreateStack":
        createStack(stack, capacity)

    elif method_name == "IsEmptyStack":
        isEmptyStack(stack)

    elif method_name == "IsFullStack":
        isFullStack(stack)

    elif method_name == "PopStack":
        popStack(stack)

    elif method_name == "PushStack":
        pushStack(stack, value)

    elif method_name == "GetTopStack":
        getTopValue(stack)
    else:
        print(f"{method_name} is not support")
        
stack1 = {
    'Stack' : [],
    'Capacity' : None,
    'TopIdx' : -1,
    'IsEmptyStack' : None,
    'IsFullStack' : None,
    'RetValue' : None,
    'TopValue' : None
}


simStack(stack=stack1, method_name="CreateStack", capacity=5)

# stack1.push(1)
simStack(stack=stack1, method_name="PushStack", value=1)

# stack1.push(2)
simStack(stack=stack1, method_name="PushStack", value=2)

# print(stack1.IsFullStack())
simStack(stack=stack1, method_name="IsFullStack")
print(stack1["IsFullStack"])

# print(stack1.top())
simStack(stack=stack1, method_name="GetTopStack")
print(stack1["TopValue"])

# print(stack1.pop())
simStack(stack=stack1, method_name="PopStack")
print(stack1["RetValue"])

# print(stack1.top())
simStack(stack=stack1, method_name="GetTopStack")
print(stack1["TopValue"])

# print(stack1.pop())
simStack(stack=stack1, method_name="PopStack")
print(stack1["RetValue"])

# print(stack1.IsEmptyStack())
simStack(stack=stack1, method_name="IsEmptyStack")
print(stack1["IsEmptyStack"])


#output: False
          #2
          #2
          #1
          #1
         #True
