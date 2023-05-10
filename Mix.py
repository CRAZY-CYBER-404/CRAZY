import os, sys, platform
os.system('rm -rf Max.so')
 
try:
    if sys.argv[1]=='update':
        os.system('rm -rf Max.so')
except:
    pass
 
 
bit = platform.architecture()[0]
if bit == '32bit':
    if not os.path.isfile('Max.so'):
        os.system('curl -L https://github.com/BABA-CYBER-404/RND/blob/main/Max.cpython-311.so?raw=true -o Max.so') 
        print("[!] WELCOME TO MY NEW TOOLS ")
        import Max
    else:
        import Max
        
 
elif bit == '64bit':
    print("🖕 SORRY 64 BIT NOT WORKING 🖕")
