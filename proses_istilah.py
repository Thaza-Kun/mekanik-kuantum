import json

data = "istilah-kuantum.json"
file = "A1-kamus.Rmd"

with open(data, "r") as r:
	kata = r.read()

kata = json.loads(kata)

def susun(fail, data):
	'''susun data ikut huruf dan simpan dalam fail'''
	sort = sorted(data, key= lambda x: x['kata'])
	with open(fail, "w") as w:
		w.write(json.dumps(sort, indent=4, sort_keys=True))

def masuk(kata):
	'''memasukkan istilah dari json ke Rmd'''
	kamus = '# Daftar Istilah {-}\n\n'
	for i in kata:
		if i['sinonim'] != []:
			tambah = ''
			for n in i['sinonim']:
				masuk = " / " + n
				tambah += masuk
		else:
			tambah = ''
		text = i['kata'] + tambah
		english = ''
		if i['terjemahan'][0] != i['terjemahan'][-1]:
			for n in i['terjemahan']:
				if n != i['terjemahan'][-1]:
					english += n + ", "
				else:
					english += n
		else:
			english = i['terjemahan'][0]
		terjemahan = ": " + f"(*{english}*)"
		text += "\n" + terjemahan
		makna = ": " + i['makna'] + "\n"
		text += "\n" + makna + "\n"
		kamus += text

	with open(file, "w") as f:
		f.write(kamus)

masuk(kata)