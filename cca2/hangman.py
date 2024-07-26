
import sys
def struct(a):
    if a==0:
        print("+---+")
        print("|   |")
        print("    |")
        print("    |")
        print("    |")
        print("    |")
        print("   ===")
  
    if a==1:
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print("      |")
        print("      |")
        print("      |")
        print("     ===")
    if a==2:
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print("  |   |")
        print("      |")
        print("      |")
        print("     ===")
    if a==3:
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print(r" /|   |")
        print("      |")
        print("      |")
        print("     ===")
    if a==4:
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print(r" /|\  |")
        print("      |")
        print("      |")
        print("     ===")
    if a==5:
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print(r" /|\  |")
        print("  |   |")
        print("      |")
        print("     ===")
    if a==6:
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print(r" /|\  |")
        print("  |   |")
        print(r" /    |")
        print("     ===")
    if a==7:
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print(r" /|\  |")
        print("  |   |")
        print(r" / \  |")
        print("     ===")
    
w=input('Enter the word:')
w=w.upper()
n=len(w)
clue=input('Enter a clue related to the word:')
for i in range(0,51):
    print("   ")
lis=[]
b=[]
c=[]
z=0
wg=0
struct(wg)
for i in w:
    lis.append(' ')
print(f"It is a {n} letter word.")
print('Clue:',clue)
for i in w:
    b.append(i)
    c.append(i)

    
while lis!=c:
    l=input('Guess a letter:')
    l=l.upper()
    z=0
    for i in b:
        if i==l:
            ix=b.index(i)
            lis[ix]=i
            b[ix]=' '
        else:
            z+=1
    print('\n'+' '.join(lis))
    print(n*'_ ','\n')
    if z==n:
        wg+=1
        print('wrong guess!!!')
        struct(wg)
        print(f'LIVES LEFT: {7-wg}'+'\n')
    if wg==7:
        print(' Sorry the man has been HANGGED ;( ')
        print(' Better luck Next time !')
        sys.exit()
    else:
        print('Correct Guess, Right on!','\n')
    
print(f" CONGRATULATIONS! The word is {' '.join(lis)},You are the Victor.")
print("Thank You for playing.")
    
        
    
            

