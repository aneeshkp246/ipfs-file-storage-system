import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)
        return hashlib.sha256(value.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(0, {"message": "Genesis Block"})

    def create_block(self, index, data):
        timestamp = time.time()
        previous_hash = self.chain[-1].hash if self.chain else "0"
        new_block = Block(index, timestamp, data, previous_hash)
        self.chain.append(new_block)
        print(f"[Blockchain] Block created: Index={new_block.index}, Hash={new_block.hash}, Data={new_block.data}")
        return new_block
