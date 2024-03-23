n = list(input())
lis_num =[int(i) for i in n ]
lis_odd = [i for i in lis_num if i%2!=0]
list_even = [i for i in lis_num if i%2==0]
print(sum(list_even),sum(lis_odd),end="")
