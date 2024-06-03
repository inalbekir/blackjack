import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    dealed_card = {}
    dealed_card["computer_cards"] = random.sample(cards, 2)
    dealed_card["my_cards"] = random.sample(cards, 2)

    computer = dealed_card["computer_cards"]
    person = dealed_card["my_cards"]

    computer_total = sum(computer)
    person_total = sum(person)

    print("Computer Cards", dealed_card["computer_cards"])
    print("Total = ", computer_total)
    print("\nMy Cards", dealed_card["my_cards"])
    print("Total = ", person_total)

    # Check for initial Blackjacks
    if computer_total == 21 or person_total == 21:
        if computer_total == 21 and person_total == 21:
            return print("It's a Draw!")
        elif computer_total == 21:
            return print("Computer Wins with a Blackjack!")
        elif person_total == 21:
            return print("You Win with a Blackjack!")

    # Player's turn
    while person_total < 21:
        another_card = input("Do you want another card? Type 'yes' or 'no': ").lower()
        if another_card == 'yes':
            new_card = random.choice(cards)
            person.append(new_card)
            person_total = sum(person)
            if 11 in person and person_total > 21:
                person_total -= 10
            print("\nMy Cards", person)
            print("Total = ", person_total)
        else:
            break

    # Check if player busts
    if person_total > 21:
        return print("You Bust! Computer Wins!")

    # Computer's turn
    while computer_total < 17:
        new_card = random.choice(cards)
        computer.append(new_card)
        computer_total = sum(computer)
        if 11 in computer and computer_total > 21:
            computer_total -= 10
        print("Computer draws a card.")
        print("Computer Cards", computer)
        print("Total = ", computer_total)

    # Check if computer busts
    if computer_total > 21:
        return print("Computer Busts! You Win!")

    # Final comparison
    if person_total > computer_total:
        return print("You Win!")
    elif person_total < computer_total:
        return print("Computer Wins!")
    else:
        return print("It's a Draw!")

deal_card()
