with open("filename.txt","r+") as f:
    lines =f.readlines()
    #pointer to top
    f.seek(0)
    #clear file content
    f.truncate()
    for line in lines:
        if not line.startswith('hi'):
            f.write(line)

f.close()