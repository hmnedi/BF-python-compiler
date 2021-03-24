import os
import random

def logo():
    r = random.randint(0, 3)
    lis = [""" ________  ________ 
|\   __  \|\  _____\
\ \  \|\ /\ \  \__/ 
 \ \   __  \ \   __\
  \ \  \|\  \ \  \_|
   \ \_______\ \__\ 
    \|_______|\|__| 
                    
                    
                    """, """ ███████████  ███████████
░░███░░░░░███░░███░░░░░░█
 ░███    ░███ ░███   █ ░ 
 ░██████████  ░███████   
 ░███░░░░░███ ░███░░░█   
 ░███    ░███ ░███  ░    
 ███████████  █████      
░░░░░░░░░░░  ░░░░░       
                         
                         
                         """, """██████╗ ███████╗
██╔══██╗██╔════╝
██████╔╝█████╗  
██╔══██╗██╔══╝  
██████╔╝██║     
╚═════╝ ╚═╝     
                """, """ ▄▄▄▄     █████▒
▓█████▄ ▓██   ▒ 
▒██▒ ▄██▒████ ░ 
▒██░█▀  ░▓█▒  ░ 
░▓█  ▀█▓░▒█░    
░▒▓███▀▒ ▒ ░    
▒░▒   ░  ░      
 ░    ░  ░ ░    
 ░              
      ░         """]

    print(lis[r])
	
def menu():
    print('please choose one of the following options')
    print("\t1) compile\t\t2) Char-ASCII-Words\n\t3) guide line\t\t4) exit\n")
    
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def compile_bf(code):
    mzrb = code.count('>')
    if mzrb > 1000000000:
        mzrb = 1000000000
    elif mzrb == 0:
        mzrb = 1
    mem = [0]*mzrb
    itr = 0

    i = 0
    while i < len(code):
        if code[i] == '+':
            mem[itr] += 1
        if code[i] == '-':
            mem[itr] -= 1
        if code[i] == '>':
            itr += 1
        if code[i] == '<':
            itr -= 1
            
        if code[i] == '[':
            if mem[itr] == 0:
                while code[i] != ']':
                    i += 1
                     
        if code[i] == ']':
            if mem[itr] != 0:
                while code[i] != '[':
                    i -= 1
            
            
        if code[i] == '.':
            print(chr(mem[itr]), end='')
            
        if code[i] == ',':
            tmp = input('> ')
            mem[itr] = ord(tmp)
        i += 1
    
 
    print()
                

print("BF-Compiler is running...\n")
logo()
menu()

cmd = 0
code = ''
while cmd != '4':
    cmd = input('>>> ')
    if cmd == '1':
        cls()
        print("Enter your code below, To exit compiling mode (enter = exit)")
        while True:
            code = input('>>>> ')
            if code == 'exit':
                break
            else:
                compile_bf(code)
        cls()
        menu()
        
    elif cmd == '2':
        cls()
        print("Enter a char, word or an ASCII code, To exit this mode (enter = exit)")
        tmp = ''
        while tmp != 'exit':
            tmp = input('>>>> ')
            if tmp.isdigit():
                print(chr(int(tmp)))
            elif tmp == 'exit':
                break
            else:
                for i in tmp:
                    print(ord(i))
                    print('+'*ord(i))
                    print()
        cls()
        menu()

    elif cmd == '3':
        cls()
        print()
        print("BrainFuck has a one-line memory, like: [0, 0, 0, 0, 0, 0,...]. It has an iterator whis starts from index[0].")
        print()
        print('The eight language commands each consist of a single character:')
        print('\t>  increment the data pointer (to point to the next cell to the right).')
        print('\t<  decrement the data pointer (to point to the next cell to the left).')
        print('\t+  increment (increase by one) the byte at the data pointer.')
        print('\t-  decrement (decrease by one) the byte at the data pointer.')
        print('\t.  output the byte at the data pointer.')
        print('\t,  accept one byte of input, storing its value in the byte at the data pointer.')
        print('\t[  if the byte at the data pointer is zero, then instead of moving the instruction pointer forward to the next command, jump it forward to the command after the matching ] command.')
        print('\t]  if the byte at the data pointer is nonzero, then instead of moving the instruction pointer forward to the next command, jump it back to the command after the matching [ command.')
        print()
        print()
        print('brainfuck command\tC equivalent')
        print('(Program Start)\tchar array[30000]={0}; char *ptr=&array[0];')
        print()
        print('\t>  ++ptr;')
        print('\t<  --ptr;')
        print('\t+  ++*ptr;')
        print('\t-  --*ptr;')
        print('\t.  putchar(*ptr);')
        print('\t,  *ptr=getchar();')
        print('\t[  while (*ptr) {')
        print('\t]  }')
        print()
        print()
        print()

        menu()
        
    elif cmd == '4':
        break
    
    else:
        cls()
        print('Please Choose One Of The Options')
        menu()
