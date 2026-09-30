import codecs
import re

path = r'c:\Users\aniketk\Desktop\Core Dna\oro commerce TASK\CSS\Dietary Restrictions.html'
with codecs.open(path, 'r', 'utf-8') as f:
    text = f.read()

# Replace the entire sp-grains-section CSS with bulletproof styles
old_css = r'\.sp-grains-section \{.*?\s*\}\s*</style>'

new_css = '''.sp-grains-section {
    padding: 60px 0 100px;
    overflow: hidden;
    width: 100%;
    display: block;
    box-sizing: border-box;
  }

  .sp-grains-inner {
    position: relative;
    width: 100%;
    max-width: 1200px; /* Use a standard max-width */
    margin: 0 auto;
    display: block;
    box-sizing: border-box;
  }

  .sp-grains-box {
    box-sizing: border-box;
    background: #C3882C;
    padding: 60px 60px 140px 80px;
    width: 75%;
    margin-left: auto;
    position: relative;
    z-index: 1;
    clip-path: polygon(0 0, calc(100% - 60px) 0, 100% 60px, 100% 100%, 0 100%);
    display: block;
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
    width: 260px;
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
    box-sizing: border-box;
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-top: -140px;
    position: relative;
    z-index: 2;
    gap: 40px;
    width: 100%;
  }

  .sp-grains-photo {
    box-sizing: border-box;
    width: 48%;
    flex: 0 0 48%;
    position: relative;
    z-index: 3;
  }

  .sp-grains-photo img {
    width: 100%;
    border-radius: 4px;
    display: block;
    box-shadow: 0 12px 30px rgba(0, 0, 0, 0.15);
    margin: 0;
  }

  .sp-botanical-left {
    position: absolute;
    left: -80px;
    bottom: -60px;
    width: 260px;
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
    box-sizing: border-box;
    width: 48%;
    flex: 0 0 48%;
    padding-right: 20px;
    padding-left: 20px;
    position: relative;
    z-index: 3;
    margin-top: 0;
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
    .sp-grains-box { width: 85%; }
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
print("Done styling layout perfectly.")
