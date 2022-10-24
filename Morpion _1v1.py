top = [" ", "1" , "2" , "3"]
a = ['a','_','_','_']
b = ['b','_','_','_']
c = ['c','_','_','_']
lists = a + b + c


    
def usr_A_check_win():

    i = 0
    j = 0
    h = 0    
       
    for x in a:
        if x == 'x':
            i += 1
        if i == 3:            
            print("A you won")
            return False

    for x in b:
        if x == 'x':
            j += 1
        if j == 3:            
            print("A you won")
            return False    

    for x in c:
        if x == 'x':
            h += 1
        if h == 3:            
            print("A you won")
            return False    
    
    if  'x' in (a[1] and b[1] and c[1]):
        print("A you won")
        return False

    if  'x' in (a[2] and b[2] and c[2]):
        print("A you won")
        return False

    if  'x' in (a[3] and b[3] and c[3]):
        print("A you won")
        return False

    if  'x' in (a[1] and b[2] and c[3]) or (a[3] and b[2] and c[1]):
        print("A you won")
        return False      


    
def board():
    print("",top ,'\n', a ,'\n', b ,'\n', c ,'\n')
def usrA():
    work = True
    while work:
        
        linSel = eval(input("Player A - please select a line a/b/c ?: "))
        culSel = int(input("Player A - please select a colmun: "))
    
        if linSel[culSel] != 'x' or 'o':
            linSel[culSel] ='x'
            work = False
        else:
            work = True

  
def usrB():
    work = True
    while work:
        linSel = eval(input("Player B - please select a line a/b/c ?: "))
        culSel = int(input("Player B - please select a colmun 1/2/3 ?: "))
        if linSel[culSel] != 'x' or 'o':
                linSel[culSel] ='o'
                work = False
        else:
            work = True
    



  
    
    
while True:
    
    board()
    usrA()
    usr_A_check_win()
    board()
    usrB()
    board()