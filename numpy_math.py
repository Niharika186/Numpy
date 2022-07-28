# import numpy as np
# a = np.array([[9,8,7],
#              [4,5,6]])
# b = np.array([[11,12,13],
#              [14,15,16]])
# print(a+b)        # [[20 20 20]
                    #  [18 20 22]]
# print(a-b)        # [[ -2  -4  -6]
                    #  [-10 -10 -10]]
# print(a*b)        # [[99 96 91]
                    #  [56 75 96]]
           
# a=np.eye(2)
# b=np.eye(2,dtype=int)
# c=np.eye(2,dtype=bool)
# print(a)      # [[1. 0.]
                # [0. 1.]]
# print(b)     # [[1 0]
               # [0 1]]
# print(c)      # [[ True False]           
                # [False  True]]
                
# x=np.array ([[2,4,6],
#             [1,3,5]])
# y=x.astype('float')
# print(y)   # [[2. 4. 6.] 
           # [1. 3. 5.]]
 
# x=np.array ([[0,1,0],
            #  [1,0,1]])
# y=x.astype('bool')
# print(y)        # [[False  True False] 
                  #  [ True False  True]]

# a=[[1,2,3],
#    [4,5,6]]
# b=[[7,8,9],
#    [9,8,7]]
# c=np.array(a)+np.array(b)
# print(c)  #  [[ 8 10 12] 
            #   [13 13 13]]
            
# a=np.array([x for x in range(9)])
# b=a.reshape([3,3])  
# print(b)       # [[0 1 2] 
               #  [3 4 5] 
               #  [6 7 8]]  
            
# a=np.array([[1,2,3],
#             [4,5,6]])
# b=np.array([[9,8,7],
#            [6,5,4]])
# c=np.hstack([a, b])            
# print(c)       # [[1 2 3 9 8 7] 
               #  [4 5 6 6 5 4]]    
            
# a=np.array([[1,2,3],
#             [4,5,6],
#             [7,8,9]])
# b=np.array([[9,8,7],
#            [6,5,4],
#            [3,2,1]])
# c=np.vstack((a, b))           
# print(c)            
            
# n=np.arange(1,50,2)   
# print(n)   # [ 1  3  5  7  9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49 ]
      
# v=np.full((3,3),8)          
# print(v)   # [[8 8 8] 
#            #  [8 8 8] 
             #  [8 8 8]]
             
# p=np.array([[1,2,3],
#             [4,5,6],
#             [7,8,9]])
# q=np.array([[9,8,7],
        #    [6,5,4],
        #    [3,2,1]]) 
# r=(p@q)  
# s=np.matmul(p,q)
# print(r)     #  [[ 30  24  18] 
               #   [ 84  69  54] 
               #   [138 114  90]]   
# print(s)     #  [[ 30  24  18] 
               #   [ 84  69  54] 
               #   [138 114  90]]                       