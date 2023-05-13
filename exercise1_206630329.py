# Shir Adler 206630329

import sys

#part 1
def find_ssr(dna_seq):
    #list of illegible sub-sequences
    possible_repeat_seq_set = set()
    #checks for every letter till -6
    for i in range(0, len(dna_seq)):
        #a list of the repeats of the first letter in the current sub-sequence
        let_repeats = []
        #checks if the first letter in the sub-sequence repeats itself in the next 6 letters
        s = 7
        if len(dna_seq[i:-1]) < s:
            s = len(dna_seq[i:-1])
        if dna_seq[i] in dna_seq[i+1:i+s]:
            #adding the repeats locations to a list
            for j in range(i+1 , i+s):
                if dna_seq[i] == dna_seq[j]:
                    let_repeats.append(j)
                #adds possible sub-sequences to a set
                    if j < i + s:
                        possible_repeat_seq_set.add(dna_seq[i:j])
                    if i == j-1:
                        possible_repeat_seq_set.add(dna_seq[i])
                    else:
                        possible_repeat_seq_set.add(dna_seq[i:j-1])

    #creating dictionary for repeating sequences that follow the requirement.
    repeating_dic = {}
    j = 0
    #checks for biggest number of repeats for the possible sequences found
    for j in range(0, len(possible_repeat_seq_set)):
        num_repeats = 3
        while (list(possible_repeat_seq_set)[j])*num_repeats in dna_seq:
            #updates repeating value for the sub-sequence from 3 repeats onwards
            repeating_dic.update({list(possible_repeat_seq_set)[j]:num_repeats})
            num_repeats+=1
    return {s: repeating_dic[s] for s in sorted(repeating_dic)}
#part 2
def transcribe(dna_seq):
    #turning the inputed string to CAPS
    dna_cap = dna_seq.upper()
    dna_cap = dna_cap.replace("A","U")
    dna_cap = dna_cap.replace("T", "A")
    # changing G temporarily so it won't intertwine with the change from C to G.
    dna_cap = dna_cap.replace("G", "g")
    dna_cap = dna_cap.replace("C", "G")
    dna_cap = dna_cap.replace("g", "C")
    # printing the RNA from 5' to 3'
    print(dna_cap[::-1])

def find_all(seq, sub_seq):
    start = 0
    while True:
        start = seq.find(sub_seq, start)
        if start == -1:
            return
        if start % 3 == 0:
            yield start
        start += len(sub_seq) # use start += 1 to find overlapping matches
#part 3
def translate(rna_seq, reading_frame):
    #dictionary for all the amino acids
    amino_acid_dic = {"UUU":"F","UUC":"F","UUA":"L","UUG":"L",
                      "CUU":"L","CUC":"L","CUA":"L","CUG":"L",
                      "AUU":"I","AUC":"I","AUA":"I","AUG":"M",
                      "GUU":"V","GUC":"V","GUA":"V","GUG":"V",
                      "UCU":"S","UCC":"S","UCA":"S","UCG":"S",
                      "CCU":"P","CCC":"P","CCA":"P","CCG":"P",
                      "ACU":"T","ACC":"T","ACA":"T","ACG":"T",
                      "GCU":"A","GCC":"A","GCA":"A","GCG":"A",
                      "UAU": "Y", "UAC": "Y", "UAA": "STOP", "UAG": "STOP",
                      "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
                      "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
                      "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
                      "UGU": "C", "UGC": "C", "UGA": "STOP", "UGG": "W",
                      "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
                      "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
                      "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}
    rna_seq = rna_seq[reading_frame:(-((len(rna_seq)-reading_frame)%3+1))]
    f = 0
    acidic_base_string = []
    #eliminating sequences without a start codon
    s_codon_list =  list(find_all(rna_seq,"AUG"))
    if not s_codon_list:
        return "None"
    for i in range(0,len(s_codon_list)):
        #temp string for finding amino bases in sub-sequences and seeing if its relevant length wise
        acidic_base_temp = []
        start = s_codon_list[i]
        #adding amino acids
        while amino_acid_dic[rna_seq[start:start + 3]] != "STOP" and start < len(rna_seq):
            acidic_base_temp.append(amino_acid_dic[rna_seq[start:start + 3]])
            start += 3
            #checking length of amino acids chain found
        if len(acidic_base_temp) > len(acidic_base_string):
            acidic_base_string=acidic_base_temp
    return acidic_base_string

#part 4-main
#function to print the SSR sub sequences we found function
def print_ssr(seq):
    ssr_dic = find_ssr(seq)
    key_list = list(ssr_dic.keys())
    if not key_list:
        print("No simple repeats in DNA sequence")
    else:
        for i in range(0, len(key_list) - 1):
            print(key_list[i] + "," + str(ssr_dic[key_list[i]]) + ";", end='')
        print(key_list[i + 1] + "," + str(ssr_dic[key_list[i + 1]]))

#function to print the transcribing function
def print_transcribe(dna_seq):
    print("RNA sequence: ",end='')
    transcribe(dna_seq)

    # function to print the translating function
def print_translation(rna_seq, reading_frame):
    acidic_bases = translate(rna_seq, reading_frame)
    if acidic_bases=="None":
        print("Non-coding RNA")
    else:
        for i in range(0, len(acidic_bases)-1):
            print(acidic_bases[i]+";", end='')
        print(acidic_bases[i+1])

if __name__ == '__main__':
    print_ssr(sys.argv[1])
    print_transcribe(sys.argv[2])
    print_translation(sys.argv[3], int(sys.argv[4]))











