import email 
import imaplib
import os
#class for gathering email attachment 
 class Get_email():
    connection = none
    error = none
    
    def __int__(self,Outlook_server,usernmae,password):
      #creates connection to the server
      self.connection = impalib.IMPA4(Outlook_server) #creates request if true then creds needed 
      self.connection = impalib.login(username,password) # creds for client 
      self.connection.select(readonly=False)#helps mark email as read
    def close_connection(self):
        """
        Lights out
        """
    def save_attachment(self,msg, file_location="/tmp"): #files location will be within temp of the user directory 
    attachment_apth = "No attachment has been found"
    for park in msg.walk():
      if part.get_content_maintype() =='multipart':
        continue 
      filename  = part.get_filename()
      att_path = os.path.join(download_folder,filename)
      
      if not os.path.isfile(att_path):
        fp - open(att_path,'wp')
        fp.write(part.get_payload(decode = True))
        return att_path
      
    def fetch_unread_message(self):
      emails = []
      (result,message) = self.connection.search(None,'Unseen')
      if result =="OK":
      for message in message[0].split(''):
      try:
          ret, data = self.connection.fetch(message,'(RFC882)')
          except: 
            print: "No New emails"
            self.close_connection()
            exit()
          msg  = email.message_from_bytes(data[0][1])
          if  isinstance(msg,str) ==False:
            emails.append(msg)
            responce,data = self.connection.store(message,'+FLAGS','\SEEN')
            return emails
            
          
        self.error = "Failed to recieve emails"
    
    def parse_email_address(self,email_address): 
      return email.utils.parsenddr(email_address)
          
    
        
      
      
