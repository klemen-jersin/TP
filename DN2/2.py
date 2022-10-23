our_list = [1,2,3,4,5,6,7]
our_list.remove(5)

#print(our_list)

our_dict = {
    "a": 2,
    "b": 5,
    "c": 8,
    "d": 12,
    "e": 357,
    "f": 12
}
our_dict["d"]= 5
print(our_dict)

our_tuple = (357, 12, 12, 8, 5, 2, 2)

our_tuple2 = list(our_tuple)
our_tuple2.append(our_dict)
our_tuple2 = tuple(our_tuple2)
#print(our_tuple2)
#print(our_tuple)
print(our_tuple==our_tuple2)