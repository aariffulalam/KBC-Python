questions=[['which of these sounds would you associated with the heart?','Dhak Dhak'],
["in the ramyana, which demon impersonated rama's voice , screeming , 'Lakshman! help me?",'Marich'],
['with which of these cards would you associate the phrase Aam Aadmi Adhikar ?','Aadhar card'],
['the sasural of which of these international sports persons from india in pakistan?','Saina mirza'],
['which of these words pharases was famously used in many of his dialogues by actor "Pran" ',"Barkhurdaar"],
['which of these is a term for a place where people gather for sayri and gazal ?','Mushaira'],
['in the Mugal era, ehich of these harbours was also known as Babul mecca and Meccaidwar','Surat'],
['after whome is the annual award, given by the Govt of India to an outstanding handloom weaver named ?','Sant kabir'],
['Damascus is the capital of witch country ?','Syria'],
['which is the largest banana producing country in the world?','India'],
['which of these words mean "water" ?','Varun'],
['which gas is most reactiveof all chemical elements','Flurine'],
['which of these spoprts man started cariar as atraivlling ticket examiner with Indian Railway','Mahendra singh dhoni'],['which is the coldest place in the india','Drass']]
answers=[['Tring Tring', 'Tap Tap','Click click','Dhak Dhak'],
['Surpanakkha','Khora','Marich','Dushana'],
['Pan card','Votter card','Aadhar card','Ration card'],
['Siana nehwal','Saina mirza','Anisa sayyed','Anjum chopra'],
['Khamosh','Barkhurdaar','Jaani','Babu mosai'],
['Rukhsar','Mushaira','Shikara','Mahabara'],
['Bharuch','Surat','Porbandar','Khambal'],
['Acharya vinoba bhave','Sant kabir','Mahatma Gandhi','Gul ahmed'],
['Tunisia','Jordan','Syria','Lebanon'],
['Brazil','India','Maxico','China'],
['Rahul','Suraj','Varun','Rajiv'],
['Oxigen','Clorine','Flurine','Hydrogen'],
['Bhuvneshwar kumar','Shekhar dhavan','Ravindra jadeja','Mahendra singh dhoni'],
['Yusmarg','Kulgam','Drass','Leh']]
m=[]
stop=0
l=0
price=2500
z=1
for i in range(0,len(questions)):
    if z<=8:
        price*=2
    elif  z<12:
        price=625000
        price*=2
    else:
        price+=40000000
    if stop>=1:
        print('Sorry you loose this game ')
        break
    else:
        print(questions[i][0])
        a=0
        for j in range (0,len(answers[i])):
            a+=1
            print(a,answers[i][j])
            if a==4:
                if l==0:
                    chance=input('Do you want 50-50     =>  yes  or  no ')
                    if chance =='yes':
                        q=0
                        p=0
                        s=[]
                        while p<len(answers[i])-2:
                            if answers[i][p] !=questions[i][1]:
                                s.append(answers[i][p])
                            p+=1
                        for r in s:
                            continue
                        for t in range(0,2):
                            if s[t] in answers[i]:
                                answers[i].remove(s[t])
                        for u in range(0,len(answers[i])):
                            print(u+1,answers[i][u])
                        anss=int(input('enter your number'))
                        if answers[i][anss-1]==questions[i][1]:
                            print(answers[i][anss-1],'\n you won ',price,'rupees')  
                            z+=1
                            l+=1
                        else:
                            stop+=1
                    elif chance=='no':
                        ans=int(input('select your number'))
                        for k in range (0,len(answers[i])):
                            if answers[i][ans-1]==questions [i][1]:
                                if answers[i][ans-1] not in m:
                                    m.append(answers[i][ans-1])
                                    print(answers[i][ans-1],'\nyou won',price,'rupees')
                                z+=1
                            else:
                                stop+=1
                    else:
                        print('Wrong input')
                        stop+=1                                
                elif l==0 or l!=0:
                    ans=int(input('select your number'))
                    for k in range (0,len(answers[i])):
                        if answers[i][ans-1]==questions [i][1]:
                            if answers[i][ans-1] not in m:
                                m.append(answers[i][ans-1])
                                print(answers[i][ans-1],'\nyou won',price,'rupees')
                            z+=1
                        else:
                            stop+=1
