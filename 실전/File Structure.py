class File:
    def __init__(self, name):
        self.name = name
        self.type = "F"

class Directory:
    def __init__(self, name):
        self.name = name
        self.content = []
        self.type = "D"
    
# traverse(myDir, [])
def traverse(dir, res):
    for n in dir.content:
        if n.type == "F":
            res.append(n.name)
        else:
            res.append(n.name)
            if n.content:
                traverse(n, res)
    return res


def traverseBFS(mainDir):
    queue = [mainDir]
    visited = []
    res = []
    while queue:
        curr = queue.pop(0)
        visited.append(curr)
        if curr.type == "F":
            res.append(curr.name)
        else:
            res.append(curr.name)
            for n in curr.content:
                if n not in visited and n not in queue:
                    queue.append(n)
    return res[1:]


def traverseDFS(mainDir):
    stack = [mainDir]
    visited = []
    res = []
    while stack:
        curr = stack.pop()
        visited.append(curr)
        if curr.type == "F":
            res.append(curr.name)
        else:
            res.append(curr.name)
            for n in curr.content:
                if n not in visited and n not in stack:
                    stack.append(n)
    return res[1:]




myDir = Directory('myDir')
subDir1 = Directory('subDir1')
subDir2 = Directory('subDir2')
subDir3 = Directory('subDir3')
subDir1.content.append(File('subDir1_File1'))
subDir1.content.append(File('subDir1_File2'))
subDir1.content.append(subDir3)
subDir2.content.append(File('subDir2_File1'))
subDir3.content.append(File('subDir3_File1'))
myDir.content.append(File('File1'))
myDir.content.append(File('File2'))
myDir.content.append(File('File3'))
myDir.content.append(subDir1)
myDir.content.append(subDir2)

#print(traverse(myDir,[]))
print(traverseBFS(myDir))
# print(traverseDFS(myDir))



















#---------------------------
# my soln
class File:
    def __init__(self, name):
        self.name = name
        self.type = "F"

class Directory:
    def __init__(self, name):
        self.name = name
        self.content = []
        self.type = "D"
    
# recursive
def traverse(dir):
    res = []
    
    def helper(dir):
        for n in dir.content:
            # file
            if n.type == "F":
                res.append(n.name)
            # directory
            else:
                res.append(n.name)
                if n.content:
                    helper(n)
    
    helper(dir)
    return res
                    
        
    

# iterative using queue
def traverseBFS(mainDir):
    q = deque([mainDir])
    visit = set()
    res = []
    while q:
        n = q.popleft()
        if n not in visit:
            visit.add(n)
            # file
            if n.type == "F":
                res.append(n.name)
            # directory
            else:
                res.append(n.name)
                for c in n.content:
                    q.append(c)
    return res[1:]

# iterative using stack 
def traverseDFS(mainDir):
    stack = [mainDir]
    visit = set()
    res = []
    while stack:
        n = stack.pop()
        if n not in visit:
            visit.add(n)
            if n.type == "F":
                res.append(n.name)
            else:
                res.append(n.name)
                for c in n.content:
                    stack.append(c)
    return res[1:]



myDir = Directory('myDir')
subDir1 = Directory('subDir1')
subDir2 = Directory('subDir2')
subDir3 = Directory('subDir3')
subDir1.content.append(File('subDir1_File1'))
subDir1.content.append(File('subDir1_File2'))
subDir1.content.append(subDir3)
subDir2.content.append(File('subDir2_File1'))
subDir3.content.append(File('subDir3_File1'))
myDir.content.append(File('File1'))
myDir.content.append(File('File2'))
myDir.content.append(File('File3'))
myDir.content.append(subDir1)
myDir.content.append(subDir2)

# print(traverse(myDir))
# print(traverseBFS(myDir))
print(traverseDFS(myDir))