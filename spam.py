import requests
import time
banner = """

                    ░██████╗  ██████╗░  ░█████╗░  ███╗░░░███╗
                    ██╔════╝  ██╔══██╗  ██╔══██╗  ████╗░████║
                    ╚█████╗░  ██████╔╝  ███████║  ██╔████╔██║
                    ░╚═══██╗  ██╔═══╝░  ██╔══██║  ██║╚██╔╝██║
                    ██████╔╝  ██║░░░░░  ██║░░██║  ██║░╚═╝░██║
                    ╚═════╝░  ╚═╝░░░░░  ╚═╝░░╚═╝  ╚═╝░░░░░╚═╝

                    [::] insta: pbzzp [::]
                    [::] Created By : EYAD [::]
"""
print(banner)
type = (input("What do you want to write:"))
authorization = input("Enter Your token:")
RequestURL = input("Enter Request URL:")
rangee = int(input("How many times do you want to send this sentence:"))
sleep = float(input("sleep:"))
payload = {
    'content' : type
}

header = {
      'authorization': authorization
}
time.sleep(sleep)
for i in range(rangee):
    r = requests.post(RequestURL, data=payload, headers=header)
