# CODE SNIPPETS LAKE

Here is my lake of code snippets to help me whe I'm coding. There is Python, Bash and more languages code lines. Some lines was write by myself and some writed by AI or at least AI based. Let's enjoy.

## PYTHON
### List text cleaner and remove special characters

`````
import unicodedata
import re
import os

def process_names(file_path, terms_to_remove, output_file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        names = file.read().splitlines()

    processed_names = []
    for name in names:
        name = name.upper()
        name = unicodedata.normalize('NFD', name)
        name = name.encode('ascii', 'ignore').decode('utf-8')
        name = re.sub(r'[^A-Z0-9\s]', '', name)
        name = name.replace('Ç', 'C')
        name = name.replace('  ', ' ')
        for term in terms_to_remove:
            name = name.replace(term, '')
        processed_names.append(name.strip())

    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for name in processed_names:
            output_file.write(name + '\n')

file_path = 'INPUTS/name_list.txt'
terms_to_remove = ["V4 NUC ", 
                   "NUC2 ", 
                   "NUC 1 ", 
                   "V1"
]
output_file_path = 'OUTPUTS/new_name_list.txt'
process_names(file_path, terms_to_remove, output_file_path)
`````