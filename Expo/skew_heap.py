#Python code implementation
 
class SkewHeap:
    def __init__(self):
        self.key = 0
        self.right = None
        self.left = None
 
    # the special merge function that's used 
    # in most of the other operations also
    def merge(self, h1, h2):
        # If one of the heaps is empty
        if h1 is None:
            return h2
        if h2 is None:
            return h1
 
        # Make sure that h1 has smaller key.
        if h1.key > h2.key:
            h1, h2 = h2, h1
 
        # Swap h1.left and h1.right
        h1.left, h1.right = h1.right, h1.left
 
        # Merge h2 and h1.left and make 
        # merged tree as left of h1.
        h1.left = self.merge(h2, h1.left)

        return h1
 
    # function to construct heap using values in the array
    def construct(self, root, heap, n):
        for i in range(n):
            temp = SkewHeap()
            temp.key = heap[i]
            root = self.merge(root, temp)
        return root
 
    # function to print the Skew Heap, as it is 
    # in form of a tree so we use
    # tree traversal algorithms
    def inorder(self, root):
        if root is None:
            return
        else:
            self.inorder(root.left)
            print(root.key, end="  ")
            self.inorder(root.right)
 
# Driver Code
if __name__ == "__main__":
    # Construct two heaps
    heap, temp1, temp2 = SkewHeap(), None, None
    heap1 = [12, 5, 10]
    heap2 = [3, 7, 8, 14]
    n1 = len(heap1)
    n2 = len(heap2)
    temp1 = heap.construct(temp1, heap1, n1)
    temp2 = heap.construct(temp2, heap2, n2)
 
    # Merge two heaps
    temp1 = heap.merge(temp1, temp2)
 
    print("The heap obtained after merging is:")
    heap.inorder(temp1)
 
# This code is contributed by karthik.
