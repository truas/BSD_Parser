'''
Created on Mar 5, 2018

@author: Terry Ruas

Important: 
1. input/output folder need to be under the same directory as text_parser package

'''
#import
import os
import sys
import argparse

#python module absolute path
pydir_name = os.path.dirname(os.path.abspath(__file__))
ppydir_name = os.path.dirname(pydir_name)

#python path definition
sys.path.append(os.path.join(os.path.dirname(__file__),os.path.pardir))


#local-imports
from text_operations import read_write as rw

if __name__ == '__main__':  
    
    #IF you want to use COMMAND LINE for folder path
    
    parser = argparse.ArgumentParser(description="BSD_Parser - Extract Synset information from documents")
    parser.add_argument('--input', type=str, action='store', dest='in_f', metavar='<folder>', required=True, help='input folder to read document(s)')
    parser.add_argument('--output', type=str, action='store', dest='out_f', metavar='<folder>', required=True, help='output folder to write document(s)')
    parser.add_argument('--ofname', type=str, action='store', dest='op_fn', metavar='<file>', required=False, help='output file name')
    parser.add_argument('--type', type=str, action='store', dest='typ', metavar='<type>', required=True, help='output file name')
    args = parser.parse_args()
     
       
    #relative input/output folders - If you want to run it from an IDE
    #in_fname= 'C:/Users/terry/Documents/Programming/eclipse-workspace/BSD_Parser/files/input/d'
    #ou_fname = 'C:/Users/terry/Documents/Programming/eclipse-workspace/BSD_Parser/files/output'
    
    #COMMAND LINE  folder paths
    input_folder = args.in_f
    output_folder = args.out_f
    output_fname =  args.op_fn
    type_option = args.typ
    
     
    #in/ou relative location
    in_fname = os.path.join(ppydir_name , input_folder)
    ou_fname = os.path.join(ppydir_name , output_folder)
    
    
    #rw.count_pos(docs, ou_fname)
    docs = rw.doclist_multifolder(in_fname)
    rw.handleParser(docs, ou_fname, type_option, output_fname)
    print('Finished...')