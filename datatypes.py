# Write a program to manipulate List data

V=['Hero','Honda','Bajaj','Suzuki','Yamaha',1,2,3,4,5]
print("\nList V :",V[:])

print("\nList V : 2 to 5",V[2:6])

print("\nList V in reverse:",V[::-1])

V.append('Vehicals')
print("\nList V after appending  :",V[:])

V.insert(3,'TVS')
print("\nList V after inserting  :",V[:])

V.pop(1)
print("\nList V after poping :",V[:])

V.remove('Suzuki')
print("\nList V after removing :",V[:])

del V[0]
print("\nList V after deleteing :",V[:])

V.clear()
print("\nList A after clearing :",V[:])

# Write a program to manipulate Tuple data

C=("Xiaomi","Realme","Vivo","Oppo","Honor","Xiaomi","Techno",101,102,103,104)

print("\nTuple C:",C)

print("\nTuple C: 2 to 5",C[2:6])

print("\nTuple C in reverse:",C[::-1])

print("\nCount of Xiaomi is :",C.count('Xiaomi'))

print("\nIndex of Realme is",C.index('Realme'))