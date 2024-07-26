import os
import unittest
from dotenv import load_dotenv
from tronpy.keys import PrivateKey, PublicKey, Signature

class TestKeys(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Load environment variables from .env file
        load_dotenv()

    def test_generate_private_key(self):
        # Test generating a random private key
        private_key = PrivateKey.random()
        self.assertIsNotNone(private_key)
        self.assertIsInstance(private_key, PrivateKey)

    def test_private_key_to_address(self):
        # Test converting a private key to a Base58Check address
        private_key = PrivateKey.random()
        address = private_key.public_key.to_base58check_address()
        self.assertIsNotNone(address)

    def test_private_key_from_hex(self):
        # Test creating a PrivateKey from a hex string
        private_key_hex = os.getenv("TRON_PRIVATE_KEY")
        self.assertIsNotNone(private_key_hex)
        priv_key = PrivateKey(bytes.fromhex(private_key_hex))
        self.assertIsInstance(priv_key, PrivateKey)
        self.assertEqual(len(priv_key.hex()), 64)  # Call the hex method and get its result

    def test_public_key_from_private_key(self):
        # Test generating a public key from a private key
        private_key = PrivateKey.random()
        public_key = private_key.public_key
        self.assertIsNotNone(public_key)
        self.assertIsInstance(public_key, PublicKey)

    def test_private_key_from_invalid_hex(self):
        # Test creating a PrivateKey from an invalid hex string
        invalid_hex = "invalid_hex"
        with self.assertRaises(ValueError):
            PrivateKey(bytes.fromhex(invalid_hex))

    def test_private_key_generation(self):
        # Test generating multiple private keys and checking their uniqueness
        private_keys = set()
        for _ in range(10):
            private_key = PrivateKey.random()
            self.assertNotIn(private_key.hex, private_keys)
            private_keys.add(private_key.hex)

if __name__ == '__main__':
    unittest.main()