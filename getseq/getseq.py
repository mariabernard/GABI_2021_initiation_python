#!/usr/bin/env python3

# BEFORE STARTING
# Try to read "input_file.txt"

# Try to write "output_file.txt"

##############################################################
#
#     MANUAL EXTRACTING
#
# Read sequences.fasta and extract sequence1
# Save it in getseq/sequence1_manual.fasta output file
#
name='sequence1'
sequences_in_path = 'getseq/sequences.fasta'
sequence_out_path = 'getseq/sequence1_manual.fasta'

#    TO COMPLETE

#
# Read sequences.fasta and extract INSERT of sequence2 (using a start and stop position)
# Save it in getseq/sequence2_insert_manual.fasta output file
#
name='sequence2'
sequences_in_path = 'getseq/sequences.fasta'
sequence_out_path = 'getseq/sequence2_insert_manual.fasta'
start = "??" # TO COMPLETE
stop = "??" # TO COMPLETE

#    TO COMPLETE

##############################################################
#
#     EXTRACTION USING BioPython SeqIO : https://biopython.org/wiki/SeqIO 
#
from Bio import SeqIO

#
# Read sequences.fasta and extract sequence1
# Save it in getseq/sequence1_biopython.fasta output file
#
name='sequence1'
sequences_in_path = 'getseq/sequences.fasta'
sequence_out_path = 'getseq/sequence1_biopython.fasta'

#    TO COMPLETE

#
# Read sequences.fasta and extract INSERT of sequence2 (using a start and stop position)
# Save it in getqes/sequence2_insert_biopython.fasta output file
#
name='sequence2'
sequences_in_path = 'getseq/sequences.fasta'
sequence_out_path = 'getseq/sequence2_insert_biopython.fasta'
start = "??" # TO COMPLETE
stop = "??" # TO COMPLETE