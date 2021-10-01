import re
from janome import tokenizer
import Analyzer

def IsGimonbun(input):

    result = False

    whitelist = u"(だれ|どこ|なに|どれ|誰|何処|何)(?=(が|に|を|で|から|だ))"
    blacklist = u"(いつ|なぜ|なんで|どのように|いくつ|いくら)(?!でも)"

    havehatena = re.search("\?$",input)

    if re.search(u"(\?|？)$",input):

        result = True

    elif re.search(whitelist, input) or re.search(blacklist, input):

        result = True

    return result
