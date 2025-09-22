class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []

    def call(self, other_phone):
        call_info = f"{self.phone_number} called {other_phone.phone_number}"
        print(call_info)
        self.call_history.append(call_info)

    def show_call_history(self):
        print(f"Call history for {self.phone_number}:")
        for call in self.call_history:
            print(call)

    def send_message(self, other_phone, content):
        message = {
            "to": other_phone.phone_number,
            "from": self.phone_number,
            "content": content
        }
        self.messages.append(message)
        print(f"Message sent from {self.phone_number} to {other_phone.phone_number}")

    def show_outgoing_messages(self):
        print(f"Outgoing messages from {self.phone_number}:")
        for msg in self.messages:
            print(msg)

    def show_incoming_messages(self):
        print(f"Incoming messages to {self.phone_number}:")
        for msg in self.messages:
            if msg["to"] == self.phone_number:
                print(msg)

    def show_messages_from(self, number):
        print(f"Messages from {number} to {self.phone_number}:")
        for msg in self.messages:
            if msg["from"] == number and msg["to"] == self.phone_number:
                print(msg)

# ------------------------
phone1 = Phone("06-15-84-56-98")
phone2 = Phone("07-45-89-62-35")

phone1.call(phone2)
phone2.call(phone1)

phone1.show_call_history()
phone2.show_call_history()

phone1.send_message(phone2, "Hello!")
phone2.send_message(phone1, "Hi there!")

phone1.show_outgoing_messages()
phone2.show_outgoing_messages()

phone1.show_incoming_messages()
phone2.show_incoming_messages()

phone1.show_messages_from("06-14-46-38-83")
