class node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.reght=None
class Bst():
    def __init(self,root):
        self.root=None
    def addnode(self,root,value):
        newnode=node(value)
        if self.root==None:
            self.root=newnode
            return self.root
        if value<root.data:
            if root.left==None:
                root.left=newnode(value)
            else:
                self.addnode(root.left,value)
        else:
            if root.right==None:
                root.right=newnode(value)
            else:
                self.addnode(root.right,value)
l=list(map(int,input().split()))
s=Bst()
for i in range(len(l)):
    s.root=s.addnode(s.root,l[i])