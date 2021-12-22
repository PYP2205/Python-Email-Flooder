"""
E-Mail Flooder

Programmed by: Paramon Yevstigneyev
Programmed in: Python 3.9.6 (64-Bit)

Description:
This Python Program, send an infinite amount of E-Mails to the E-Mail Address
specified by the user. If the user wants to stop the flooder, they can press
'ctrl + c' to end the E-Mail flooder.
"""

# Used for flooding an e-mail
import flood

print("Python E-Mail Flooder:\n")

try:
    # Prompts user for the E-Mail to flood
    reciver_email = input("Enter E-Mail to flood: ")
    print("\nFlooding '" + reciver_email + "' (Ctrl + c to stop)")

    # Runs infinite-while loop
    while True:

        # Calls function to endlessly flood the reciver e-mail
        flood.email_inbox(reciver_email)

# If the user presses Ctrl + C, it will end the program
except KeyboardInterrupt:
    pass