import os
import unittest
import time
from dotenv import load_dotenv
from tronpy import Tron
from tronpy.providers import HTTPProvider

class TestTronPyClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Load environment variables from .env file
        load_dotenv()

    def test_create_client(self):
        # Test creating a Tron client instance
        client = Tron()
        self.assertIsInstance(client, Tron)

    def test_create_client_with_api_key(self):
        # Test creating a Tron client with a TronGrid API key
        api_key = os.getenv("TRON_API_KEY")
        self.assertIsNotNone(api_key)
        client = Tron(HTTPProvider(api_key=api_key))
        self.assertIsInstance(client, Tron)

    time.sleep(5)
    def test_get_latest_block_number(self):
        # Test retrieving the latest block number
        client = Tron()
        latest_block_number = client.get_latest_block_number()
        self.assertGreater(latest_block_number, 0)

    def test_get_account_info(self):
        # Test retrieving account information
        client = Tron()
        sender_address = "TTzPiwbBedv7E8p4FkyPyeqq4RVoqRL3TW"
        account_info = client.get_account(sender_address)
        self.assertIsNotNone(account_info)
        self.assertEqual(account_info['address'], sender_address)

if __name__ == '__main__':
    unittest.main()