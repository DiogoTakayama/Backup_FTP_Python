import os.path, os
from ftplib import FTP, error_perm

host = 'localhost'
port = 21

ftp = FTP()
ftp.connect(host,port)
ftp.login('ftp','3664')
nomeArquivo = "E:\\images"

def placeFiles(ftp, path):
    for nome in os.listdir(path):
        localpath = os.path.join(path, nome)
        if os.path.isfile(localpath):
            print("STOR", nome, localpath)
            ftp.storbinary('STOR ' + nome, open(localpath,'rb'))
        elif os.path.isdir(localpath):
            print("MKD", nome)

            try:
                ftp.mkd(nome)


            except error_perm as e:
                if not e.args[0].startswith('550'): 
                    raise

            print("CWD", nome)
            ftp.cwd(nome)
            placeFiles(ftp, localpath)           
            print("CWD", "..")
            ftp.cwd("..")

placeFiles(ftp, nomeArquivo)

ftp.quit()
