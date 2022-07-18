# python-email-flooder
A simple Python E-Mail flooder, that can endlessly flood an e-mail inbox. You type in an e-mail address, and it will flood the e-mail with randomly generated subjects and messages. This is supported for Linux and Windows 10 and later. Note that this program was programmed in Python v3.9.6, versions of python later than 3.9.x are no longer supported for Windows 7 and earlier (as specified on the offcial Python.org website).

When running this script, all you have to specify is the e-mail address you want to flood. And in order to stop the script, you would have to press Ctrl +C or Ctrl + Z. Which would stop the script, and end the flooder.

# Instructions
Clone this repository:
* "git clone https://github.com/ParamonPlay2205/python-email-flooder/"

Install the required python packages (note smtplib is installed by default in python):
* "pip install -r requirenments.txt"

Before you run the script, you must specify an e-mail address and its password for the script to flood.
If your using a GMail account for this python script, you must go to the account settings. Go to "Security" and enable "Less secure app access". It is recommended to not use your personal account for security reasons.

NOTE: As of May 31, 2022 Google has removed the option to enable "Less secure app access". Generate and use app passwords instead for this email flooder application to work.

# Optional (Windows Only)
If you wish to make a portable executable file out of this python program, then run:
pip install -r optional.txt

This will install pyinstaller and auto-py-to-exe, which are used to make a portable executable. Pyinstaller is a command line python program, while auto-py-to-exe is a user-friendly alternative that uses pyinstaller in a GUI to make a portable executable. Both programs can be used to make the executable in one executable file, or an executable in one directory with multiple files in it.

# Note:
Some e-mail services that have been tested on for flooding (listed below), would mark the e-mails as spam:
* Google: Rarely had e-mails marked as spam
* Yahoo: Had some e-mails marked as spam
* Mail.ru: Had (almost) every e-mail marked as spam
* Yandex: Had (almost) every e-mail marked as spam
