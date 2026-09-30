path = r'c:\Users\aniketk\Desktop\Core Dna\oro commerce TASK\about-us-organic-farming-production\code.html'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('width: 57.8125%;', 'width: 50%;')
text = text.replace('width: 42.1875%;', 'width: 50%;')
text = text.replace('padding: clamp(30px, 5vw, 70px) clamp(24px, 4vw, 60px);', 'padding: clamp(30px, 5vw, 70px) 0;')

old_left_content = """    .vitality-left-content {
        position: relative;
        z-index: 2;
        padding-left: clamp(80px, 10vw, 140px);
        color: #ffffff;
        max-width: 680px;
    }"""
new_left_content = """    .vitality-left-content {
        position: relative;
        z-index: 2;
        padding-left: 20px;
        padding-right: 40px;
        margin-left: auto;
        color: #ffffff;
        width: 100%;
        max-width: 770px; /* Aligns precisely to the 1540px grid */
    }"""
text = text.replace(old_left_content, new_left_content)

old_mobile_padding = """        .vitality-left-content {
            padding-left: clamp(60px, 15vw, 100px);
        }"""
new_mobile_padding = """        .vitality-left-content {
            padding-left: 20px;
            padding-right: 20px;
        }"""
text = text.replace(old_mobile_padding, new_mobile_padding)

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print("code.html successfully updated!")
