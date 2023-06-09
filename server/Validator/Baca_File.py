import pathlib

# fungsi read file 
def readkey(filename):
    with open(filename, "r") as f:
        text = f.read().split(",")
    return(text)    

# fungsi read file 
def readfile(filename):
    with open(filename, "r") as f:
        text = f.read()
    return(text)         

# fungsi read file in bytes
def readfilebin(filename):
    bytes=[]
    with open(filename, "rb") as f:
        while True:
            b = f.read(1)
            if not b:
                break
            bytes.append(int.from_bytes(b, byteorder="big"))
    text =""
    for i in range(len(bytes)):
        text+=chr(bytes[i])
    return(text) 

#funsi write file txt
def writefile(text,filename):
    with open('%s.txt' % (pathlib.Path(filename).stem), 'w') as f:
        f.write(text)
    f.close()

#fungsi return file extention
def fileext(filename):
    return pathlib.Path(filename).suffix

def name(filename):
    return pathlib.Path(filename).stem

def appendfile(text, filename):
    with open('%s.txt' % (pathlib.Path(filename).stem), "a") as f:
        f.write(text)
    f.close()