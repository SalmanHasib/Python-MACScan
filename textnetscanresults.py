#!/usr/bin/python

import os
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

## This is only if you have your email password in a separate text file
## Otherwise you can hardcode it into the variable 'passw'
passpath = os.environ["HOME"] + "/path/to/email/password/text/file/"
fp = open(passpath, 'r')
passw = fp.read()
fp.close()

unknown = []
unknownpath = os.environ["HOME"] + "/path/to/unknown/list/directory/"
with open(unknownpath) as fu:
    for line in fu:
        unknown.append(line.strip())
fu.closed
unknownlen = len(unknown)
unknownstr = "\nUnknowns: %s\n" % str(unknownlen)
for addr in unknown:
    unknownstr = unknownstr + "%s\n" % addr

msg = MIMEText(unknownstr, 'plain')

me = 'your_email@your_domain.com'
you = 'your_phone_number@your_carriers_domain.something'
##    The recipients email address will be their phone number
##    and a specific domain, depending on the carrier:
##    AT&T: 				number@txt.att.net
##    T-Mobile: 			number@tmomail.net
##    Verizon: 				number@vtext.com
##    Sprint: 				number@messaging.sprintpcs.com or number@pm.sprint.com
##    Virgin Mobile: 		number@vmobl.com
##    Tracfone: 			number@mmst5.tracfone.com
##    Metro PCS: 			number@mymetropcs.com
##    Boost Mobile: 		number@myboostmobile.com
##    Cricket: 				number@sms.mycricket.com
##    Ptel: 				number@ptel.com
##    Republic Wireless: 	number@text.republicwireless.com
##    Suncom: 				number@tms.suncom.com
##    Ting: 				number@message.ting.com
##    U.S. Cellular: 		number@email.uscc.net
##    Consumer Cellular: 	number@cingularme.com
##    C-Spire: 				number@cspire1.com
##    Page Plus: 			number@vtext.com

time = datetime.now().date()

msg['Subject'] = str(time)
msg['From'] = me
msg['To'] = you

s = smtplib.SMTP('smtp.gmail.com:587')
s.starttls()
s.login(me, passw)
s.sendmail(me, you, msg.as_string())
s.quit()