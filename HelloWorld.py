##print("Hello World")

#x = 5
#y = "Five is greater than two!"
#if x > 2: #this is to test if x is greater than 2
   # print(y)

#x = str(3) #declares x as a string
#X = "Sally" #X will not override x - python is case sensitive in this case.
#print(type(x)) 

#snake_case = "Naming format should be done in snake_case, not camelCase"
#a, b, c = "Orange", "Banana", "Cherry"
#print(a)
#print(b)
#print(c)
#a, b, c = "Orange"

#fruits = ["apple", "banana", "cherry"] #This is called a tuple/collection, it is packed.
#x, y, z = fruits #A tuple/collection can be unpacked
#print(x + y + z) #You can use addition signs to output, but only work for same data types
#print(x, y, z) #You can also use commas

#x = "awesome"
#def myfunc(): 
#  x = "fantastic" #A variable can be created wthin the function, this function is local.
#  print("Python is " + x)
#myfunc()
#print("Python is " + x)

#def myfunc():
#    global x #The global keyword makes it so the variable will not be local
#    x = "fantastic"

#myfunc()
#print("Python is " + x)

#q = 35e3 #A float can be used for a number with decimals and numbers in scientific notation
#print(type(q))
#u = 4
#u = float(u) #Convert data type from in to float
#import random
#print(random.randrange(1,10))
#e = int(2.8) #Casting will cut off decimals result will be 2.
#w = float(1) #Converts to float, x will be 1.0
#p = str("28.2") #Saves as string

#a = """Lorem ipsum dolor sit amet, #Multiline string
#consectetur adipiscing elit,
#sed do eiusmod tempor incididunt
#ut labore et dolore magna aliqua."""
#print(a)
#b = "Hello, World!"
#print(b[1]) #To access a specific characters
#for x in "banana":
#   print(x)
#print(len(b))

#txt = "The best things in life are free!"
#print("free" in txt) #Print a word in a string
#if "free" in txt: #Can can also search a string to see if a certain word is present
#   print("Yes, 'free' is present")
#print("expensive" not in txt) #Will test if a word is not in the string
#if "expensive" not in txt: #You can also use this in an if statement
#   print("No, 'expensive' is NOT present.") 

#b = "Hello, World!"
#print(b[2:5]) #Prints letters contained in the slice
#print(b[:5]) #The starting index can also be left out - it will start from the beginning
#print(b[2:]) #You can also slice from a point to the end of the string
#print(b[-5:-2]) #You can also index from the end of the string using negative indexing - working backwards from the end
#print(b.upper()) #Print in uppercase
#print(b.lower()) #Print in lowercase
#print(b.strip()) #Removes extra space ex. " Hello, World! " --> "Hello, World!"
#print(b.replace("H", "J")) #Replaces first string in quotes with second.
#print(b.split(",")) #Splits string

#d = "Hello, "
#e = "World!"
#c = d + e #String concatanation
#print(c)

#age = 36
#txt = "My is is John, and I am {}" #How to set up different variable types with a string.
#print(txt.format(age))

#quantity = 3 
#itemno = 567
#price = 49.95
#myorder = "I want {2} pieces of item {0} for {1} dollars." #You can put any amount of arguements in format
#print(myorder.format(quantity, itemno, price)) #You can also assign index numbers.

#txt = "We are the so-called \"Vikings\" from the north."
#print(txt) #Escape characters allow you to print illegal charcters such as double quotes.

#a = 200 #print(10>9) #Booleans can be evalutated to true or false
#if b > a: #Booleans can also be used in if statements to determine true/false.
#    print("b is greater than a")
#else:
#   print("b is not greater than a")
#print(bool("Hello")) #Evaluates if a value is entered
#print(bool(15))  #Evaluates if a number has been entered, 0 will return false
#x = "Hello"
#y = 15
#print(bool(x))
#print(bool(y))

#class myclass(): #Will also return false if object is made of a class with __len__ in it.
#   def __len__(self):
#      return 0
#myobj = myclass()
#print(bool(myobj))

#def myFunction() : #You can also get a function to return a bool
#  return True
#print(myFunction())
#if myFunction():
#   print("YES!")
#else:
#   print("NO!)")
#x = 200
#print(isinstance(x, int))

#print(10 + 5) #Python operators
#Most of the operators and assignment operators should be fimiliar
#x = 7
#print(x < 5 and x < 10) #Can be used to test if multiple conditions are true
#print(x > 6 or x < 1) #Can be used to test if one of the conditions is true
#print(not(x > 3 and x < 10)) #not is used to reverse the result
#y = 6
#print(x is y) #Prints if the variables are the same
#print(x is not y) #Tests if the variables are not the same
#p = ["apple", "banana"]
#print("banana" in p) #Tests if object is in a tuple
#print("orange" not in p) #Tests if an object is not in a tuple

mylist = ["apple","banana", "cherry"] #Lists, sets, dictionary, and tuples hold collections of data
#print(mylist)
#mylist = ["apple","banana", "cherry", "apple"] #Lists can contain duplicqates because they are indexed
#print(len(mylist)) #You get get the length of a list
list1 = [True, "orange", 6, 8, 14, False, "grape"] #Lists can contain different data types.
#print(type(list1)) #All lists are considered data type 'list'
#List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#Dictionary is a collection which is ordered** and changeable. No duplicate members.
#print(list1[1]) #You can print items from lists via indexing
#print(list1[-1]) #You can also use negative indexing to print from the end
#print(list1[1:4]) #Used to print a range of indexes. *Note 4 is not included but 1 is
#print(list1[3:]) #Prints from index 3 to the end
#print(list1[-4:-2]) #Prints a range of negative indexes
#if "apple" in mylist: #You can test if apple is in mylist
#   print("Yes, 'apple' is in this list")
