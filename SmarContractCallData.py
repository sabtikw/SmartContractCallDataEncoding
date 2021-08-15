from web3 import Web3
from eth_abi import encode_abi
from cmd import Cmd

 
class SmartContractCallData(Cmd):


   

    def do_function(self, args):
        """Get function Selector == Type function signature :: function transfer(address,uint256)"""
        if len(args) == 0:
            print("INVAID input")
        else:
            encode_function(args)

    def do_input(self, args):
        """Get encoded function inputs == Type input  :: input address,uint256 0x882C8e57Cf50ea8563182D331a3ECf8C99e953Cf,1 """
        if len(args) == 0:
            print("INVAID input")
        else:
            encode_data(args)

    def do_quit(self, args):
        """Quits the program."""
        print("Quitting.")
        raise SystemExit


def encode_function(fun_signature):
    

    approve_function_selector = Web3.keccak(text=fun_signature)[0:4]

    print(approve_function_selector.hex())

    
def encode_data(calldata):

    calldata = calldata.split(' ')
     
    
    types = calldata[0].split(',')
    values = calldata[1].split(',')

    for index in range(len(types)):

        if 'uint' in types[index]:
            values[index] = int(values[index])
    
    data = encode_abi(types,values)

    print(data.hex())
   

if __name__ == '__main__':
    prompt = SmartContractCallData()
    prompt.prompt = '> '
    prompt.cmdloop('Starting prompt...')


