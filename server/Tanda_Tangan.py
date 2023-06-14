import hashlib
import Baca_File
import Pembangkitan_Kunci
import zipfile
import pathlib
import os


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

    # Simpan new_signature dalam file teks dengan nama yang sama dengan filename
    signature_filename = filename.split(".")[0] + "_signature.txt"
    Baca_File.writefile(new_signature, signature_filename)

    # Mendapatkan direktori "Downloads"
    downloads_directory = os.path.expanduser("~/Downloads")

    # Membuat path absolut ke file kunci private
    kunci_pri_path = pathlib.Path(os.path.join(downloads_directory, privatekey_filename))

    # Membuat path absolut ke file kunci publik
    kunci_pub_path = kunci_pri_path.with_suffix('.pub')

    # print(kunci_pri_path)
    # print(kunci_pub_path)

    signed_zip_filename = filename.split(".")[0] + ".zip"
    with zipfile.ZipFile(signed_zip_filename, 'w') as myzip:
        myzip.write(filename)
        # myzip.write('%s.pub' % (Baca_File.name((privatekey_filename))))
        myzip.write(kunci_pub_path, os.path.basename(kunci_pub_path))
        # myzip.writestr('signature.txt', new_signature)
        myzip.write(signature_filename)


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