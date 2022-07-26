from ftplib import FTP
ftp = FTP('ftp.cse.buffalo.edu')
print(ftp.login())
ftp.retrlines('LIST')
ftp.cwd('mirror')
ftp.retrlines('LIST')