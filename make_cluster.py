txt_file = open("correct_pred.txt", "r")

content_list = txt_file.readlines()
clusters = {}
i = 0 
for item in content_list : 
    clusters[i] = item.split(',')
    i += 1 

import os
import shutil

source_folder = os.getcwd()+'\\'
destination_folder = os.getcwd()+'\\'
print(os.getcwd())
i = 0 
for i in range(len(clusters)):
    for file_name in clusters[i]:
        # construct full file path
        if '\n' in file_name : 
            file_name = file_name.replace('\n', '')
        source = source_folder + file_name+'.jpg'
        
        destination = destination_folder + 'correct' + '\\' +file_name+'.jpg'
    
        # copy only files
        try : 
            shutil.move(source, destination)
        except : 
            print('')

    i+= 1 

