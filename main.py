import os
import sys
import asyncio
from colorama import init, Fore, Style
import inquirer

# Khởi tạo colorama
init(autoreset=True)

# Độ rộng viền cố định
BORDER_WIDTH = 80

# Hàm hiển thị viền đẹp mắt
def print_border(text: str, color=Fore.CYAN, width=BORDER_WIDTH):
    text = text.strip()
    if len(text) > width - 4:
        text = text[:width - 7] + "..."  # Cắt dài và thêm "..."
    padded_text = f" {text} ".center(width - 2)
    print(f"{color}┌{'─' * (width - 2)}┐{Style.RESET_ALL}")
    print(f"{color}│{padded_text}│{Style.RESET_ALL}")
    print(f"{color}└{'─' * (width - 2)}┘{Style.RESET_ALL}")

# Hàm hiển thị banner
def _banner():
    banner = r"""


███╗░░░███╗███████╗░██████╗░░█████╗░███████╗████████╗██╗░░██╗  ████████╗███████╗░██████╗████████╗███╗░░██╗███████╗████████╗
████╗░████║██╔════╝██╔════╝░██╔══██╗██╔════╝╚══██╔══╝██║░░██║  ╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝████╗░██║██╔════╝╚══██╔══╝
██╔████╔██║█████╗░░██║░░██╗░███████║█████╗░░░░░██║░░░███████║  ░░░██║░░░█████╗░░╚█████╗░░░░██║░░░██╔██╗██║█████╗░░░░░██║░░░
██║╚██╔╝██║██╔══╝░░██║░░╚██╗██╔══██║██╔══╝░░░░░██║░░░██╔══██║  ░░░██║░░░██╔══╝░░░╚═══██╗░░░██║░░░██║╚████║██╔══╝░░░░░██║░░░
██║░╚═╝░██║███████╗╚██████╔╝██║░░██║███████╗░░░██║░░░██║░░██║  ░░░██║░░░███████╗██████╔╝░░░██║░░░██║░╚███║███████╗░░░██║░░░
╚═╝░░░░░╚═╝╚══════╝░╚═════╝░╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░╚═╝  ░░░╚═╝░░░╚══════╝╚═════╝░░░░╚═╝░░░╚═╝░░╚══╝╚══════╝░░░╚═╝░░░


    """
    print(f"{Fore.GREEN}{banner:^80}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}{'═' * BORDER_WIDTH}{Style.RESET_ALL}")
    print_border("MEGAETH TESTNET", Fore.GREEN)
    print(f"{Fore.YELLOW}│ {'Liên hệ / Contact'}: {Fore.CYAN}https://t.me/thog099{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}│ {'Replit'}: {Fore.CYAN}Thog{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}│ {'Channel Telegram'}: {Fore.CYAN}https://t.me/thogairdrops{Style.RESET_ALL}")
    print(f"{Fore.GREEN}{'═' * BORDER_WIDTH}{Style.RESET_ALL}")

# Hàm xóa màn hình
def _clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Các hàm giả lập cho các lệnh (cần triển khai thực tế)
async def run_faucetgte(language: str):
    from scripts.faucetgte import run_faucetgte as faucetgte_run
    await faucetgte_run(language)

async def run_mintcap(language: str):
    from scripts.mintcap import run_mintcap as mintcap_run
    await mintcap_run(language)

async def run_bebopswap(language: str):
    from scripts.bebopswap import run_bebopswap as bebopswap_run
    await bebopswap_run(language)


    

async def run_sendtx(language: str):
    from scripts.sendtx import run_sendtx as sendtx_run
    await sendtx_run(language)

async def run_deploytoken(language: str):
    from scripts.deploytoken import run_deploytoken as deploytoken_run
    await deploytoken_run(language)

async def run_sendtoken(language: str):
    from scripts.sendtoken import run_sendtoken as sendtoken_run
    await sendtoken_run(language)

async def run_deploynft(language: str):
    from scripts.deploynft import run_deploynft as deploynft_run
    await deploynft_run(language)

async def cmd_exit(language: str):
    print_border(f"Exiting...", Fore.GREEN)
    sys.exit(0)

# Danh sách lệnh menu
SCRIPT_MAP = {
    "faucetgte": run_faucetgte,
    "mintcap": run_mintcap,
    "bebopswap": run_bebopswap,
    "sendtx": run_sendtx,
    "deploytoken": run_deploytoken,
    "sendtoken": run_sendtoken,
    "deploynft": run_deploynft,
    "exit": cmd_exit
}

def get_available_scripts(language):
    scripts = {
        'vi': [
            {"name": "1. GTE Testnet - Faucet ETH | MegaETH Testnet", "value": "faucetgte"},
            {"name": "2. CAP Testnet - Mint 1000 $cUSD | MegaETH Testnet", "value": "mintcap"},
            {"name": "3. TEKO Finance - Mint 1 $tkETH | MegaETH Testnet", "value": "mint_tkETH"},
            {"name": "4. TEKO Finance - Mint 2000 $tkUSDC | MegaETH Testnet", "value": "mint_tkUSDC"},
            {"name": "5. TEKO Finance - Mint 0.02 $tkWBTC | MegaETH Testnet", "value": "mint_tkWBTC"},
            {"name": "6. TEKO Finance - Mint 1000 $cUSD | MegaETH Testnet", "value": "mint_tkcUSD"},
            {"name": "7. Bebop Swap | MegaETH Testnet", "value": "bebopswap"},
            {"name": "8. GTE Swap Testnet | MegaETH Testnet", "value": ""},
            {"name": "9. GTE Earn Testnet | MegaETH Testnet", "value": ""},
            {"name": "10. TEKO Earn Testnet | MegaETH Testnet", "value": ""},
            {"name": "11. TEKO Borrow Testnet | MegaETH Testnet", "value": ""},



            
            {"name": "12. Gửi TX ngẫu nhiên hoặc File (address.txt) | MegaETH Testnet", "value": "sendtx"},
            {"name": "13. Deploy Token smart-contract | MegaETH Testnet", "value": "deploytoken"},
            {"name": "14. Gửi Token ERC20 ngẫu nhiên hoặc File (addressERC20.txt) | MegaETH Testnet", "value": "sendtoken"},
            {"name": "15. Deploy NFT smart-contract | MegaETH Testnet", "value": "deploynft"},
            {"name": "16. Thoát", "value": "exit"},
        ],
        'en': [
            {"name": "1. GTE Testnet - Faucet ETH | MegaETH Testnet", "value": "faucetgte"},
            {"name": "2. CAP Testnet - Mint 1000 $cUSD | MegaETH Testnet", "value": "mintcap"},
            {"name": "3. TEKO Finance - Mint 1 $tkETH | MegaETH Testnet", "value": "mint_tkETH"},
            {"name": "4. TEKO Finance - Mint 2000 $tkUSDC | MegaETH Testnet", "value": "mint_tkUSDC"},
            {"name": "5. TEKO Finance - Mint 0.02 $tkWBTC | MegaETH Testnet", "value": "mint_tkWBTC"},
            {"name": "6. TEKO Finance - Mint 1000 $cUSD | MegaETH Testnet", "value": "mint_tkcUSD"},
            {"name": "7. Bebop Swap | MegaETH Testnet", "value": "bebopswap"},
            {"name": "8. GTE Swap Testnet | MegaETH Testnet", "value": "swapgte"},
            {"name": "9. GTE Earn Testnet | MegaETH Testnet", "value": ""},
            {"name": "10. TEKO Earn Testnet | MegaETH Testnet", "value": ""},
            {"name": "11. TEKO Borrow Testnet | MegaETH Testnet", "value": ""},


            
            {"name": "12. Send Random TX or File (address.txt) | MegaETH Testnet", "value": "sendtx"},
            {"name": "13. Deploy Token smart-contract | MegaETH Testnet", "value": "deploytoken"},
            {"name": "14. Send ERC20 Token Random or File (addressERC20.txt) | MegaETH Testnet", "value": "sendtoken"},
            {"name": "15. Deploy NFT smart-contract | MegaETH Testnet", "value": "deploynft"},
            {"name": "16. Exit", "value": "exit"},
        ]
    }
    return scripts[language]

def run_script(script_func, language):
    """Chạy script bất kể nó là async hay không."""
    if asyncio.iscoroutinefunction(script_func):
        asyncio.run(script_func(language))
    else:
        script_func(language)

def select_language():
    while True:
        print(f"{Fore.GREEN}{'═' * BORDER_WIDTH}{Style.RESET_ALL}")
        print_border("CHỌN NGÔN NGỮ / SELECT LANGUAGE", Fore.YELLOW)
        questions = [
            inquirer.List('language',
                          message=f"{Fore.CYAN}Vui lòng chọn / Please select:{Style.RESET_ALL}",
                          choices=[("1. Tiếng Việt", 'vi'), ("2. English", 'en')],
                          carousel=True)
        ]
        answer = inquirer.prompt(questions)
        if answer and answer['language'] in ['vi', 'en']:
            return answer['language']
        print(f"{Fore.RED}❌ {'Lựa chọn không hợp lệ / Invalid choice':^76}{Style.RESET_ALL}")

def main():
    _clear()
    _banner()
    language = select_language()

    while True:
        _clear()
        _banner()
        print_border("MENU CHÍNH / MAIN MENU", Fore.YELLOW)

        available_scripts = get_available_scripts(language)
        questions = [
            inquirer.List('script',
                          message=f"{Fore.CYAN}{'Chọn script để chạy / Select script to run'}{Style.RESET_ALL}",
                          choices=[script["name"] for script in available_scripts],
                          carousel=True)
        ]
        answers = inquirer.prompt(questions)
        if not answers:
            continue

        selected_script_name = answers['script']
        selected_script_value = next(script["value"] for script in available_scripts if script["name"] == selected_script_name)

        script_func = SCRIPT_MAP.get(selected_script_value)
        if script_func is None:
            print(f"{Fore.RED}{'═' * BORDER_WIDTH}{Style.RESET_ALL}")
            print_border(f"{'Chưa triển khai / Not implemented'}: {selected_script_name}", Fore.RED)
            input(f"{Fore.YELLOW}⏎ {'Nhấn Enter để tiếp tục... / Press Enter to continue...'}{Style.RESET_ALL:^76}")
            continue

        try:
            print(f"{Fore.CYAN}{'═' * BORDER_WIDTH}{Style.RESET_ALL}")
            print_border(f"ĐANG CHẠY / RUNNING: {selected_script_name}", Fore.CYAN)
            run_script(script_func, language)
            print(f"{Fore.GREEN}{'═' * BORDER_WIDTH}{Style.RESET_ALL}")
            print_border(f"{'Hoàn thành / Completed'} {selected_script_name}", Fore.GREEN)
            input(f"{Fore.YELLOW}⏎ {'Nhấn Enter để tiếp tục... / Press Enter to continue...'}{Style.RESET_ALL:^76}")
        except Exception as e:
            print(f"{Fore.RED}{'═' * BORDER_WIDTH}{Style.RESET_ALL}")
            print_border(f"{'Lỗi / Error'}: {str(e)}", Fore.RED)
            input(f"{Fore.YELLOW}⏎ {'Nhấn Enter để tiếp tục... / Press Enter to continue...'}{Style.RESET_ALL:^76}")

if __name__ == "__main__":
    main()
