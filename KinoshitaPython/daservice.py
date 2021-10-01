#coding: utf-8

from urllib.parse import urlencode
from urllib.request import urlopen
from xml.etree import ElementTree


class DAService:
    
    def GetChunkList(self, text):

        sentence = text.encode("utf-8")

        postdata = {
            "appid":"dj00aiZpPVZDdm5kaTN6YnNGbSZzPWNvbnN1bWVyc2VjcmV0Jng9NmM-",
            "sentence":sentence,
            }

        params = urlencode(postdata).encode("ascii")

        url = "https://jlp.yahooapis.jp/DAService/V1/parse"

        result = urlopen(url,params)

        return self.Parse(result.read())

    def Parse(self, xml):

        c = []

        elem = ElementTree.fromstring(xml)

        for chunk in elem.getiterator('{urn:yahoo:jp:jlp:DAService}Chunk'):
            surface = ""
            for surfaces in chunk.getiterator("{urn:yahoo:jp:jlp:DAService}Surface"):

                surface += surfaces.text

            c.append([surface, chunk.find("{urn:yahoo:jp:jlp:DAService}Dependency").text])

        for item in c:
        
            if item[1] == "-1":
        
                item[1] = None
            else:

                item[1] = c[int(item[1])][0]

        return c