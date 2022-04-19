#upload file using FTP


import ftplib

ftp = ftplib.FTP("ftp.example.com")
ftp.login("user", "password")

ftp.cwd("/public_html/")

filename = "file.txt"

with open(filename, "rb") as f:
    ftp.storbinary("STOR " + filename, f)