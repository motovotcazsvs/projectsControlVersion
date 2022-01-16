import ftplib
import os

ftp = ftplib.FTP()
host = '192.168.0.106'
port = 221
ftp.connect(host, port)
print(ftp.getwelcome())
respMessage = ftp.login();
print(respMessage);
dat0 = ftp.retrlines('LIST')
dat = ftp.nlst()
print(dat0)
 
for filename in dat:
    host_file = os.path.join('C:\\newfolde', filename)
    
    try:
        with open(host_file, 'wb') as local_file:
            ftp.retrbinary('RETR ' + filename, local_file.write)
    except ftplib.error_perm:
        pass
 
ftp.quit()

"""
def ftp_upload(ftp_obj, path, ftype='TXT'):
    if ftype == 'TXT':
        with open(path) as ftp_obj:
            ftp.storlines('STOR ' + path, ftp_obj)
    else:
        with open(path, 'rb') as ftp_obj:
            ftp.storbinary('STOR ' + path, ftp_obj, 1024)

if __name__ == '__main__':
    ftp = ftplib.FTP()
    host = '192.168.0.106'
    port = 221
    ftp.connect(host, port)
    ftp.login()    
    path = 'README.txt'
    ftp_upload(ftp, path)
    pdf_path = 'karpets.pdf'
    ftp_upload(ftp, pdf_path, ftype='PDF')
    ftp.quit()


filename = "karpets.pdf"
 
ftp = ftplib.FTP()
host = '192.168.0.106'
port = 221
ftp.connect(host, port)
ftp.login()    
# Открываем файл для передачи в бинарном режиме
f = open(filename, "rb")
# Передаем файл на сервер
send = ftp.storbinary("STOR "+ filename, f)
# Закрываем FTP соединение
ftp.close"""