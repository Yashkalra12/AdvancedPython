class BinarySearchTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def add_child(self,data):
        if data==self.data:
            return

        if data<self.data:
            if self.left:
                self.left.add_child(data) 
            else:
                self.left=BinarySearchTreeNode(data)    
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right=BinarySearchTreeNode(data)            
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
    
    def calculate_sum(self):
        left_sum= self.left.calculate_sum() if self.left else 0
        right_sum= self.right.calculate_sum() if self.right else 0

        return self.data + left_sum + right_sum
    
    def in_order_traversal(self):
        elements=[]

        #Visit left node
        if self.left:
            elements+=self.left.in_order_traversal()

        #Visit     
        elements.append(self.data)

        #Visit right node
        if self.right:
            elements+=self.right.in_order_traversal()

        return elements
    
    def pre_order_traversal(self):
        elements=[]
        #Visit     
        elements.append(self.data)
        #Visit left node
        if self.left:
            elements+=self.left.pre_order_traversal()
        #Visit right node
        if self.right:
            elements+=self.right.pre_order_traversal()

        return elements
    
    def post_order_traversal(self):
        elements=[]
        #Visit left node
        if self.left:
            elements+=self.left.post_order_traversal()
        #Visit right node
        if self.right:
            elements+=self.right.post_order_traversal()
        #Visit     
        elements.append(self.data)

        return elements
    
    def search(self,value):
        if self.data==value:
            return True
        if value<self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False    
        if value>self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False     
            

    def delete(self,value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)
        else:  # Found the node to delete
            if self.left is None and self.right is None:
                return None  # Node has no children
            elif self.left is None:
                return self.right  # Node has only right child
            elif self.right is None:
                return self.left  # Node has only left child
            else:
                # Node has both left and right children
                # Find the minimum value in the right subtree
                min_value = self.right.find_min()
                self.data = min_value
                # Delete the node with the minimum value in the right subtree
                self.right = self.right.delete(min_value)
        return self
        
        
def build_tree(elements):
    root=BinarySearchTreeNode(elements[0])
    for i in range(len(elements)):
        root.add_child(elements[i])

    return root    
         
if __name__=='__main__':
    numbers=[17,4,1,20,9,23,18,34]
    numbers_tree= build_tree(numbers)
    print(f'Maximum_Value: {numbers_tree.find_max()}')
    print(f'InOrder: {numbers_tree.in_order_traversal()}')
    numbers_tree.delete(34)
    print(f'PreOrder: {numbers_tree.pre_order_traversal()}')
    print(f'PostOrder: {numbers_tree.post_order_traversal()}')
    print(f'Minimum_Value: {numbers_tree.find_min()}')
    print(f'Maximum_Value: {numbers_tree.find_max()}')
    print(f'Sum: {numbers_tree.calculate_sum()}')
    print(numbers_tree.search(9))