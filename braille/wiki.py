from lxml import html
import requests
import braille

page = requests.get('http://en.wikipedia.org/wiki/Fortnite')
tree = html.fromstring(page.content)

tableOfContent = tree.xpath('//*[@id="toc"]/ul/li/a/span[@class="toctext"]/text()')
subTitles = tree.xpath('//h2/span[@class="mw-headline"]/text()')
content = tree.xpath('//div[@class="mw-parser-output"]/p/text() | //div[@class="mw-parser-output"]/p/*/text() |'
                     ' //div[@class="mw-parser-output"]/p/*/*/text()')


print(tableOfContent)
print(subTitles)
print(content)

#for c in content:
#   braille.textToBraille(c)
# print (content)

# for c in braille.textToAsciiBraille(content):
#     print(c)

braille.textToBraille('matt')
arr = braille.textToAsciiBraille('matt')

print(str(arr))
    

