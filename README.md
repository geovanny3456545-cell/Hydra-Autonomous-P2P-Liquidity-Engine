# Hydra: Autonomous P2P Liquidity Engine 🐲⚡💎

Hydra is an automated arbitrage system designed to provide liquidity to P2P Bitcoin exchanges while hedging positions in real-time on major spot exchanges.

## 🚀 Key Features
- **P2P Automation**: Programmatic order creation and management using the RoboSats API.
- **Privacy by Design**: Fully compatible with the **Ghost Protocol** (Tor, PGP-encrypted identities, and Nostr).
- **Autonomous Hedging**: Real-time arbitrage between decentralized order books and centralized spot markets (Binance).
- **Anti-Fraud Engine**: Automated fiat payment verification via bank notification parsing (IMAP).
- **Telegram Ops**: Complete remote management and alerts via Telegram Bot.

## 🛠️ Tech Stack
- **Language**: Python 3.10+
- **Protocols**: Tor (SOCKS5), PGP (v1.0), Nostr (NIP-04/NIP-44).
- **Integrations**: Binance REST API, RoboSats (API v0.8.x), Banco Inter (IMAP Notification).
- **Infrastructure**: Designed for isolated server environments (e.g., Umbrel/Dell Servers).

## 🛡️ Security
This project implements **Privacy-First** principles:
- **No KYC**: Operates entirely through non-custodial P2P protocols.
- **Isolated Identity**: Every robot has a unique PGP/Nostr keypair.
- **Encrypted Comms**: All API traffic is routed via Tor.

## 📂 Project Structure
- `robosats_adapter.py`: Core logic for interacting with the P2P exchange.
- `engine_arbitrage.py`: The decision engine for buy/sell cycles.
- `fiat_observer.py`: Notification monitor for bank confirmations.
- `notifier.py`: High-reliability alerting system.

---
*Disclaimer: This project is for educational purposes and high-frequency trading research.*
