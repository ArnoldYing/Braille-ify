from lxml import html
import requests
import braille

page = requests.get('http://en.wikipedia.org/wiki/Fortnite')
tree = html.fromstring(page.content)
tableOfContent = tree.xpath('//*[@id="toc"]/ul/li/a/span[@class="toctext"]/text()')
subTitles = tree.xpath('//h2/span[@class="mw-headline"]/text()')
content = tree.xpath('//div[@class="mw-parser-output"]/p/text() | //div[@class="mw-parser-output"]/p/*/text() |'
                     ' //div[@class="mw-parser-output"]/p/*/*/text()')
for c in subTitles:
    arr = braille.textToAsciiBraille(c)

