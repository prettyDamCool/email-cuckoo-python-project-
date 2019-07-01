import hashlib
import glob

def hash_func():
    file = glob.glob("/temp")
for f in file(f,'rb') as getmd5:
    data = getmd5.read()
    gethash = hashlib.md5(data).hexdigest()
    check_file = gethash
#gets chcksum of file 
#now to compare that to file of known hashes if not found bam send file
   with open ('evil_checksums.txt') as badfile:
       if check_file in badfile.read():
           print ("Match found")
           #then email client
           from win32com.client import Dispatch
           session = Dispatch('MAPI.session')
           session.Logon('','',0,1,0,0,'exchange.foo.com\nUserName');
           msg = session.Outbox.Messages.Add('Hello', 'malware match found',print(check_hash))
           msg.Recipients.Add('Corey', 'SMTP:corey@foo.com')
           msg.Send()
         session.Logoff()
