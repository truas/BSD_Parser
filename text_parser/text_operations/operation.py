'''
Created on Mar 5, 2018

@author: Terry Ruas
'''
#import-modules
from text_operations import read_write as rw

#input/output
input_folder = 'C:/tmp_project/BSDParser/input'
output_folder = 'C:/tmp_project/BSDParser/output'

docs = rw.make_doc_list(input_folder)
rw.process_one_file(docs, output_folder)
#rw.process_many_files(docs, input_folder, output_folder) #in case you want one file per document
print('Finished...')