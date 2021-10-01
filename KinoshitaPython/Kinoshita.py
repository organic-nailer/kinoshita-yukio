from Responder import *
from Dictionary import *
from Analyzer import *
from Emotion import *

class Kinoshita: #本体

    def __init__(self, name):

        self.name = name

        self.dictionary = Dictionary()

        self.emotion = Emotion(self.dictionary)

        self.res_random = RandomResponder("Randomdom", self.dictionary)
        self.res_repeat = RepeatResponder("Repeat?", self.dictionary)
        self.res_pattern = PatternResponder("Pattern", self.dictionary)
        self.res_template = TemplateResponder("Template",self.dictionary)
        self.res_markov = MarkovResponder("Markov",self.dictionary)

    def Dialogue(self,input):

        #カッコを全角に変換
        #全角に変換しないとエラーが出る
        input = input.replace("(","（")
        input = input.replace(")","）")

        #感情関数　使ってない
        self.emotion.update(input)
        #単語と品詞を抽出
        parts = Analyze(input)

        print(parts)

        #レスポンダーの振り分け
        x = random.randint(1,100)

        if x <= 33:
            self.responder = self.res_pattern
        elif x < 66:
            self.responder = self.res_markov
        else:
            self.responder = self.res_template

        #レスポンスを取得
        resp = self.responder.response(input,self.emotion.mood,parts)
        #学習
        self.dictionary.study(input,parts)


        return resp

    def save(self):

        self.dictionary.save()

    def Getrespondername(self):

        return self.responder.name

    def Getname(self):

        return self.name



