from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
import pysnooper

@pysnooper.snoop('outputs/file.log')

def adder():
	tokenizer = AutoTokenizer.from_pretrained("fidukm34/biobert_v1.1_pubmed-finetuned-ner-finetuned-ner")
	model = AutoModelForTokenClassification.from_pretrained("fidukm34/biobert_v1.1_pubmed-finetuned-ner-finetuned-ner")
	nlp = pipeline("ner", model=model, tokenizer=tokenizer)

	with open("Akshat_A100/example.txt", 'r') as f:
		example = f.read()
		f.close()

	ner_results = nlp(example)

	with open("outputs/result.txt",'w+') as f:
		f.write(ner_results)

	f.close()
adder()





