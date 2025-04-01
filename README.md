# MegaETH Testnet Scripts

This repository contains a collection of Python scripts designed to interact with the MegaETH Testnet, a high-performance blockchain test network. These scripts allow users to perform various actions such as claiming faucet ETH, minting tokens and NFTs, swapping tokens, staking, and deploying contracts using the MegaETH Testnet RPC. Each script is built with the `web3.py` library and offers bilingual support (English and Vietnamese) for user interaction.

Faucet: [MegaETH Faucet](https://testnet.megaeth.com/)

## Features Overview

### General Features

- **Multi-Account Support**: Reads private keys from `pvkey.txt` to perform actions across multiple accounts.
- **Colorful CLI**: Uses `colorama` for visually appealing output with colored text and borders.
- **Asynchronous Execution**: Built with `asyncio` for efficient blockchain interactions.
- **Error Handling**: Comprehensive error catching for blockchain transactions and RPC issues.
- **Bilingual Support**: Supports both English and Vietnamese output based on user selection.

### Included Scripts

1. **faucetgte.py**: Claim ETH from the GTE Testnet faucet on MegaETH Testnet.
2. **mintcap.py**: Mint 1000 $cUSD tokens on the CAP Testnet within MegaETH Testnet.
3. **minttk.py**: Mint tokens on TEKO Finance within MegaETH Testnet.
4. **conftnft.py**: Mint the "ConftApp Community Member of MegaETH" NFT.
5. **domain.py**: Mint a domain on MegaETH Testnet.
6. **xlmeme.py**: Buy/Sell $mRBIT meme tokens on XL Meme Testnet within MegaETH Testnet.
7. **bebopswap.py**: Perform swaps on Bebop Swap within MegaETH Testnet.
8. **wl.py**: Register for waitlists (Euphoria, Valhalla, Noise) on MegaETH Testnet.
9. **swapgte.py**: Perform swaps on GTE Swap Testnet within MegaETH Testnet.
10. **stakingteko.py**: Stake tokens on TEKO Staking Testnet within MegaETH Testnet.
11. **mintomnihub.py**: Mint NFTs on OmniHub NFT Studio within MegaETH Testnet.
12. **brontoswap.py**: Perform swaps on Bronto Swap Testnet within MegaETH Testnet.
13. **mintair.py**: Deploy and interact with the Mintair smart contract on MegaETH Testnet.
14. **sendtx.py**: Send random transactions or transactions to addresses from `address.txt` on MegaETH Testnet.
15. **deploytoken.py**: Deploy an ERC20 token smart contract on MegaETH Testnet.
16. **sendtoken.py**: Send ERC20 tokens to random addresses or addresses from `addressERC20.txt` on MegaETH Testnet.
17. **deploynft.py**: Deploy an NFT smart contract on MegaETH Testnet.

## Prerequisites

Before running the scripts, ensure you have the following installed:

- Python 3.8+
- `pip` (Python package manager)
- **Dependencies**: Install via `pip install -r requirements.txt` (ensure `web3.py`, `colorama`, `asyncio`, `eth-account`, and `inquirer` are included).
- **pvkey.txt**: Add private keys (one per line) for wallet automation.
- Access to the MegaETH Testnet RPC (https://carrot.megaeth.com/rpc)
- **address.txt / addressERC20.txt**: Optional files for specifying recipient addresses.

## Installation

1. **Clone this repository:**
- Open cmd or Shell, then run the command:
```sh
git clone https://github.com/thog9/MegaETH-testnet.git
```
```sh
cd MegaETH-testnet
```
2. **Install Dependencies:**
- Open cmd or Shell, then run the command:
```sh
pip install -r requirements.txt
```
3. **Prepare Input Files:**
- Open the `pvkey.txt`: Add your private keys (one per line) in the root directory.
```sh
nano pvkey.txt 
```
- Open the `address.txt`(optional): Add recipient addresses (one per line) for `sendtx.py`, `deploytoken.py`, `sendtoken.py`.
```sh
nano address.txt 
```
```sh
nano addressERC20.txt
```
```sh
nano contractERC20.txt
```
4. **Run:**
- Open cmd or Shell, then run command:
```sh
python main.py
```
- Choose a language (Vietnamese/English).

## Contact

- **Telegram**: [thog099](https://t.me/thog099)
- **Channel**: [CHANNEL](https://t.me/thogairdrops)
- **Group**: [GROUP CHAT](https://t.me/thogchats)
- **X**: [Thog](https://x.com/thog099) 
