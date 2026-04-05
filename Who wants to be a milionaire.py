questions=[
    ["Which planet is known as the Red Planet?","Venus","Mars","Jupiter","Saturn",2],
    ["Who is known as the Father of the Indian Constitution?","Mahatma Gandhi","Jawaharlal Nehru","B. R. Ambedkar","Sardar Patel",3],
    ["What is the capital of Japan?","Beijing","Seoul","Tokyo","Bangkok",3],
    ["Which gas do plants absorb from the atmosphere?","Oxygen","Nitrogen","Carbon dioxide","Hydrogen",3],
    ["Who wrote the play Romeo and Juliet?","Charles Dickens" ,"William Wordsworth", "William Shakespeare ","Jane Austen",3],
    ["Which is the largest ocean on Earth?" ,"Indian Ocean ","Atlantic Ocean", "Arctic Ocean ","Pacific Ocean",4],
    ["What is the chemical symbol for Gold?","Go","Gd","Au","Ag",3],
    ["Which country is home to the Great Pyramid of Giza?","Mexico","Egypt","Peru","Greece",2]
]

prizes=[10000,8000,6000,5000,4000,3000,2000,1000]
i=0
for question in questions:
    print(f"{question[0]}")
    print(f"{question[1]}")    
    print(f"{question[2]}")    
    print(f"{question[3]}")    
    print(f"{question[4]}")    
    answer=int(input('Enter your answer , 1 for a , 2 for b, 3 for c, 4 for d\n'))
    if(question[5]==answer):
        print("Correct answer")
    else:
        print("incorrect answer")
        print("Better luck next time")
        break
    print(f"You won {prizes[i]}")
    i+=1






