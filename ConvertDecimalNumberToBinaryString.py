def generateBinaryString(n):
    queue1 = {
    'Queue' : [],
    'Capacity' : None,
    'IsEmptyQueue' : None,
    'IsFullQueue' : None,
    'RetValue' : None,
    'FirstValue' : None
    }

    results = {}
    if n > 0:
        simQueue(queue=queue1, method_name="CreateQueue", capacity=n+1)

        simQueue(queue=queue1, method_name="Enqueue", value="1")

        
        for i in range(1, n + 1):
            simQueue(queue=queue1, method_name="Dequeue")
            bin1 = queue1["RetValue"]
            results[i] = bin1
            
            simQueue(queue=queue1, method_name="Enqueue", value=bin1+"0")
            simQueue(queue=queue1, method_name="Enqueue", value=bin1+"1")
    else:
        print("n must be greater than 0")
        return
    return results
    
    
generateBinaryString(16)

#output: {1: '1',
         #2: '10',
         #3: '11',
         #4: '100',
         #5: '101',
         #6: '110',
         #7: '111',
         #8: '1000',
         #9: '1001',
        #10: '1010',
        #11: '1011',
        #12: '1100',
        #13: '1101',
        #14: '1110',
        #15: '1111',
        #16: '10000'}
