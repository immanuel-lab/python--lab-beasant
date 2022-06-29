# l1={1,2,3}
# l2={5,6}
# l3=l1^l2
# print(l3)

#& applicable for int and bool types only

>>> A = {0, 2, 4, 6, 8};
>>> B = {1, 2, 3, 4, 5};

>>> print("Union :", A | B)  
Union : {0, 1, 2, 3, 4, 5, 6, 8}

>>> print("Intersection :", A & B)
Intersection : {2, 4}

>>> print("Difference :", A - B)
Difference : {0, 8, 6}

# elements not present both sets
>>> print("Symmetric difference :", A ^ B)   
Symmetric difference : {0, 1, 3, 5, 6, 8}