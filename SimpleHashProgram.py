#In python the use of the built in dict class is useful for working with hash maps
def main():
    #Create a hash map, add some values to it, and print the initial state of the hash map
    hashMap = dict()
    hashMap = {0:"banana", 1:"tomato", 2:"apple", 3:"pear", 4:"orange", 5:"guava", 6:"mango", 7:"kiwi", 8:"pomegranate", 9:"pineapple"}
    print("Initial HashMap Contents: ", hashMap)

    userInput(hashMap)
    
#Ask user for input to edit the hash map in different ways
def userInput(hashMap):
    #User input without any error checking because this is just a sample program using a hash map
    key = int(input("Enter the key (integer) to search for a fruit: "))
    print("The fruit corresponding to the key", key, "is: ", hashMap[key] )
    
    #Remove a given key from the hash map and print the resulting hash map
    removalKey = int(input("Enter the key to remove from the HashMap: "))
    hashMap.pop(removalKey)
    print("After removing key", removalKey, "the HashMap contents are: ", hashMap)
    
#If there is a main method, run it
if __name__ == "__main__":
    main()