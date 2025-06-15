import random
import time
import os
from colorama import Fore, Back, Style, init

# 初始化colorama
try:
    init(autoreset=True)
    COLORS_AVAILABLE = True
except ImportError:
    COLORS_AVAILABLE = False

class CyberpunkHackingGame:
    def __init__(self):
        self.target = self.generate_target()
        self.attempts = 0
        self.max_attempts = 15
        self.history = []
        self.hacker_name = "ANONYMOUS"
        self.target_system = "MAINFRAME_ALPHA"
        
    def clear_screen(self):
        """清除終端"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def neon_print(self, text, color='cyan', bg=None, effect=None, end='\n'):
        """霓虹燈效果打印"""
        if not COLORS_AVAILABLE:
            print(text, end=end)
            return
            
        colors = {
            'neon_cyan': '\033[96m\033[1m',      # 亮青色 + 粗體
            'neon_pink': '\033[95m\033[1m',      # 亮粉色 + 粗體
            'neon_green': '\033[92m\033[1m',     # 亮綠色 + 粗體
            'neon_yellow': '\033[93m\033[1m',    # 亮黃色 + 粗體
            'neon_red': '\033[91m\033[1m',       # 亮紅色 + 粗體
            'neon_blue': '\033[94m\033[1m',      # 亮藍色 + 粗體
            'cyber_white': '\033[97m\033[1m',    # 亮白色 + 粗體
            'dark_gray': '\033[90m',
            'ultra_neon_cyan': '\033[96m\033[1m\033[5m',    # 閃爍青色
            'ultra_neon_pink': '\033[95m\033[1m\033[5m',    # 閃爍粉色
            'ultra_neon_green': '\033[92m\033[1m\033[5m'    # 閃爍綠色
        }
        
        if effect == 'glitch':
            # 強化閃爍效果 - 更頻繁、更明顯
            glitch_colors = ['neon_cyan', 'neon_pink', 'neon_green', 'neon_red']
            for i in range(6):
                random_color = random.choice(glitch_colors)
                print(f"\r{colors.get(random_color, '')}{text}", end='', flush=True)
                time.sleep(0.08)
                print(f"\r{' ' * len(text)}", end='', flush=True)
                time.sleep(0.04)
            print(f"\r{colors.get(color, '')}{text}\033[0m", end=end)
        elif effect == 'pulse':
            # 脈衝效果
            for _ in range(3):
                print(f"\r{colors.get(f'ultra_{color}', colors.get(color, ''))}{text}", end='', flush=True)
                time.sleep(0.3)
                print(f"\r{colors.get(color, '')}{text}", end='', flush=True)
                time.sleep(0.3)
            print(f"\r{colors.get(color, '')}{text}\033[0m", end=end)
        elif effect == 'rainbow':
            # 彩虹效果 - 每個字符不同顏色
            rainbow_colors = ['neon_cyan', 'neon_pink', 'neon_green', 'neon_yellow', 'neon_blue']
            for i, char in enumerate(text):
                color_choice = rainbow_colors[i % len(rainbow_colors)]
                print(f"{colors.get(color_choice, '')}{char}", end='', flush=True)
                time.sleep(0.02)
            print("\033[0m", end=end)
        else:
            print(f"{colors.get(color, '')}{text}\033[0m", end=end)
    
    def matrix_effect(self, duration=3):
        """超強數字雨效果"""
        # 更豐富的字符集
        chars = "0123456789ABCDEFアイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン"
        width = 70
        colors = ['neon_green', 'neon_cyan', 'neon_pink']
        
        # 多層數字雨
        for frame in range(int(duration * 15)):
            lines = []
            for row in range(8):  # 8行數字雨
                line = ""
                for col in range(width):
                    if random.random() < 0.15:
                        line += random.choice(chars)
                    else:
                        line += " "
                lines.append(line)
            
            # 清除並重繪
            print("\033[H\033[J", end='')  # 清屏
            for i, line in enumerate(lines):
                color = colors[i % len(colors)]
                self.neon_print(line, color)
            
            time.sleep(0.08)
        
        print("\033[H\033[J", end='')  # 最後清屏
    
    def cyberpunk_banner(self):
        """超炫賽博朋克標題"""
        # 先顯示閃爍的警告
        self.neon_print("⚡ NEURAL INTERFACE INITIALIZING ⚡", 'neon_pink', effect='glitch')
        time.sleep(1)
        
        # 彩虹標題
        title_lines = [
            "╔═══════════════════════════════════════════════════════════════════╗",
            "║                                                                   ║",
            "║    ▄▄▄▄▄▄▄ ▄   ▄ ▄▄▄▄▄▄  ▄▄▄▄▄▄▄ ▄▄▄▄▄▄                        ║",
            "║   █       █ █▄█ █      ██       █   ▄  █   H A C K I N G         ║",
            "║   █       █▄▄▄▄▄█  ▄    █    ▄▄▄█  █ █ █                        ║",
            "║   █     ▄▄       █ █▄   █   █▄▄▄   █▄▄▄█   S Y S T E M          ║",
            "║   █    █  █▄▄▄▄▄▄█▄▄▄█  █    ▄▄▄█    ▄▄█                        ║",
            "║   █    █▄▄       █     █ █   █▄▄▄█   █  █   v2.077               ║",
            "║   █▄▄▄▄▄▄▄█▄▄▄▄▄▄█▄▄▄▄▄██▄▄▄▄▄▄▄█▄▄▄█  █                        ║",
            "║                                                                   ║",
            "║   💀 NEURAL INTERFACE ACTIVATED 💀                         ║",
            "║                                                                   ║",
            "╚═══════════════════════════════════════════════════════════════════╝"
        ]
        
        banner_colors = ['neon_cyan', 'neon_cyan', 'neon_pink', 'neon_green', 
                        'neon_yellow', 'neon_blue', 'neon_pink', 'neon_green',
                        'neon_cyan', 'neon_cyan', 'neon_pink', 'neon_cyan', 'neon_cyan']
        
        for i, line in enumerate(title_lines):
            if i == 10:  # 特殊行加閃爍效果
                self.neon_print(line, banner_colors[i], effect='pulse')
            else:
                self.neon_print(line, banner_colors[i])
            time.sleep(0.1)
    
    def system_boot(self):
        """系統啟動動畫"""
        boot_sequence = [
            "[SYSTEM] Initializing neural link...",
            "[SYSTEM] Connecting to mainframe...",  
            "[SYSTEM] Bypassing firewall...",
            "[SYSTEM] Quantum encryption detected...",
            "[SYSTEM] Loading crack protocols...",
            "[SYSTEM] Ready for infiltration..."
        ]
        
        for msg in boot_sequence:
            self.neon_print(f">>> {msg}", 'neon_green')
            time.sleep(0.8)
        
        time.sleep(1)
        self.neon_print("=" * 70, 'neon_cyan')
        self.neon_print("🔓 TARGET ACQUIRED: 5-DIGIT SECURITY CODE", 'neon_yellow', effect='glitch')
        self.neon_print("=" * 70, 'neon_cyan')
    
    def generate_target(self):
        """生成目標密碼"""
        digits = list(range(10))
        first_digit = random.choice(range(1, 10))
        digits.remove(first_digit)
        remaining = random.sample(digits, 4)
        return ''.join(map(str, [first_digit] + remaining))
    
    def validate_input(self, guess):
        """驗證輸入"""
        if len(guess) != 5:
            return False, "⚠️ ERROR: Code must be exactly 5 digits"
        
        if not guess.isdigit():
            return False, "⚠️ ERROR: Only numeric input accepted"
        
        if len(set(guess)) != 5:
            return False, "⚠️ ERROR: Duplicate digits detected"
        
        if guess[0] == '0':
            return False, "⚠️ ERROR: Leading zero not permitted"
        
        return True, ""
    
    def calculate_breach_status(self, guess):
        """計算破解狀態"""
        direct_hits = 0  # 直接命中 (A)
        data_matches = 0  # 數據匹配 (B)
        
        target_list = list(self.target)
        guess_list = list(guess)
        
        # 計算直接命中
        for i in range(5):
            if guess_list[i] == target_list[i]:
                direct_hits += 1
                target_list[i] = None
                guess_list[i] = None
        
        # 計算數據匹配
        for i in range(5):
            if guess_list[i] is not None:
                if guess_list[i] in target_list:
                    data_matches += 1
                    target_list[target_list.index(guess_list[i])] = None
        
        return direct_hits, data_matches
    
    def display_hack_result(self, guess, direct_hits, data_matches):
        """顯示破解結果"""
        print()
        self.neon_print("┌─ NEURAL ANALYSIS ─────────────────────────────────────┐", 'neon_cyan')
        
        # 分析動畫
        analysis_steps = [
            "[NEURAL] Scanning quantum signatures...",
            "[NEURAL] Cross-referencing data patterns...", 
            "[NEURAL] Calculating probability matrices...",
            "[NEURAL] Analysis complete."
        ]
        
        for step in analysis_steps:
            self.neon_print(f"│ {step:<54} │", 'dark_gray')
            time.sleep(0.5)
        
        self.neon_print("├───────────────────────────────────────────────────────┤", 'neon_cyan')
        
        # 顯示輸入的代碼
        code_display = f"│ INPUT CODE: [{' '.join(guess)}] "
        self.neon_print(code_display + " " * (56 - len(code_display)) + "│", 'cyber_white')
        
        # 根據結果顯示不同的狀態
        if direct_hits == 5:
            self.neon_print("│ STATUS: 🔓 MAINFRAME BREACHED! FULL ACCESS GRANTED    │", 'neon_green', effect='glitch')
        elif direct_hits >= 3:
            self.neon_print("│ STATUS: ⚡ CRITICAL BREACH - SYSTEM VULNERABLE        │", 'neon_yellow')
        elif direct_hits >= 1:
            self.neon_print("│ STATUS: 🔍 PARTIAL ACCESS - KEEP PROBING             │", 'neon_blue')
        else:
            self.neon_print("│ STATUS: 🛡️ SECURITY HOLDING - RECALIBRATE            │", 'neon_red')
        
        # 顯示破解數據
        result_line = f"│ DIRECT_HITS: {direct_hits} | DATA_MATCHES: {data_matches} | "
        breach_percent = (direct_hits * 20 + data_matches * 5)
        result_line += f"BREACH: {breach_percent}%"
        result_line += " " * (56 - len(result_line)) + "│"
        
        if direct_hits >= 3:
            self.neon_print(result_line, 'neon_green')
        elif direct_hits >= 1:
            self.neon_print(result_line, 'neon_yellow')
        else:
            self.neon_print(result_line, 'neon_red')
        
        self.neon_print("└───────────────────────────────────────────────────────┘", 'neon_cyan')
    
    def show_system_status(self):
        """顯示系統狀態"""
        remaining = self.max_attempts - self.attempts
        used = self.attempts
        
        # 進度條
        progress = "["
        for i in range(self.max_attempts):
            if i < used:
                progress += "█"
            else:
                progress += "░"
        progress += "]"
        
        print()
        self.neon_print("┌─ SYSTEM STATUS ───────────────────────────────────────┐", 'neon_cyan')
        
        # 危險級別
        if remaining <= 3:
            self.neon_print(f"│ 🚨 CRITICAL: {remaining} attempts remaining           │", 'neon_red')
            self.neon_print(f"│ {progress} TRACE DETECTED        │", 'neon_red')
        elif remaining <= 7:
            self.neon_print(f"│ ⚡ CAUTION: {remaining} attempts remaining            │", 'neon_yellow')
            self.neon_print(f"│ {progress} STEALTH MODE         │", 'neon_yellow')
        else:
            self.neon_print(f"│ 💚 SECURE: {remaining} attempts remaining             │", 'neon_green')
            self.neon_print(f"│ {progress} GHOST PROTOCOL       │", 'neon_green')
        
        self.neon_print("└───────────────────────────────────────────────────────┘", 'neon_cyan')
    
    def show_hack_history(self):
        """顯示破解歷史"""
        if not self.history:
            return
            
        print()
        self.neon_print("┌─ BREACH HISTORY ──────────────────────────────────────┐", 'neon_cyan')
        
        recent_attempts = self.history[-5:]  # 顯示最近5次
        for i, (guess, hits, matches) in enumerate(recent_attempts):
            attempt_num = len(self.history) - len(recent_attempts) + i + 1
            
            if hits >= 2:
                color = 'neon_green'
                status = "HIGH"
            elif hits >= 1:
                color = 'neon_yellow' 
                status = "MED "
            else:
                color = 'neon_red'
                status = "LOW "
            
            line = f"│ #{attempt_num:2} [{' '.join(guess)}] → {hits}H {matches}M [{status}] "
            line += " " * (56 - len(line)) + "│"
            self.neon_print(line, color)
        
        self.neon_print("└───────────────────────────────────────────────────────┘", 'neon_cyan')
    
    def victory_sequence(self):
        """超炫勝利序列"""
        self.clear_screen()
        
        # 多重閃爍慶祝
        victory_messages = [
            ("🔓 BREACH SUCCESSFUL 🔓", 'neon_green'),
            ("⚡ MAINFRAME COMPROMISED ⚡", 'neon_cyan'),
            ("💀 SYSTEM PWNED 💀", 'neon_pink'),
            ("🏆 ELITE HACKER STATUS 🏆", 'neon_yellow')
        ]
        
        for msg, color in victory_messages:
            print("\n" * 8)
            self.neon_print("═" * 70, color)
            self.neon_print(msg.center(70), color, effect='rainbow')
            self.neon_print("═" * 70, color)
            time.sleep(1)
            
            # 額外的脈衝效果
            for _ in range(2):
                print("\n" * 8)
                self.neon_print("█" * 70, color, effect='pulse')
                time.sleep(0.3)
            
            self.clear_screen()
        
        # 最終勝利畫面 - 超炫版本
        print("\n" * 3)
        victory_box = [
            "╔══════════════════════════════════════════════════════════════════╗",
            "║                     🎊 MISSION ACCOMPLISHED 🎊                  ║",
            "║                                                                  ║",
            f"║           TARGET CODE: {self.target}                                    ║",
            f"║           BREACH TIME: {self.attempts} attempts                          ║",
            "║           STATUS: LEGENDARY HACKER                               ║",
            "║                                                                  ║",
            "╚══════════════════════════════════════════════════════════════════╝"
        ]
        
        box_colors = ['neon_green', 'neon_pink', 'neon_green', 'neon_cyan', 
                     'neon_cyan', 'neon_yellow', 'neon_green', 'neon_green']
        
        for i, line in enumerate(victory_box):
            if i == 1 or i == 5:  # 特殊行
                self.neon_print(line, box_colors[i], effect='glitch')
            else:
                self.neon_print(line, box_colors[i])
            time.sleep(0.2)
    
    def game_over_sequence(self):
        """遊戲結束序列"""
        print("\n" * 3)
        self.neon_print("╔══════════════════════════════════════════════════════════════════╗", 'neon_red')
        self.neon_print("║                        💀 TRACE DETECTED 💀                     ║", 'neon_red')
        self.neon_print("║                                                                  ║", 'neon_red')
        self.neon_print("║                    CONNECTION TERMINATED                         ║", 'cyber_white')
        self.neon_print(f"║                    SECURITY CODE: {self.target}                       ║", 'neon_yellow')
        self.neon_print("║                                                                  ║", 'neon_red')
        self.neon_print("║                [INITIATING COUNTER-HACK PROTOCOLS]              ║", 'dark_gray')
        self.neon_print("╚══════════════════════════════════════════════════════════════════╝", 'neon_red')
    
    def hack_mainframe(self):
        """主要遊戲循環"""
        self.clear_screen()
        self.cyberpunk_banner()
        
        print()
        self.neon_print("🔌 ESTABLISHING NEURAL CONNECTION...", 'neon_pink')
        time.sleep(1)
        
        # 數字雨效果
        self.matrix_effect(1.5)
        
        self.system_boot()
        
        # 遊戲說明
        rules = [
            "┌─ MISSION BRIEFING ────────────────────────────────────┐",
            "│ OBJECTIVE: Crack the 5-digit quantum security code   │",
            "│ DIRECT_HITS: Correct digit in correct position       │", 
            "│ DATA_MATCHES: Correct digit in wrong position        │",
            "│ ATTEMPTS: 15 before trace detection                  │",
            "│ WARNING: No duplicate digits in target code          │",
            "└───────────────────────────────────────────────────────┘"
        ]
        
        for rule in rules:
            self.neon_print(rule, 'cyber_white')
        
        # 主遊戲循環
        while self.attempts < self.max_attempts:
            try:
                self.show_system_status()
                self.show_hack_history()
                
                print()
                self.neon_print("┌─ NEURAL INTERFACE ────────────────────────────────────┐", 'neon_cyan')
                attempt_text = f"│ ATTEMPT #{self.attempts + 1:2}/15 - Enter 5-digit breach code:      │"
                self.neon_print(attempt_text, 'cyber_white')  
                self.neon_print("└───────────────────────────────────────────────────────┘", 'neon_cyan')
                
                guess = input(f"{Fore.MAGENTA if COLORS_AVAILABLE else ''}NEURAL>>> {Style.RESET_ALL if COLORS_AVAILABLE else ''}").strip()
                
                is_valid, error_msg = self.validate_input(guess)
                if not is_valid:
                    self.neon_print(f"⚡ {error_msg}", 'neon_red')
                    continue
                
                self.attempts += 1
                direct_hits, data_matches = self.calculate_breach_status(guess)
                self.history.append((guess, direct_hits, data_matches))
                
                self.display_hack_result(guess, direct_hits, data_matches)
                
                if direct_hits == 5:
                    self.victory_sequence()
                    break
                    
            except KeyboardInterrupt:
                print(f"\n\n{Fore.RED if COLORS_AVAILABLE else ''}[SYSTEM] Connection terminated by user")
                print(f"[SYSTEM] Security code was: {self.target}{Style.RESET_ALL if COLORS_AVAILABLE else ''}")
                break
        
        if self.attempts >= self.max_attempts and direct_hits != 5:
            self.game_over_sequence()

def main():
    """主程式入口"""
    if not COLORS_AVAILABLE:
        print("💡 Enhanced experience available with: pip install colorama")
        print()
    
    while True:
        game = CyberpunkHackingGame()
        game.hack_mainframe()
        
        print()
        again = input(f"{Fore.CYAN if COLORS_AVAILABLE else ''}🔄 Initialize new hack session? (y/n): {Style.RESET_ALL if COLORS_AVAILABLE else ''}").lower().strip()
        
        if again in ['y', 'yes', '是', '好']:
            continue
        elif again in ['n', 'no', '否', '不']:
            print(f"{Fore.MAGENTA if COLORS_AVAILABLE else ''}👋 Neural link terminated. Stay in the shadows, hacker.{Style.RESET_ALL if COLORS_AVAILABLE else ''}")
            break
        else:
            print("Invalid input. Terminating session...")
            break

if __name__ == "__main__":
    main()