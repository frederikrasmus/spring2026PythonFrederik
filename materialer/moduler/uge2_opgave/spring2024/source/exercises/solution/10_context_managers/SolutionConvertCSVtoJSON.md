# (Solution) Convert CSV to JSON

> Convert the [Frida20190612da_utf8.csv](https://github.com/python-elective-fall-2019/Lesson-09-context-managers/blob/master/exercises/Frida20190612da_utf8.csv) file into json


```python
import csv
import json

with open('Frida20190612da_utf8.csv', 'r') as f:
    reader = csv.DictReader(f, delimiter=";")
    with open('frida.json', 'w') as j:
        j.write(json.dumps(list(reader)))
```
