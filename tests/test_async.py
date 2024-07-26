import asyncio
import unittest
from tronpy import AsyncTron
from tronpy.keys import PrivateKey
import os

class TestAsyncTransactions(unittest.TestCase):
    async def async_transfer(self):
        # Retrieve private key from environment variables
        private_key = os.getenv("TRON_PRIVATE_KEY")
        self.assertIsNotNone(private_key)
        
        async with AsyncTron(network='nile') as client:
            txb = (
                client.trx.transfer(os.getenv("SENDER_ADDRESS"), os.getenv("RECIPIENT_ADDRESS"), 1_000)
                .memo("test memo")
                .fee_limit(100_000_000)
            )
            txn = await txb.build()
            txn_ret = await txn.sign(PrivateKey(bytes.fromhex(private_key))).broadcast()
            confirmation = await txn_ret.wait()
            self.assertIsNotNone(confirmation)

    def test_async_transfer(self):
        asyncio.run(self.async_transfer())

if __name__ == '__main__':
    unittest.main()