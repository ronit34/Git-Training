

A = [x for x in input().split()]
# print(A)1,2
B = [x for x in input().split()]
C = [x for x in input().split()]


tuple = set(A).symmetric_difference(set(B))
new_tuple = tuple.symmetric_difference(set(C))
new_list = list(new_tuple)
print(new_list)

