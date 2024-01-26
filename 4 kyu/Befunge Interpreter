import random

def update(char: str) -> list:
    match char:
        case '>':
            return [0, 1]
        case '<':
            return [0, -1]
        case '^':
            return [-1, 0]
        case 'v':
            return [1, 0]
    

def interpret(code):
    output = ""
    stack = []
    code = code.split('\n')
    
    dir = '>'
    index = [0, 0]
    current = code[index[0]][index[1]]
    
    while True:
        match current:
            case _ if current.isnumeric():
                stack.append(current)
            
            case '+':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(a+b)

            
            case '-':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b-a)
            
            case '*':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(a*b)
            
            case '/':
                a = int(stack.pop())
                b = int(stack.pop())
                
                if a == 0:
                    stack.append(0)
                else:
                    stack.append(int(b//a))
            
            case '%':
                a = int(stack.pop())
                b = int(stack.pop())
                
                if a == 0:
                    stack.append(0)
                else:
                    stack.append(b%a)
            
            case '!':
                if str(stack.pop()) == '0':
                    stack.append('1')
                else:
                    stack.append('0')
            
            case '`':
                a = stack.pop()
                b = stack.pop()
                if (b > a):
                    stack.append(1)
                else:
                    stack.append(0)
            
            case '>' | '<' | '^'| 'v':
                dir = current

            case '?':
                dir = random.choice(['>', '<', '^', 'v'])
            
            case '_':
                if str(stack.pop()) == '0':
                    dir = '>'
                else:
                    dir = '<'
                    
            case '|':
                if str(stack.pop()) == '0':
                    dir = 'v'
                else:
                    dir = '^'
            
            case '"':
                index = [sum(x) for x in zip(index, update(dir))]
                current = code[index[0]][index[1]]
                while current != '"':
                    stack.append(ord(current))
                    index = [sum(x) for x in zip(index, update(dir))]
                    current = code[index[0]][index[1]]
                    
            case ':':
                if len(stack) == 0:
                    stack.append('0')
                else:
                    stack.append(stack[-1])
            
            case '\\':
                if len(stack) == 1:
                    stack.insert(0, 0)
                else:
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(a)
                    stack.append(b)
            
            case '$':
                stack.pop()

            case '.':
                output += str(stack.pop())
                    
            case ',':
                value = stack.pop()
                if type(value) == str:
                    output += value
                elif type(value) == int:
                    output += chr(value)
            
            case '#':
                if dir == '>':
                    index[1] += 2
                elif dir == '<':
                    index[1] -= 2
                current = code[index[0]][index[1]]
                continue
            
            case 'p':
                y = int(stack.pop())
                x = int(stack.pop())
                v = int(stack.pop())
                
                code[y] = code[y][:x] + chr(v) + code[y][x+1:]
                
            
            case 'g':
                y = int(stack.pop())
                x = int(stack.pop())
                stack.append(ord(code[y][x]))
            
            case '@':
                break
        
        index = [sum(x) for x in zip(index, update(dir))]
        current = code[index[0]][index[1]]
        
    return output