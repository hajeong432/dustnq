import random
import time

# 1. 설정값 (가챠 비용 하향 조정!)
money = 1000
goal = 10000
bet_cost = 100  # 단돈 10원!

# 2. 아이템별 보상 설정 (딕셔너리 문법)
# { "이모지": 배당배수 }
rewards = {
    "💎": 500,  # 잭팟! 베팅금의 500배 (5,000원)
    "👑": 100,  # 대박! 100배 (1,000원)
    "💰": 20,   # 중박! 20배 (200원)
    "🍎": 5,    # 소박! 5배 (50원)
    "🍬": 2,    # 사탕! 2배 (20원)
    "💀": -10,  # 해골! 오히려 벌금 (돈 뺏김)
    "💩": 0     # 꽝! 0원
}

# 확률을 위해 아이템 리스트 생성 (해골과 똥을 많이 넣어서 난이도 조절 가능)
items = ["💎", "👑", "💰", "💰", "🍎", "🍎", "🍎", "🍬", "🍬", "🍬", "💀", "💀", "💩", "💩", "💩", "💩", "💩"]

print(f"🔥 도파민 공장 가동! 목표는 {goal}원!")
print(f"💸 가챠 한 번에 단돈 {bet_cost}원! 인생 역전 가즈아!")

while 0 < money < goal:
    cmd = input(f"\n[자산: {money}원] Enter(가챠) / 'all'(올인) / 'stop': ").lower()
    
    if cmd == 'stop': break
    
    # 올인 모드 추가 (도파민 극대화!)
    current_bet = money if cmd == 'all' else bet_cost
    money -= current_bet
    
    print("데굴데굴... 결과는? ", end="", flush=True)
    time.sleep(0.3)
    
    # 랜덤 뽑기
    pick = random.choice(items)
    multiplier = rewards[pick]
    win_amount = current_bet * multiplier
    
    # 결과 계산 (마이너스 보상은 0원 아래로 안 떨어지게 계산)
    if multiplier > 0:
        print(f"[{pick}] 당첨! +{win_amount}원! 🎊")
        money += (current_bet + win_amount) # 원금 회수 + 상금
    elif multiplier < 0:
        print(f"[{pick}] 으악! 벌금 {abs(win_amount)}원... 💀")
        money += win_amount # 마이너스 정산
    else:
        print(f"[{pick}] 꽝입니다. (침묵) 💩")

# 최종 결과
if money >= goal:
    print(f"\n🏆 축하합니다! {money}원으로 은퇴합니다! 당신은 도파민의 왕!")
elif money <= 0:
    print("\n💸 파산했습니다. 다시 알바하러 가세요...")
