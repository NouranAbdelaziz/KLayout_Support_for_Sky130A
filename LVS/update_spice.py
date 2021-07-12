#input file
fin = open("sky130_fd_sc_hd.spice ", "rt")
#output file to write the result to
fout = open("sky130_fd_sc_hd_new.spice", "wt")
#for each line in the input file
for line in fin:
	#read replace the string and write to output file
    if (line.startswith('X')):
        line = line.replace('X', 'M')
    fout.write(line)
#close input and output files
fin.close()
fout.close()