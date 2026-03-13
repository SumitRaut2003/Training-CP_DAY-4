# for i in range(1,5):
#     if i== 3:
#         break
#     print(i)
# break terminates the loop no further execution occurs 

# for i in range(1,5):
#     if i== 3:
#         continue
#     print(i)

# continue skips the iteration 


# for i in range(1,6):
#     if i== 3:
#         continue
#     print(i)


# for i in range(5,0,-1):
#     if i==3:
#         continue
#     print(i)

# using zip function 

for i,j in zip(range(1,6),range(5,0,-1)):
    if i==3 and j==3:
        continue
    print(i,j)