'''
Created on Mar 5, 2018

@author: Terry Ruas
'''
import argparse
import os
import errno
import sys
from fnmatch import fnmatch
import shutil


def doclist_multifolder(folder_name):
    input_file_list = []
    for roots, dir, files in os.walk(folder_name):
        for file in files:
            file_uri = os.path.join(roots, file)
            #file_uri = file_uri.replace("\\","/") #if running on windows           
            if file_uri.endswith('txt'): input_file_list.append(file_uri)
    return(input_file_list)
#creates list of documents in many folders

def handleParser(src_files, dst_out, type, output_name="combined.txt"):
    combined = 'combined'
    separate = 'separate'
    
    if(type==combined):
        process_one_file(src_files, dst_out, output_name)
    elif(type==separate):
        process_many_files(src_files, dst_out)
    else:
        print('No type was selected, exiting')
    

def read(file_name):
    try:
        f = open(file_name,'r', encoding= 'utf-8', errors="ignore")
        content = f.read()
        f.close()
    except IOError as exc:
        if exc.errno != errno.EISDIR:
            raise ("problem reading file: " + file_name)
    return(content)
#reads the entire file in one shot  

def mkdirnotex(filename, outputpath):
    print('File-READ_WRITE: ', os.path.dirname(os.path.abspath(__file__)))
    print('outputpath: ', outputpath)
    print('os.path: ', os.path.curdir)
    folder=os.path.dirname(filename)
    if not os.path.exists(folder):
        os.makedirs(folder)
#creates directory for a given file name

def process(src_dir, dst_dir, pattern='*'):
    """Iterate through src_dir, processing all files that match pattern and
    store them, including their parent directories in dst_dir.
    """
    assert(src_dir != dst_dir, 'Source and destination dir must differ.')
    for dirpath, dirnames, filenames in os.walk(src_dir):
        # Filter out files that match pattern only.
        filenames = filter(lambda fname: fnmatch(fname, pattern), filenames)

        if filenames:
            dir_ = os.path.join(dst_dir, dirpath)
            os.makedirs(dir_)
            for fname in filenames:
                in_fname = os.path.join(dirpath, fname)
                out_fname = os.path.join(dir_, fname)

                # At this point, the destination directory is created and you
                # have a valid input / output filename, so you'd call your
                # function to process these files.  I just copy them :D
                shutil.copyfile(in_fname, out_fname)



def process_one_file(files, output_fpath, output_fname):
    op_fname = os.path.join(output_fpath, output_fname)
    big_document = open(op_fname, 'w+')    
    for counter, file in enumerate(files):
        #if(counter%5000==0): print('Processing %s' %file)#checking processing files
        print('Processing File: %s' %file)
        try:
            with open(file, 'r', encoding='utf-8', errors = 'ignore') as fin:
                for line in fin:
                    block = line.split('\t')
                    #block[0] - word block[1] - synset block[2] offset block[3] - pos
                    big_document.write(block[0] +'#'+ block[2] +'#'+ block[3].strip('\n') + '\t')
            big_document.write('\n')
        except IOError as exc:
            if exc.errno != errno.EISDIR: raise ("problem reading file: " + file)
    big_document.close()   
#creates one file with each line being a document in the files list

def process_many_files(files, output_folder):
    separator = '\t' #content file separator   
    for file in files:
        fname = adjustFileName(file)
        output_fname = os.path.join(output_folder,fname)
        new_file = open(output_fname, 'w+')
        print('Processing %s' %file)
        with open(file, 'r', encoding='utf-8') as fin:
            for line in fin:
                block = line.split(separator)
                #block[0]:word; block[1]:synset; block[2]:offset; block[3]:pos - this has \n at the end
                new_file.write(block[0] +'#'+ block[2] +'#'+ block[3].strip('\n') + '\n') #big_document.write(block[2] +'-'+ block[3].strip('\n') + '\t')
        new_file.close()   
#creates one file per document parsed - clean features -> block[x]          
 
def adjustFileName(file):
    fname_index = -1 #last position for file-name
    fname = file.split(os.sep)
    fname = fname[fname_index]
    return(fname)
#receives absloute path for a file and returns its name.extension
 
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
    