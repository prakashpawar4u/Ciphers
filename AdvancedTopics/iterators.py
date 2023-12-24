# Iterators
# An iterator is an object that can be iterated upon which means that you can traverse through all the values. Lists, tuples, dictionaries, and sets are all iterable objects.

# To create an object as an iterator you have to implement the methods __iter__() and __next__() to your object where —

# __iter__() returns the iterator object itself. This is used in for and in statements.

# __next__() method returns the next value in the sequence. In order to avoid the iteration to go on forever, raise the StopIteration exception.

# Why use iterators?

# Iterators allow us to create and work with lazy iterable which means you can use an iterator for the lazy evaluation. This allows you to get the next element in the list without re-calculating all of the previous elements. Iterators can save us a lot of memory and CPU time.

# Python has many built-in classes that are iterators, e.g — enumerate, map ,filer , zipand reversed etc. objects are iterators.





# class example_range:
#     def __init__(self, n):
#         self.i = 4
#         self.n = n
    
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.i < self.n:
#             i = self.i
#             self.i +=1
#             return i
#         else:
#             raise StopIteration()
        
# n = example_range(10)
# print(list(n))

class remoteControl():
    def __init__(self):
        self.index = -1
        self.channels = ["HBO", "CNN", "MGM", "Starsport", "ESPN"]
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.index += 1
        if self.index == len(self.channels):
            raise StopIteration
        return self.channels[self.index]

r = remoteControl()
itr = iter(r)
# print (next(itr))
# print (next(itr))
# print (next(itr))
# print (next(itr))
# print (next(itr))
# print (next(itr))
# print (next(itr))

for i in itr : 
    print (i, end=',\n')

