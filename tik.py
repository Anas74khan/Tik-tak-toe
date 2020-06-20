import random




def elementaftercomp():
    y=0
    for i in range(3):
        for j in range(3):
            a[i][j] = b[i+j+y]
        y+=2



def compmove(x,uv):
    true=True
    for i in range(0,9,3):
        if(b[i]==x and b[i+1]==b[i] and b[i+2]==' ' and true==True):
            b[i+2]=x
            true=False
        elif(b[i+1]==x and b[i+1]==b[i+2] and b[i]==' ' and true==True):
            b[i]=x
            true=False
        elif(b[i]==x and b[i]==b[i+2] and b[i+1]==' ' and true==True):
            b[i+1]=x
            true=False
    for i in range(3):
        if(b[i]==x and b[i+3]==b[i] and b[i+6]==' ' and true==True):
            b[i+6]=x
            true=False
        elif(b[i+3]==x and b[i+3]==b[i+6] and b[i]==' ' and true==True):
            b[i]=x
            true=False
        elif(b[i]==x and b[i]==b[i+6] and b[i+3]==' ' and true==True):
            b[i+3]=x
            true=False
    if(b[0]==x and b[4]==b[0] and b[8]==' ' and true==True):
        b[8]=x
        true=False
    elif(b[4]==x and b[4]==b[8] and b[0]==' ' and true==True):
        b[0]=x
        true=False
    elif(b[0]==x and b[0]==b[8] and b[4]==' ' and true==True):
        b[4]=x
        true=False
    elif(b[2]==x and b[4]==b[2] and b[6]==' ' and true==True):
        b[6]=x
        true=False
    elif(b[4]==x and b[4]==b[6] and b[2]==' ' and true==True):
        b[2]=x
        true=False
    elif(b[2]==x and b[2]==b[6] and b[4]==' ' and true==True):
        b[4]=x
        true=False
    for i in range(0,9,3):
        if(b[i]==uv and b[i+1]==b[i] and b[i+2]==' ' and true==True):
            b[i+2]=x
            true=False
        elif(b[i+1]==uv and b[i+1]==b[i+2] and b[i]==' ' and true==True):
            b[i]=x
            true=False
        elif(b[i]==uv and b[i]==b[i+2] and b[i+1]==' ' and true==True):
            b[i+1]=x
            true=False
    for i in range(3):
        if(b[i]==uv and b[i+3]==b[i] and b[i+6]==' ' and true==True):
            b[i+6]=x
            true=False
        elif(b[i+3]==uv and b[i+3]==b[i+6] and b[i]==' ' and true==True):
            b[i]=x
            true=False
        elif(b[i]==uv and b[i]==b[i+6] and b[i+3]==' ' and true==True):
            b[i+3]=x
            true=False
    if(b[0]==uv and b[4]==b[0] and b[8]==' ' and true==True):
        b[8]=x
        true=False
    elif(b[4]==uv and b[4]==b[8] and b[0]==' ' and true==True):
        b[0]=x
        true=False
    elif(b[0]==uv and b[0]==b[8] and b[4]==' ' and true==True):
        b[4]=x
        true=False
    elif(b[2]==uv and b[4]==b[2] and b[6]==' ' and true==True):
        b[6]=x
        true=False
    elif(b[4]==uv and b[4]==b[6] and b[2]==' ' and true==True):
        b[2]=x
        true=False
    elif(b[2]!='X' and b[2]==b[6] and b[4]==' ' and true==True):
        b[4]=x
        true=False
    elif(true==True):
        m=[]
        for i in range(9):
            if b[i]==' ':
                m.append(i)
        if len(m)==9:
                b[4]=x
        elif(len(m)>1 and len(m)!=9):
                i=random.choice(m)
                b[i]=x
        else:
                i=m[0]
                b[i]=x




def elementsOfb(u,pos):
    b[pos] = u
    y=0
    for i in range(3):
        for j in range(3):
            a[i][j] = b[i+j+y]
        y+=2



def PrintBoard():
    for i in range(1,6):
        for j in range(1,6):
            if(j%2==0):
                print('|', end=' ')
            if((j%2!=0)and(i%2==0)):
                print('-', end=' ')
            if((j%2!=0)and(i%2!=0)):
                print(a[int((i-1)/2)][int((j-1)/2)],end=' ')
        print(' ')



def CheckBoard(y):
    if((b[0]==y)and(b[0]==b[1]) and(b[1]==b[2])):
        return b[0]
    if((b[3]==y)and(b[3]==b[4]) and(b[4]==b[5])):
        return b[3]
    if((b[6]==y)and(b[6]==b[7]) and(b[7]==b[8])):
        return b[6]
    if((b[0]==y)and(b[0]==b[3]) and(b[3]==b[6])):
        return b[0]
    if((b[1]==y)and(b[1]==b[4]) and(b[4]==b[8])):
        return b[1]
    if((b[2]==y)and(b[2]==b[5]) and(b[5]==b[8])):
        return b[2]
    if((b[0]==y)and(b[0]==b[4]) and(b[4]==b[8])):
        return b[0]
    if((b[2]==y)and(b[2]==b[4]) and(b[4]==b[6])):
        return b[2]



def userInput(u):
    while(True):
        try:
            while(True):
                j = int(input("Enter position[1-9]: "))
                print("\n")
                if(j>9 or j<1 or b[j-1]!=' '):
                    print("Entered a wrong position try again")
                else:
                    break
            break
        except ValueError:
             print("You have entered a invalid position enter correct position")
    elementsOfb(u,j-1)
    PrintBoard()
    



char = 'y'
print("*"*12+"WELCOME TO TIK TAK TOE WORLD"+"*"*12)
while(char=='y' or char=='Y'):
    b = [' ' for i in range(9)]
    a = [[' ' for i in range(3)]for i in range(3)]
    let='c'
    PrintBoard()
    while(let=='c' or let=='C'):
        uv=input("Choose what you want to take[O,X]: ")
        u=uv.upper()
        if(u=='O' or u=='X'):
            break
        let=input("Wrong choice press c to choose again or any other key to exit: ")
    print("_"*70)
    user = random.choice(['c','u'])
    if(u=='O'):
        x='X'
    else:
        x='O'
    k=1
    while True:
        if(user=='c'):
            user='u'
            input("Computer's turn press enter\n\n")
            s = compmove(x,u)
            elementaftercomp()
            PrintBoard()
            result = CheckBoard(x)
            print('_'*70)
        else:
            user='c'
            s = userInput(u)
            result = CheckBoard(u)
            print('_'*70)
        if(result == x):
            s="Oooh!! You lost."
            break
        elif(result == u):
            s="Congratulations!! You won."
            break
        if(k==9 and result==None):
            s='Game tie'
            break
        k+=1
    print(s)
    char = input("Enter y if you want to play again and any other key to exit: ")
    print("\n\n"+"*"*70)
