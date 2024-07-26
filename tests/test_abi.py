import os
import unittest
from dotenv import load_dotenv
from tronpy.abi import trx_abi

class TestABIEncoding(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Load environment variables from .env file
        load_dotenv()

    def test_encode_single_argument(self):
        # Test encoding a single function argument
        raw = trx_abi.encode_single("(address,uint256)", ["TLfuw4tRywtxCusvTudbjf7PbcXjfe7qrw", 100_000_000])
        self.assertIsNotNone(raw)
        self.assertIsInstance(raw, bytes)  # Check that the output is in bytes

    def test_decode_single_argument(self):
        # Test decoding a single argument
        encoded_data = trx_abi.encode_single("(address,uint256)", ["TLfuw4tRywtxCusvTudbjf7PbcXjfe7qrw", 100_000_000])
        decoded_data = trx_abi.decode_single("(address,uint256)", encoded_data)
        self.assertEqual(decoded_data[0], "TLfuw4tRywtxCusvTudbjf7PbcXjfe7qrw")
        self.assertEqual(decoded_data[1], 100_000_000)


if __name__ == '__main__':
    unittest.main()