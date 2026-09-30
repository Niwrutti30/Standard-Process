import os, re
path = r'c:\Users\aniketk\Desktop\Core Dna\oro commerce TASK\CSS\Dietary Restrictions.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace the broken absolute-positioned HTML
html_old = r'<section class="full-width-screen grains-section">.*?<div class="anc">.*?<div class="stage">.*?<div class="bottom-panel">.*?</section>'
html_new = '''<section class="sp-grains-section full-width-screen mrgn-tp-btm">
  <div class="sp-container-wrapper">
    <div class="sp-grains-inner">
      <div class="sp-botanical-left">
        <img src="/media/cache/attachment/filter/wysiwyg_original/87ce74c18aefc3f765aae166bfe23016/14245/69bd618f86fc1689813755-Left-botanical-illustration.png" alt="">
      </div>
      <div class="sp-grains-box">
        <div class="sp-botanical-right">
          <img src="/media/cache/attachment/filter/wysiwyg_original/87ce74c18aefc3f765aae166bfe23016/14244/69bd617a115be381525123-right-imafe-1.png" alt="">
        </div>
        <div class="sp-grains-box-content">
          <h2>Whole Grains Compatible With Many Common Diets</h2>
          <p>Our high-quality, certified organic whole grains bring healthful living into the kitchen. Full of vital nutrients, they provide health benefits that improve quality of life. All products are certified organic and many are compatible with common diets, including acid alkaline diet, Atkins diet, gluten-free diet, low-carb diet, macrobiotic diet, and the Mediterranean diet.</p>
          <a href="https://sp-prod.oro-cloud.com/practitioner-benefits-insite" class="wht-bg-btn" style="margin-top: 15px;">Visit Royal Lee Organics</a>
        </div>
      </div>
      <div class="sp-grains-photo">
        <img src="/media/cache/attachment/filter/wysiwyg_original/87ce74c18aefc3f765aae166bfe23016/14243/69bd61643d9f7515995971-Main-product-photo.png" alt="Organic grain products" loading="lazy">
      </div>
      <div class="sp-grains-research">
        <h2>Products Backed by Clinical Research</h2>
        <p>Our scientists verify the quality, purity, and integrity of our ingredients by running up to 2,100 tests per week. Using state-of-the-art equipment, the team at our Nutrition Innovation Center also conducts innovative research that helps us to develop new targeted formulations as well as substantiate existing ones. We go the extra step to ensure confidence in choosing Standard Process.</p>
        <a href="#" target="_blank" class="btn sp-prod-links" style="align-self: flex-start; margin-top: 20px;">Learn More</a>
      </div>
    </div>
  </div>
</section>'''
content = re.sub(html_old, html_new, content, flags=re.DOTALL)

# 2. Strip the massive absolute-positioned CSS
content = re.sub(r'  /\* laste section  \*/\s*img \{.*?/\* laste section  \*/\s*', '', content, flags=re.DOTALL)

# 3. Add clip-path to .sp-grains-box (desktop)
css_box_old = '''  .sp-grains-box {
    grid-column: 2;
    grid-row: 1;
    background: #C3882C;
    position: relative;
    overflow: hidden;
    padding: 50px 40px 50px 60px;
    z-index: 1;
  }'''
css_box_new = '''  .sp-grains-box {
    grid-column: 2;
    grid-row: 1;
    background: #C3882C;
    position: relative;
    overflow: hidden;
    padding: 50px 40px 100px 60px;
    z-index: 1;
    clip-path: polygon(0 0, calc(100% - 60px) 0, 100% 60px, 100% 100%, 0 100%);
  }'''
content = content.replace(css_box_old, css_box_new)

# 4. Add clip-path to .sp-grains-box (mobile)
css_box_mobile_old = '''    .sp-grains-box {
      grid-column: 1;
      grid-row: 1;
      padding: 40px 20px;
    }'''
css_box_mobile_new = '''    .sp-grains-box {
      grid-column: 1;
      grid-row: 1;
      padding: 40px 20px;
      clip-path: polygon(0 0, calc(100% - 30px) 0, 100% 30px, 100% 100%, 0 100%);
    }'''
content = content.replace(css_box_mobile_old, css_box_mobile_new)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Successfully fixed Dietary Restrictions layout!')
