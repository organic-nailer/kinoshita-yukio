from Analyzer import *
import re
import random

def MakeMkey(p1,p2,p3):

    return str(p1) + "\t" + str(p2) + "\t" + str(p3)

def Getkey(mkey):

    return re.split("\t",mkey,2)

class Markov:



    def make(self):

        #log
        print("ファイルを読み込んでいます…")
        #log
        filename = "lib/log.txt"
        
        with open(filename,
          "r",
          encoding = "utf_8") as f:
            text = f.read()
            
        #log
        print("マルコフ連鎖のためのDBを用意しています…")
        #log
            
        text = re.sub("\n","",text)

        text = re.sub("> ","",text)
        text = re.sub(
            "Yukio：Pattern|Yukio：Randomdom|Yukio：Repeat?|Yukio:Markov|Yukio:Template",
            "",text)

        text = re.sub("Kinoshita_.*\n","",text)
        text = re.sub("\n\n","\n",text)

            
        wordlist = parse(text)
            
        markov = {}
            
        p1 = ""
        p2 = ""
        p3 = ""
            
        for word in wordlist:
                
            if p1 and p2 and p3:

                mkey = MakeMkey(p1,p2,p3)
                    
                if mkey not in markov:
                        
                    markov[mkey] = []
                        
                markov[mkey].append(word)
                    
            p1,p2,p3 = p2,p3,word
                
        sentence = ""

        p1,p2,p3 = Getkey(random.choice(list(markov.keys())))

        count = 0
            
        while count < 30:

            mkey = MakeMkey(p1,p2,p3)
             
            if(mkey in markov) == True:
                    
                tmp = random.choice(markov[mkey])

                sentence += tmp

            p1,p2,p3 = p2,p3,tmp

            count += 1

        sentence = re.sub("^.+?。","",sentence)

        if re.search(".+。",sentence):

            sentence = re.search(".+。",sentence).group()
        
        sentence = re.sub("「","",sentence)
        sentence = re.sub("」","",sentence)
        sentence = re.sub("　","",sentence)

        return sentence
