words_path = 'words.txt'

words = open(words_path,"r").readlines()
wn = []
for word in words: wn.append(word.lower().replace("\n",""))
words = wn
wn = []

while True:
	opt=input("Compress or decompress? (c/d): ")
	out = ""
	if opt == "c":
		inp = input("Text: ")
		
		for iword in inp.split(" "):
			if iword != ";":
				try:
					out += str(words.index(iword.lower())) + ";"
				except ValueError:
					out += iword + ";"
		print(out)
	elif opt == "d":
		inp = input("CP26 text: ")
		out = ""
	
		for iword in inp.split(";"):
			if iword.isnumeric():
				out += words[int(iword)] + " " # fun thing to do is instead of "[int(iword)]" do "[int(iword)+1]" to shift the output
			else:
				out += iword + " "
		print(out)