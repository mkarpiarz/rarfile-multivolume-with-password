import rarfile

with rarfile.RarFile('multivolume.part1.rar') as rf:
    if rf.needs_password():
        rf.setpassword('abc123')
    print(rf.volumelist())
    for f in rf.infolist():
        rf.extract(f.filename, path='./content')

    print('DONE')
