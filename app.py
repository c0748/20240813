import random
valid_choise =["グー","チョキ","パー"]
user_choice= input("グーチョキパーの中から選んでください")

if user_choice not in valid_choise:
    print("グーチョキパーの中から選んでください")
else:
    computer_choice  = random.choice(valid_choise) 
    print(f"コンピューターの選択：{computer_choice}")

    if user_choice == computer_choice:
        result ="あいこです"
    elif (user_choice == "グー" and computer_choice == "チョキ") or (user_choice == "チョキ" and computer_choice == "パー") or (user_choice == "パー" and computer_choice == "グー"):
        result="あなたの勝ち"
    else:
        result="コンピューターの勝ち"

    print(f"結果;{result}")
        