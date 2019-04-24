#BSD_Parser

Takes directory with text (.txt) files with the following format:

	token1 \t token2 \t token3 \t token4 \n

Example:
		gray	Synset('gray.n.09')	11012474	n

Produces one file which each line is an entire document with the desired token# (remember to strip the '\n' in the last token. One file per document is also possible (see commented line in 'operation.py')

COMMAND LINE
=============
	python3 operation.py  --input <input_folder> --ouput <output_folder> [--ofname <filename>] --type <type_value>

- <--input> : input folder with .txt files or folders with .txt
- <--output>: output folder where the file(s) will be saved
- <--ofname>: output file name [OPTIONAL]. If no name is provided `combined.txt` is used
- <--type>: `--type combined` - All files are combined in one single 
            `--type separate` - Each file is parsed separately

UPDATES
=======
[2019-04-24]
1. Update on `type` variable values

[2019-01-31]
1. text_parser package removed
2. flag `type` inserted. To combine all inputs in one single file  use `--type combined`, or for separate files `--type separated`
3. README update


[2018-12-01]
1. Fixing relative path to combine multiple files into one
2. Provide output file name too

[2018-05-22]
1. Fix on counting function for statistics of corpus

[2018-03-28]
1. *count_pos(files, output_folder)* implemented - it calculates the amount (unique and in total) of words in the corpus considering the following POS: NOUN - n ; VERB - v; ADVERB - v; ADJECTIVE - a/s

[2018-03-13] 
1. No need to use PYTHONPATH=.. before compiling it. It was included in  'sys.path.'
2. Code is now capable of reading text files dispersed over any multi directory structure

[2018-03-12] 
1. Code developed on Eclipse, if compiled on command line need to set 'PYTHONPATH=..' before calling python3 to avoid local-import problems
2. input/output folder need to be under the same directory as sys.path (currently text_parser/text_operations)

