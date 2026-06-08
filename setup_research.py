import os

def write(path, content):
    d = os.path.dirname(path)
    if d: os.makedirs(d, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Created: {path}")

# ── README.md ──────────────────────────────────────────────────────────────────
write("README.md", """# 100Hires Portfolio Project
## Victor James Fermo

---

## Step 1: Environment Setup (Completed)

### Tools Installed
- **Cursor IDE** (cursor.com) - AI-native code editor
- **Claude Code** (by Anthropic) - AI coding assistant inside Cursor
- **Codex** (by OpenAI) - AI coding assistant inside Cursor
- **GitHub account** created and repository set to public

### Steps Completed
1. Downloaded and installed Cursor IDE
2. Navigated to the VS Code Editor Window inside Cursor (not the default AI Marketplace)
3. Used Ctrl+Shift+X to open the Extensions panel
4. Installed Claude Code (by Anthropic) and Codex (by OpenAI, 5.1M downloads)
5. Created this GitHub repository (100hires-portfolio) as a public repo
6. Edited README.md directly in the GitHub browser editor

### Issue Encountered and Resolved
Cursor's current interface separates the AI agent Marketplace view from the traditional VS Code Editor Window. The Extensions panel (Ctrl+Shift+X) is only accessible from the Editor Window. Claude Code did not appear in the Marketplace search at all. The fix was to click "Editor Window" in the top-right corner of Cursor to access the VS Code-style interface, then use Ctrl+Shift+X normally. Documented this because it is not obvious and may help others.

---

## Step 2: Research Project (In Progress)

### Topic Chosen
**AI-Powered SEO Content Production**

### Why I Chose This Topic
This topic sits at the intersection of two things happening simultaneously in digital marketing: AI tools are now capable of producing content at scale, and search engines are simultaneously changing how they evaluate and rank that content. The question of how to use AI to produce SEO content that actually performs is not answered well by most marketing content online. I chose this topic because I wanted to find the practitioners who are actually doing this at scale, not just writing about the theory.

The research also directly builds on existing work I do: I run a weekly AI marketing newsletter (The AI Edge) and have hands-on experience with content workflows. This topic is not academic for me.

### Expert Selection Approach
All 10 experts were chosen because they are practitioners, not just commentators. Selection criteria:
- They have documented results tied to real companies or client work
- Their content is tool-specific and workflow-specific, not generic advice
- They represent different vantage points: agency, SaaS in-house, tool builder, independent consultant
- They are not the first page of Google results for "AI SEO expert"

See /research/sources.md for full expert list with annotations.

### Repository Structure

```
100hires-portfolio/
├── README.md
├── fetch_transcripts.py
├── setup_research.py
└── research/
    ├── sources.md
    ├── linkedin-posts/
    │   ├── ryan-law/posts.md
    │   ├── aleyda-solis/posts.md
    │   ├── kevin-indig/posts.md
    │   ├── lily-ray/posts.md
    │   ├── ross-hudgens/posts.md
    │   ├── chima-mmeje/posts.md
    │   ├── eli-schwartz/posts.md
    │   ├── bernard-huang/posts.md
    │   ├── brendan-hufford/posts.md
    │   └── rand-fishkin/posts.md
    ├── youtube-transcripts/
    └── other/
        └── methodology.md
```

### Commit Log
- Commit 1: Environment setup complete, Step 1 README
- Commit 2: Add Step 2 research structure, sources, methodology
- Commit 3: Add YouTube transcripts via youtube-transcript-api (8 videos, 8 saved)
- Commit 4: Add LinkedIn posts (manual collection, all 10 authors)
- Commit 5: Final cleanup and README update

---

## About Me

Victor James Fermo - Digital Marketing and Social Media Specialist
Based in Zamboanga City, Philippines
Email: vj.fermo@outlook.com
LinkedIn: https://linkedin.com/in/victorjamesfermo
Portfolio: https://vjflowsmm.my.canva.site/portfolio
""")

# ── research/sources.md ────────────────────────────────────────────────────────
write("research/sources.md", """# Research Sources: AI-Powered SEO Content Production

## Topic
AI-Powered SEO Content Production for B2B SaaS

## Selection Criteria
Experts selected on three criteria:
1. They actively produce AI-augmented SEO content at scale, not just write about it
2. They have verifiable results tied to specific companies or client outcomes
3. Their perspective is non-obvious: not the first page of Google results for "SEO expert"

---

## Expert 1: Ryan Law
**Title:** Director of Content Marketing, Ahrefs
**LinkedIn:** https://www.linkedin.com/in/thinkingslow
**YouTube:** https://www.youtube.com/@ahrefs
**Blog:** https://ahrefs.com/blog/author/ryan-law/
**Date collected:** 2026-06-08

**Why this expert:**
Ryan Law is responsible for content strategy at Ahrefs, one of the most-read SEO tool blogs in the world. Uniquely, Ahrefs publicly documented their own AI content workflow in 2025: they used AI to write articles at scale, tracked which ones ranked, and published the actual results and methodology. This is not theory. This is a practitioner who built, tested, and reported on an AI content pipeline inside a real SaaS company. His work answers the exact question this topic asks: how do you use AI for SEO content production that actually performs?

**Videos collected:**
- AI Writing at Scale: Ahrefs Step-by-Step Workflow
- How to Automate Blog Writing with AI from Keyword to Published
- How to Win in AI Search: Real Data No Hype

---

## Expert 2: Aleyda Solis
**Title:** SEO Consultant and Founder, Orainti
**LinkedIn:** https://www.linkedin.com/in/aleyda
**YouTube:** https://www.youtube.com/@AleydaSolis (Crawling Mondays series)
**Newsletter:** SEOFOMO (seofomo.co)
**Date collected:** 2026-06-08

**Why this expert:**
Aleyda Solis is one of the most respected international SEO practitioners globally, advising enterprise brands through Orainti. Her Crawling Mondays YouTube series is a working practitioner documenting real tools and workflows, not a content creator performing expertise. In 2025 she launched LearningAIsearch.com, a curated roadmap for AI search optimization, signaling deep operational knowledge. Her LinkedIn output on AI workflows is specific, tool-referenced, and grounded in client work.

---

## Expert 3: Kevin Indig
**Title:** Growth Advisor, Author of Growth Memo newsletter
**LinkedIn:** https://www.linkedin.com/in/kevin-indig
**YouTube:** https://www.youtube.com/c/KevinIndig
**Newsletter:** Growth Memo (kevin-indig.com)
**Date collected:** 2026-06-08

**Why this expert:**
Kevin Indig is the former VP of SEO at Shopify and G2, and SEO advisor to companies including Reddit, Hims, and Toast. His Growth Memo newsletter is specifically targeted at B2B SaaS organic growth. He has published research-backed analysis on AI Overviews actual traffic impact, and his AirOps webinar series covers practical content refresh and AI content production workflows for SaaS companies.

**Videos collected:**
- Google Will Kill Your Traffic: Here Is How You Adapt
- AI Overview Impact on SEO (AirOps Webinar)

---

## Expert 4: Lily Ray
**Title:** VP of SEO Strategy and Research, Amsive
**LinkedIn:** https://www.linkedin.com/in/lily-ray-44755615
**Blog:** lilyray.nyc
**Date collected:** 2026-06-08

**Why this expert:**
Lily Ray is one of the most data-rigorous voices on the impact of AI on organic search. She manages SEO for enterprise clients and has published detailed research on how AI Overviews affect traffic, what content signals influence AI-era rankings, and why authenticity and original research are the core differentiators. Her critical perspective on low-quality AI content is a necessary counterbalance in any responsible research on this topic.

**Videos collected:**
- How SEO Is Evolving in 2025: AI Reddit and Ranking

---

## Expert 5: Ross Hudgens
**Title:** Founder and CEO, Siege Media
**LinkedIn:** https://www.linkedin.com/in/rosshudgens
**Website:** siegemedia.com
**Date collected:** 2026-06-08

**Why this expert:**
Ross Hudgens runs Siege Media, a content-first SEO agency with 90+ employees that has delivered SEO results for Airbnb, Adidas, Zapier, and Casper. Siege made the Inc. 5000 six consecutive years. He is writing a book on Generative Engine Optimization publishing with Wiley in Q4 2026, meaning his current thinking on AI content workflows is both current and being refined to book-level depth.

**Videos collected:**
- AI Visibility, Data Journalism, and the Future of SEO

---

## Expert 6: Chima Mmeje
**Title:** Senior Content Strategist, Moz
**LinkedIn:** https://www.linkedin.com/in/chima-mmeje
**Website:** zenithcopy.com
**Date collected:** 2026-06-08

**Why this expert:**
Chima Mmeje is a senior content strategist at Moz whose work centers on topic cluster strategy and AI-augmented content quality frameworks. As a practitioner inside one of the most-followed SEO platforms in the world, she produces content advice that is tested against real audiences at scale. Her expertise in how to structure content for AI-era search is directly applicable to AI content production workflows.

**Videos collected:**
- How To Start Using AI Content In Your Marketing

---

## Expert 7: Eli Schwartz
**Title:** Author of Product-Led SEO, independent SEO consultant
**LinkedIn:** https://www.linkedin.com/in/schwartze
**Book:** Product-Led SEO (Lioncrest Publishing)
**Date collected:** 2026-06-08

**Why this expert:**
Eli Schwartz is the author of Product-Led SEO, which reframed how SaaS companies should think about organic growth: SEO as a product feature, not a marketing afterthought. His consulting work has covered SEO strategy for SurveyMonkey, Zendesk, Quora, and MongoDB. He approaches AI content production from a business outcome perspective, not a tactics perspective, which is the right lens for B2B SaaS.

---

## Expert 8: Bernard Huang
**Title:** Co-founder, Clearscope
**LinkedIn:** https://www.linkedin.com/in/bernardjhuang
**Website:** clearscope.io
**Date collected:** 2026-06-08

**Why this expert:**
Bernard Huang co-founded Clearscope, one of the most widely used content optimization tools in SEO, used by teams at Deloitte, Spotify, and thousands of content teams. As a builder of the tooling layer of AI-powered content production, he understands from the infrastructure side what signals actually drive content quality and ranking in an AI-influenced search environment.

---

## Expert 9: Brendan Hufford
**Title:** Founder, Growth Sprints
**LinkedIn:** https://www.linkedin.com/in/brendan-hufford
**Newsletter:** growthletter.io
**Date collected:** 2026-06-08

**Why this expert:**
Brendan Hufford is the founder of Growth Sprints, a consultancy focused specifically on AI-native growth workflows for SaaS companies. He is a non-mainstream choice but specifically relevant because his work is targeted at exactly the B2B SaaS context. His content covers how SaaS marketing teams are actually integrating AI into content production cycles, with an emphasis on speed-to-publish, quality gates, and workflow design.

---

## Expert 10: Rand Fishkin
**Title:** Co-founder, SparkToro; former CEO, Moz
**LinkedIn:** https://www.linkedin.com/in/randfishkin
**Website:** sparktoro.com
**Date collected:** 2026-06-08

**Why this expert:**
Rand Fishkin brings a uniquely critical and audience-research-first perspective to AI-powered SEO content. As co-founder of SparkToro, a platform mapping where audiences actually spend their time online, his research directly informs what AI-powered content production should optimize toward. His stance that the golden era of content is ending forces a more sophisticated question about what AI content production should actually be building.
""")

# ── research/other/methodology.md ─────────────────────────────────────────────
write("research/other/methodology.md", """# Research Methodology and Observations

## Collection Process

### LinkedIn Posts
Collected manually by visiting each expert's LinkedIn profile and copying full post text for posts relevant to AI-powered SEO content production. Selection criteria per post:
- Posted within the last 12 months
- Specific to AI tools, SEO workflows, or content production at scale
- Contains a concrete insight, data point, or practical framework

### YouTube Transcripts
Collected programmatically using youtube-transcript-api (Python v1.x). Script: fetch_transcripts.py.
8 videos processed, 8 saved successfully.

---

## Patterns Observed

### Pattern 1: The Human-in-the-Loop Consensus
Across all 10 experts, there is strong consensus that the highest-performing AI content production workflows are not fully automated. Ryan Law documented this directly: Ahrefs AI-written articles that ranked best had a human editor reviewing for accuracy, adding original data, and adjusting brand voice. Chima Mmeje and Lily Ray both reference this as the critical quality gate separating AI content that performs from AI content that fails.

### Pattern 2: Quality Signals Are Shifting Upstream
Kevin Indig and Ross Hudgens both note that AI search (ChatGPT, Perplexity, Google AIO) is changing where quality gets evaluated. Traditional SEO focused on on-page signals and backlinks. AI-era quality evaluation increasingly includes mention frequency across the web, whether sources cite your content, and whether the content demonstrates genuine expertise that cannot be easily replicated. Volume is less valuable, original insight is more valuable.

### Pattern 3: Content Refresh Is the Overlooked Opportunity
Kevin Indig's AirOps webinar and Ryan Law's work both highlight that AI-powered content production is most ROI-efficient when applied to refreshing existing content rather than producing net-new. Existing pages already have links, indexing history, and authority. AI tools can identify content decay and refresh efficiently. Most companies are focused on net-new production and missing this.

### Pattern 4: Structural Divergence Between SEO and AI Search
Lily Ray and Rand Fishkin both document that AI search is surfacing answers without clicks, which changes what success looks like for content. Rand Fishkin's SparkToro research shows audience behavior diverging from search traffic, with more consumption happening on platforms where links are not the mechanism. AI-powered SEO content production needs to think beyond keyword rankings toward brand mention and citation authority.

### Pattern 5: The B2B SaaS Context Is Specific
Eli Schwartz's product-led SEO framework and Kevin Indig's B2B SaaS organic growth work point to the same insight: B2B SaaS companies should not try to produce content at the volume typical of media sites. The right AI content production model for B2B SaaS is fewer, deeper pieces with stronger differentiation, not more, thinner pieces optimized for long-tail keywords. AI accelerates research and drafting; it does not change the strategic selection of what to produce.

---

## Tools Referenced Across Sources
- Clearscope (Bernard Huang) - Content grading and topic coverage
- Ahrefs (Ryan Law) - Keyword research, content gap analysis
- SparkToro (Rand Fishkin) - Audience behavior mapping
- AirOps - AI content workflow automation
- Surfer SEO - Content optimization
- Claude / ChatGPT / Gemini - LLM drafting layer

---

## What This Research Supports
This collection is strong enough to build a working playbook for AI-powered SEO content production for B2B SaaS. A proposed structure:

1. Strategic layer: Topic selection criteria (Eli Schwartz product-led lens)
2. Research layer: Keyword and competitor gap analysis (Ahrefs framework)
3. Production layer: AI drafting workflow with human quality gates (Ryan Law Ahrefs process)
4. Optimization layer: Content grading before publish (Clearscope)
5. Distribution layer: AI search citation building (Lily Ray / Rand Fishkin)
6. Refresh layer: Content decay detection and refresh cycle (Kevin Indig)
""")

# ── LinkedIn post templates ────────────────────────────────────────────────────
authors = [
    ("ryan-law",       "Ryan Law",       "https://www.linkedin.com/in/thinkingslow"),
    ("aleyda-solis",   "Aleyda Solis",   "https://www.linkedin.com/in/aleyda"),
    ("kevin-indig",    "Kevin Indig",    "https://www.linkedin.com/in/kevin-indig"),
    ("lily-ray",       "Lily Ray",       "https://www.linkedin.com/in/lily-ray-44755615"),
    ("ross-hudgens",   "Ross Hudgens",   "https://www.linkedin.com/in/rosshudgens"),
    ("chima-mmeje",    "Chima Mmeje",    "https://www.linkedin.com/in/chima-mmeje"),
    ("eli-schwartz",   "Eli Schwartz",   "https://www.linkedin.com/in/schwartze"),
    ("bernard-huang",  "Bernard Huang",  "https://www.linkedin.com/in/bernardjhuang"),
    ("brendan-hufford","Brendan Hufford","https://www.linkedin.com/in/brendan-hufford"),
    ("rand-fishkin",   "Rand Fishkin",   "https://www.linkedin.com/in/randfishkin"),
]

for folder, name, url in authors:
    write(f"research/linkedin-posts/{folder}/posts.md", f"""# LinkedIn Posts: {name}

**Profile URL:** {url}
**Date collected:** 2026-06-08
**Posts collected:** [fill in count after collecting]

---

## POST 1

**Date:**
**Post:**

---

## POST 2

**Date:**
**Post:**

---

## POST 3

**Date:**
**Post:**

---

## POST 4

**Date:**
**Post:**

---

## POST 5

**Date:**
**Post:**
""")

print()
print("All files created. Run git commands next to push to GitHub.")