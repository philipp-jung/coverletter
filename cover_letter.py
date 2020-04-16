import os
import csv
import tempfile
import datetime
import subprocess
from configuration import get_config

def get_recipients():
    with open('./recipients.csv', 'r') as f:
        reader = csv.DictReader(f)
        return [{'rec_company': r['rec_company'],
                 'rec_street': r['rec_street'],
                 'rec_zip': r['rec_zip']
                 } for r in reader]

def get_snippets():
    snippets = []
    for filename in os.listdir('./snippets'):
        f = open('./snippets/'+filename)
        snip = [row for row in f]
        snip = ''.join(snip)
        snippets.append((filename, snip))
    return snippets

def get_template():
    with open('./brief.md') as f:
        return f.read()

template = get_template()
sender_info = get_config()

for i, rec in enumerate(get_recipients()):
    print(f'{i}: {rec}')
rec_id = int(input('Choose recipient (int): '))
rec_info = get_recipients()[rec_id]

for i, snip in enumerate(get_snippets()):
    print(f'{i}: {snip[0]}')
snip_id = int(input('Choose snippet (int): '))
snippet = get_snippets()[snip_id][1]

dat = {**sender_info,
        **rec_info,
        'snippet': snippet,
        'date': datetime.date.today().strftime('%d.%m.%Y'),
        'subject': 'Bewerbung',
        }

formatted_for_pandoc = [('-V', dat[k]) for k in dat.keys()]

new_markdown = template.format(**dat)

with open('./cache.md', 'w') as f:
    f.write(new_markdown)

subprocess.call(['/usr/bin/pandoc', './cache.md',
                 '-o', './brief.pdf',
                 '--template=./letter.latex',
                 '--latex-engine=xelatex'])
                 #'--pdf-engine=xelatex'])
