import sys
import imaplib
import getpass
import email
import email.header
import datetime
import sqlite3
import re
import smtplib
import os
import time
import hashlib
import subprocess
import zipfile
import tarfile
import errno
import logging
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
from subprocess import call
import threading
import Queue



log = logging.getlogger('email-automation')
momiter = logging.getlogger('user-moniter')
#cvd file, this will be created and stored via python  files form the lsit will be encrypted and removed after one day 
sqlitefile = '/location'

def file_content(M):
    global MD5 
    global SHA1
    global SHA256
    global SH1512
    global URL
    global sender 
    global number 
    global attachment_location 
    global sampleFile_name
    global sql_light_file
    
    log.info('Looking for emails')
    rv, data = M.search(None,'All')
    if rv != 'OK'
    log.debug('No new emails have been found')
    return
    rv,data = M.fetch(number,'(RFC822)') #http://jkorpela.fi/rfc/822addr.html 
    if rv != 'OK'
         log.debug('Nouthing')
         return 
   log.info("searching for the  most recent email")
   rv,data = M.fetch(number '(RFC822)')
   if rv != 'OK':
       log.debug("|Error finding the email sorry", number)
       return 
   #gets email and makes it to a tring format 
   print("making a string of the email")
   msg = data[0][1]
   raw_email_string = msg.decode('utf-8')
   email_message = email.message_from_string(raw_email_string) #https://docs.python.org/3/library/email.parser.html 
   #header to stirng 
   sender = re.findall('.*?\<(.*?)\>.*?', received)  #https://docs.python.org/2/library/email.parser.html 
   sender = sender[0]
   monitor.info("Email received from: %s", sender)
   i = datetime.now() #current date and time 
   monitoriter.info("Todays date and time",%i)
   #walks over email header for attachments 
    for part in email_message.walk():
        if part.get('Content-Dispoition') is not None:
            if 'attachment;' in part.get('Content-Disposition'):
                log.info('No inline attachments') #downlaod lication for the email attachments
                download_dir ='/somewhere_fam'
                sampleFile_name = part.get_filename()
                attachment_location = os.path.join(download_dir,sampleFile_name)
                monitoriter.info("attachment Name:",%s,sampleFile_name)
                log.debug('Opening file content writng to the virtual machies folder',attachment_location)
                fp = open(attachment_location,'wb')
                fp.write(part.get_payload(Decode=True)) #https://docs.python.org/2/library/email.message.html
                fp.close()
                if attachment_location.endswitch((".7z"))
                log.info("checks if file has an attachment if so extract and paswrd it to stop detenation")
                zip_reff = zipfile.zipfile(attachment_location,'r')
                password = "MenWith_V3n"
                sampleFile_name = zip_reff.namelist() #https://docs.python.org/2/library/zipfile.html
                sampleFile_name = sampleFile_name[0]
                monitor.info("failed to extract")
                extraction_failture()
                return 
            try:
                zip_reff.extract(member=sampleFile_name,path =download_dir,password ="password")
                except RuntimeError:
                        log.debug("Extraction has failed")
                        extraction_failture()
                        return 
                    zip_reff.close()
                    attachment_location = os.path.join(download_dir,sampleFile_name)
                elif attachment_location.endswitch(("tar.gz")) or attachment_location.endswitch(("tar")):
                    log.info("if the file has bene comparessed it can be passed and extracted to the user")
                    tar = tarfile.open(attachment_location,'r:')
                    sampleFile_name = tar.get_filename()
                    monitor.info("Extracted sample",sampleFile_name[0])
                    try:
                        zip_reff.extract(number=sampleFile_name,path=download_dir,pwd="password")
                        except RuntimeError:
                            log.debug("Extracting file has failed")
                            extraction_failture()
                            return
                        zip_reff.close()
                        attachment_location = os.path.join(download_dir,sampleFile_name)
                elif attachment_location.endswitch(("tar.gz")) or attachment_location.endswitch(("tar")):
                    log.info("extracting the file into a tar file")
                    tar = tarfile.open(attachment_location,"r:")
                    sampleFile_name = tar.get_filename()
                    monitor.info("File Extratced name %s",sampleFile_name[0])
                    try:
                        tar.extractall(download_dir)
                        except RuntimeError:
                            log.debug("Extracting file faied")
                            extraction_failture()
                            tar.close()
                            attachment_location = os.path.join(download_dir,sampleFile_name[0])
                            
                            cuckoo_submission() #goes to func where it is handeled correctly 
                            return
                        
                    #eats the main body of the email 
            if part.get_get_content_type() == "text/plain":
                        log info("makes body of the email readable")
                        body = part.get_payload(Decode=True)
                        #file hashes 
                        md5 = re.search(r'\b[0-9a-fA-F]{32}\b', body)
			    # Regular Expression to select the 40 character long hexadecimal string (sha-1 Hash)
			            sha1 = re.search(r'\b[0-9a-fA-F]{40}\b', body)
			            # Regular Expression to select the 64 character long hexadecimal string (sha-256 Hash)
			            sha256 = re.search(r'\b[0-9a-fA-F]{64}\b', body)
			# Regular Expression to select the 128 character long hexadecimal string (sha-512 Hash)
			            sha512 = re.search(r'\b[0-9a-fA-F]{128}\b', body)
			# A regular expression to get any URL help within the body of the email
			            url = re.search('(?<!<)http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', body)
		            	if md5 is not None:
				                log.info("MD5 hash contained within the email")
			                   	md5 = md5.group(0)
			                	monitor.info("MD5 submitted: %s", md5)
				                get_hash_report()
	                			return
	                 	elif sha1 is not None:
				                log.info("MD5 hash contained within the email")
			                   	sha1 = sha1.group(0)
			                	monitor.info("sha1 submitted: %s", sha1)
				                get_hash_report()
	                			return
						
			            elif sha256 is not None:
				                log.info("MD5 hash contained within the email")
			                   	sha256 = sha256.group(0)
			                	monitor.info("MD5 submitted: %s", sha256)
				                get_hash_report()
	                			return
			 	        elif url is not None:
				                log.info("MD5 hash contained within the email")
			                   	md5 = md5.group(0)
			                	monitor.info("MD5 submitted: %s", md5)
				                get_hash_report()
	                			return
			else:
	            	log.info("No hash, URL or attachment contained within the email")
	            	send_no_content()
		            
		# Hello World program in Python
def get_hash_report():
        global md5
        global sha1
        global sha256
        flobal report_locaton 
        global sql_file
        
        log.debug("connecting to the database")
        conn = sqllite2.connect(sqi_file) #connection to database
        c = conn.cursor()
        
        log.debug("coloms form samples table")
        if md5 is not None:
            c.execute("SELECT id, md5 FROM samples WHERE md5 ='%s'" % md5)
        elif sha1 is not None:
            c.execute("SELECT id, sha1 FROM samples WHERE sha1 ='%s'" % sha1)
        elif sha256 is not None:
            c.execute("SELECT id, sha256 FROM samples WHERE sha256 ='%s'" % sha256)
        elif sha512 is not None:
            c.execute("SELECT id, sha512 FROM samples WHERE sha512 ='%s'" % sha512)
        
        #fetches data 
        data = c.fetclone()
        if data == None:
                log.info("No report for the hash value which has been submitted")
                send_no_hash()
        else:
                log.info("Found hash: %s" % data[1])
               sampleID = data[0]
               log.info("Select id and sample_id from tasks table where sample_id is the same as the id retrieved from the previous table")
	           c.execute("SELECT id, sample_id FROM tasks WHERE sample_id = '%s'" %sampleID)
	           #gets the results to report ID 
	           reportID = c.fetchone()
	           reportID = reportID[0]
	           reportllication  = "/location"
	           
def send_no_content():
    global sender
    time.sleep(10)
    recipients = [sender]
    email_list = [elem.strip().split(',') for elm in recipients]
    #makes email 
    msg = MINEMultipart()
    msg['Subject'] = "set header name"
    msg ['from'] = "somwwheew"
    
    msg.preamble = 'You will not see this in a MIME-aware mail reader.\n'
	
	# Define the body of the email
	part = MIMEText("Hi, \n\n Please disregard the submission confirmation email as unfortunately your submission could not be analysed.\n Please ensure that the email you send contains one of the following: MD5 Hash, URL or Attachment\n\nThanks, \nMalware Labs.\n\n\nPlease do not reply to this e-mail.")
	msg.attach(part)
	 
	# Send the email via gmails SMTP server
	server = smtplib.SMTP("smtp.gmail.com:587")
	server.ehlo()
	server.starttls()
	server.login("example@gmail.com", "password")
	server.sendmail(msg['From'], emaillist , msg.as_string())
	print "Email sent."
	return


   
