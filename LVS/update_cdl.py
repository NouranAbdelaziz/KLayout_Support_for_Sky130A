#input file
fin = open("my_library.cdl", "rt")
#output file to write the result to
fout = open("libraries_updated.cdl", "wt")
#for each line in the input file
for line in fin:
	#read replace the string and write to output file
	line = line.replace('phighvt', 'pfet_01v8_hvt')
	line = line.replace('nshort', 'nfet_01v8')
	if not (line.startswith('+')):
		fout.write(line)
#close input and output files
fin.close()
fout.close()