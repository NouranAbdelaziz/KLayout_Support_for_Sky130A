#input file
fin = open("gpio_logic_high_cells.spice ", "rt")
#output file to write the result to
fout = open("gpio_logic_high_cells_new.spice", "wt")
#for each line in the input file
for line in fin:
	#read replace the string and write to output file
    
    if (line.startswith('X')):
        line = line.replace('X', 'M', 1)
    fout.write(line)
#close input and output files
fin.close()
fout.close()
