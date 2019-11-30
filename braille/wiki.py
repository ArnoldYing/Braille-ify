from lxml import html
import requests
import braille

page = requests.get('http://en.wikipedia.org/wiki/Dog')
tree = html.fromstring(page.content)

content = tree.xpath('//div[@class="mw-parser-output"]/p/text()')

print (content)

for c in content:
    braille.textToBraille(c)

