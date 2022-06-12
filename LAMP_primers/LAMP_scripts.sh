##Downloaded All Genomes from NCBI with Entrez##
esearch -db nucleotide -query “Cacao swollen shoot virus AND complete genome” | efetch -format fasta > cssv_genomes.fasta

##Doing the same thing but getting them as individual files##

def BacteriaSearch(Organism):
    Entrez.email = 's2037423@ed.ac.uk'
    search_term = f'{Organism} AND complete genome'
    handle = Entrez.esearch(db='nucleotide', term=search_term, retmax=1000)
    genome_ids = Entrez.read(handle)['IdList'] 
    os.mkdir(f"/Users/maartenvandenancker/Desktop/genomes/{Organism}")

    for genome_id in genome_ids:
        record = Entrez.efetch(db="nucleotide", id=genome_id, rettype = "fasta", retmode = "text")
        filename = 'genBankRecord_{}'.format(genome_id)
        print('Writing:{}'.format(filename))
        f = open(f"/Users/maartenvandenancker/Desktop/genomes/{Organism}/{filename}.txt", "x")
        f = open(f"/Users/maartenvandenancker/Desktop/genomes/{Organism}/{filename}.txt", 'w')
        f.write(record.read())
        print('Completed:{}'.format(filename))
    return("Done")

print(BacteriaSearch('Cacao swollen shoot virus'))

##Used Clustal Omega to do Multiple Sequence Alignment##
##job clustalo-I20220607-154940-0829-3214838-p2m##

##Used EMBOSS Cons to generate consensus sequence##
##job emboss_cons-I20220607-204027-0433-85067673-p1m##

##Generating some files which are needed to make common and specific primers##
cd GLAPD
./Single -in cssv_consensus.txt -out cssv_consensus
##Two files, Inner/cssv_consensus and Outer/cssv_consensus are generated##

##Using GLAPD to generate LAMP primers and account for commonality and specificity##
##Use the previously generated Inner and Outer files##
##Generating bowtie indexes because you need to for GLAPD##
bowtie-build cssv_genomes.fasta cssv_index

##Generating the headers (in --common in par.pl)##
grep -A0 '^>' Desktop/cssv_genomes.fasta | grep -v '^--$' > Desktop/cssv_headers.txt


ls -m ~/Desktop/genomes/Cacao\ swollen\ shoot\ virus/ | sed -e 's/.txt//g' | tr -d " \t\n\r" > ~/Desktop/index_list.txt
perl ./par.pl --in cssv_consensus --ref ~/Desktop/cssv_consensus.txt --bowtie /usr/local/bin/bowtie --index ~/Desktop/cssv_index --common ~/Desktop/cssv_headers.txt --left

./LAMP -in cssv_consensus -ref ~/Desktop/cssv_consensus.txt -out common_specific_primers.txt -common -specific

##All the GLAPD stuff is done to account for commonality and specificity, above is generating the needed files and doing it with the aligned genomes, below is doing the same but for every sequenced genome individually##



for genome in ~/Desktop/genomes/Cacao\ swollen\ shoot\ virus/*;\
do \
filename=$(basename $genome .txt);\
cd ~/GLAPD;\
./Single -in $genome -out $filename;\
perl ./par.pl --in $filename --ref $genome --bowtie /usr/local/bin/bowtie --index ~/Desktop/cssv_index --common ~/Desktop/cssv_headers.txt --left;\
./LAMP -in $filename -ref $genome -out ~/LAMP_primers/${filename}_CS_primers.txt -common -specific;\
done;\


