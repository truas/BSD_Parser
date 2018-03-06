'''
Created on Mar 5, 2018

@author: Terry Ruas
'''
#import
import os
import sys

#python module absolute path
pydir_name = os.path.dirname(os.path.abspath(__file__))

#python path definition
sys.path.append(os.path.join(os.path.dirname(__file__), 'text_parser/text_operatinos'))

#local-imports
from text_operations import read_write as rw

#relative input/output folders
input_folder = '/tmp_project/BSDParser/input'
output_folder = '/tmp_project/BSDParser/output'

#in/ou relative location
in_fname = os.path.join(pydir_name, input_folder)
ou_fname = os.path.join(pydir_name, output_folder)

docs = rw.make_doc_list(in_fname)
rw.process_one_file(docs, ou_fname)
#rw.process_many_files(docs, in_fname, ou_fname) #in case you want one file per document
print('Finished...')