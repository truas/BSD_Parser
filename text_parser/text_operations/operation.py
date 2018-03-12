'''
Created on Mar 5, 2018

@author: Terry Ruas

Important: 
1. Code developed on Eclipse, if compiled on command line need to set 'PYTHONPATH=..' before calling python3 to avoid local-import problems
2. input/output folder need to be under the same directory as sys.path (currently text_parser/text_operations)
'''
#import
import os
import sys
import argparse

#python module absolute path
pydir_name = os.path.dirname(os.path.abspath(__file__))

#python path definition
sys.path.append(os.path.join(os.path.dirname(__file__), 'text_parser/text_operations'))

#local-imports
from text_operations import read_write as rw

if __name__ == '__main__':  
    
    #IF you want to use COMMAND LINE for folder path
    
    parser = argparse.ArgumentParser(description="BSD_Parser - Extract Synset information from documents")
    parser.add_argument('--input', type=str, action='store', dest='in_f', metavar='<folder>', required=True, help='input folder to read document(s)')
    parser.add_argument('--output', type=str, action='store', dest='out_f', metavar='<folder>', required=True, help='outnput folder to write document(s)')
    args = parser.parse_args()
    
       
    #relative input/output folders - If you want to run it from an IDE
    #input_folder = '/tmp_project/BSDParser/input'
    #output_folder = '/tmp_project/BSDParser/output'
    
    #COMMAND LINE  folder paths
    input_folder = args.in_f
    output_folder = args.out_f
    
    #in/ou relative location
    in_fname = os.path.join(pydir_name, input_folder)
    ou_fname = os.path.join(pydir_name, output_folder)
    
    
    docs = rw.make_doc_list(in_fname)
    rw.process_one_file(docs, ou_fname)
    #rw.process_many_files(docs, in_fname, ou_fname) #in case you want one file per document
    print('Finished...')