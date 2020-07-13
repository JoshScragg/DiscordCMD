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
                    #print("new messages POG")
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


def main():
    test = DisClient()
    test.displayLoop()
    '''
    messages = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    one = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
    three = ["5", "6", "7", "8", "9", "10", "11", "12", "13", "14"]

    for i, message in enumerate(three):
        if message == messages[-1]:
            split_index = i
    
    test = messages + three[split_index:]
    print(test)
    '''


if __name__ == '__main__':
    main()

