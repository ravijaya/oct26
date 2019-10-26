"""demo for the context manager - file copy """



with open('passwd.txt') as fp, open('passwd_copy.txt', 'w') as fw:
    fw.write(fp.read())
