#!/usr/bin/env python3

# BEFORE STARTING
# Try to read "input_file.txt"
FH_in = open('getseq/input_file.txt', 'rt')
FH_in.readlines()
FH_in.close()

#[‘Hello World!\n’,’How are you?\n’]


# Try to write "output_file.txt"
FH_out = open('getseq/output_file.txt','wt')
FH_out.write('I am fine.\nGood Bye World!\n')
FH_out.close()

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

FH_in = open(sequences_in_path, 'rt')
FH_out = open(sequence_out_path, 'wt')

for line in FH_in.readlines():
  # this is a sequence header
  if line[0] == '>':
    if line == '>' + name + '\n' :
      write_seq = True
      FH_out.write(line)
    else:
      write_seq = False
  # this a nucleic sequence line
  elif write_seq == True:
    FH_out.write(line)

FH_in.close()
FH_out.close()

#
# Read sequences.fasta and extract INSERT of sequence2 (using a start and stop position)
# Save it in getseq/sequence2_insert_manual.fasta output file
#

name='sequence2'
sequences_in_path = 'getseq/sequences.fasta'
sequence_out_path = 'getseq/sequence2_insert_manual.fasta'
start = 8 # TO COMPLETE
stop = 13 # TO COMPLETE

FH_in = open(sequences_in_path, 'rt')
FH_out = open(sequence_out_path, 'wt')

for line in FH_in.readlines():
  if line[0] == '>':
    if line == '>' + name + '\n' :
      write_seq = True
      FH_out.write(line)
    else:
      write_seq = False
  # this a nucleic sequence line
  elif write_seq == True:
    FH_out.write(line[start:stop+1] + '\n')

FH_in.close()
FH_out.close()

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

write_seq = False

for record in SeqIO.parse(sequences_in_path, "fasta"):
  if record.id == name :
    write_seq = True
    SeqIO.write(record, sequence_out_path, "fasta")

#
# Read sequences.fasta and extract INSERT of sequence2 (using a start and stop position)
# Save it in getseq/sequence2_insert_biopython.fasta output file
#
name='sequence2'
sequences_in_path = 'getseq/sequences.fasta'
sequence_out_path = 'getseq/sequence2_insert_biopython.fasta'
start = 8
stop = 13
write_seq = False

for record in SeqIO.parse(sequences_in_path, "fasta"):
  if record.id == name:
    write_seq = True
    record.seq = record.seq[start:stop+1]
    SeqIO.write(record, sequence_out_path, "fasta")
