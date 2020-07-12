from DisWrapper import DisWrapper
import re

message = ["swag", "test", "gachi" "🍆"]

class DisClient:
    def __init__(self):
        pass
        self.client = DisWrapper()
        self.client.auth("scraggjoshua@gmail.com", "ek63KbW41Ked")
        #self.client.request_logging = True

    def display(self):
        messages = self.client.readMessage(10, "558149491333660674")
        messages.reverse()
        for message in messages:
            date = message.timestamp.split("T")[0]
            time = message.timestamp.split("T")[1].split(".")[0]
            if "<@!" in message.content:
                at_index = message.content.find("<@!")
                username = self.client.getUserInfo(message.content[at_index+3:at_index+21]).username
                new_content = re.sub(r'<.+?>', '', message.content)
                new_content = new_content[:at_index] + "@" + username + new_content[at_index:]
                print(f"{time} {message.author.username}: {new_content}")
            else:
                print(f"{time} {message.author.username}: {message.content}")
        print()
        user_message = input("[ * ] > ")

def main():
    test = DisClient()
    test.display()

if __name__ == '__main__':
    main()