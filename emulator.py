import time
import random


class Message:
    def __init__(self, msg_type, byte_1, byte_2):
        self.msg_type = msg_type
        self.byte_1 = byte_1
        self.byte_2 = byte_2


class MockServerInterface:
    @staticmethod
    def request_and_response_1(msg: Message) -> Message:
        pass

    @staticmethod
    def request_and_response_2(msg: Message) -> Message:
        pass


class Correct(MockServerInterface):
    @staticmethod
    def request_and_response_1(msg: Message) -> Message:
        time.sleep(1)
        return Message(msg.msg_type, random.randint(0, 255), msg.byte_1)

    @staticmethod
    def request_and_response_2(msg: Message) -> Message:
        time.sleep(2)
        return Message(msg.msg_type, msg.byte_2, random.randint(0, 255))


class Wrong(MockServerInterface):
    @staticmethod
    def request_and_response_1(msg: Message) -> Message:
        time.sleep(2)
        return Message(msg.msg_type, random.randint(0, 500), random.randint(0, 500))

    @staticmethod
    def request_and_response_2(msg: Message) -> Message:
        time.sleep(1)
        return Message(msg.msg_type, random.randint(0, 500), random.randint(0, 500))
