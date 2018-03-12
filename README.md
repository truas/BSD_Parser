#BSD_Parser

Takes direcotry with text (.txt) files with the following format:

		token1 \t token2 \t token3 \token4 \n

Example:
		gray	Synset('gray.n.09')	11012474	n

Produces one file which each line is an entire document with the desired token# (remember to strip the '\n' in the last token. One file per document is also possible (see commented line in 'operation.py')

[2018-03-12] 
1. Code developed on Eclipse, if compiled on command line need to set 'PYTHONPATH=..' before calling python3 to avoid local-import problems
2. input/output folder need to be under the same directory as sys.path (currently text_parser/text_operations)

