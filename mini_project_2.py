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
#ideas :-try to sort  all songs alphabetically, give sr no. to songs 
