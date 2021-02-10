from Bio import SeqIO
from Bio import Entrez
import pandas as pd
from Bio.Seq import Seq


#### INSTRUCTION ####

#run as:
    #nohup python3 borna_parse &
    #log will be outputed in nohup.out

#first edit the two variables below (i.e. email and input file)

#add your email here:
Entrez.email = ""

#enter name of csv file here:
    #required columns:
        #acc - contains scaffold NCBI accessions
        #start - integer of EVE starting position in the scaffold
        #end - integer of EVE ending position in the scaffold
        #name - EVE names
file = '21kawasaki_ebln.csv'

#N.B.: This script requires a fairly stable internet connection.
    #If internet drops you can restart from where it stopped at line 62.

######################



def strshow(thestr):
    print(len(thestr))
    print('%s...%s'%(thestr[0:100], thestr[-100:]))
    print('\n')
    
def rmhead(s):
    nohead = s[s.find('\n')+1:]
    noreturn = nohead.replace('\n', '')
    noreturn = noreturn.replace('\r', '')
    return noreturn

def writefas(h, theseq, thefas):
    fasseq = '>%s\n%s\n'%(h, str(theseq))
    with open(thefas, 'a+') as tw:
        tw.write(fasseq)

    

df = pd.read_csv(file)

# print(df)

accs = list(df.acc)
allstarts = list(df.start)
allends = list(df.end)
names = list(df.name)
strands = list(df.strand)

#change start here if need to restart
for i in range(0, len(accs)):
    # range(len(accs))


    header = "%s|%s"%(names[i],accs[i])

    print(header)

    net_handle = Entrez.efetch(db="nucleotide", id=accs[i], rettype='fasta', retmode="text")

    fasraw = net_handle.read()

    strshow(fasraw)

    fas = rmhead(fasraw)

    strshow(fas)

    ebln = str(fas)[(allstarts[i]-1):(allends[i])]
    
    seqebln = Seq(ebln)
    
    if strands[i] == '-':
        ebln = seqebln.reverse_complement()
    else:
        pass     

    writefas(header, ebln, file.replace('.csv', '_nt.fas'))

    # print('\n\n')
    # print(ebln)
    seqebln = Seq(str(ebln))

    aaebln = str(seqebln.translate())
    writefas(header, aaebln, file.replace('.csv', '_aa.fas'))
    print('\n')
    print('THIS IS %i'%i)
    print('\n\n')

