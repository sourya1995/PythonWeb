from ftplib import FTP
ftp = FTP('ftp.debian.org')
print(ftp.login())
print(ftp.cwd('debian'))

out = 'README'
with open(out, 'wb') as f:
    ftp.retrbinary('RETR' + 'README.html', f.write)