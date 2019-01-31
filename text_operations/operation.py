'''
Created on Mar 5, 2018

@author: Terry Ruas

Important: 
1. input/output folder need to be under the same directory as text_parser package

'''
#import
import os
import sys


#python module absolute path
pydir_name = os.path.dirname(os.path.abspath(__file__))
ppydir_name = os.path.dirname(pydir_name)

#python path definition
sys.path.append(os.path.join(os.path.dirname(__file__),os.path.pardir))


#local-imports
from text_operations import read_write as rw
from text_operations.commandLineInterface import commandLine

if __name__ == '__main__':  
    params= commandLine() #command line parameter validation
    
       
    #relative input/output folders - If you want to run it from an IDE
    #in_fname= 'C:/Users/terry/Documents/Programming/eclipse-workspace/BSD_Parser/files/input/d'
    #ou_fname = 'C:/Users/terry/Documents/Programming/eclipse-workspace/BSD_Parser/files/output'
        
     
    #in/ou relative location
    in_fname = os.path.join(ppydir_name , params.input_folder)
    ou_fname = os.path.join(ppydir_name , params.output_folder)
    
    
    #rw.count_pos(docs, ou_fname)
    docs = rw.doclist_multifolder(in_fname)
    rw.handleParser(docs, ou_fname, params.parser_type, params.output_filename)
    print('Finished...')