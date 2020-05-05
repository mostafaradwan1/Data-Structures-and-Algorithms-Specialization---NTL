from queue import LifoQueue


def balanced_brackets(stri):
    stack = LifoQueue()
    for index,char in enumerate(stri,start=1):
        if char in '([{':
            stack.put(stri[index])
        elif char in '}])':
            if stack.empty():
                return index 
            print(char)
            
            top = stack.get()
            print(top)
            if (top == '(' and char != ')') or (top == '[' and char != ']') or (top == '{' and char != '}'):
                return index 

    if stack.empty():
        return 'Success'
    else:
        return stri.index(stack.get())
        


stri = input()

print(balanced_brackets(stri))
