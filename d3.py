class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class genString:
    def __init__(self):
        self.string = ""

    def reset(self):
        self.string = ""

    def addToString(self,inp):
        self.string=self.string+str(inp)

    def toString(self):
        return self.string

temp = ""

def serialize(root):
    global temp
    srlze(root,0)

    return temp

def srlze(root,count):
    global temp
    print(count)
    print(root.val)
    if(root.val=="root"):
        temp+="N"
    if(root.left==None and root.right==None):
        if(root.val[-5:].replace('.','')=='right'):
            temp = temp + "1"
        if(root.val[-5:].replace('.','')=='left'):
            temp = temp + "2"
        #print(root.val)
    if(root.left!=None):
        temp = temp + "L"
        srlze(root.left,count+1)
    if(root.right!=None):
        temp = temp + "R"
        srlze(root.right,count+1)

    return "done"

def deserialize(string):
    pass

node = Node('root', Node('left', Node('left.left'), Node('left.right')), Node('right'))
print(serialize(node))


#assert deserialize(serialize(node)).left.left.val == 'left.left'

'''
def serialize(root):
    temp = ""
    global temp
    if(root.val=="root"):
        temp+="N"
    if(root.left==None and root.right==None):
        if(root.val[-5:].replace('.','')=='right'):
            temp = temp + "1"
        if(root.val[-5:].replace('.','')=='left'):
            temp = temp + "2"
        #print(root.val)
    if(root.left!=None):
        temp = temp + "L"
        serialize(root.left)
    if(root.right!=None):
        temp = temp + "R"
        serialize(root.right)

'''
