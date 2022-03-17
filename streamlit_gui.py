import random
import streamlit as st
st.title("Know Your Name Meaning")
choice = st.selectbox("Select your choice",["","Play","Exit"])
if choice=="Play":
    name = st.text_input("Enter your name:").upper()
    str_lth = len(name)
    for i in range(0,str_lth):
        char1 = name[i]
        if char1=="A":
            alist = ["Abderian","Ablaze","A1","Awesome","Amazing"]
            st.write(name[i],":",random.choice(alist))
        elif char1=="B":
            blist = ["Balmy","BadBoy","Blooming","Blessed","Baronical"]
            st.write(name[i],":",random.choice(blist))
        elif char1=="C":
            clist = ["Cheerful","Choosy","Caring","Courage","Calm"]
            st.write(name[i],":",random.choice(clist))
        elif char1=="D":
            dlist = ["Dynamic","Daring","Devotional","Delightful","Determined"]
            st.write(name[i],":",random.choice(dlist))
        elif char1=="E":
            elist = ["Eager","Elegant","Emotive","Enamored","Endeary"]
            st.write(name[i],":",random.choice(elist))
        elif char1=="F":
            flist = ["Fabulous","Fantastic","Facile","Festive","Fortunefull"]
            st.write(name[i],":",random.choice(flist))
        elif char1=="G":
            glist = ["Great","Graceful","Gracios","Glourious","Guilty"]
            st.write(name[i],":",random.choice(glist))
        elif char1=="H":
            hlist = ["Heroic","Hardcore","Hazy","Heated","Helpful"]
            st.write(name[i],":",random.choice(hlist))
        elif char1=="I":
            ilist = ["Impressive","Imaginative","Impulsive","Innovative","Imitative"]
            st.write(name[i],":",random.choice(ilist))
        elif char1=="J":
            jlist = ["Jealous","Joyful","Jocular","Jesting","Jittery"]
            st.write(name[i],":",random.choice(jlist))
        elif char1=="K":
            klist = ["Kind","Killer","Keen","Kindhearted","Knowledgable"]
            st.write(name[i],":",random.choice(klist))
        elif char1=="L":
            llist = ["Lame","Lazy","Logical","Lonely","Lucky"]
            st.write(name[i],":",random.choice(llist))
        elif char1=="M":
            mlist = ["Mad","Maniac","Messy","Mature","Marvelous"]
            st.write(name[i],":",random.choice(mlist))
        elif char1=="N":
            nlist = ["Nice","Neat","Numb","Natural","Nasty"]
            st.write(name[i],":",random.choice(nlist))
        elif char1=="O":
            olist = ["Obssesive","Offensive","Outstanding","Organized","Otious"]
            st.write(name[i],":",random.choice(olist))
        elif char1=="P":
            plist = ["Pacifist","Passionate","Perfect","Polite","Pretty"]
            st.write(name[i],":",random.choice(plist))
        elif char1=="Q":
            qlist = ["Queasy","Quick","Quiet","Quaint","Quizzed"]
            st.write(name[i],":",random.choice(qlist))
        elif char1=="R":
            rlist = ["Rebel","Rich","Rigid","Rude","Rumped"]
            st.write(name[i],":",random.choice(rlist))
        elif char1=="S":
            slist = ["Scabby","Silent","Screaky","Scurby","Superb"]
            st.write(name[i],":",random.choice(slist))
        elif char1=="T":
            tlist = ["Tearful","Terrific","Tough","Truthful","Tricky Person"]
            st.write(name[i],":",random.choice(tlist))
        elif char1=="U":
            ulist = ["Ugly","Unaffraid","Unlucky","Understanding","Unsure"]
            st.write(name[i],":",random.choice(ulist))
        elif char1=="V":
            vlist = ["Vibrant","Vicious","Vigorous","Vigorous","Vigorous"]
            st.write(name[i],":",random.choice(vlist))
        elif char1=="W":
            wlist=["Wonderful","Warm","Wild","Wonderfull","Weak"]
            st.write(name[i],":",random.choice(wlist))
        elif char1=="X":
            xlist=["Xenophobic","Xenial","Xenodolnial"]
            st.write(name[i],":",random.choice(xlist))
        elif char1=="Y":
            ylist = ["Youthful","Young","Youthful","Young","Young"]
            st.write(name[i],":",random.choice(ylist))
        elif char1=="Z":
            zlist = ["Zealous","Zealous","Zealous","Zealous","Zealous"]
            st.write(name[i],":",random.choice(zlist))
        else:
            st.write("Invalid Input")
elif choice=="Exit":
    st.write("Thank You")
elif choice=="":
    st.write("Please select a choice")
else:
    st.write("Invalid Input")