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
        
        # 💎 新增道具系統
        self.tools = {
            'scope': {'count': 2, 'name': '透視鏡', 'icon': '🔍', 'used_positions': []},
            'eliminator': {'count': 3, 'name': '排除器', 'icon': '❌', 'eliminated_digits': []}
        }
        self.revealed_positions = {}  # 存儲透視鏡揭示的位置
        self.eliminated_digits = set()  # 存儲被排除的數字
        
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
            'ultra_neon_green': '\033[92m\033[1m\033[5m',   # 閃爍綠色
            'neon_purple': '\033[35m\033[1m',    # 新增紫色
            'neon_orange': '\033[33m\033[1m'     # 新增橙色
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
            "║   █    █▄▄       █     █ █   █▄▄▄█   █  █   v2.088 💎 ENHANCED   ║",
            "║   █▄▄▄▄▄▄▄█▄▄▄▄▄▄█▄▄▄▄▄██▄▄▄▄▄▄▄█▄▄▄█  █                        ║",
            "║                                                                   ║",
            "║   💀 NEURAL INTERFACE ACTIVATED WITH QUANTUM TOOLS 💀      ║",
            "║                                                                   ║",
            "╚═══════════════════════════════════════════════════════════════════╝"
        ]
        
        banner_colors = ['neon_cyan', 'neon_cyan', 'neon_pink', 'neon_green', 
                        'neon_yellow', 'neon_blue', 'neon_pink', 'neon_purple',
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
            "[SYSTEM] 💎 Quantum tools initialized...",
            "[SYSTEM] Ready for infiltration..."
        ]
        
        for msg in boot_sequence:
            if "Quantum tools" in msg:
                self.neon_print(f">>> {msg}", 'neon_purple', effect='glitch')
            else:
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
    
    # 💎 新增道具功能
    def use_scope(self):
        """使用透視鏡道具"""
        if self.tools['scope']['count'] <= 0:
            self.neon_print("⚠️ ERROR: No scope charges remaining", 'neon_red')
            return False
        
        # 找出還沒有透視過的位置
        available_positions = [i for i in range(5) if i not in self.tools['scope']['used_positions']]
        
        if not available_positions:
            self.neon_print("⚠️ ERROR: All positions already revealed", 'neon_yellow')
            return False
        
        # 隨機選擇一個位置進行透視
        position = random.choice(available_positions)
        digit = self.target[position]
        
        self.tools['scope']['count'] -= 1
        self.tools['scope']['used_positions'].append(position)
        self.revealed_positions[position] = digit
        
        # 超炫透視動畫
        self.neon_print("🔍 QUANTUM SCOPE ACTIVATING...", 'neon_purple', effect='glitch')
        time.sleep(1)
        
        scope_messages = [
            "[SCOPE] Penetrating quantum barriers...",
            "[SCOPE] Analyzing neural patterns...",
            "[SCOPE] Decrypting position data...",
            "[SCOPE] Target acquired!"
        ]
        
        for msg in scope_messages:
            self.neon_print(msg, 'neon_blue')
            time.sleep(0.6)
        
        print()
        self.neon_print("┌─ QUANTUM SCOPE RESULT ────────────────────────────────┐", 'neon_purple')
        reveal_msg = f"│ POSITION {position + 1}: [{digit}] - NEURAL PATTERN REVEALED    │"
        self.neon_print(reveal_msg, 'neon_green', effect='pulse')
        self.neon_print("└───────────────────────────────────────────────────────┘", 'neon_purple')
        
        return True
    
    def use_eliminator(self):
        """使用排除器道具"""
        if self.tools['eliminator']['count'] <= 0:
            self.neon_print("⚠️ ERROR: No eliminator charges remaining", 'neon_red')
            return False
        
        # 找出不在目標中且還沒被排除的數字
        target_digits = set(self.target)
        all_digits = set('0123456789')
        available_digits = all_digits - target_digits - self.eliminated_digits
        
        if not available_digits:
            self.neon_print("⚠️ ERROR: No digits available for elimination", 'neon_yellow')
            return False
        
        # 隨機選擇一個數字進行排除
        eliminated_digit = random.choice(list(available_digits))
        
        self.tools['eliminator']['count'] -= 1
        self.tools['eliminator']['eliminated_digits'].append(eliminated_digit)
        self.eliminated_digits.add(eliminated_digit)
        
        # 超炫排除動畫
        self.neon_print("❌ QUANTUM ELIMINATOR ACTIVATING...", 'neon_orange', effect='glitch')
        time.sleep(1)
        
        eliminator_messages = [
            "[ELIMINATOR] Scanning probability matrices...",
            "[ELIMINATOR] Cross-referencing data patterns...",
            "[ELIMINATOR] Isolating irrelevant sequences...",
            "[ELIMINATOR] Target eliminated!"
        ]
        
        for msg in eliminator_messages:
            self.neon_print(msg, 'neon_red')
            time.sleep(0.6)
        
        print()
        self.neon_print("┌─ QUANTUM ELIMINATOR RESULT ───────────────────────────┐", 'neon_orange')
        eliminate_msg = f"│ DIGIT [{eliminated_digit}] - ELIMINATED FROM SEARCH SPACE        │"
        self.neon_print(eliminate_msg, 'neon_red', effect='pulse')
        self.neon_print("└───────────────────────────────────────────────────────┘", 'neon_orange')
        
        return True
    
    def show_tools_status(self):
        """顯示道具狀態"""
        print()
        self.neon_print("┌─ QUANTUM TOOLS ───────────────────────────────────────┐", 'neon_purple')
        
        # 透視鏡狀態
        scope_line = f"│ 🔍 SCOPE: {self.tools['scope']['count']} charges"
        if self.revealed_positions:
            positions_str = ", ".join([f"P{pos+1}={digit}" for pos, digit in self.revealed_positions.items()])
            scope_line += f" | Revealed: {positions_str}"
        scope_line += " " * (56 - len(scope_line)) + "│"
        self.neon_print(scope_line, 'neon_cyan')
        
        # 排除器狀態
        elim_line = f"│ ❌ ELIMINATOR: {self.tools['eliminator']['count']} charges"
        if self.eliminated_digits:
            elim_digits = ", ".join(sorted(self.eliminated_digits))
            elim_line += f" | Eliminated: [{elim_digits}]"
        elim_line += " " * (56 - len(elim_line)) + "│"
        self.neon_print(elim_line, 'neon_orange')
        
        # 使用說明
        self.neon_print("│ Commands: 'scope' or 's' | 'eliminator' or 'e'        │", 'dark_gray')
        self.neon_print("└───────────────────────────────────────────────────────┘", 'neon_purple')
    
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
        
        # 顯示輸入的代碼 - 加上透視鏡提示
        code_display = "│ INPUT CODE: ["
        for i, digit in enumerate(guess):
            if i in self.revealed_positions:
                code_display += f"💎{digit}"  # 用鑽石標記透視過的位置
            else:
                code_display += f" {digit}"
        code_display += " ]"
        code_display += " " * (56 - len(code_display)) + "│"
        self.neon_print(code_display, 'cyber_white')
        
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
            ("🏆 ELITE HACKER STATUS 🏆", 'neon_yellow'),
            ("💎 QUANTUM TOOLS MASTERED 💎", 'neon_purple')
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
        
        # 計算道具使用效率獎勵
        tools_used = (2 - self.tools['scope']['count']) + (3 - self.tools['eliminator']['count'])
        efficiency_bonus = ""
        if tools_used == 0:
            efficiency_bonus = "🎯 PURE SKILL MASTERY"
        elif tools_used <= 2:
            efficiency_bonus = "💎 TACTICAL GENIUS"
        else:
            efficiency_bonus = "🔧 TOOL SPECIALIST"
        
        victory_box = [
            "╔══════════════════════════════════════════════════════════════════╗",
            "║                     🎊 MISSION ACCOMPLISHED 🎊                  ║",
            "║                                                                  ║",
            f"║           TARGET CODE: {self.target}                                    ║",
            f"║           BREACH TIME: {self.attempts} attempts                          ║",
            f"║           EFFICIENCY: {efficiency_bonus}                  ║",
            "║           STATUS: LEGENDARY QUANTUM HACKER                      ║",
            "║                                                                  ║",
            "╚══════════════════════════════════════════════════════════════════╝"
        ]
        
        box_colors = ['neon_green', 'neon_pink', 'neon_green', 'neon_cyan', 
                     'neon_cyan', 'neon_purple', 'neon_yellow', 'neon_green', 'neon_green']
        
        for i, line in enumerate(victory_box):
            if i == 1 or i == 5 or i == 6:  # 特殊行
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
        
        # 顯示道具使用情況
        tools_used = (2 - self.tools['scope']['count']) + (3 - self.tools['eliminator']['count'])
        self.neon_print(f"║                    QUANTUM TOOLS USED: {tools_used}/5                ║", 'neon_purple')
        
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
        
        # 遊戲說明 - 新增道具說明
        rules = [
            "┌─ MISSION BRIEFING ────────────────────────────────────┐",
            "│ OBJECTIVE: Crack the 5-digit quantum security code   │",
            "│ DIRECT_HITS: Correct digit in correct position       │", 
            "│ DATA_MATCHES: Correct digit in wrong position        │",
            "│ ATTEMPTS: 15 before trace detection                  │",
            "│ WARNING: No duplicate digits in target code          │",
            "│ 💎 QUANTUM TOOLS AVAILABLE:                          │",
            "│   🔍 SCOPE (2x): Reveals one correct position       │",
            "│   ❌ ELIMINATOR (3x): Excludes one wrong digit      │",
            "└───────────────────────────────────────────────────────┘"
        ]
        
        for rule in rules:
            if "QUANTUM TOOLS" in rule:
                self.neon_print(rule, 'neon_purple')
            elif "SCOPE" in rule or "ELIMINATOR" in rule:
                self.neon_print(rule, 'neon_orange')
            else:
                self.neon_print(rule, 'cyber_white')
        
        # 主遊戲循環
        while self.attempts < self.max_attempts:
            try:
                self.show_system_status()
                self.show_tools_status()
                self.show_hack_history()
                
                print()
                self.neon_print("┌─ NEURAL INTERFACE ────────────────────────────────────┐", 'neon_cyan')
                attempt_text = f"│ ATTEMPT #{self.attempts + 1:2}/15 - Enter code or use tools:           │"
                self.neon_print(attempt_text, 'cyber_white')  
                self.neon_print("└───────────────────────────────────────────────────────┘", 'neon_cyan')
                
                user_input = input(f"{Fore.MAGENTA if COLORS_AVAILABLE else ''}NEURAL>>> {Style.RESET_ALL if COLORS_AVAILABLE else ''}").strip().lower()
                
                # 處理道具命令
                if user_input in ['scope', 's']:
                    if self.use_scope():
                        input(f"{Fore.CYAN if COLORS_AVAILABLE else ''}Press Enter to continue...{Style.RESET_ALL if COLORS_AVAILABLE else ''}")
                    continue
                elif user_input in ['eliminator', 'e']:
                    if self.use_eliminator():
                        input(f"{Fore.CYAN if COLORS_AVAILABLE else ''}Press Enter to continue...{Style.RESET_ALL if COLORS_AVAILABLE else ''}")
                    continue
                
                # 處理數字輸入
                is_valid, error_msg = self.validate_input(user_input)
                if not is_valid:
                    self.neon_print(f"⚡ {error_msg}", 'neon_red')
                    continue
                
                self.attempts += 1
                direct_hits, data_matches = self.calculate_breach_status(user_input)
                self.history.append((user_input, direct_hits, data_matches))
                
                self.display_hack_result(user_input, direct_hits, data_matches)
                
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