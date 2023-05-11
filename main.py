# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sys
#    print(sys.argv[1])

'''def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')'''
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

print(find_ssr(sys.argv[1]))
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
transcribe("CttGAT")

#part 3
def translate(rna_seq, reading_frame):
    acidic_base_string = []
    for i in rna_seq[reading_frame:-(len(rna_seq-(reading_frame))%3+1):3]:
        if rna_seq[i] == "A":
            if "AUG" in rna_seq[i:i+3]:
                acidic_base_string.append("M ")









