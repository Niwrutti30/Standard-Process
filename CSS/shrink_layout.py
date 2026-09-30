import codecs
path = r'c:\Users\aniketk\Desktop\Core Dna\oro commerce TASK\CSS\Dietary Restrictions.html'
with codecs.open(path, 'r', 'utf-8') as f:
    text = f.read()

text = text.replace('max-width: 1540px;', 'max-width: 1140px;')
text = text.replace('padding: 60px 50px 140px 60px;', 'padding: 50px 40px 100px 40px;')
text = text.replace('width: 65%;', 'width: 55%;')
text = text.replace('margin-top: -120px;', 'margin-top: -80px;')
text = text.replace('width: 55%;', 'width: 48%;')
text = text.replace('flex: 0 0 55%;', 'flex: 0 0 48%;')
text = text.replace('width: 40%;', 'width: 45%;')
text = text.replace('flex: 0 0 40%;', 'flex: 0 0 45%;')
text = text.replace('margin-top: 100px;', 'margin-top: 50px;')

with codecs.open(path, 'w', 'utf-8') as f:
    f.write(text)
print("Size adjustments applied.")
