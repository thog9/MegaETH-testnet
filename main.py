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

async def run_minttk(language: str):
    from scripts.minttk import run_minttk as minttk_run
    await minttk_run(language)
    
async def run_xlmeme(language: str):
    from scripts.xlmeme import run_xlmeme_script as xlmeme_run
    await xlmeme_run(language)

async def run_conftnft(language: str):
    from scripts.conftnft import run_conftnft as conftnft_run
    await conftnft_run(language)

async def run_wl(language: str):
    from scripts.wl import run_wl as wl_run
    await wl_run(language)

async def run_mintair(language: str):
    from scripts.mintair import run_mintair as mintair_run
    await mintair_run(language)

async def run_swapgte(language: str):
    from scripts.swapgte import run_swapgte as swapgte_run
    await swapgte_run(language)

async def run_stakingteko(language: str):
    from scripts.stakingteko import run_stakingteko as stakingteko_run
    await stakingteko_run(language)
    
async def run_domain(language: str):
    from scripts.domain import run_domain as domain_run
    await domain_run(language)
    
async def run_sendtx(language: str):
    from scripts.sendtx import run_sendtx as sendtx_run
    await sendtx_run(language)

async def run_mintomnihub(language: str):
    from scripts.mintomnihub import run_mintomnihub as mintomnihub_run
    await mintomnihub_run(language)

async def run_brontoswap(language: str):
    from scripts.brontoswap import run_brontoswap as brontoswap_run
    await brontoswap_run(language)

async def run_deploytoken(language: str):
    from scripts.deploytoken import run_deploytoken as deploytoken_run
    await deploytoken_run(language)

async def run_sendtoken(language: str):
    from scripts.sendtoken import run_sendtoken as sendtoken_run
    await sendtoken_run(language)

async def run_nftcollection(language: str):
    from scripts.nftcollection import run_nftcollection as nftcollection_run
    await nftcollection_run(language)

async def run_hopwl(language: str):
    from scripts.hopwl import run_hopwl as hopwl_run
    await hopwl_run(language)

async def run_brontolock(language: str):
    from scripts.brontolock import run_brontolock as brontolock_run
    await brontolock_run(language)

async def run_brontovote(language: str):
    from scripts.brontovote import run_brontovote as brontovote_run
    await brontovote_run(language)

async def run_brontoliquidity(language: str):
    from scripts.brontoliquidity import run_brontoliquidity as brontoliquidity_run
    await brontoliquidity_run(language)

async def run_rariblefun(language: str):
    from scripts.rariblefun import run_rariblefun as rariblefun_run
    await rariblefun_run(language)

async def run_mintnerzo(language: str):
    from scripts.mintnerzo import run_mintnerzo as mintnerzo_run
    await mintnerzo_run(language)

async def run_mintaura(language: str):
    from scripts.mintaura import run_mintaura as mintaura_run
    await mintaura_run(language)

async def run_mintmorkie(language: str):
    from scripts.mintmorkie import run_mintmorkie as mintmorkie_run
    await mintmorkie_run(language)

async def run_superboard(language: str):
    from scripts.superboard import run_superboard as superboard_run
    await superboard_run(language)

async def run_easynode(language: str):
    from scripts.easynode import run_easynode as easynode_run
    await easynode_run(language)

async def run_owlto(language: str):
    from scripts.owlto import run_owlto as owlto_run
    await owlto_run(language)

async def run_rubic(language: str):
    from scripts.rubic import run_rubic as rubic_run
    await rubic_run(language)

async def cmd_exit(language: str):
    print_border(f"Exiting...", Fore.GREEN)
    sys.exit(0)

# Danh sách lệnh menu
SCRIPT_MAP = {
    "faucetgte": run_faucetgte,
    "mintcap": run_mintcap,
    "bebopswap": run_bebopswap,
    "minttk": run_minttk,
    "xlmeme": run_xlmeme,
    "conftnft": run_conftnft,
    "wl": run_wl,
    "domain": run_domain,
    "sendtx": run_sendtx,
    "mintomnihub": run_mintomnihub,
    "swapgte": run_swapgte,
    "mintair": run_mintair,
    "brontoswap": run_brontoswap,
    "stakingteko": run_stakingteko,
    "deploytoken": run_deploytoken,
    "sendtoken": run_sendtoken,
    "nftcollection": run_nftcollection,
    "hopwl": run_hopwl,
    "brontolock": run_brontolock,
    "brontovote": run_brontovote,
    "brontoliquidity": run_brontoliquidity,
    "rariblefun": run_rariblefun,
    "mintnerzo": run_mintnerzo,
    "mintaura": run_mintaura,
    "mintmorkie": run_mintmorkie,
    "superboard": run_superboard,
    "easynode": run_easynode,
    "owlto": run_owlto,
    "rubic": run_rubic,
    "exit": cmd_exit
}

def get_available_scripts(language):
    scripts = {
        'vi': [
            
            {"name": "1. CAP Testnet - Mint 1000 $cUSD | MegaETH Testnet", "value": "mintcap"},
            {"name": "2. TEKO Finance - Mint Tokens | MegaETH Testnet", "value": "minttk"},
            {"name": "3. Mint ConftApp Community Member of MegaETH │ MegaETH Testnet", "value": "conftnft"},
            {"name": "4. Mint Domain │ MegaETH Testnet", "value": "domain"},
            {"name": "5. XL Meme Testnet - Buy/Sell Meme $mRBIT │ MegaETH Testnet", "value": "xlmeme"}, 
            {"name": "6. Bebop Swap | MegaETH Testnet", "value": "bebopswap"},
            {"name": "7. Rubic Exchange Swap | MegaETH Testnet", "value": "rubic"},
            {"name": "8. GTE Swap Testnet | MegaETH Testnet", "value": "swapgte"},
            {"name": "9. TEKO Staking Testnet | MegaETH Testnet", "value": "stakingteko"}, 
            
            #{"name": "10. Bronto Swap Testnet | MegaETH Testnet", "value": "brontoswap"},
            #{"name": "11. Bronto Lock BRONTO -> veNFT [COMING SOON] | MegaETH Testnet", "value": "brontolock"},
            #{"name": "12. Bronto Vote Testnet [COMING SOON] | MegaETH Testnet", "value": "brontovote"},
            #{"name": "13. Bronto Liquidity Testnet [COMING SOON] | MegaETH Testnet", "value": "brontoliquidity"},
            {"name": "10. WL HOPNetwork Testnet | MegaETH Testnet", "value": "hopwl"},

            {"name": "11. Mint NFT RaribleFUN [ FUN Starts Here ] | MegaETH Testnet", "value": "rariblefun"},
            {"name": "12. Mint NFT Nerzo [ MEGA ETH PASS ] | MegaETH Testnet", "value": "mintnerzo"},
            {"name": "13. Mint NFT Aura [ BUNNY NFT ] | MegaETH Testnet", "value": "mintaura"},
            {"name": "14. Mint NFT Morkie [ MORKIE NFT ] | MegaETH Testnet", "value": "mintmorkie"},
            {"name": "15. Mint OmniHub NFT Studio | MegaETH Testnet", "value": "mintomnihub"},

            {"name": "16. SuperBoard Quests | MegaETH Testnet", "value": "superboard"},

            {"name": "17. Deploy Smart Contract Mintair | MegaETH Testnet", "value": "mintair"},
            {"name": "18. Deploy Smart Contract EasyNode | MegaETH Testnet", "value": "easynode"},
            {"name": "19. Deploy Smart Contract Owlto | MegaETH Testnet", "value": "owlto"},
            {"name": "20. Gửi TX ngẫu nhiên hoặc File (address.txt) | MegaETH Testnet", "value": "sendtx"},
            {"name": "21. Deploy Token smart-contract | MegaETH Testnet", "value": "deploytoken"},
            {"name": "22. Gửi Token ERC20 ngẫu nhiên hoặc File (addressERC20.txt) | MegaETH Testnet", "value": "sendtoken"},
            {"name": "23. Deploy NFT smart-contract | MegaETH Testnet", "value": "nftcollection"},
            {"name": "24. Thoát", "value": "exit"},

           # {"name": "25. TEKO Finance - Mint 1 $tkETH | MegaETH Testnet", "value": "mint_tkETH"},
           # {"name": "26. TEKO Finance - Mint 2000 $tkUSDC | MegaETH Testnet", "value": "mint_tkUSDC"},
           # {"name": "27. TEKO Finance - Mint 0.02 $tkWBTC | MegaETH Testnet", "value": "mint_tkWBTC"},
           # {"name": "28. TEKO Finance - Mint 1000 $cUSD | MegaETH Testnet", "value": "mint_tkcUSD"},
           # {"name": "29. GTE Testnet - Faucet ETH [ FAUCET END ] | MegaETH Testnet", "value": "faucetgte"},
           # {"name": "30. REGISTER WAITLIST [ Euphoria | Valhalla | Noise ] | MegaETH Testnet", "value": "wl"},


        ],
        'en': [
            
            {"name": "1. CAP Testnet - Mint 1000 $cUSD | MegaETH Testnet", "value": "mintcap"},
            {"name": "2. TEKO Finance - Mint Tokens | MegaETH Testnet", "value": "minttk"},
            {"name": "3. Mint ConftApp Community Member of MegaETH │ MegaETH Testnet", "value": "conftnft"},
            {"name": "4. Mint Domain │ MegaETH Testnet", "value": "domain"},
            {"name": "5. XL Meme Testnet - Buy/Sell Meme $mRBIT │ MegaETH Testnet", "value": "xlmeme"},
            {"name": "6. Bebop Swap | MegaETH Testnet", "value": "bebopswap"},
            {"name": "7. Rubic Exchange Swap | MegaETH Testnet", "value": "rubic"},
            {"name": "8. GTE Swap Testnet | MegaETH Testnet", "value": "swapgte"},
            {"name": "9. TEKO Staking Testnet | MegaETH Testnet", "value": "stakingteko"},
            
            #{"name": "12. Bronto Swap Testnet | MegaETH Testnet", "value": "brontoswap"},
            #{"name": "13. Bronto Lock BRONTO -> veNFT [COMING SOON] | MegaETH Testnet", "value": "brontolock"},
            #{"name": "14. Bronto Vote Testnet [COMING SOON] | MegaETH Testnet", "value": "brontovote"},
            #{"name": "15. Bronto Liquidity Testnet [COMING SOON] | MegaETH Testnet", "value": "brontoliquidity"},
            {"name": "10. WL HOPNetwork Testnet | MegaETH Testnet", "value": "hopwl"},

            {"name": "11. Mint NFT Rarible FUN [ FUN Starts Here ] | MegaETH Testnet", "value": "rariblefun"},
            {"name": "12. Mint NFT Nerzo [ MEGA ETH PASS ] | MegaETH Testnet", "value": "mintnerzo"},
            {"name": "13. Mint NFT Aura [ BUNNY NFT ] | MegaETH Testnet", "value": "mintaura"},
            {"name": "14. Mint NFT Morkie [ MORKIE NFT ] | MegaETH Testnet", "value": "mintmorkie"},
            {"name": "15. Mint OmniHub NFT Studio | MegaETH Testnet", "value": "mintomnihub"},

            {"name": "16. SuperBoard Quests | MegaETH Testnet", "value": "superboard"},
            
            {"name": "17. Deploy Smart Contract Mintair | MegaETH Testnet", "value": "mintair"},
            {"name": "18. Deploy Smart Contract EasyNode | MegaETH Testnet", "value": "easynode"},
            {"name": "19. Deploy Smart Contract Owlto | MegaETH Testnet", "value": "owlto"},
            {"name": "20. Send Random TX or File (address.txt) | MegaETH Testnet", "value": "sendtx"},
            {"name": "21. Deploy Token smart-contract | MegaETH Testnet", "value": "deploytoken"},
            {"name": "22. Send ERC20 Token Random or File (addressERC20.txt) | MegaETH Testnet", "value": "sendtoken"},
            {"name": "23. Deploy NFT smart-contract | MegaETH Testnet", "value": "nftcollection"},
            {"name": "24. Exit", "value": "exit"},


          #  {"name": "25. TEKO Finance - Mint 1 $tkETH | MegaETH Testnet", "value": "mint_tkETH"},
          #  {"name": "26. TEKO Finance - Mint 2000 $tkUSDC | MegaETH Testnet", "value": "mint_tkUSDC"},
          #  {"name": "27. TEKO Finance - Mint 0.02 $tkWBTC | MegaETH Testnet", "value": "mint_tkWBTC"},
          #  {"name": "28. TEKO Finance - Mint 1000 $cUSD | MegaETH Testnet", "value": "mint_tkcUSD"},
          #  {"name": "29. GTE Testnet - Faucet ETH [ FAUCET END ] | MegaETH Testnet", "value": "faucetgte"},
          #  {"name": "30. REGISTER WAITLIST [ Euphoria | Valhalla | Noise ] | MegaETH Testnet", "value": "wl"},
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
