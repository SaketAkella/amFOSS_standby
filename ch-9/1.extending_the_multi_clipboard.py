import shelve
import pyperclip
import sys

emcb_shelf=shelve.open('emcb')
if len(sys.argv)==3 and sys.argv[1].lower()=='save':
    emcb_shelf[sys.argv[1]]=pyperclip.paste()
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    emcb_shelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del emcb_shelf[sys.argv[2]]
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(emcb_shelf.keys())))
    elif sys.argv[1].lower() == 'deleteall':
        for keyword in list(emcb_shelf.keys()):
            del emcb_shelf[keyword]
    elif sys.argv[1] in emcb_shelf:
        pyperclip.copy(emcb_shelf[sys.argv[1]])
emcb_shelf.close()