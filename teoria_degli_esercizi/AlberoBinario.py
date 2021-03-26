class Node:
    def __init__(self, data): #costruttore
        self.left = None
        self.right = None
        self.data = data

      
    def printTreeRoot(self): #stampa la radice dell'albero
        print(self.data)
    

    def insert(self, data): #inserisce un elemento nell'albero
        if self.data: #se la radice esiste
            if data<self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data>self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data=data

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

    
root =Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.insert(33)
root.printTree() #stampa tutti gli elementi
root.printTreeRoot() #stampa las radice
