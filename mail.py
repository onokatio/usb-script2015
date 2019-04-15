#! /usr/bin/env python

#import smbus, time
import imaplib
from email.mime.text import MIMEText

SERVER_NAME = "imap.gmail.com"
USERNAME = ""
PASSWORD = ""

mail = imaplib.IMAP4_SSL(SERVER_NAME)
mail.login(USERNAME, PASSWORD)
mail.select("Inbox")
st, mlist = mail.status('Inbox', "(UNSEEN)")

if st == "OK":
	mcount = int(mlist[0].split()[2].strip(').,]'))
	if mcount > 0:
		exec "mplayer  -ao alsa:device=bluetooth /sounds/chime.wav"
		print str(mcount) + " new mail"
	else:
		print "No new mail"
mail.close()
mail.logout()
