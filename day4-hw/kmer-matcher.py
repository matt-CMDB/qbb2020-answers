#!/usr/bin/env python3


import sys

from fasta_iterator_class import FASTAReader

target = sys.argv[1]
query = sys.argv[2]
k = int(sys.argv[3])

target = FASTAReader(open(target, 'r'))
query = FASTAReader(open(query, 'r'))

q_kmer_dic = {} # kmers_query

for seq_id, sequence in query:
    for i in range(0, len(sequence) - k + 1): #iterates by nucleotide
        kmer = sequence[i:i + k] # defines single kmer acc to seq
        q_kmer_dic.setdefault(kmer, []) # starts off empty
        q_kmer_dic[kmer].append(i) # adds each kmer to dictionary


k = 11 # dummy (we'll use argument for file)

for seq_id, sequence in target:
    for i in range(0, len(sequence) - k + 1): #iterates by nucleotide
        kmer = sequence[i:i + k] # defines single kmer acc to seq
        if kmer in q_kmer_dic: # checks if target kmer is in query dic
            print(seq_id, i, q_kmer_dic[kmer], kmer) #if yes, prints 
            # print: (# target_sequence_name   # target_start    # query_start  # k-mer)
        else:
            continue
