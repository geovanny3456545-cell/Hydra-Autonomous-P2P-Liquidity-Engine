import requests
import json
import time
import hashlib
import os

# Hydra Project - RoboSats API Adapter
# (Public Version for Portfolio)

def base91_encode(data):
    """Encode binary data to base91 string (RoboSats Standard)."""
    base91_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                      'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                      'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                      'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                      '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '#', '$',
                      '%', '&', '(', ')', '*', '+', ',', '.', '/', ':', ';', '<', '=',
                      '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~', '"']
    b = 0
    n = 0
    out = ""
    for byte in data:
        b |= byte << n
        n += 8
        if n > 13:
            v = b & 8191
            if v > 88:
                b >>= 13
                n -= 13
            else:
                v = b & 16383
                b >>= 14
                n -= 14
            out += base91_alphabet[v % 91]
            out += base91_alphabet[v // 91]
    if n > 0:
        out += base91_alphabet[b % 91]
        if n > 7 or b > 90:
            out += base91_alphabet[b // 91]
    return out

class RoboSatsAPI:
    """
    Automated Interface for RoboSats P2P Exchange.
    Supports Ghost Protocol authentication (PGP + Nostr).
    """
    def __init__(self, proxy_url=None):
        self.api_token = os.getenv("ROBOSATS_ROBOT_TOKEN", "your_token_here")
        self.pgp_public = os.getenv("ROBOSATS_PGP_PUB", "")
        self.pgp_private = os.getenv("ROBOSATS_PGP_PRIV", "")
        self.nostr_pubkey = os.getenv("ROBOSATS_NOSTR_PUB", "")
        
        # Derivation: API_TOKEN = Base91(SHA256(Robot_Token))
        sha256_hash = hashlib.sha256(self.api_token.encode('utf-8')).digest()
        self.derived_token = base91_encode(sha256_hash)

        self.proxies = {'http': proxy_url, 'https': proxy_url} if proxy_url else None
        self.base_url = "http://librebazovfmmkyi2jekraxsuso3mh622avuuzqpejixdl5dhuhb4tid.onion/api"

    def _get_auth_header(self):
        """Constructs the Ghost Protocol multi-auth header."""
        pub = self.pgp_public.replace('\n', ' ').strip()
        priv = self.pgp_private.replace('\n', ' ').strip()
        if pub and priv:
            return f"Token {self.derived_token} | {pub} | {priv} | {self.nostr_pubkey}"
        return f"Token {self.derived_token}"

    def create_order(self, order_type, currency_id, amount, premium):
        """
        Creates a new Maker order.
        order_type: 0 for BUY, 1 for SELL
        currency_id: Numerical ID (e.g., 20 for BRL)
        """
        url = f"{self.base_url}/make/"
        payload = {
            "type": order_type,
            "currency": currency_id,
            "amount": amount,
            "premium": premium,
            "payment_methods": [1], # Default to Pix/Instant
            "escrow_duration": 14400,
            "bond_size": 3.0
        }
        
        headers = {"Authorization": self._get_auth_header()}
        response = requests.post(url, json=payload, headers=headers, proxies=self.proxies)
        return response.status_code, response.json()

if __name__ == "__main__":
    # Example usage
    api = RoboSatsAPI(proxy_url="socks5h://localhost:9050")
    print("RoboSats API Adapter initialized.")
