#BSD_Parser

Takes directory with text (.txt) files with the following format:

	token1 \t token2 \t token3 \t token4 \n

Example:
		gray	Synset('gray.n.09')	11012474	n

Produces one file which each line is an entire document with the desired token# (remember to strip the '\n' in the last token. One file per document is also possible (see commented line in 'operation.py')

COMMAND LINE
=============
	python3 operation.py  --input <input_folder> --ouput <output_folder>

UPDATES
=======
[2018-03-28]
1. *count_pos(files, output_folder)* implemented - it calculates the amount (unique and in total) of words in the corpus considering the following POS: NOUN - n ; VERB - v; ADVERB - v; ADJECTIVE - a/s

[2018-03-13] 
1. No need to use PYTHONPATH=.. before compiling it. It was included in  'sys.path.'
2. Code is now capable of reading text files dispersed over any multi directory structure

[2018-03-12] 
1. Code developed on Eclipse, if compiled on command line need to set 'PYTHONPATH=..' before calling python3 to avoid local-import problems
2. input/output folder need to be under the same directory as sys.path (currently text_parser/text_operations)

