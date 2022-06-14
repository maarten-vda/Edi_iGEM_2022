# Edi_iGEM_2022
GitHub repository for Edinburgh-UHAS Ghana iGEM 2022 team

Hi everyone! Here is the GitHub repository where we will be storing our code and mathematical modelling.

In the folder LAMP_primers you will see the data I have generated to make the LAMP primers, as well as the scripts I wrote.
Please when you are adding code make sure it is well annotated so we can follow your thought process.

Cheers,

-Maarten


# Results for multiplexing primers
So, from the code weve got some results as to what is the maximum number of strains we could target with 2 sets of primers, while still having the Togo_B strain (most prevalent strain in Ghana by a long shot), and it is 29/51 strains can be identified with the LAMP primers. These strains are:
'MN433962.1', 'MN433961.1', 'MN433960.1', 'MN433959.1', 'MN433958.1', 'MN433957.1', 'MN433956.1', 'MN433955.1', 'MN433954.1', 'MN433953.1', 'MN433952.1', 'MN433951.1', 'MN433950.1', 'MN433949.1', 'MN433948.1', 'MN433947.1', 'KX592581.1', 'KX592580.1', 'KX592579.1', 'KX592578.1', 'KX592577.1', 'KX592576.1', 'KX592575.1', 'AJ609019.1', 'AJ609020.1', 'NC_001574.1', 'AJ781003.1', 'L14546.1', 'AJ534983.1'

And they use primers designed from the 2 genomes:
Aligned_file_CS_primers.txt
genBankRecord_347868_CS_primers.txt

The primer sets themselves are:
Aligned_file_CS_primers.txt:
  F3: pos:6450,length:19 bp, primer(5'-3'):GAGTGGTTAGTTATGCCCT
  
  F2: pos:6483,length:20 bp, primer(5'-3'):GCTCCTGCAGTATTTCAAAG
  
  F1c: pos:6524,length:23 bp, primer(5'-3'):CAGCTATGAATTCTTCTGTGCCT
  
  B1c: pos:6553,length:23 bp, primer(5'-3'):TTGATGACATCTTGGTCTTCAGC
  
  B2: pos:6608,length:20 bp, primer(5'-3'):GGCAGATTGTTAGCATGATT
  
  B3: pos:6642,length:24 bp, primer(5'-3'):ACATATTTTATTTGGGCTTAGGAC

genBankRecord_347868_CS_primers.txt:
  F3: pos:460,length:24 bp, primer(5'-3'):TAGTATACAAGAGTGGTATGAGAA
  F2: pos:485,length:18 bp, primer(5'-3'):TCACACACAGCAAACCTT
  F1c: pos:527,length:23 bp, primer(5'-3'):AACTGGTTGTTGGTCACTTTACT
  B1c: pos:550,length:22 bp, primer(5'-3'):AGCACATAACCTTGCAGTAACC
  B2: pos:610,length:21 bp, primer(5'-3'):TCTTGAATCTGCTTCAGGTTT
  B3: pos:638,length:20 bp, primer(5'-3'):ACACGGGTGTTTAATTCAAG
  
To find which pair of primer sets was the best I wrote a python script, its called multiplexity.py. To generate the primers themselves, look at LAMP_scripts.sh
