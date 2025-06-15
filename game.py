import random

class BullsCowsGame:
    def __init__(self):
        self.target = self.generate_target()
        self.attempts = 0
        self.max_attempts = 15
        
    def generate_target(self):
        """生成5位不重複數字作為目標"""
        digits = list(range(10))
        # 確保第一位不是0
        first_digit = random.choice(range(1, 10))
        digits.remove(first_digit)
        
        # 隨機選擇剩下4位數字
        remaining = random.sample(digits, 4)
        target = [first_digit] + remaining
        
        return ''.join(map(str, target))
    
    def validate_guess(self, guess):
        """驗證猜測是否有效"""
        if len(guess) != 5:
            return False, "請輸入5位數字"
        
        if not guess.isdigit():
            return False, "請只輸入數字"
        
        if len(set(guess)) != 5:
            return False, "數字不能重複"
        
        if guess[0] == '0':
            return False, "第一位數字不能是0"
        
        return True, ""
    
    def calculate_bulls_cows(self, guess):
        """計算幾A幾B"""
        bulls = 0  # A: 數字和位置都對
        cows = 0   # B: 數字對但位置錯
        
        target_digits = list(self.target)
        guess_digits = list(guess)
        
        # 先計算Bulls (A)
        for i in range(5):
            if guess_digits[i] == target_digits[i]:
                bulls += 1
                target_digits[i] = None  # 標記為已匹配
                guess_digits[i] = None
        
        # 再計算Cows (B)
        for i in range(5):
            if guess_digits[i] is not None:
                if guess_digits[i] in target_digits:
                    cows += 1
                    target_digits[target_digits.index(guess_digits[i])] = None
        
        return bulls, cows
    
    def play(self):
        print("🎯 歡迎來到5位數幾A幾B遊戲！")
        print(f"🎲 我已經想好一個5位數（數字不重複，第一位不為0）")
        print(f"📋 規則：A = 數字和位置都對，B = 數字對但位置錯")
        print(f"⏰ 你有 {self.max_attempts} 次機會猜中！")
        print("-" * 50)
        
        while self.attempts < self.max_attempts:
            try:
                guess = input(f"\n第 {self.attempts + 1} 次猜測，請輸入5位數：")
                
                # 驗證輸入
                is_valid, error_msg = self.validate_guess(guess)
                if not is_valid:
                    print(f"❌ {error_msg}")
                    continue
                
                self.attempts += 1
                bulls, cows = self.calculate_bulls_cows(guess)
                
                if bulls == 5:
                    print(f"🎉 恭喜你猜對了！答案就是 {self.target}")
                    print(f"🏆 你用了 {self.attempts} 次就猜中了！")
                    break
                else:
                    print(f"📊 結果：{bulls}A{cows}B")
                    remaining = self.max_attempts - self.attempts
                    if remaining > 0:
                        print(f"💪 還有 {remaining} 次機會！")
            
            except KeyboardInterrupt:
                print(f"\n\n👋 遊戲結束！答案是 {self.target}")
                break
                
        if self.attempts >= self.max_attempts and bulls != 5:
            print(f"\n😅 很遺憾，你已經用完所有機會了！")
            print(f"🔍 正確答案是：{self.target}")
    
    def play_again(self):
        """重新開始遊戲"""
        self.__init__()
        self.play()

def main():
    while True:
        game = BullsCowsGame()
        game.play()
        
        while True:
            again = input("\n🔄 想再玩一次嗎？(y/n): ").lower().strip()
            if again in ['y', 'yes', '是', '好']:
                break
            elif again in ['n', 'no', '否', '不']:
                print("👋 謝謝遊玩！再見！")
                return
            else:
                print("請輸入 y 或 n")

if __name__ == "__main__":
    main()