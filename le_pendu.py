import random

    

#ask for level and store it
path_txt = r"C:\Users\PX229\Desktop\laplateforme\python-projects\job01 le pendu\dico_france.txt"
lifes = 0
expert = False
with open(path_txt,'r') as file: #open file
    data = str(file.read())
    words = list(map(str, data.split()))#storing data as splited words
    word = (random.choice(words))#randomly choosing a word
    list(word)#storing word inside a list
    #print(list(word))#debug print

vid = ("_")#word not found yet
list = []#updated list of found words
noobList=[]#list to show worng guessd letters
 



#ask user for his level and adjust lifes number
work = True 
while work:
    print("Lets play hangman -_-")
    usr_lvl = int(input("please select your level: 1-for beginer , 2-for intermadte , 3-for expert "))
    if usr_lvl == 1:
        lifes = 15
        work = False
    elif usr_lvl == 2:
        lifes = 10
        work = False
    elif usr_lvl == 3:
        lifes = 8
        
        expert = True#this varibale will block expert user from seeing worng guessd letter list
        work = False

    else:
        work = True#this will make sure to to keep asking level till user answer


#loop to create empty list    
l = 0
while l != len(word):
    list.append(vid)
    l+=1        

print(list) 

#loop to create a list that getting updated if letter is correct
while lifes > 0:
    usr_ges = str(input("please type a letter you think is inside word "))

    if usr_ges in word:
        l = 0
        while l != len(word):
            if usr_ges == word[l]:
                list[l] = usr_ges
            l+=1
    else:
        lifes -=1
        print("you are worng please try again, you have " , lifes , "left")
        if not expert:
            noobList.append(usr_ges)
            print(  "letters you have already choosen: " , noobList)
            
    print(list)           
    if lifes == 0:
        print("Game Is Over, the word was:", word)
        
    

          
        
         