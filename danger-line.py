import time
import os
import platform
from colorama import Fore, Style, init

init(autoreset=True)

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def show_lirik(lirik, judul):
    for eng, indo, warna, jeda in lirik:
        clear_screen()
        print(Fore.MAGENTA + judul + Style.RESET_ALL + "\n")
        print(warna + eng + Style.RESET_ALL)
        print(Fore.WHITE + indo + Style.RESET_ALL + "\n")
        time.sleep(jeda)

def main():
    judul = "\n🎵 Avenged Sevenfold - Danger Line 🎵\n"

    lirik_lagu = [
        ("I NEVER MEANT TO LEAVE", "tak pernah ingin kutinggalkan", Fore.CYAN, 1.7),
        ("THIS WORLD ALONE", "dunia ini sendirian", Fore.CYAN, 3.6),
        ("I NEVER MEANT TO HURT", "tak pernah ku bermaksud melukai", Fore.CYAN, 1.9),
        ("THE ONES WHO CARED", "orang-orang yang kusayangi", Fore.CYAN, 3.2),
        ("AND THOUGH THIS TIME I THOUGHT", "dan meskipun kali ini kukira", Fore.CYAN, 2),
        ("WE'D JUST GROW OLD", "kita semakin menua", Fore.CYAN, 3.2),
        ("YOU KNOW..", "kau tau..", Fore.CYAN, 3),
        ("NO ONE SAID IT'S FAIR", "tak ada yang bilang ini adil", Fore.CYAN, 2.7),
        ("TELL MY BABY GIRL THAT IT'S ALRIGHT", "katakan pada putriku bahwa semua akan baik-baik saja", Fore.CYAN, 4.1),
        ("I'VE SUNG MY LAST SONG TODAY", "telah kunyayikan lagu terakhirku hari ini", Fore.CYAN, 4.8),
        ("REMIND THE LORD", "ingatkan Tuhan", Fore.CYAN, 3),
        ("TO LEAVE HIS LIGHT ON", "untuk sinarkan cahayanya", Fore.CYAN, 3.4),
        ("FOR ME", "padaku", Fore.CYAN, 5.6),
        ("I'M FREE..", "aku bebas..", Fore.CYAN, 3),
    ]
    
    show_lirik(lirik_lagu, judul)
    
    print(Fore.MAGENTA + "\n_-_ Follow Instagram : @ridhocrnv _-_\n")

if __name__ == "__main__":
    main()
