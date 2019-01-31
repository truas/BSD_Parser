'''
Created on Mar 5, 2018

@author: Terry Ruas
'''
import argparse
import os


def doclist_multifolder(folder_name):
    input_file_list = []
    for roots, dir, files in os.walk(folder_name):
        for file in files:
            file_uri = os.path.join(roots, file)
            #file_uri = file_uri.replace("\\","/") #if running on windows           
            if file_uri.endswith('txt'): input_file_list.append(file_uri)
    return(input_file_list)
#creates list of documents in many folders

def get_folders(folder_root):
    folders = []
    for dirname, dirnames, filenames in os.walk(folder_root):
        for subdirname in dirnames:
            folders.append(os.path.join(dirname, subdirname))
            
    return folders

def process_one_file(files, output_folder):
    big_document = open(output_folder, 'w+')    
    for counter, file in enumerate(files):
        #if(counter%5000==0): print('Processing %s' %file)#checking processing files
        print('Processing File: %s' %file)
        with open(file, 'r', encoding='utf-8', errors = 'ignore') as fin:
            for line in fin:
                block = line.split('\t')
                #block[0] - word block[1] - synset block[2] offset block[3] - pos
                big_document.write(block[0] +'#'+ block[2] +'#'+ block[3].strip('\n') + '\t')
        big_document.write('\n')
    big_document.close()   
#creates one file with each line being a document in the files list

def process_many_files(files, input_folder, output_folder):
    names = os.listdir(input_folder)   
    for index, file in enumerate(files):
        big_document = open(output_folder+'/'+names[index], 'w+')
        print('Processing %s' %file)
        with open(file, 'r', encoding='utf-8') as fin:
            for line in fin:
                block = line.split('\t')
                #block[0]:word; block[1]:synset; block[2]:offset; block[3]:pos - this has \n at the end
                big_document.write(block[0] +'#'+ block[2] +'#'+ block[3].strip('\n') + '\t') #big_document.write(block[2] +'-'+ block[3].strip('\n') + '\t')
        big_document.write('\n')
        big_document.close()   
#creates one file per document parsed - clean features -> block[x]          
 
def count_pos(files, output_folder):
    big_document = open(output_folder+'/'+'POS_statistics.txt', 'w+') 
    T = 0 #total
    N = 0
    V = 0
    A = 0
    R = 0 
    ndict = dict()
    vdict = dict()
    adict = dict()
    rdict = dict()
    sdict = dict() 
    for file in files:
        print('Processing %s' %file)
        with open(file, 'r', encoding='utf-8') as fin:
            for line in fin:
                block = line.split('\t')
                pos_tag = block[3].strip('\n')
                pos_tok = block[0]
                syn_tok = block[1]
                
                T +=1
                sdict[syn_tok] = 0
                
                if pos_tag == 'n':
                    N+=1
                    ndict[syn_tok] = 0
                elif pos_tag =='v':
                    V+=1
                    vdict[syn_tok] = 0
                elif pos_tag =='r':
                    R+=1
                    rdict[syn_tok] = 0
                elif pos_tag =='a' or pos_tag =='s':
                    A+=1
                    adict[syn_tok] = 0
                
    big_document.write('Total: ' + str(T) + '\n' +
                       'Nouns: ' + str(N) + '\n' +
                       'Verbs: ' + str(V) + '\n' +
                       'Adverbs: ' + str(R) + '\n' +
                       'Adjectives: ' + str(A) + '\n')
    big_document.write('\n' + 
                       'Unique POS \n'+
                       'Synsets: ' + str(len(sdict.keys())) + '\n' +
                       'Nouns: ' + str(len(ndict.keys())) + '\n' +
                       'Verbs: ' + str(len(vdict.keys())) + '\n' +
                       'Adverbs: ' + str(len(rdict.keys())) + '\n' +
                       'Adjectives: ' + str(len(adict.keys())) + '\n')
    big_document.close()   
#count the amount of items in each POS tag
    