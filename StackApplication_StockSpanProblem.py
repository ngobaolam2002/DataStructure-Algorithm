def stock_span(test_list):
    # create a stack
    stack1 = {
    'Stack' : [],
    'Capacity' : None,
    'TopIdx' : -1,
    'IsEmptyStack' : None,
    'IsFullStack' : None,
    'RetValue' : None,
    'TopValue' : None
    }
    simStack(stack=stack1, method_name="CreateStack", capacity=len(test_list))

    results = []
    # check emtpy stack
    simStack(stack=stack1, method_name="IsEmptyStack")
    if stack1["IsEmptyStack"]:
        # push current index to the stack
        simStack(stack=stack1, method_name="PushStack", value=0)
        results.append(1)
    else:
        print('Stack is not empty')
        return 

    for idx in range(1, len(test_list)):
        # Pop the stack until 
        # case1 current value < value of index  
        # which is hold in the top of the stack
        # case2 the stack is empty
        simStack(stack=stack1, method_name="GetTopStack")
        while(test_list[idx] >= test_list[stack1["TopValue"]]):
            simStack(stack=stack1, method_name="PopStack")

            # check emtpy stack
            simStack(stack=stack1, method_name="IsEmptyStack")
            if stack1["IsEmptyStack"]:
                results.append(idx+1)
                break

            simStack(stack=stack1, method_name="GetTopStack")
        
        # simStack(stack=stack1, method_name="IsEmptyStack")
        if not stack1["IsEmptyStack"]:
            # get result 
            simStack(stack=stack1, method_name="GetTopStack")
            results.append(idx-stack1["TopValue"])
        
        # push current index to the stack
        simStack(stack=stack1, method_name="PushStack", value=idx)
    return results
  
  prices = [100, 80, 60, 70, 60, 75, 85]
stock_span(prices)

#output: [1, 1, 1, 2, 1, 4, 6]
