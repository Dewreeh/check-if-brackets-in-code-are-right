class custom_stack:
   def __init__(self):
       self.items = []
   def push(self, item):
       self.items.append(item)
   def pop(self):
       self.items.pop()
   def is_empty(self):
       return len(self.items) == 0
   def size(self):
       return len(self.items)
   def top(self):
     return self.items[len(self.items) - 1]
    
def is_balanced(string):
    stack = custom_stack()
    position_stack = custom_stack()
    for i in range(0, len(string)):
        char = string[i]
        if (char == "(" or char == "[" or char == "{"):
            stack.push(char)
            position_stack.push(i);
        elif (char == ")" or char == "]" or char == "}"):
            if stack.is_empty(): return i + 1
            top = stack.top()
            stack.pop()
            if(top == "(" and char != ")"
               or top == "[" and char != "]"
               or top == "{" and char != "}"): return i + 1
            position_stack.pop();
            
    return  True if stack.is_empty() else position_stack.top()
file = open("test.txt", "r")
print(is_balanced("some input"))
