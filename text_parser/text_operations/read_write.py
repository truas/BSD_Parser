'''
Created on Mar 5, 2018

@author: Terry Ruas
'''

from os import listdir


#input-folder:
doc_list = 'BSID_doclist.txt'
corpus_bsd = 'bsd_corpus'


def make_doc_list(folder_name):
    #read all files in a  folder with .txt format and makes a list of them
    input_file_list = [folder_name+'/'+name for name in listdir(folder_name) if name.endswith('txt')]
    doc_data_list = open(doc_list, 'w+')
    
    #saving document list
    for file in input_file_list:
        doc_data_list.write(file +'\n')
    doc_data_list.close() #raw-input list with absolute path
    
    #show the number of files in the directory
    print ('Found %s documents under the dir %s .....'%(len(input_file_list), folder_name))
    return (input_file_list)
#creates list of documents in a folder

def process_one_file(files, output_folder):
    big_document = open(output_folder+'/'+corpus_bsd, 'w+')    
    for file in files:
        print('Processing %s' %file)
        with open(file, 'r', encoding='utf-8') as fin:
            for line in fin:
                block = line.split('\t')
                #block[0]:word; block[1]:synset; block[2]:offset; block[3]:pos - this has \n at the end
                big_document.write(block[2] +'-'+ block[3].strip('\n') + '\t')
        big_document.write('\n')
    big_document.close()   
#creates one file with each line being a document in the files list



def process_many_files(files, input_folder, output_folder):
    names = listdir(input_folder)   
    for index, file in enumerate(files):
        big_document = open(output_folder+'/'+names[index], 'w+')
        print('Processing %s' %file)
        with open(file, 'r', encoding='utf-8') as fin:
            for line in fin:
                block = line.split('\t')
                #block[0]:word; block[1]:synset; block[2]:offset; block[3]:pos - this has \n at the end
                big_document.write(block[1] + '\t') #big_document.write(block[2] +'-'+ block[3].strip('\n') + '\t')
        big_document.write('\n')
        big_document.close()   
#creates one file per document parsed - clean features -> block[x]          
            