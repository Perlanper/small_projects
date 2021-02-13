def insertion_sort(inpt):
    outpt = list()
    for i in range(len(inpt)):
        if isempty(outpt):
            insert(outpt,i, inpt[i])
        else:
            for j in range(len(outpt)):
                if inpt[i] <= outpt[j]:
                    insert(outpt, j, inpt[i])
                else:
                    continue #prolly not needed
    return outpt

def isempty(inpt):
    if inpt == None:
        return True
    return False

def insert(target, i, inpt):
    temp = target[i]
    target[i] = inpt
    for i in range(len(target)):
        target[i+1] = temp 
        temp = target 
        


def main():
    inpt = [4,5,2,6,8,1,9,3,6,8,1,3,0,2]
    result = insertion_sort(inpt)
    print(result)
