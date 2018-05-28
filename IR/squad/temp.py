
import nltk
import json
with open('/home/arusia/data/squad/valid-v1.1.json') as f, open('valid.json','w') as g:
	dat=eval(f.read())
	dat2=[]
	for s in dat['data']:
		story={'context':[],'questions':[],'targets':[],'answer':[]}
		px={}
		for i,p in enumerate(s['paragraphs']):
			story['context'].append(p['context'])
			for q in p['qas']:
				story['questions'].append(q['question'])
				story['answer'].append(q['answers'][0]['answer_start'])
				story['targets'].append(i)
		dat2.append(story)
	json.dump(dat2,g)
