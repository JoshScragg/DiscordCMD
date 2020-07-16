from DisWrapper import DisWrapper
from creds import email, password
import re
import time
import os


class DisClient:
    def __init__(self):
        pass
        self.client = DisWrapper()
        self.client.auth(email, password)
        #self.client.request_logging = True

    def displayLoop(self, auto_update=True):
        messages = []
        while True:
            if auto_update:
                if messages:
                    new_messages = self.client.readMessage(
                        10, "558149491333660674")
                    if new_messages[-1].message_id != messages[-1].message_id:
                        for i, message in enumerate(new_messages):
                            if message.message_id == messages[-1].message_id:
                                message_index = i+1
                        messages = messages + new_messages[message_index:]
                        self.display(messages)
                    else:
                        continue
                else:
                    new_messages = self.client.readMessage(
                        10, "558149491333660674")
                    messages = messages + new_messages
                    self.display(messages)

            time.sleep(10)

    def display(self, messages):
        os.system("clear")
        for message in messages:
            date = message.timestamp.split("T")[0]
            time = message.timestamp.split("T")[1].split(".")[0]
            if "<@!" in message.content:
                at_index = message.content.find("<@!")
                username = self.client.getUserInfo(
                    message.content[at_index+3:at_index+21]).username
                new_content = re.sub(r'<.+?>', '', message.content)
                new_content = new_content[:at_index] + \
                    "@" + username + new_content[at_index:]
                print(f"{time} {message.author.username}: {new_content}")
            else:
                print(f"{time} {message.author.username}: {message.content}")
        print()
        #user_message = input("[ * ] > ")
        #self.client.sendMessage("729131457301184605", user_message)

    def printHeader(self):
        print("""
  _____  _                       _  _____ __  __ _____  
 |  __ \(_)                     | |/ ____|  \/  |  __ \ 
 | |  | |_ ___  ___ ___  _ __ __| | |    | \  / | |  | |
 | |  | | / __|/ __/ _ \| '__/ _` | |    | |\/| | |  | |
 | |__| | \__ \ (_| (_) | | | (_| | |____| |  | | |__| |
 |_____/|_|___/\___\___/|_|  \__,_|\_____|_|  |_|_____/ 
                                                        

        """)

    def login(self):
        email = input("[Login] Email > ")
        password = input("[Login] Password > ")
        token = self.client.auth(email, password)

        if token:
            for i in range(5):
                os.system("clear")
                self.printHeader()
                print("[Login] Logging in /")
                time.sleep(0.1)
                os.system("clear")
                self.printHeader()
                print("[Login] Logging in -")
                time.sleep(0.1)
                os.system("clear")
                self.printHeader()
                print("[Login] Logging in \\")
                time.sleep(0.1)

            os.system("clear")
            self.printHeader()
            print("[Login] Logged in!")
            time.sleep(2)

    
    def commands(self, u_input):
        if u_input == "help":
            print("""



            """)



    def welcome(self):
        os.system("clear")
        self.printHeader()
        user_info = self.client.getUserInfo("@me")
        print(f"Welcome {user_info.username}! type help to begin.")




def main():
    DiscordCMD = DisClient()
    DiscordCMD.printHeader()
    DiscordCMD.login()
    DiscordCMD.welcome()
    while True:
        cmd = input("👾 > ")
        DiscordCMD.commands(cmd.lower())




if __name__ == '__main__':
    main()
