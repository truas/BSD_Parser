import argparse

class commandLine:
    input_folder = None
    output_folder = None
    output_filename = None
    parser_type = None
    
    def __init__(self):
        parser = self.commandLineParameters()
        args = parser.parse_args()
        self.input_folder = args.in_f
        self.output_folder = args.on_f
        self.output_filename = args.op_f
        self.parser_type = args.type
    #constructor for parameters

    def commandLineParameters(self):
        parser = argparse.ArgumentParser(description="BSD_Parser - Extract Synset information from documents")
        parser.add_argument('--input', type=str, action='store', dest='in_f', metavar='<folder>', required=True, help='input folder to read document(s)')
        parser.add_argument('--output', type=str, action='store', dest='on_f', metavar='<folder>', required=True, help='output folder to write document(s)')
        parser.add_argument('--ofname', type=str, action='store', dest='op_f', metavar='<file>', required=False, help='output file name')
        parser.add_argument('--type', type=str, action='store', dest='type', metavar='<type>', required=True, help='type of parser to execute [separate,combined]', choices=["combined", "separate"])
        return(parser)
    #parameter list for command line