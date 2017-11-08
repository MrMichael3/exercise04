def word_count(a):
    counter = 1
    for x in a:
        if x  == " ":
            counter += 1
    return "The string has %d words" %(counter)





text = "A list, similarly to a tuple, is an ordered set of values (or " \
       "elements), where each value is identified by an index. The contained " \
       "values can be of any type and a single list can even contain mixed " \
       "values. The main difference between the twodata structures is that " \
       "lists are mutable."
print(word_count(text)) # prints: "The string has 51 words."