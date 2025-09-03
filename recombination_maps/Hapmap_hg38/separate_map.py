#!/usr/bin/env python

map_file = "genetic_map_hg38_withX.txt"

with open(map_file,'r') as map:
    next(map) # skip header
    header = "chr position COMBINED_rate(cM/Mb) Genetic_Map(cM)\n"
    for line in map:
        line=line.strip().split(" ")
        chrom = line[0]
        with open("per_chr/hapmap_hg38_chr%s.txt" % chrom,'a') as chr_map:
            if not chr_map.tell():
                print("Writing file: hapmap_hg38_chr%s.txt" % chrom)
                chr_map.write(header)
            chr_map.write(" ".join(line) + "\n")
