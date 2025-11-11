print(" 1 = x% of y \n","2 = x% is y of z\n","3 = x increases by y%\n" \
"4 = x decreases with y%\n","5 = x changed from y what % effect positive\n",
"6 = x changed from y what % effect negative\n" "7 = x changed to y what % effect positive\n"
"8 = x changed to y what % effect negative")
ans=int(input("What do u wanna train "))
match ans:
    case 1:
        c1=int(input("Choose a precentage "))
        c1s=int(input("Choose a number "))
        ans1=round((c1/100*c1s))
        print(str(ans1)+"%")
    case 2:
        c2=int(input("Choose the lowest number "))
        c2s=int(input("Choose the higher number "))
        ans2=round((c2/c2s*100))
        print(str(ans2)+"%")
    case 3:
        c3=int(input("Choose the original number "))
        c3s=int(input("Choose a percentage "))
        ans3=round((c3*((c3s+100)/100)))
        print(str(ans3))
    case 4:
        c4=int(input("Choose the original number"))
        c4s=int(input("Choose the percentage decrease "))
        ans4=round((c4*((100-c4s)/100)))
        print(str(ans4))
    case 5:
        c5=int(input("Choose the original number "))
        c5s=int(input("Choose the result "))
        ans5=round((c5s/c5*100-100))
        print(str(ans5)+"%")
    case 6:
        c6=int(input("Choose the original number "))
        c6s=int(input("Choose the result "))
        ans6=round(c6s/c6*100-100)
        ans6=ans6*-1
        print(str(ans6)+"%")
    case 7:
        c7=int(input("Choose current value "))
        c7s=int(input("Choose the percentage "))
        ans7=round(c7/((c7s+100)/100))
        print(str(ans7))
    case 8:
        c8=int(input("Choose current value "))
        c8s=int(input("Choose the percentage "))
        ans8=round(c8/((100-c8s)/100))
        print(str(ans8))
    case _:
        print("Nee")
    case _:
        print("Nee")
