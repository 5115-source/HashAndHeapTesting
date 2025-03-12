#Python has a nice heapq class that allows for use of priority queues
import heapq

def main():
    #Create a list to use as a heap
    minHeap = []
    #Add values to the heap with varying priorities
    minHeap = {0:"banana", 1:"tomato", 2:"apple", 3:"pear", 4:"orange", 5:"guava", 6:"mango", 7:"kiwi", 8:"pomegranate", 9:"pineapple"}
    
    heapq.heappush(minHeap, (0, "banana"))
    
    print("Heap elements (Min-Heap): ", minHeap)

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