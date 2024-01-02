"""
Code that converts hex code back to the original file type.

Needed: Hex code, file type, name of the file.

The code works with an excel file that locks three columns with the needed data.

Note:Before running that code make sure to choose a folder that will save all your files. Folder lock needed through your compiler.

Note: Some lines of code have (Will need change) comment. This changes will be needed based on your excel file. 

Note: The code only locks the names of the columns, try changing your excel file to work with this code.

Note: Excel file example is attached in GitHub.

Running the code:
Input will show 4 choices (All, Multiple, Specific, By file type)
Choosing one will push you to an if statement that will run your hex code. 

All: Will convert all the file types into one folder.
Multiple: Locks row index. Input ex: [1 2 3 4 26 564] do not use commas.
Specific: Empty. Works the same ways as multiple. Use multiple and just input one index.
By file type: Locks specific file types that are inputed. Input ex: [jpg pdf] do not use commas or periods.

Extra code might be helpful if wanting to modify the existing code.

"""

import pandas as pd
import inquirer 
import base64
import codecs
import os.path
from pathlib import Path
from array import array
import numpy as np 

#Connecting data and locking needed columns
hex_excel = pd.read_excel(r"\\numbers\Users\TanyaM\My Documents\CC\Hex_Excel.xlsx")

file_name = hex_excel['File Name:'].tolist()

file_type = hex_excel['File Type:'].tolist()

hex_code = hex_excel['Hex:'].tolist()


#Getting input 
question = [
    inquirer.List('choice',
                  message = "What type of convertion would you like to perform?",
                  choices = ['All','Multiple','Specific','By File Type'],              
    ),
]
    
answer = inquirer.prompt(question)

#For each input creating an if statement: Four statements in total
while True:

    if answer['choice'] == 'All':
            
        file_name_nan = [x for x in file_name if not pd.isnull(x)]        #Will need change
        file_type_nan = [x for x in file_type if not pd.isnull(x)]        #Will need change
        hex_code_nan = [x for x in hex_code if not pd.isnull(x)]          #Will need change

        hex_code_nan_x2 = []

        for x in range(len(hex_code_nan)):

            ii = hex_code_nan[x]
            hex_code_nan_x2.append(ii[2:])


        file_name_type_all = ['.'.join(pair) for pair in zip(file_name_nan,file_type_nan)]

        empty = []

        for x in range(len(hex_code_nan)):
            yy = hex_code_nan_x2[x] = bytes.fromhex(hex_code_nan_x2[x])
            empty.append(yy)


        for x in range(len(file_name_type_all)):
            with open(file_name_type_all[x],'wb') as f:
                for y in range(len(empty)):
                    f.write(empty[y])
           
        break
        
    
    if answer['choice'] == 'Multiple':

        amount_of_rows = [int(x) for x in input("Please enter row index:" ).split()]

        file_name_l =[]
        file_type_l = []
        hex_code_l = []

        hex_code_b = []
        
        multiple_file_name = hex_excel['File Name:']       #Will need change
        multiple_file_type = hex_excel['File Type:']       #Will need change
        multiple_hex_code = hex_excel['Hex:']              #Will need change

        for x in amount_of_rows:
    
            bb = multiple_file_name.loc[x]
            file_name_l.append(bb)

            mm = multiple_file_type.loc[x]
            file_type_l.append(mm)

            ll = multiple_hex_code.loc[x]
            hex_code_l.append(ll[2:])
            
        file_name_type = ['.'.join(pair) for pair in zip(file_name_l,file_type_l)]
        
        for x in range(len(hex_code_l)):
            yy = hex_code_l[x] = bytes.fromhex(hex_code_l[x])
            hex_code_b.append(yy)
        
        for x in range(len(file_name_type)):
            with open(file_name_type[x],'wb') as f:
                for y in range(len(hex_code_b)):
                    f.write(hex_code_b[x])
        
        break
        
    if answer['choice'] == 'Specific':

        break

    if answer['choice'] == 'By File Type':

        amount_of_types = [x for x in input("Please enter file type whithout periods:" ).split()]

        mask = hex_excel['File Type:'].isin(amount_of_types) #Find specific values from your list in the dataframe. #Will need change
        columns_needed = hex_excel[mask]

        df = pd.DataFrame(columns_needed)

        file_name_by = df['File Name:'].tolist()       #Will need change
        file_type_by = df['File Type:'].tolist()       #Will need change
        hex_code_by = df['Hex:'].tolist()              #Will need change

        hex_code_by_x2 = []

        for x in range(len(hex_code_by)):
            
            ii = hex_code_by[x]
            hex_code_by_x2.append(ii[2:])
        
        file_name_type_all = ['.'.join(pair) for pair in zip(file_name_by,file_type_by)]
        
        empty = []

        for x in range(len(hex_code_by)):
            yy = hex_code_by_x2[x] = bytes.fromhex(hex_code_by_x2[x])
            empty.append(yy)

        for x in range(len(file_name_type_all)):
            with open(file_name_type_all[x],'wb') as f:
                for y in range(len(empty)):
                    f.write(empty[y])

        break
        

 

#Extra code:

#file_name_nan = [x for x in file_name if not pd.isnull(x)]
#file_type_nan = [x for x in file_type if not pd.isnull(x)]
#hex_code_nan = [x for x in hex_code if not pd.isnull(x)]

"""
  for x in amount_of_types:

            file_type_jpg = []

            file_name_jpg = []

            hex_code_jpg = []

            for x in range(len(file_type)):
                jj = file_type[x]
                oo = file_name[x]
                pp = hex_code[x]

                if jj =='jpg':
                    file_type_jpg.append(jj)
                    file_name_jpg.append(oo)
                    hex_code_jpg.append(pp[2:])

                file_name_type_jpg = ['.'.join(pair) for pair in zip(file_name_jpg,file_type_jpg)]



file_type_jpg = []

file_name_jpg = []

hex_code_jpg = []

for x in range(len(file_type)):
    jj = file_type[x]
    oo = file_name[x]
    pp = hex_code[x]

    if jj =='jpg':
        file_type_jpg.append(jj)
        file_name_jpg.append(oo)
        hex_code_jpg.append(pp)


file_name_type_jpg = ['.'.join(pair) for pair in zip(file_name_jpg,file_type_jpg)]

for x in hex_code_jpg:
    hex_bytes = bytes.fromhex(x[2:])

for x in hex_bytes:
    with open("image1.jpg",'wb') as f:
    f.write(x)
"""








   





