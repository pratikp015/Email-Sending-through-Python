
#Assignment Day 6
#Project NO 2
#Send mail Via PYTHON SCRIPT
import emails
html_text ='''<p><span style="color: rgb(243, 121, 52); background-color: rgb(0, 0, 0);">Hey Rowdy,</span></p>
<p>I&apos;m Your Name&nbsp;</p>
<p>I like to study with lets Upgrade</p>
<p>There is 3 courses I&apos;m completed with lets Upgrade</p>
<p><strong>Regards ,</strong></p>
<p><strong>Your Name</strong></p>'''
message = emails.html(html=html_text,
                          subject="Your EMAIL FROM PYTHON SCRIPT",
                          mail_from=('Your Name', 'mailAddress@xyz.com'))
mail_via_python = message.send(to="Reciever Mail Address", smtp={'host': 'smtp.gmail.com', 'timeout': 5, 'port' : 587,
'user':'Your mail Address','password':'Your Mail password','tls' : True})
print(mail_via_python.status_code)
def sendmail(email,name):
    html_text ='''<p><span style="color: rgb(243, 121, 52); background-color: rgb(0, 0, 0);">Hey Rowdy,'''+name+'''</span></p>
                  <p>I&apos;m Your Name&nbsp;</p>
                  <p>I like to study with lets Upgrade</p>
                  <p>There is 3 courses I&apos;m completed with lets Upgrade</p>
                  <p><strong>Regards ,</strong></p>
                  <p><strong>Your Name</strong></p>'''
    subject ="Hey Reciever"+ name+"You have EMAIL FROM Your Name"
    message = emails.html(html=html_text,
                              subject=subject ,
                              mail_from=('Your Name', 'YourMail@xyz.com'))
    mail_via_python = message.send(to=email, smtp={'host': 'smtp.gmail.com', 'timeout': 5, 'port' : 587,
                                                   'user':'Your Mail Address','password':'Your Mail password','tls' : True})
    return mail_via_python.status_code
sendmail("​Reciever mail Address","Reciever Name")
