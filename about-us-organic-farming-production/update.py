import re

path = r'c:\Users\aniketk\Desktop\Core Dna\oro commerce TASK\about-us-organic-farming-production\index.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# CSS changes
old_css_root = """    #sp-organic-page {
        --max-width: 1540px;
        --font-sans: 'Open Sans', sans-serif;
        --font-serif: 'Libre Baskerville', serif;

        --color-white: #ffffff;
        --color-black: #000000;
        --color-dark-green: #0a4f31;
        --color-olive: #6a824e;
        --color-brown: #a06b3a;
        --color-light-green: #7d9e52;
        --color-orange: #d69c4c;

        font-family: var(--font-sans);
        line-height: 1.6;
        background-color: var(--color-white);
        color: #333;
        max-width: var(--max-width);
        margin: 0 auto;
        overflow: hidden;
        position: relative;
        text-align: left;
    }"""

new_css_root = """    #sp-organic-page {
        --max-width: 1540px;
        --font-sans: 'Open Sans', sans-serif;
        --font-serif: 'Libre Baskerville', serif;

        --color-white: #ffffff;
        --color-black: #000000;
        --color-dark-green: #0a4f31;
        --color-olive: #6a824e;
        --color-brown: #a06b3a;
        --color-light-green: #7d9e52;
        --color-orange: #d69c4c;

        font-family: var(--font-sans);
        line-height: 1.6;
        background-color: var(--color-white);
        color: #333;
        width: 100%;
        overflow: hidden;
        position: relative;
        text-align: left;
    }

    .sp-container {
        max-width: var(--max-width) !important;
        margin: 0 auto !important;
        padding: 0 40px !important;
        width: 100% !important;
    }

    .sp-split-inner-left {
        max-width: 770px !important;
        margin-left: auto !important;
        width: 100% !important;
        padding: 0 20px 0 40px !important;
    }

    .sp-split-inner-right {
        max-width: 770px !important;
        margin-right: auto !important;
        width: 100% !important;
        padding: 0 40px 0 20px !important;
    }"""

content = content.replace(old_css_root, new_css_root)

content = content.replace("    .sp-vitality-text {\n        padding: 80px 60px !important;", "    .sp-vitality-text {\n        padding: 80px 0 !important;")
content = content.replace("    .sp-explore-content {\n        padding: 80px 60px !important;", "    .sp-explore-content {\n        padding: 80px 0 !important;")
content = content.replace("    .sp-method-item {\n        padding: 30px 40px !important;\n        align-items: flex-start !important;\n        gap: 25px !important;\n        flex: 1 !important;\n        display: flex !important;\n    }", "    .sp-method-item {\n        flex: 1 !important;\n        display: flex !important;\n    }")
content = content.replace("    .sp-farmer-stats {\n        padding: 60px 80px !important;", "    .sp-farmer-stats {\n        padding: 0;")

# Section 2
sect2_old = """        <div class="sp-vitality-text sp-bg-olive sp-col-50">
            <p class="sp-text-sm">"""
sect2_new = """        <div class="sp-vitality-text sp-bg-olive sp-col-50">
            <div class="sp-split-inner-left">
            <p class="sp-text-sm">"""
if sect2_old in content: content = content.replace(sect2_old, sect2_new)
else: print('Failed sec 2.1')

secto2_bot_old = """        </div>
        <div class="sp-vitality-image sp-col-50 sp-block-relative">"""
secto2_bot_new = """            </div>
        </div>
        <div class="sp-vitality-image sp-col-50 sp-block-relative">"""
if secto2_bot_old in content: content = content.replace(secto2_bot_old, secto2_bot_new)
else: print('Failed sec 2.2')

# Section 3
for x in ['brown', 'light-green', 'dark-green']:
    s3_old = f"""            <div class="sp-method-item sp-bg-{x}">
                <div class="sp-method-icon">"""
    s3_new = f"""            <div class="sp-method-item sp-bg-{x}">
                <div class="sp-split-inner-left sp-d-flex" style="padding: 30px 40px; align-items: flex-start; gap: 25px;">
                <div class="sp-method-icon">"""
    if s3_old in content: content = content.replace(s3_old, s3_new)
    else: print(f'Failed sec 3 {x}')

content = content.replace("""                </div>
            </div>
            <div class="sp-method-item sp-bg-light-green">""", """                </div></div>
            </div>
            <div class="sp-method-item sp-bg-light-green">""")

content = content.replace("""                </div>
            </div>
            <div class="sp-method-item sp-bg-dark-green">""", """                </div></div>
            </div>
            <div class="sp-method-item sp-bg-dark-green">""")

content = content.replace("""                </div>
            </div>
        </div>
        <div class="sp-methods-image sp-col-50 sp-block-relative">""", """                </div></div>
            </div>
        </div>
        <div class="sp-methods-image sp-col-50 sp-block-relative">""")

# Section 4
sect4_old1 = """            <div class="sp-farmer-quote-overlay">
                <div class="sp-quote-marks">"</div>"""
sect4_new1 = """            <div class="sp-farmer-quote-overlay">
                <div class="sp-split-inner-left sp-d-flex" style="flex-direction: column; align-items: center; text-align: center;">
                <div class="sp-quote-marks">"</div>"""
if sect4_old1 in content: content = content.replace(sect4_old1, sect4_new1)
else: print('Failed sec 4.1')

sect4_old2 = """            </div>
        </div>
        <div class="sp-farmer-stats sp-col-50 sp-bg-white">
            <h2>Meet Our Farmers</h2>"""
sect4_new2 = """                </div>
            </div>
        </div>
        <div class="sp-farmer-stats sp-col-50 sp-bg-white">
            <div class="sp-split-inner-right" style="padding-top: 60px; padding-bottom: 60px;">
            <h2>Meet Our Farmers</h2>"""
if sect4_old2 in content: content = content.replace(sect4_old2, sect4_new2)
else: print('Failed sec 4.2')

sect4_old3 = """            </div>
        </div>
    </section>

    <!-- Section 5: Explore Map -->"""
sect4_new3 = """            </div>
            </div>
        </div>
    </section>

    <!-- Section 5: Explore Map -->"""
if sect4_old3 in content: content = content.replace(sect4_old3, sect4_new3)
else: print('Failed sec 4.3')

# Section 5
sect5_old = """        <div class="sp-explore-content sp-bg-dark-green-2 sp-col-50">
            <p>Explore the Standard Process farm."""
sect5_new = """        <div class="sp-explore-content sp-bg-dark-green-2 sp-col-50">
            <div class="sp-split-inner-left">
            <p>Explore the Standard Process farm."""
if sect5_old in content: content = content.replace(sect5_old, sect5_new)
else: print('Failed sec 5.1')

sect5_bot = """            <button class="sp-btn sp-btn-outline">Explore the Farm</button>
        </div>
        <div class="sp-explore-image sp-col-50 sp-block-relative">"""
sect5_bot_new = """            <button class="sp-btn sp-btn-outline">Explore the Farm</button>
            </div>
        </div>
        <div class="sp-explore-image sp-col-50 sp-block-relative">"""
if sect5_bot in content: content = content.replace(sect5_bot, sect5_bot_new)
else: print('Failed sec 5.2')

# Section 6
sect6_old = """    <!-- Section 6: Christine Quote -->
    <section class="sp-christine-section sp-section-padding sp-text-center">
        <div class="sp-christine-container">"""
sect6_new = """    <!-- Section 6: Christine Quote -->
    <section class="sp-christine-section sp-section-padding sp-text-center">
        <div class="sp-container">
        <div class="sp-christine-container">"""
if sect6_old in content: content = content.replace(sect6_old, sect6_new)
else: print('Failed sec 6.1')

sect6_bot = """            </div>
        </div>
    </section>

    <!-- Section 7: Process Intro -->"""
sect6_bot_new = """            </div>
        </div>
        </div>
    </section>

    <!-- Section 7: Process Intro -->"""
if sect6_bot in content: content = content.replace(sect6_bot, sect6_bot_new)
else: print('Failed sec 6.2')

# Section 7
sect7_old = """    <!-- Section 7: Process Intro -->
    <section class="sp-process-intro sp-section-padding-lg">
        <div class="sp-process-left sp-col-50">"""
sect7_new = """    <!-- Section 7: Process Intro -->
    <section class="sp-process-intro sp-section-padding-lg">
        <div class="sp-container sp-d-flex">
        <div class="sp-process-left sp-col-50">"""
if sect7_old in content: content = content.replace(sect7_old, sect7_new)
else: print('Failed sec 7.1')

sect7_bot = """                high bar with excellence as our standard.</p>
        </div>
    </section>

    <!-- Section 8: Five Process Columns -->"""
sect7_bot_new = """                high bar with excellence as our standard.</p>
        </div>
        </div>
    </section>

    <!-- Section 8: Five Process Columns -->"""
if sect7_bot in content: content = content.replace(sect7_bot, sect7_bot_new)
else: print('Failed sec 7.2')

# Section 8
sect8_old = """    <!-- Section 8: Five Process Columns -->
    <section class="sp-process-steps sp-section-padding sp-text-center">
        <div class="sp-steps-images">"""
sect8_new = """    <!-- Section 8: Five Process Columns -->
    <section class="sp-process-steps sp-section-padding sp-text-center">
        <div class="sp-container">
        <div class="sp-steps-images">"""
if sect8_old in content: content = content.replace(sect8_old, sect8_new)
else: print('Failed sec 8.1')

sect8_bot = """        <div class="sp-process-cta sp-text-center">
            <button class="sp-btn sp-btn-primary">Our Manufacturing Process</button>
        </div>
    </section>

    <!-- Section 9: Methods Grid -->"""
sect8_bot_new = """        <div class="sp-process-cta sp-text-center">
            <button class="sp-btn sp-btn-primary">Our Manufacturing Process</button>
        </div>
        </div>
    </section>

    <!-- Section 9: Methods Grid -->"""
if sect8_bot in content: content = content.replace(sect8_bot, sect8_bot_new)
else: print('Failed sec 8.2')

# Section 9
sect9_old = """    <!-- Section 9: Methods Grid -->
    <section class="sp-methods-grid sp-section-padding sp-text-center sp-bg-white">
        <h2 class="sp-section-title">Our Organic Farming Methods</h2>"""
sect9_new = """    <!-- Section 9: Methods Grid -->
    <section class="sp-methods-grid sp-section-padding sp-text-center sp-bg-white">
        <div class="sp-container">
        <h2 class="sp-section-title">Our Organic Farming Methods</h2>"""
if sect9_old in content: content = content.replace(sect9_old, sect9_new)
else: print('Failed sec 9.1')

sect9_bot = """        <div class="sp-map-cta">
            <button class="sp-btn sp-btn-primary">Interactive Map</button>
        </div>
    </section>

</div>"""
sect9_bot_new = """        <div class="sp-map-cta">
            <button class="sp-btn sp-btn-primary">Interactive Map</button>
        </div>
        </div>
    </section>

</div>"""
if sect9_bot in content: content = content.replace(sect9_bot, sect9_bot_new)
else: print('Failed sec 9.2')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Done!')
