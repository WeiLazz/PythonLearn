with open('test.txt','r',encoding='utf-8') as f:
    content = f.read()
    print(content)
    f.seek(0)
    first_line = f.readline()
    print('first_linr:',first_line.strip())
    f.seek(0)
    lines = f.readlines()
    print('lines:',lines)
