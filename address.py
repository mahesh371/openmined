book = {}
book['tom']={
    'name': 'tom',
    'address': '12-66',
    'phone': 5263564355
}
book['bob']={
    'name': 'bob',
    'address': '12-68',
    'phone': 7635872562
}

import json
s=json.dumps(book)
with open("book.txt","w") as f:
    f.write(s)