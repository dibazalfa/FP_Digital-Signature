import hashlib
import Baca_File
import Pembangkitan_Kunci
import zipfile


def hashText(text):
    hash = hashlib.new("sha3_224", text.encode())
    return hash.hexdigest()

def generateDigitalSigned(filename, privatekey):
    if Baca_File.fileext(filename) == ".txt":
        text = Baca_File.readfile(filename) 
    else:
        text = Baca_File.readfilebin(filename)
    digest = hashText(text)
    key = Baca_File.readkey(privatekey)
    d = int(key[2])
    N = int(key[1])
    signature = Pembangkitan_Kunci.dekripsihex(d, N, digest) #enkripsi dengan private key
    new_signature = "\n---Begin of Digital Signature---\n"+signature+"\n---End of Digital Signature---" 
    if Baca_File.fileext(filename) == ".txt":
        Baca_File.appendfile(new_signature,filename)  
    else:
        Baca_File.writefile(new_signature,filename)
        myzip = zipfile.ZipFile('Tanda_Tangan.zip', 'w')
        myzip.write('%s.txt' % (Baca_File.name(filename)))
        myzip.write('%s.pub' % (Baca_File.name(privatekey)))
        myzip.write('%s.pdf' % (Baca_File.name(filename)))


def validateDigitalSigned(filename, publickey, filesig=""):
    key = Baca_File.readkey(publickey)
    e = int(key[2])
    N = int(key[1])
    text = Baca_File.readfilebin(filename)
    digest = hashText(text)
    isisig = Baca_File.readfile(filesig).split("---Begin of Digital Signature---\n")
    plaintext = isisig[1].split("\n---End of Digital Signature---")
    signature = plaintext[0]
    signatureDigest = Pembangkitan_Kunci.enkripsihex(e,N,signature)
    digests = ""
    for c in digest: 
        digests += str(ord(c))
    hexdigest = hex(int(digests))
    if hexdigest == signatureDigest:
        return("Valid")
    else:
        return("Tidak Valid")


# generateDigitalSigned("dea.docx", "del.pri")
# validateDigitalSigned("dea.docx","del.pub","dea.txt")

# generateDigitalSigned("aed.txt", "del.pri")
# validateDigitalSigned("aed.txt","del.pub")