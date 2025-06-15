import random
import time
import os
from colorama import Fore, Back, Style, init

# need to install colorma first:
# pip install colorama

# 初始化colorama (跨平台彩色終端)
try:
    init(autoreset=True)
    COLORS_AVAILABLE = True
except ImportError:
    COLORS_AVAILABLE = False

class StylishBullsCowsGame:
    def __init__(self):
        self.target = self.generate_target()
        self.attempts = 0
        self.max_attempts = 15
        self.history = []
        
    def clear_screen(self):
        """清空螢幕"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_colored(self, text, color=None, bg=None, style=None):
        """彩色印出文字"""
        if not COLORS_AVAILABLE:
            print(text)
            return
            
        color_map = {
            'red': Fore.RED,
            'green': Fore.GREEN,
            'yellow': Fore.YELLOW,
            'blue': Fore.BLUE,
            'magenta': Fore.MAGENTA,
            'cyan': Fore.CYAN,
            'white': Fore.WHITE,
        }
        
        bg_map = {
            'red': Back.RED,
            'green': Back.GREEN,
            'yellow': Back.YELLOW,
            'blue': Back.BLUE,
            'magenta': Back.MAGENTA,
            'cyan': Back.CYAN,
        }
        
        style_map = {
            'bright': Style.BRIGHT,
            'dim': Style.DIM,
        }
        
        output = ""
        if style and style in style_map:
            output += style_map[style]
        if bg and bg in bg_map:
            output += bg_map[bg]
        if color and color in color_map:
            output += color_map[color]
        
        print(output + text + Style.RESET_ALL)
    
    def animate_text(self, text, delay=0.05, color=None):
        """逐字動畫顯示"""
        for char in text:
            if COLORS_AVAILABLE and color:
                print(getattr(Fore, color.upper(), '') + char, end='', flush=True)
            else:
                print(char, end='', flush=True)
            time.sleep(delay)
        print(Style.RESET_ALL if COLORS_AVAILABLE else '')
    
    def print_banner(self):
        """顯示遊戲標題"""
        banner = """
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║   🎯 █▀▀ █░█ █▀█ █▀▀ █▀█   █▄░█ █░█ █▀▄▀█ █▄▄ █▀▀ █▀█     ║
║      █▄█ █▄█ █▄█ ▄▄█ █▄█   █░▀█ █▄█ █░▀░█ █▄█ ██▄ █▀▄     ║
║                                                              ║
║                    💀 極限挑戰模式 💀                         ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
"""
        self.print_colored(banner, 'cyan', style='bright')
    
    def generate_target(self):
        """生成5位不重複數字作為目標"""
        digits = list(range(10))
        first_digit = random.choice(range(1, 10))
        digits.remove(first_digit)
        remaining = random.sample(digits, 4)
        target = [first_digit] + remaining
        return ''.join(map(str, target))
    
    def validate_guess(self, guess):
        """驗證猜測是否有效"""
        if len(guess) != 5:
            return False, "💥 長度錯誤！必須是5位數字！"
        
        if not guess.isdigit():
            return False, "⚡ 只能輸入數字！"
        
        if len(set(guess)) != 5:
            return False, "🔥 數字不能重複！"
        
        if guess[0] == '0':
            return False, "❌ 第一位不能是0！"
        
        return True, ""
    
    def calculate_bulls_cows(self, guess):
        """計算幾A幾B"""
        bulls = 0
        cows = 0
        
        target_digits = list(self.target)
        guess_digits = list(guess)
        
        for i in range(5):
            if guess_digits[i] == target_digits[i]:
                bulls += 1
                target_digits[i] = None
                guess_digits[i] = None
        
        for i in range(5):
            if guess_digits[i] is not None:
                if guess_digits[i] in target_digits:
                    cows += 1
                    target_digits[target_digits.index(guess_digits[i])] = None
        
        return bulls, cows
    
    def show_dramatic_result(self, bulls, cows, guess):
        """戲劇化顯示結果"""
        print("\n" + "="*60)
        self.animate_text("⚡ 正在分析你的答案", 0.1, 'yellow')
        
        # 假裝運算過程
        for i in range(3):
            print(".", end='', flush=True)
            time.sleep(0.5)
        
        print("\n")
        
        if bulls == 5:
            self.victory_animation()
        elif bulls >= 3:
            self.print_colored("🔥 非常接近！你快成功了！", 'yellow', style='bright')
        elif bulls >= 1:
            self.print_colored("⚡ 有進展！繼續努力！", 'blue')
        else:
            self.print_colored("💀 還差得遠呢...", 'red')
        
        # 顯示結果
        result_text = f"📊 結果：{bulls}A {cows}B"
        if bulls > 0:
            self.print_colored(result_text, 'green', style='bright')
        else:
            self.print_colored(result_text, 'white')
    
    def victory_animation(self):
        """勝利動畫"""
        victory_frames = [
            "🎉 PERFECT! 🎉",
            "✨ AMAZING! ✨", 
            "🏆 WINNER! 🏆",
            "🎊 SUCCESS! 🎊"
        ]
        
        for frame in victory_frames:
            self.clear_screen()
            self.print_colored("\n" * 5, 'green')
            self.print_colored("   " + "="*50, 'yellow')
            self.print_colored("   " + frame.center(50), 'green', style='bright')
            self.print_colored("   " + "="*50, 'yellow')
            time.sleep(0.5)
    
    def show_progress_bar(self):
        """顯示進度條"""
        remaining = self.max_attempts - self.attempts
        used = self.attempts
        
        progress = "["
        for i in range(self.max_attempts):
            if i < used:
                progress += "█"
            else:
                progress += "░"
        progress += "]"
        
        if remaining <= 3:
            self.print_colored(f"⚠️  {progress} {remaining}/{self.max_attempts} 危險！", 'red', style='bright')
        elif remaining <= 7:
            self.print_colored(f"⚡ {progress} {remaining}/{self.max_attempts} 小心！", 'yellow')
        else:
            self.print_colored(f"💪 {progress} {remaining}/{self.max_attempts} 加油！", 'green')
    
    def show_history(self):
        """顯示歷史記錄"""
        if not self.history:
            return
            
        print("\n" + "─"*50)
        self.print_colored("📋 你的挑戰歷史：", 'cyan', style='bright')
        
        for i, (guess, bulls, cows) in enumerate(self.history[-5:], 1):  # 只顯示最近5次
            result_color = 'green' if bulls >= 2 else 'yellow' if bulls >= 1 else 'red'
            self.print_colored(f"   {i:2}. {guess} → {bulls}A{cows}B", result_color)
    
    def play(self):
        """主遊戲循環"""
        self.clear_screen()
        self.print_banner()
        
        self.animate_text("🎲 神秘數字已生成...", 0.05, 'magenta')
        time.sleep(1)
        
        rules = [
            "📋 遊戲規則：",
            "   💎 A = 數字和位置都正確",
            "   💎 B = 數字正確但位置錯誤", 
            "   ⏰ 你只有15次機會！",
            "   🎯 目標：猜中5位不重複數字！"
        ]
        
        for rule in rules:
            self.print_colored(rule, 'white')
            time.sleep(0.3)
        
        print("\n" + "="*60)
        
        while self.attempts < self.max_attempts:
            try:
                print("\n")
                self.show_progress_bar()
                self.show_history()
                
                print("\n" + "─"*50)
                self.animate_text(f"🎯 第 {self.attempts + 1} 次挑戰", 0.03, 'cyan')
                
                guess = input("輸入你的5位數字 >> ").strip()
                
                is_valid, error_msg = self.validate_guess(guess)
                if not is_valid:
                    self.print_colored(error_msg, 'red', style='bright')
                    continue
                
                self.attempts += 1
                bulls, cows = self.calculate_bulls_cows(guess)
                self.history.append((guess, bulls, cows))
                
                self.show_dramatic_result(bulls, cows, guess)
                
                if bulls == 5:
                    print(f"\n🎊 你用了 {self.attempts} 次就破解了密碼！")
                    self.print_colored(f"🔐 神秘數字：{self.target}", 'green', style='bright')
                    break
                    
            except KeyboardInterrupt:
                print(f"\n\n👋 遊戲中斷！神秘數字是：{self.target}")
                break
        
        if self.attempts >= self.max_attempts and bulls != 5:
            self.print_colored("\n💀 挑戰失敗！你已經用完所有機會了！", 'red', style='bright')
            self.print_colored(f"🔍 神秘數字是：{self.target}", 'yellow', style='bright')

def main():
    """主程式"""
    if not COLORS_AVAILABLE:
        print("💡 提示：安裝 colorama 套件可獲得更好的視覺效果")
        print("   pip install colorama")
        print()
    
    while True:
        game = StylishBullsCowsGame()
        game.play()
        
        while True:
            print("\n" + "="*50)
            again = input("🔄 想要再次挑戰嗎？(y/n): ").lower().strip()
            if again in ['y', 'yes', '是', '好']:
                break
            elif again in ['n', 'no', '否', '不']:
                print("👋 感謝你的挑戰！期待下次再見！")
                return
            else:
                print("請輸入 y 或 n")

if __name__ == "__main__":
    main()