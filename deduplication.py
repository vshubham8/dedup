import re, math
from collections import Counter

WORD = re.compile(r'\w+')

# Counter(WORD.findall('hello world')) --> Counter({'world': 1, 'hello': 1})
# Counter(WORD.findall('hello')) --> Counter({'hello': 1})

def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    nmr = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    dnr = math.sqrt(sum1) * math.sqrt(sum2)

    if not dnr:
        return 0.0
    else:
        return float(nmr) / dnr

def text_to_vector(text):
    return Counter(WORD.findall(text))

def get_similarity(a, b):
    a = text_to_vector(a.strip().lower())
    b = text_to_vector(b.strip().lower())
    return get_cosine(a, b)

def main():
	handle = open('Deduplication Problem - Sample Dataset.csv','rU').readlines()
	header = handle[0]
	data = handle[1::]

	dict_acc_to_dob_gn = {}
	for line in data:
		features = line.split(',')
		dob = features[1]
		gn = features[2]
		fn = features[-1].split('\n')[0]
		ln = features[0]
		s = ln+'#'+dob+'#'+gn+'#'+fn
		dob_gn = dob+gn
		try:
			dict_acc_to_dob_gn[dob_gn].append(s)
		except:
			dict_acc_to_dob_gn[dob_gn] = []
			dict_acc_to_dob_gn[dob_gn].append(s)
	deduplicated_records = {}
	for i in dict_acc_to_dob_gn:
		dict_acc_to_dob_gn[i] = list(set(dict_acc_to_dob_gn[i]))
		names = dict_acc_to_dob_gn[i]
		mega = []
		for j in names:
			cluster = []
			for k in names:
				ln1 = j.split('#')[0]
				ln2 = k.split('#')[0]
				fn1 = j.split('#')[-1]
				fn2 = k.split('#')[-1]
				theta1 = get_similarity(fn1,fn2)
				theta2 = get_similarity(ln1,ln2)
				if theta1 > 0.5 and theta2 > 0.5:
					cluster.append(max(j,k))
			mega.append(list(set(cluster)))
		deduplicated_records[i] = mega

	ans = {}
	for j in deduplicated_records:
		mega2 = []
		lol = deduplicated_records[j]
		for k in lol:
			mega2.append(max(k))
		ans[j] = set(mega2)
	actual_distinct_records = 0
	op = open('output.csv','w')
	print 'RECORDS after DEDUPLICATION:-'
	print '--------------------------------------'
	print header
	op.write(header)
	for i in ans.values():
		for j in i:
			record = ','.join(j.split('#'))
			print record
			op.write(record+'\n')
			actual_distinct_records += 1
	print '--------------------------------------'

	# print actual_distinct_records


if __name__ == '__main__':
	main()
	#### removing lastline from csv file ####
	f = open('output.csv','rU').readlines()
	ff = open('output.csv','w')
	for i in xrange(0,len(f)):
		if i == len(f)-1:
			ff.write(f[i].split('\n')[0])
		else:
			ff.write(f[i].split('\n')[0]+'\n')



# #################### test cases to cross validate ###################

# # get_similarity('Vladimir Antonio Frometa Garo','Vladimir Antonio Frometa Garo') = 1
# # get_similarity('Vladimir Antonio Frometa Garo','Vladimir Antonio F Garo') = 0.75
# # get_similarity('Vladimir Antonio Frometa Garo','Vladimir A Frometa Garo') = 0.75
# # get_similarity('Vladimir Antonio Frometa Garo','Vladimir Frometa Garo') = 0.866
# # get_similarity('Vladimir Antonio Frometa Garo','Vladimir Antonio Garo') = 0.866
# # get_similarity('Vladimir Antonio Frometa Garo','Vladimir Frometa') = 0.707
# # get_similarity('Vladimir Garo','Vladimir Frometa') = 0.5
# # get_similarity('Vladimir Garo','Vladimir G') = 0.5

# # good test cases:
# # test = dict_acc_to_dob_gn['24/11/34M']
# # test = dict_acc_to_dob_gn['07/10/37M']
# # test = dict_acc_to_dob_gn['06/12/37F']
# # for i in test:
# # 	print i
# # print get_similarity('HAROLD SMITH JR','HAROLD FAGEN JR')

# # print deduplicated_records['24/11/34M']
# # for i in deduplicated_records['24/11/34M']:
# 	# print ' '.join(i[0].split('#'))
# # print deduplicated_records['24/11/34M']

# # from nltk.corpus import wordnet
# # print 'FAGEN'.wup_similarity('SMITH')
# # wordFromList1 = wordnet.synsets(word1)[0]
