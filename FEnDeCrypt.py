#+++File encrypter+++
#import sec
import os; import glob; from cryptography.fernet import Fernet
#File Pick up 

def encrypt():
    global inputdir
    ori=os.getcwd()
    inputdir=input("Input file dir")
    os.chdir(ori)

def filefind():
    """change dir to file path, 
    picks up files places them in a dict
    
    Args:
     directory path(str)
     
    Returns: 
     Panda DataFrame"""
    global filenms
    filenms=[]
    try:
        os.chdir(inputdir)
    except FileNotFoundError as e:
        print('Input correct path directory')
        filefind()
    #
    files=[f for f in os.listdir('.') if os.path.isfile(f)]
    val=len(files)
    lon=list(range(1, val+1))
    zipf=dict(zip(lon,files))
    #
    print(zipf)
    selfile=input("Select file number")
    inum=int(selfile)
    filenms.append(zipf.get(inum))
    mr=input('Another File? y/n')
    if mr=='y':
        filefind()
    if mr=='n':
        return(filenms)



















def



    try:
        
        fileinput=input('Enter file name')

    except FileNotFoundError as e:
        print('File not found')
        filefind
    ()
    
    state=input('More files to collect? y/n')
    if state=='y':
        filefind
    
    if state=='n':
        return(filenm)





    files=[]
    for file in os.curdir():
        if file != fileinput:
            continue
    if os.path.isfile(file):
        files.append






    file=glob.glob(inputdir + '\\*.rsc')
    di_selfile={ i : file[i] for i in range(0, len(file) ) }
    return(di_selfiles) 






    files = []
    for file in os.listdir():
        if file == 'FernetEncrypt.py' or file == 'tokn_AES128' or file == 'FernetDecrypt.py':
            continue
    if os.path.isfile(file):
        files.append(file)






#File selection func

#File encryption

#Encryption key creation and export

#File Decryption