from DisWrapper import DisWrapper
from creds import email, password
import re
import time
import os
import sys


class DisClient:
    def __init__(self):
        pass
        self.client = DisWrapper()
        self.client.auth(email, password)

    def displayLoop(self, channel_id, read_only=False):
        messages = []
        while True:
            if messages:
                new_messages = self.client.readMessage(
                    10, channel_id)
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
                    10, channel_id)
                messages = messages + new_messages
                self.display(messages, channel_id)
            
            if read_only:
                time.sleep(10)
            else:
                user_message = input("👾 > ")
                if user_message == "-exit":
                    return
                else:
                    self.client.sendMessage(channel_id, user_message)


    def display(self, messages, channel_id):
        os.system("clear")
        self.printHeader()
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

    def userInfo(self, user_id):
        user = self.client.getUserInfo(user_id)
        print(f"""
  UserID: {user.user_id}
Username: {user.username}:{user.discriminator}
  Avatar: https://cdn.discordapp.com/avatars/{user.user_id}/{user.avatar}.png?size=256
   Flags: {user.public_flags}
        """)

    def commands(self, u_input):
        args = u_input.split()
        command = args.pop(0)
        for i, arg in enumerate(args):
            temp = arg[1:]
            args.pop(i)
            args.insert(i, temp)
        # actually returns item it pops so i just use that
        if command == "help":
            print("""
clear | clears the current screen | clear
   ls | lists all servers         | ls
   jc | joins text channel        | jc -[channel_id]
   js | joins a server            | js -[server_id]
 user | gets a users info         | user -[user_id]
debug | toggles debug logging     | debug
 exit | closes the program        | exit
            """)
        elif command == "clear":
            os.system("clear")
            self.printHeader()
        elif command == "ls":
            pass
        elif command == "js":
            pass
        elif command == "jc":
            self.displayLoop(args[0])
        elif command == "debug":
            if self.client.request_logging:
                self.client.request_logging = False
            else:
                self.client.request_logging = True
        elif command == "user":
            self.userInfo(args[0])

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
        if cmd == "exit":
            sys.exit(0)
        try:
            DiscordCMD.commands(cmd.lower())
        except:
            print("[error] something went wrong")


if __name__ == '__main__':
    main()
