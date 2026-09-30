import codecs
import re

path = r'c:\Users\aniketk\Desktop\Core Dna\oro commerce TASK\CSS\Dietary Restrictions.html'
with codecs.open(path, 'r', 'utf-8') as f:
    text = f.read()

# Replace HTML
old_html = r'<section class="sp-grains-section full-width-screen mrgn-tp-btm">.*?</section>'
new_html = '''<section class="sp-grains-section full-width-screen mrgn-tp-btm">
  <div class="sp-container-wrapper">
    <div class="sp-grains-inner">
      <!-- Golden Box -->
      <div class="sp-grains-box">
        <div class="sp-botanical-right">
          <img src="/media/cache/attachment/filter/wysiwyg_original/87ce74c18aefc3f765aae166bfe23016/14244/69bd617a115be381525123-right-imafe-1.png" alt="">
        </div>
        <h2>Whole Grains Compatible With Many Common Diets</h2>
        <p>Our high-quality, certified organic whole grains bring healthful living into the kitchen. Full of vital nutrients, they provide health benefits that improve quality of life. All products are certified organic and many are compatible with common diets, including acid alkaline diet, Atkins diet, gluten-free diet, low-carb diet, macrobiotic diet, and the Mediterranean diet.</p>
        <a href="https://sp-prod.oro-cloud.com/practitioner-benefits-insite" class="wht-bg-btn" style="margin-top: 15px; display: inline-block;">Visit Royal Lee Organics</a>
      </div>

      <!-- Bottom Container (Flex) -->
      <div class="sp-grains-bottom">
        <div class="sp-botanical-left">
          <img src="/media/cache/attachment/filter/wysiwyg_original/87ce74c18aefc3f765aae166bfe23016/14245/69bd618f86fc1689813755-Left-botanical-illustration.png" alt="">
        </div>
        <div class="sp-grains-photo">
          <img src="/media/cache/attachment/filter/wysiwyg_original/87ce74c18aefc3f765aae166bfe23016/14243/69bd61643d9f7515995971-Main-product-photo.png" alt="Organic grain products" loading="lazy">
        </div>
        <div class="sp-grains-research">
          <h2>Products Backed by Clinical Research</h2>
          <p>Our scientists verify the quality, purity, and integrity of our ingredients by running up to 2,100 tests per week. Using state-of-the-art equipment, the team at our Nutrition Innovation Center also conducts innovative research that helps us to develop new targeted formulations as well as substantiate existing ones. We go the extra step to ensure confidence in choosing Standard Process.</p>
          <a href="#" target="_blank" class="btn sp-prod-links" style="display: inline-block;">Learn More</a>
        </div>
      </div>
    </div>
  </div>
</section>'''
text = re.sub(old_html, new_html, text, flags=re.DOTALL)

# Replace CSS
old_css = r'\.sp-grains-section \{.*?\}\s*</style>'
new_css = '''.sp-grains-section {
    padding: 60px 0 100px;
    overflow: hidden;
  }

  .sp-grains-inner {
    position: relative;
    max-width: 1540px;
    margin: 0 auto;
  }

  .sp-grains-box {
    background: #C3882C;
    padding: 60px 50px 140px 60px;
    width: 65%;
    margin-left: auto;
    position: relative;
    z-index: 1;
    clip-path: polygon(0 0, calc(100% - 60px) 0, 100% 60px, 100% 100%, 0 100%);
  }

  .sp-grains-box h2 {
    color: #fff !important;
    font-size: 28px;
    margin-bottom: 16px;
    position: relative;
    z-index: 2;
  }

  .sp-grains-box p {
    color: #fff !important;
    font-size: 16px !important;
    line-height: 1.6 !important;
    position: relative;
    z-index: 2;
  }

  .sp-botanical-right {
    position: absolute;
    right: -20px;
    top: 0;
    width: 220px;
    opacity: 0.2;
    pointer-events: none;
    z-index: 1;
  }

  .sp-botanical-right img {
    width: 100%;
    height: auto;
    display: block;
    margin: 0;
  }

  .sp-grains-bottom {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-top: -120px;
    position: relative;
    z-index: 2;
    gap: 40px;
  }

  .sp-grains-photo {
    width: 55%;
    flex: 0 0 55%;
    position: relative;
    z-index: 3;
  }

  .sp-grains-photo img {
    width: 100%;
    border-radius: 4px;
    display: block;
    box-shadow: 0 12px 30px rgba(0,0,0,0.15);
    margin: 0;
  }

  .sp-botanical-left {
    position: absolute;
    left: -80px;
    bottom: -40px;
    width: 220px;
    opacity: 0.15;
    pointer-events: none;
    z-index: 1;
  }

  .sp-botanical-left img {
    width: 100%;
    height: auto;
    display: block;
    margin: 0;
  }

  .sp-grains-research {
    width: 40%;
    flex: 0 0 40%;
    padding-right: 40px;
    position: relative;
    z-index: 3;
    margin-top: 100px;
  }

  .sp-grains-research h2 {
    color: #404040;
    font-size: 28px;
    margin-bottom: 16px;
  }

  .sp-grains-research p {
    color: #404040;
    font-size: 16px !important;
    line-height: 1.6 !important;
    margin-bottom: 20px;
  }

  @media (max-width: 1024px) {
    .sp-grains-box { width: 80%; }
    .sp-grains-bottom { margin-top: -80px; }
  }

  @media (max-width: 768px) {
    .sp-grains-box {
      width: 100%;
      clip-path: polygon(0 0, calc(100% - 30px) 0, 100% 30px, 100% 100%, 0 100%);
      padding: 40px 20px 80px;
    }
    .sp-grains-bottom {
      flex-direction: column;
      margin-top: -60px;
      gap: 30px;
    }
    .sp-grains-photo { width: 100%; flex: 0 0 100%; }
    .sp-grains-research {
      width: 100%;
      flex: 0 0 100%;
      padding-right: 0;
      padding-left: 20px;
      padding-bottom: 30px;
      margin-top: 0;
    }
    .sp-botanical-left, .sp-botanical-right { display: none; }
  }
</style>'''
text = re.sub(old_css, new_css, text, flags=re.DOTALL)

with codecs.open(path, 'w', 'utf-8') as f:
    f.write(text)
print("Done")
