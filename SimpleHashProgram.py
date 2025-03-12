#In python the use of the built in dict class is useful for working with hash maps


def main():
    #Create a hash map
    hashMap = dict()
    #Add some key value pairs to the hash map
    hashMap = {0:"bananna", 1:"tomato", 2:"apple", 3:"pear", 4:"orange", 5:"guava", 6:"mango", 7:"kiwi", 8:"pomegranate", 9:"pineapple"}
    #Print all entries in the hashMap
    print("Initial HashMap Contents: ", hashMap)

    userInput(hashMap)
    
def userInput(hashMap):
    #User input without any error checking because this is just a sample program using a hash map
    key = int(input("Enter the key (integer) to search for a fruit: "))
    print("The fruit corresponding to the key", key, "is: ", hashMap[key] )
    
    removalKey = int(input("Enter the key to remove from the HashMap: "))
    
    print("After removing key", removalKey, "the HashMap contents are: ", hashMap)
    
#If there is a main method, run it
if __name__ == "__main__":
    main()
