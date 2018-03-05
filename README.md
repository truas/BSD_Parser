#BSD_Parser

Takes direcotry with text (.txt) files with the following format:

		token1 \t token2 \t token3 \token4 \n

Example:
		gray	Synset('gray.n.09')	11012474	n

Produces one file which each line is an entire document with the desired token# (remember to strip the '\n' in the last token. One file per document is also possible (see commented line in 'operation.py')

