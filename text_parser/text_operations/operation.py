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
ppydir_name = os.path.dirname(ppydir_name)
#python path definition
sys.path.append(os.path.join(os.path.dirname(__file__),os.path.pardir))


#local-imports
from text_operations import read_write as rw

if __name__ == '__main__':  
    
    #IF you want to use COMMAND LINE for folder path
    
    parser = argparse.ArgumentParser(description="BSD_Parser - Extract Synset information from documents")
    parser.add_argument('--input', type=str, action='store', dest='in_f', metavar='<folder>', required=True, help='input folder to read document(s)')
    parser.add_argument('--output', type=str, action='store', dest='out_f', metavar='<folder>', required=True, help='outnput folder to write document(s)')
    args = parser.parse_args()
     
       
    #relative input/output folders - If you want to run it from an IDE
    #in_fname= 'C:/tmp_datasets/Wikipedia_Dump/2018_01_20/corpora/wikidump_dbsd_synsets_sp_20180120/output'
    #ou_fname = 'C:/tmp_datasets/Wikipedia_Dump/2018_01_20/corpora/wikidump_dbsd_synsets_sp_20180120/'
    
    
    #COMMAND LINE  folder paths
    input_folder = args.in_f
    output_folder = args.out_f
    
    #in/ou relative location
    in_fname = os.path.join(ppydir_name , input_folder)
    ou_fname = os.path.join(ppydir_name , output_folder)
    
    
    #docs = rw.doclist_singlefolder(in_fname) #if there is one level -  folder/document.txt
    docs = rw.doclist_multifolder(in_fname) #for single and multiple file-folder structure  - folder/../document.txt
    #rw.count_pos(docs, ou_fname)
    rw.process_one_file(docs, ou_fname)
    #rw.process_many_files(docs, in_fname, ou_fname) #in case you want one file per document
    print('Finished...')