#!/usr/bin/env python3

'''Usage: python ported_decoder.py --decode --input [fasta_file]'''



import argparse as ap
#import numpy as np

parser = ap.ArgumentParser(description='encode and decode secret messages in DNA; ported from dna-encode.pl')
'''create mutually exclusive arguments where one is required. inclusion of the flag will make the argument true
and the script's functionality will follow'''
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-d', '--decode', action='store_true', dest='decode_bool', help='use this flag if you want to decode a message from a DNA sequence')
group.add_argument('-e', '--encode', action='store_true', dest='encode_bool', help='use this flag if you want to encode a message into DNA sequence')

parser.add_argument('--input', action='store', dest='input_fm', required=True, help='If --decode flag used, then this is the FASTA file which has a single DNA sequence with the encoded message; alternatively, if the --encode flag, this is a single line text file with the message to encode in DNA sequence form')

args = parser.parse_args()

def main(args):
	if args.decode_bool:
		dna_to_decode = get_dna(args.input_fm)
		decoded_message = decode(dna_to_decode)
		print("The decoded message : ", decoded_message)
	elif args.encode_bool:
		message = get_message(args.input_fm)
		encoded_message = encode(message)
		print("The encoded message : ", encoded_message)


def get_dna(input_file):
	'''read in a single sequence from a fasta_file'''
	f = open(input_file)
	first_line = f.readline().strip('\r\n')
	assert first_line.startswith('>'), 'Not a FASTA file'
	sequence = ''
	while True:
		line = f.readline().strip('\r\n')
		if line == "":
			break
		sequence += line
	return sequence

def get_message(input_message):
	message_to_encode = open(input_message).readline().strip('\r\n')
	return message_to_encode

def decode(dna_to_decode):
	'''Find binary representation'''
	
	binary_rep_str = ''
	base_to_binary = {'A': '0', 'C': '0', 'G': '1', 'T': '1'}	
	for base in dna_to_decode.upper():
		assert base in base_to_binary, 'Not a nucleotide'
		binary_rep_str += base_to_binary[base]
	binary_rep_str = binary_rep_str.encode()

	# binary_rep = int(bin(0), 2)
	# for base in dna_to_encode.upper():
	# 	assert base in ['A', 'C', 'G', 'T'], 'Not a nucleotide'
	# 	binary_rep = binary_rep << 1
	# 	if base == 'G' or base == 'T':
	# 		binary_rep += 1	

	
	'''convert binary representation to text'''
	decoded_str = ''
	for i in range(len(dna_to_decode)//8):
		decoded_str += chr(int(binary_rep_str[i*8:i*8+8], 2))
	return decoded_str

def encode(message):
	binary_result = ''.join(f"{ord(char):08b}" for char in message)
	generated = ''
	to_gen_from = {'0': np.array(['A', 'C']),
					'1': np.array(['G', 'T'])}
	for bit_val in binary_result:
		generated += np.random.choice(to_gen_from[bit_val])
	return generated

main(args)

