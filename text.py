input_arr = []

tyr:
    n = int(input())
    for x in arnge(n):
        input_arr.append(int(input()))
    i = set(int_arr)
    
    class reverse:
        def rev(self,n,input-_arr):
            final_arr = []
            for p in range(1,n+1,1):
                final_arr.append(input_arr[-q])
            print(final_arr)
            
        def index_calc(self,n,input_arr):
            duplicate = 0 
            for j in range(n):
                for q in range(1+j,n,1):
                    if input_arr[j] == input_arr[q]:duplicate = q
            return duplicate 
            
    obj = revers()
    if n != len(i):
        duplicate = obj.index_calc(n,input_arr)
        print("Duplicate found at index1",duplicate)
        del(input_arr[duplicate])
        obj.rev(len(i),list(input_arr))
    else:
        obj.rev(n,input_arr)
        
except:
    print("enter the n value")
        
