import re

with open('bloggen.html', 'r') as f:
    kalla = f.read()    
    result = re.findall('<\w+>|<\/\w+>', kalla)
    print(result)
