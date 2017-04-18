
"""
 Return all contents of a file in a string when line_number=-1, 
 otherwise will return one line as a string from the file according to the line_number value
 
"""
def show(filename, line_number = -1):
    
    
     if line_number == -1: #when you call this function in option 1, prints out all the contents of the text file
        
        
    else: #When you call this function in option 2 (returning one line) this part will be run
        
    
    
    
    
    
    return content
    
    
    
"""
 Replace all occurrences of keyword with target_word in string.
 keyword and target_word might have different length! 
 Do not change the occourance of the keyword if it is a substring of another word!
 The words are seperated by [ '?' ,  '!' , ' ' , '.']
 
"""   
def replace_word(string , keyword , target_word): 
    
    
    
    
    
    
    return line
    
    
"""
 Save the contents of the filename in the new_file_name.
 if the user never choses option 3 then
 the contents of filename and new_file_name will be the same!
 otherwise, the last line that has been changed in the option 3
 will be the only different between the contents of filename and new_file_name.
 If the user never choose option 3 then line_number=-1
 otherwise you should change the line (line_number)  according to value
 of the new_line.

 
"""      
def save(filename , new_file_name , new_line , line_number = -1):






    
    print('Success!')
    return 
 
#Do not change anything other than path in the following lines. Your job is to fill the functions above!   
menu = True
line_number = -1
new_line = ''
path = 'C:/Users/Farin/'#change this part according to the path to your file
name = input('Please Enter your file name: ') 
filename = path + name + '.txt'
while menu:
    print('\n1-Show all\n2-Show Line\n3-Replace\n4-Save\n5-Exit')
    option = input('\nPlease enter your option:')
    option = int(option)
    
    if option == 1:
        print(show(filename))
        
    elif option == 2:
        line_number = input('\nPlease enter the line number? ')
        print(show(filename , int(line_number)))
        
    elif option == 3:
        line_number = input('\nPlease enter the line number? ')
        string = (show(filename , int(line_number)))
        print(string)
        keyword = input('Please enter your keyword? ')
        target_word = input('Replace it with:  ')
        new_line = replace_word(string , keyword , target_word)
        print(new_line)
        
    elif option == 4:
        name = input('\nPlease enter your new file name: ')
        new_file_name = path + name + '.txt'
        save(filename, new_file_name, new_line, int(line_number))
        
    elif option == 5:
         menu = False
    else:
         print('Wrong number! Please select a number between 1-5: ')