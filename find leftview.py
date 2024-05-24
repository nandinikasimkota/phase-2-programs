def findLeftView(root):
    if root == None:
        return []
    result = []
    Q = [root]
 
    while len(Q) > 0:
        n = len(Q)
        for i in range(n):
            curr = Q.pop(0)
            if i == 0:
                result.append(curr.data)
            if curr.left != None:
                Q.append(curr.left)
 
            if curr.right != None:
                Q.append(curr.right)
    return result
 
def findRightView(root):
    if root == None:
        return []
    result = []
    Q = [root]
 
    while Q:
        n = len(Q)
        for i in range(n):
            curr = Q.pop(0)
            if i == n - 1:
                result.append(curr.data)
            if curr.left != None:
                Q.append(curr.left)
 
            if curr.right != None:
                Q.append(curr.right)
    return result
 
def topViewHelper(root, store, hd, level):
    if root == None:
        return 
 
    if hd not in store or store[hd][0] > level:
        store[hd] = [level, root.data]
 
    topViewHelper(root.left, store, hd - 1, level + 1)
    topViewHelper(root.right, store, hd + 1, level + 1)
 
def findTopView(root):
    result = []
    if root == None:
        return result
 
    store = {}
    topViewHelper(root, store, 0, 0)
    sortedKeys = sorted(store.keys())
    for key in sortedKeys:
        result.append(store[key][1])
    return result
 
def bottomViewHelper(root, store, hd, level):
    if root == None:
        return 
 
    if hd not in store or store[hd][0] < level:
        store[hd] = [level, root.data]
 
    bottomViewHelper(root.left, store, hd - 1, level + 1)
    bottomViewHelper(root.right, store, hd + 1, level + 1)
 
def findBottomView(root):
    result = []
    if root == None:
        return result
 
    store = {}
    bottomViewHelper(root, store, 0, 0)
    sortedKeys = sorted(store.keys())
    for key in sortedKeys:
        result.append(store[key][1])
    return result