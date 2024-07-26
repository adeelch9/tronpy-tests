import os
import unittest
from dotenv import load_dotenv
from tronpy import Tron
from tronpy.keys import PrivateKey
import time

class TestQuickstart(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Load environment variables from .env file
        load_dotenv()

    def test_install_tronpy(self):
        # Test that tronpy can be imported without any issues
        import tronpy
        self.assertIsNotNone(tronpy)

    def test_create_tron_client(self):
        # Test creating a Tron client instance
        client = Tron()
        self.assertIsInstance(client, Tron)

    def test_generate_random_address(self):
        # Test generating a random address
        private_key = PrivateKey.random()
        address = private_key.public_key.to_base58check_address()
        self.assertIsNotNone(address)

    def test_get_latest_block_number(self):
        # Test retrieving the latest block number
        client = Tron()
        latest_block_number = client.get_latest_block_number()
        self.assertGreater(latest_block_number, 0)

    time.sleep(5)
    def test_send_trx_transaction(self):
        # Retrieve private key from environment variable
        private_key = os.getenv("TRON_PRIVATE_KEY")
        self.assertIsNotNone(private_key)

        # Retrieve sender and recipient addresses from environment variables
        sender_address = os.getenv("SENDER_ADDRESS")
        recipient_address = os.getenv("RECIPIENT_ADDRESS")
        self.assertIsNotNone(sender_address)
        self.assertIsNotNone(recipient_address)

        # Test sending a TRX transaction
        client = Tron()
        priv_key = PrivateKey(bytes.fromhex(private_key))
        txn = (
            client.trx.transfer(sender_address, recipient_address, 1_000)
            .memo("Test transaction")
            .build()
            .sign(priv_key)
        )
        self.assertIsNotNone(txn)

if __name__ == '__main__':
    unittest.main()