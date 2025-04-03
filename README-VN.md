# MegaETH Testnet Scripts

Kho lưu trữ này chứa một bộ sưu tập các tập lệnh Python được thiết kế để tương tác với MegaETH Testnet, một mạng lưới thử nghiệm blockchain hiệu suất cao. Các tập lệnh này cho phép người dùng thực hiện nhiều hành động như nhận ETH từ faucet, đúc token và NFT, hoán đổi token, staking và triển khai hợp đồng bằng MegaETH Testnet RPC. Mỗi tập lệnh được xây dựng bằng thư viện `web3.py` và cung cấp hỗ trợ song ngữ (tiếng Anh và tiếng Việt) để tương tác với người dùng.

Faucet: [MegaETH Faucet](https://faucet.megaeth.app/)

## Tổng quan về tính năng

### Tính năng chung

- **Hỗ trợ nhiều tài khoản**: Đọc khóa riêng từ `pvkey.txt` để thực hiện các hành động trên nhiều tài khoản.
- **CLI đầy màu sắc**: Sử dụng `colorama` để có đầu ra hấp dẫn về mặt hình ảnh với văn bản và đường viền có màu.
- **Thực thi không đồng bộ**: Được xây dựng với `asyncio` để tương tác blockchain hiệu quả.
- **Xử lý lỗi**: Bắt lỗi toàn diện cho các giao dịch blockchain và sự cố RPC.
- **Hỗ trợ song ngữ**: Hỗ trợ cả đầu ra tiếng Việt và tiếng Anh dựa trên lựa chọn của người dùng.

### Các tập lệnh được bao gồm

1. **faucetgte.py**: Nhận ETH từ faucet GTE Testnet trên MegaETH Testnet.
2. **mintcap.py**: Đúc 1000 token $cUSD trên CAP Testnet trong MegaETH Testnet.
3. **minttk.py**: Đúc token trên TEKO Finance trong MegaETH Testnet.
4. **conftnft.py**: Đúc NFT "ConftApp Community Member of MegaETH".
5. **domain.py**: Đúc một tên miền trên MegaETH Testnet.
6. **xlmeme.py**: Mua/Bán token meme $mRBIT trên XL Meme Testnet trong MegaETH Testnet.
7. **bebopswap.py**: Thực hiện hoán đổi trên Bebop Swap trong MegaETH Testnet.
8. **wl.py**: Đăng ký danh sách chờ (Euphoria, Valhalla, Noise) trên MegaETH Testnet.
9. **swapgte.py**: Thực hiện hoán đổi trên GTE Swap Testnet trong MegaETH Testnet.
10. **stakingteko.py**: Stake token trên TEKO Staking Testnet trong MegaETH Testnet.
11. **mintomnihub.py**: Đúc NFT trên OmniHub NFT Studio trong MegaETH Testnet.
12. **brontoswap.py**: Thực hiện hoán đổi trên Bronto Swap Testnet trong MegaETH Testnet.
13. **mintair.py**: Triển khai và tương tác với hợp đồng thông minh Mintair trên MegaETH Testnet.
14. **sendtx.py**: Gửi giao dịch ngẫu nhiên hoặc đến các địa chỉ từ `address.txt` trên MegaETH Testnet.
15. **deploytoken.py**: Triển khai hợp đồng thông minh token ERC20 trên MegaETH Testnet.
16. **sendtoken.py**: Gửi token ERC20 đến các địa chỉ ngẫu nhiên hoặc từ `addressERC20.txt` trên MegaETH Testnet.
17. **deploynft.py**: Triển khai hợp đồng thông minh NFT trên MegaETH Testnet.

## Điều kiện tiên quyết

Trước khi chạy tập lệnh, hãy đảm bảo bạn đã cài đặt các phần sau:

- Python 3.8 trở lên
- `pip` (trình quản lý gói Python)
- **Phụ thuộc**: Cài đặt qua `pip install -r requirements.txt` (đảm bảo `web3.py`, `colorama`, `asyncio`, `eth-account`, và `inquirer` được bao gồm).
- **pvkey.txt**: Thêm khóa riêng (mỗi dòng một khóa) để tự động hóa ví.
- Truy cập vào MegaETH Testnet RPC (https://rpc-testnet.megaeth.app)
- **address.txt / addressERC20.txt**: Các tệp tùy chọn để chỉ định địa chỉ người nhận.

## Cài đặt

1. **Clone this repository:**
- Mở cmd hoặc Shell, sau đó chạy lệnh:
```sh
git clone https://github.com/thog9/MegaETH-testnet.git
```
```sh
cd MegaETH-testnet
```
2. **Install Dependencies:**
- Mở cmd hoặc Shell, sau đó chạy lệnh:
```sh
pip install -r requirements.txt
```
3. **Prepare Input Files:**
- Mở `pvkey.txt`: Thêm khóa riêng của bạn (mỗi dòng một khóa) vào thư mục gốc.
```sh
nano pvkey.txt
```
- Mở `address.txt`(tùy chọn): Thêm địa chỉ người nhận (mỗi dòng một khóa) cho `sendtx.py`, `deploytoken.py`, `sendtoken.py`.
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
- Mở cmd hoặc Shell, sau đó chạy lệnh:
```sh
python main.py
```
- Chọn ngôn ngữ (Tiếng Việt/Tiếng Anh).

## Liên hệ

- **Telegram**: [thog099](https://t.me/thog099)
- **Channel**: [CHANNEL](https://t.me/thogairdrops)
- **Group**: [GROUP CHAT](https://t.me/thogchats)
- **X**: [Thog](https://x.com/thog099) 
