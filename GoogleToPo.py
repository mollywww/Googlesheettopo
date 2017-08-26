# -*- coding: utf-8 -*-
# GoogleSheets to po
msgid = None
msgtxt = None
msgstr = None
with open('msgid.txt', 'r', encoding='utf-8') as f:
    msgid = [_.strip() for _ in f.readlines()]

with open('msgtxt.txt', 'r', encoding='utf-8') as f:
    msgtxt = [_.strip() for _ in f.readlines()]

with open('msgstr.txt', 'r', encoding='utf-8') as f:
    msgstr = [_.strip() for _ in f.readlines()]

if len(msgid) !=  len(msgtxt) != len(msgstr):
    print('文件長度不同, 請檢查檔案!')
else:
    with open('zh_TW.po', 'w', encoding='utf-8') as f:
        f.write('"Application: Dont\' Starve\\n"\n"POT Version: 2.0\\n"\n\n\n')
        for i in range(len(msgtxt)):
            f.write(f'#. {msgtxt[i]}\nmsgctxt "{msgtxt[i]}"\nmsgstr "{msgstr[i]}"\n\n')
