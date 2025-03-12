#Python has a nice heapq class that allows for use of priority queues
import heapq

#I didn't think that any part of this main method was long enough to justify separating it into separate methods, but I did separate functionality by line breaks
def main():
    #Create an empty list to use as a heap and add values to the heap with varying priorities (the lower the number the higher the priority)
    minHeap = []
    values = [2, 4, 6, 5, 7, 0, 9, 1, 3, 8]
    for value in values:
        heapq.heappush(minHeap, value)  
    print("Heap elements (Min-Heap): ", minHeap, "\n")
    
    #The element in the heap that is at the first index is the smallest value in the heap (min heap)
    smallestElement = minHeap[0]
    print("Smallest element in the heap: ", smallestElement, "\n")
    
    #Remove five elements in priority order from the heap
    print("Elements removed from the heap: ", end = "")
    i = 5
    while i != 0:
        removedElement = heapq.heappop(minHeap)
        print(removedElement, end = " ")
        i -= 1
        
    #User input without any error checking because this is just a sample program using a hash map
    userInput = input("Enter numbers to insert into the heap (space-separated): ")
    #Chat GPT was really useful in getting line 28 just right
    addNumbers = list(map(int, userInput.split()))
    for addNumber in addNumbers: 
        heapq.heappush(minHeap, addNumber)
    print("\nHeap after insertions: ", minHeap)
    
#If there is a main method, run it
if __name__ == "__main__":
    main()