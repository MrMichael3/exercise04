def element_type(tuple,position):
    return type(tuple[position])

t = (1, "python", 2.5, [9, 8, 7], {1: "One", 2: "Two", 3: "Three"}, (1,))
print(element_type(t, 0))  # prints: <class: 'int'>
print(element_type(t, 1))  # prints: <class: 'str'>
print(element_type(t, 2))  # prints: <class: 'float'>
print(element_type(t, 3))  # prints: <class: 'list'>
print(element_type(t, 4))  # prints: <class: 'dict'>
print(element_type(t, 5))  # prints: <class: 'tuple'>