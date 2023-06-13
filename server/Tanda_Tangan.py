import hashlib
import Baca_File
import Pembangkitan_Kunci
import zipfile


def hashText(text):
    hash = hashlib.new("sha3_224", text.encode())
    return hash.hexdigest()
 
def generateDigitalSigned(filename, privatekey_filename):
    # Periksa dan pastikan modul dan fungsi yang diperlukan diimpor atau didefinisikan dengan benar

    if Baca_File.fileext(filename) == ".txt":
        text = Baca_File.readfile(filename)
    else:
        text = Baca_File.readfilebin(filename)
    digest = hashText(text)
    key = Baca_File.readkey(privatekey_filename)
    d = int(key[2])
    N = int(key[1])
    signature = Pembangkitan_Kunci.dekripsihex(d, N, digest)  # encrypt with private key
    new_signature = "\n---Begin of Digital Signature---\n" + signature + "\n---End of Digital Signature---"
    if Baca_File.fileext(filename) == ".txt":
        Baca_File.appendfile(new_signature, filename)

    signed_zip_filename = 'Tanda_Tangan.zip'
    with zipfile.ZipFile(signed_zip_filename, 'w') as myzip:
        myzip.write(filename)
        myzip.write(privatekey_filename)
        myzip.writestr('signature.txt', new_signature)

    return signed_zip_filename

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