# Class to read filename and create a dictionary
class read_file:
	def __init__ (self,filename):
		self.filename = filename

	def read_into_list_byLine(self):
		try: #exception handeling in case of bad input file
			with open (self.filename, 'r') as in_file:
				self.file_list = [line.split(",") for line in in_file.read().splitlines()]	 	
		except IOError:
			raise IOError("{} is not found in directory".format(self.filename))


class create_dictionary:
	def __init__ (self,file_list):
		self.file_list = file_list

	def create_list_by_line(self):
		self.ls_to_str=[]
		for i in range(len(self.file_list)):
			for j in range(len(self.file_list[i])):
				self.ls_to_str.append(self.file_list[i][j])

	def create_str_char(self):
		self.str_by_char = ''.join(self.ls_to_str)

	def create_list_word(self):
		self.ls_by_word = self.str_by_char.split(" ")
		
	def create_dict(self,listt):
		self.dictionary_name={}
		for char in listt:
			self.dictionary_name[char] = self.dictionary_name.get(char,0) + 1


class Protein:
	def __init__(self,string):
		self.string = string
		self.condon_dict = {
		"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
       	"UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
       	"UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
       	"UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
       	"CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
       	"CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
       	"CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
       	"CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
      	"AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
       	"ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
       	"AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
       	"AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
       	"GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
       	"GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
       	"GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
       	"GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",
       	}

       	self.Monoisotopic_mass_dict = {
       	'A': 71.03711,
    	'C': 103.00919,
    	'D': 115.02694,
    	'E': 129.04259,
    	'F': 147.06841,
    	'G': 57.02146,
    	'H': 137.05891,
    	'I': 113.08406,
    	'K': 128.09496,
    	'L': 113.08406,
    	'M': 131.04049,
    	'N': 114.04293,
    	'P': 97.05276,
    	'Q': 128.05858,
    	'R': 156.10111,
    	'S': 87.03203,
    	'T': 101.04768,
    	'V': 99.06841,
    	'W': 186.07931,
    	'Y': 163.06333,
    	}

	def transcription(self):
		self.new_string = self.string.replace("T","U")

	def reverse_compliment(self):
		new_string1 = self.string.replace("A","X").replace("T","A").replace("X","T")
		new_string2 = new_string1.replace("C","X").replace("G","C").replace("X","G")
		self.reverse_string = self.new_string2[-1::-1] #string[start,end,step]
		

	def translation(self,mRNA):
		self.peptide = ""
		start_sequence = mRNA.find("AUG")
		if(.start_sequence != -1):
    		while(start_sequence + 2 < len(mRNA)):
        		code = mRNA[start_sequence:start_sequence + 3]
        		if(code == "UAA" or code == "UAG" or code == "UGA"):
            		break
        		start_sequence += 3 # index to the next 3 nucleotides
        		self.peptide += codon_dict[code]

   #optimizw code above ^^^

   	def weight(self):
   		mass = 0
   		for AA in self.peptide:
   			mass += self.Monoisotopic_mass_dict[char]





