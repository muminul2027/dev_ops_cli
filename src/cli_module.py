#devOps_CLI
#HANDLE:    _MUMINUL__ISLAM___


#CODE->
import argparse

def parser_function():
    #Make A Parser
    parser=argparse.ArgumentParser(description="CLI For DevOps_CLI")

    #Add CLI Arguments
    parser.add_argument("--output",action="store_true",help="Show Output at Terminal")

    #Parse It
    arg_list=parser.parse_args()
    
    if arg_list.output:
        return True
    else:
        return False

