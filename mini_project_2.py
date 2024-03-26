flag = True
while flag:
    x = input('Enter Song name or exit:-')
    if x.lower() == 'exit':
        flag = False
    else:
        y = input('Enter field(Marathi,Hindi,English) of song:- ')
        if y.lower() == 'marathi':
            file_path = 'C:\Prathamesh\python_txt_files\All_songs\marathi.txt'
            with open (file_path,'a') as file_obj:
                file_obj.write(x +'\n')
        elif y.lower() == 'hindi':
            file_path = 'C:\Prathamesh\python_txt_files\All_songs\hindi.txt'
            with open (file_path,'a') as file_obj:
                file_obj.write(x+'\n')
        elif y.lower() == 'english':
            file_path = 'C:\Prathamesh\python_txt_files\All_songs\english.txt'
            with open(file_path,'a') as file_obj:
                file_obj.write(x+'\n')
        else:
            print('Our senior prathamesh sir will solve error ')
#Sucess zalou pn file madhye append karta yet nahi ahe
'''print('Your all reacords till todays date are as follows :- ') 
file_path = 'C:\Prathamesh\python_txt_files\All_songs\marathi.txt'
with open(file_path,'r+') as file_obj_1:
    content  = file_obj_1.readlines()
y = 1
a = 0
z = len(content)
while y <= z: 
    with open (file_path,'r+') as file_obj:
        print(str(y) +":- "+content[a])
        y += 1
        a += 1
file_path = 'C:\Prathamesh\python_txt_files\All_songs\hindi.txt'
with open(file_path,'r+') as file_obj_1:
    content  = file_obj_1.readlines()
y = 1
a = 0
z = len(content)
while y <= z: 
    with open (file_path,'r+') as file_obj:
        print(str(y) +":- "+content[a])
        y += 1
        a += 1
file_path = 'C:\Prathamesh\python_txt_files\All_songs\english.txt'
with open(file_path,'r+') as file_obj_1:
    content  = file_obj_1.readlines()
y = 1
a = 0
z = len(content)
while y <= z: 
    with open (file_path,'r+') as file_obj:
        print(str(y) +":- "+content[a])
        y += 1
        a += 1'''

    
   











#Congratulations Prathu you made it !! but try some following things to stylize youe code :- 
#ideas :- sort alphabetically all songs , give sr no. to songs 
