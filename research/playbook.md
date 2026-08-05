# AI-Powered SEO Content Production: A Practical Playbook for B2B SaaS

**Author:** Victor James Fermo
**Based on:** 10 practitioners, 8 YouTube transcripts, 30+ LinkedIn posts collected June 2026
**Last updated:** June 2026

---

## Overview

This playbook answers one question: how does a B2B SaaS company use AI to produce SEO content that actually performs in 2026?

It is not a summary of what experts say. It is a framework built from their work, filtered through my own judgment, with the parts I disagreed with flagged explicitly.

The core thesis, borrowed from Eli Schwartz and updated for the AI era: stop treating SEO as a content problem. It is a strategy and product problem. AI accelerates the production layer. It does not fix weak strategy.

---

## The Six-Phase Framework

### Phase 1: Strategic Selection

Before writing a single word, determine whether a topic is worth producing at all.

**Step 1.1: Run the pre-mortem prompt test.**
For any candidate topic, manually run the target prompt through ChatGPT, Perplexity, and Gemini. Document who gets cited and whether brands appear at all. If no brand achieves more than 20% mention rate, the AI is likely treating the prompt as educational rather than a brand recommendation query. This is a prompt intent problem, not a content quality problem. Adjust the angle before writing, not after.
(source: adapted from Bernard Huang, linkedin.com/in/bernardjhuang, May 2026)

**Step 1.2: Apply the 50% brand visibility threshold for TOFU topics.**
If a top-of-funnel topic returns brand recommendations in AI results, it is worth pursuing only if you can realistically achieve 50%+ brand visibility on that prompt. HubSpot achieves 83% for "what is CRM." Use competitor visibility as your benchmark before commissioning content.
(source: Ross Hudgens, linkedin.com/in/rosshudgens, May 2026)

**Step 1.3: Prioritize "X vs Y" comparison pages for transactional intent.**
A B2B GEO study across 116 sites and 1,112 pages found that versus content had a Spearman correlation of 0.65 with AI search referrals, roughly 2x the next-best content type. The first 20 comparison pages correspond to a 350% median lift in AI search sessions. Build these before anything else.
(source: Ross Hudgens, linkedin.com/in/rosshudgens, June 2026)

**Step 1.4: Reject generic TOFU.**
AI has claimed the awareness layer for most educational queries. Focus on transactional intent where your product IS the answer. Content that talks about your product category is less valuable than content that demonstrates your product solving the query.
(source: Eli Schwartz, linkedin.com/in/schwartze, CapitalG playbook, May 2026)

---

### Phase 2: Prompt Validation

**Step 2.1: Check fan-out query frequency before committing.**
Run target prompts through a prompt tracking tool (Clearscope Prompt Tracking, Profound, or manually via ChatGPT with web search enabled). Fan-out queries appearing at above 30% frequency are stable signals worth building content against. Queries below 15% are too variable. The same prompt may generate completely different sub-queries next week; content built against unstable signals is content that may never get cited reliably.
(source: Bernard Huang, linkedin.com/in/bernardjhuang, May 2026)

**Step 2.2: Map sub-query coverage before drafting.**
Under high AI reasoning, a single comparison query can break into separate retrievals for API rate limits, compliance certifications, pricing tiers, integration support, and more. The brand that wins is the one whose documentation surfaces clearly for each sub-query. Map these before writing, then verify your draft covers them.
(source: Kevin Indig, linkedin.com/in/kevinindig, June 2026)

---

### Phase 3: Production

**Step 3.1: Use a structured pipeline, not open-ended prompting.**
The Ahrefs content team built an 11-stage AI pipeline: keyword input, brief generation, outline, draft, product mention insertion, topic gap analysis, approve/reject interface, internal linking suggestions, and performance reporting. Each stage has a defined input and output. Open-ended prompting is not a production system.
(source: Ryan Law, linkedin.com/in/thinkingslow, June 2026; https://www.youtube.com/watch?v=D7LBx8RFOcQ)

**Step 3.2: Integrate AI into your existing toolstack via Claude Code and MCP.**
Ryan Law's team built their content automation system using Claude Code, 23 custom skill files, and the Ahrefs MCP. The pattern is replicable: identify the tools your workflow already uses, connect them through MCP, and let Claude Code orchestrate the pipeline. You do not need to rebuild your toolstack; you need to connect it.
(source: Ryan Law, linkedin.com/in/thinkingslow, June 2026; https://www.youtube.com/watch?v=iVZrVeESnFQ)

**Step 3.3: Train the LLM on your brand voice before drafting.**
Before using AI for any branded content: provide writing examples, a style guide, write in sections rather than asking for complete drafts, share your revised copy so the model learns from corrections, and explicitly tell it what mistakes it is making. The goal is output that reflects your brand voice, not the averaged voice of the internet.
(source: Chima Mmeje, linkedin.com/in/chima-mmeje, May 2026; https://www.youtube.com/watch?v=wLjTTlG3oNk)

**Step 3.4: Human editing is not optional.**
The Ahrefs AI content experiment found that articles which ranked best had a human editor reviewing for factual accuracy, adding original data or examples, and adjusting brand voice. This is the quality gate. Removing it is the difference between AI content that performs and AI content that does not.
(source: Ryan Law, https://www.youtube.com/watch?v=D7LBx8RFOcQ)

---

### Phase 4: Pre-Publish Optimization

**Step 4.1: Grade content against topic coverage tools before publishing.**
Verify the content covers the topic comprehensively relative to what AI systems expect. Clearscope and Surfer SEO are purpose-built for this. A piece that passes keyword intent but misses topic depth will underperform in AI-mediated search.
(source: Bernard Huang, linkedin.com/in/bernardjhuang)

**Step 4.2: Write meta descriptions for two impressions.**
On AIO SERPs, 47.5% of scrolling goes backward. The median user who reverses direction spends nearly half their total scroll going back up the page. Your title and meta description will get a second impression. Write the first hook for trust on the way down. Write the second hook for specificity or a data point on the way back up.
(source: Kevin Indig, linkedin.com/in/kevinindig, May 2026)

---

### Phase 5: Distribution and AI Citation Building

**Step 5.1: Stop using traffic as the primary KPI.**
AI search is surfacing answers without clicks. Traffic-as-KPI misses brand mention rate, citation frequency, and AI recommendation visibility. These are the metrics that matter in an AI-intermediated search environment. Three principles: stop using traffic as the main KPI for AI search impact, build topical authority with content that AI systems can retrieve and cite, and strengthen brand authority through third-party corroboration.
(source: Aleyda Solis, linkedin.com/in/aleyda, May 2026)

**Step 5.2: Track brand visibility across six AI platforms.**
ChatGPT, Perplexity, Gemini, Claude, Copilot, and Meta AI behave differently. A brand visible in ChatGPT may be invisible in Gemini. Track all six. Run your category prompts across each platform every 30 days. Profound is a purpose-built tool for this.
(source: Brendan Hufford, linkedin.com/in/brendanhufford, May 2026)

**Step 5.3: Build third-party corroboration deliberately.**
Reviews, comparisons, forum mentions, and third-party documentation shape AI answers. Owned content alone is insufficient. A systematic program of getting your brand mentioned in non-owned sources is now a content production input, not a separate PR function.
(source: Aleyda Solis, linkedin.com/in/aleyda; Eli Schwartz, linkedin.com/in/schwartze)

**Step 5.4: Do not destroy your SEO chasing GEO.**
Sites losing SEO visibility are also losing ChatGPT citation rates shortly after. The tactics being promoted for fast GEO gains, including inauthentic mentions and manipulation, are now catching manual actions from Google. SEO is the foundation. GEO is built on top of it, not instead of it.
(source: Lily Ray, linkedin.com/in/lily-ray-44755615, May 2026; https://www.youtube.com/watch?v=mgI1U7XPsUA)

---

### Phase 6: Refresh

**Step 6.1: Refresh before you create net-new.**
AI-powered content production delivers its best ROI when applied to existing content. Existing pages have indexing history, links, and authority. Use AI to identify content decay (outdated claims, topic gaps, missing product mentions) and refresh efficiently. This is the most underutilized phase in most content teams.
(source: Kevin Indig, linkedin.com/in/kevinindig; Ryan Law, linkedin.com/in/thinkingslow)

**Step 6.2: Automate the performance monitoring layer.**
Ryan Law's team built an automated monthly performance report that pulls GSC and Ahrefs Web Analytics into one view with KPIs, trends, and winner/loser tables, generated on the 2nd of each month. This is the signal layer that triggers the refresh cycle. Build this infrastructure before you need it.
(source: Ryan Law, linkedin.com/in/thinkingslow, June 2026)

---

## Where Experts Disagree

### Disagreement 1: Is TOFU content worth producing in the AI era?

**Eli Schwartz says no** (for most cases): AI has robbed TOFU. Generic top-of-funnel content is being summarized by AI without brand recommendations. The strategy should shift toward transactional intent, where your product IS the answer.
(source: linkedin.com/in/schwartze, May 2026)

**Ross Hudgens says yes** (under specific conditions): TOFU is back. Companies like HubSpot and Pipedrive appear in AI recommendations for TOFU queries like "what is CRM," with HubSpot achieving 83% brand visibility. The stress test is whether you can hit 50%+ brand visibility on the prompt.
(source: linkedin.com/in/rosshudgens, May 2026)

**My take:** Both are right, but about different types of TOFU. Eli is correct that generic educational TOFU, the kind that explains industry concepts without tying to your product, is not worth producing if AI summarizes it without recommending brands. Ross is correct that product-connected TOFU, where the query intent connects directly to your product's core category, can earn AI brand recommendations. The filter is this: does the answer to this query naturally require recommending a tool like yours? If yes, produce it. If no, skip it.

---

### Disagreement 2: How much content should a B2B SaaS company produce?

**Eli Schwartz argues for selective depth:** B2B SaaS should not try to produce at media-site volume. The winning teams are building fewer, deeper pieces tied directly to product utility. Quality beats volume in AI-mediated search.
(source: linkedin.com/in/schwartze)

**Ryan Law demonstrates production at scale:** The Ahrefs team built an 11-stage AI pipeline that generates full article drafts, automates monthly reporting, and monitors competitor content daily. Their content production volume is substantial.
(source: linkedin.com/in/thinkingslow, June 2026)

**My take:** Eli's framework is the correct strategy layer; Ryan's system is the correct execution layer. The mistake most teams make is running Ryan's production system without Eli's selection filter first. Volume without strategic selection produces a large library that AI summarizes without recommending your brand. The sequence matters: apply Eli's criteria to decide what to produce, then use Ryan's system to produce it efficiently.

---

### Disagreement 3: How central should human expertise be in the AI production process?

**Chima Mmeje argues for human-first:** "I have not seen a single AI automation or agent that has created copy I was impressed with." Full automation is a lie. AI cannot make you a better writer. Human expertise must remain central; use AI to create better, not to avoid the work of creating.
(source: linkedin.com/in/chima-mmeje, MozCon 2026)

**Ryan Law demonstrates more complete automation:** The Ahrefs pipeline has human editing as one stage in 11, not as the primary stage. The degree of AI automation in their workflow is higher than Chima's framework would accept.
(source: linkedin.com/in/thinkingslow, June 2026)

**My take:** The disagreement is about content type, not philosophy. For brand content, thought leadership, and conversion copy, Chima's human-first approach is correct. For informational SEO content at scale (product comparisons, category pages, topic cluster articles), Ryan's pipeline approach works when human editing is present. The error is applying Ryan's automation level to brand content, or applying Chima's caution to high-volume informational content production. Know which type of content you are producing before choosing your workflow.

---

## What I Rejected and Why

### Rejected 1: Optimizing content separately for each AI platform

Bernard Huang documented that Gemini, GPT, Perplexity, Grok, and Claude behave like five different search engines with different retrieval patterns and ranking behaviors.
(source: linkedin.com/in/bernardjhuang, May 2026)

The logical implication is to build platform-specific content optimization strategies. I rejected this for B2B SaaS teams operating at typical resource levels.

The overlap in what these systems reward, including topical authority, clear entity relationships, E-E-A-T signals, and comprehensive topic coverage, is large enough that a single well-executed strategy covers most of the ground. Platform-specific optimization is a level-three problem. Most teams have not yet solved level-one problems: consistent production, systematic tracking, and refresh cycles. Fragmenting effort across five platforms before the fundamentals are in place is a distraction that most teams cannot afford.

The right approach is to build the core strategy first, then use tracking data (from Profound or manual testing) to identify which platforms are underperforming and adjust specifically for those.

### Rejected 2: Chasing low-frequency fan-out queries as "less competitive" opportunities

Bernard Huang's fan-out frequency data (below 15% = noise) could be read as identifying less competitive territory worth targeting for fast traction. If AI has not settled on how to answer a prompt, maybe you can be the first to get cited.
(source: linkedin.com/in/bernardjhuang, May 2026)

I rejected this because the problem with low-frequency queries is not competition but instability. A query below 15% frequency may generate completely different sub-queries the next time AI runs it. Content built against an unstable signal may never be reliably retrieved, regardless of its quality. The investment-to-return ratio is poor.

Build against stable signals first (above 30% frequency). Revisit low-frequency opportunities only after the core playbook is producing measurable results and you have surplus capacity.

---

## My Original Ideas

### Idea 1: The Pre-Mortem Prompt Test as a commissioning gate

Every expert in this research uses some form of prompt tracking or AI visibility monitoring. Bernard Huang's Clearscope experiment, Brendan Hufford's category prompt testing, and Ross Hudgens' brand visibility stress test all measure prompt performance. But all of them are measurement tools applied after publishing or after strategy is set.

My original idea is to make the prompt test a pre-commissioning gate that happens before any content is briefed.

The process: before commissioning any piece of content, spend 30 minutes running the target prompt across ChatGPT, Perplexity, and Gemini. Document who gets cited, what content format gets cited, and whether the AI treats the query as educational or brand-recommendation intent. If no brand achieves more than 20% mention rate, the prompt is likely educational intent. Adjust the content angle before writing, not after. If competitors dominate, reverse-engineer their content structure before drafting.

Why it could work: the most common waste in content production is producing high-quality content that AI never recommends because the prompt intent was misread from the start. A 30-minute pre-mortem eliminates this before weeks of production effort are committed. The test costs nothing and can be done with free tools. The return is avoiding the most expensive mistake in AI-era content production: building the right content for the wrong prompt.

This is not explicitly in any of the 10 experts' work. Bernard Huang's methodology is the closest analogue, but he frames it as a tracking tool applied after publishing. Moving the test upstream to before content investment decisions is the original contribution here.

---

## Weaknesses of This Playbook

**1. The research base is practitioner opinion and observational data, not controlled experiments.**
Ross Hudgens' B2B GEO study across 116 sites is compelling but it is a correlation study, not a randomized experiment. The 0.65 Spearman correlation between versus pages and AI search referrals does not prove causation. Bernard Huang's 30% and 15% fan-out thresholds come from Clearscope's own data. These are strong signals, not proven laws.

**2. The playbook assumes existing domain authority and content infrastructure.**
The refresh layer assumes a content library already exists. Topical authority building assumes some existing brand presence. For a brand-new B2B SaaS company with no content history, the timelines implied here are much longer than the framework suggests.

**3. The AI search landscape is changing faster than this research can keep up.**
Bernard Huang's frequency thresholds, Kevin Indig's backward-scrolling data, and Brendan Hufford's buyer behavior numbers are from late 2025 to mid-2026. This playbook should be reviewed quarterly. Some recommendations may be outdated within six months.

**4. The distribution layer is underspecified.**
Third-party corroboration is cited as critical by both Aleyda Solis and Eli Schwartz, but this playbook does not specify how to build it. A systematic program for earning non-owned mentions (review platforms, industry comparisons, partner content) is its own project, not a checklist item.

**5. Tool costs are not addressed.**
Clearscope, Profound, AirOps, and Ahrefs are referenced throughout. The combined subscription cost for a full implementation is significant for early-stage SaaS companies. A zero-budget implementation is possible but slower and less measurable.

---

## Who I Would NOT Recommend Following for This Specific Topic

**Rand Fishkin** (SparkToro, linkedin.com/in/randfishkin)

I want to be precise about what this means and does not mean.

Rand Fishkin produces some of the most rigorous audience behavior data in marketing. His State of Search reports and SparkToro research are among the few sources in this space that cite actual clickstream data from tens of millions of devices rather than survey responses or single-platform analytics. His finding that ChatGPT is approximately 3% of desktop web search, not the 20%+ that went viral, is exactly the kind of skepticism this industry needs.
(source: linkedin.com/in/randfishkin, June 2026)

The problem is that his work is built for a different question than the one this playbook is answering.

Rand's core message is that the golden era of content-driven organic traffic is ending, that zero-click is winning, and that audience-building in non-search channels is the durable long-term strategy. This is probably true at the market level. But it is not actionable for a B2B SaaS marketing team that still needs to produce SEO content this quarter.

Following Rand as a strategic guide for AI-powered SEO content production leads to one of two failure modes. The first is paralysis: why produce content if the era is ending? The second is misdirection: building audience research programs instead of fixing the content production system. Neither is useful for a team that needs a workflow this week.

The other nine experts on this list, even where they disagree, are all pointing toward actionable production systems. Rand is pointing toward a different problem entirely.

Use Rand's data for calibration and to check whether industry narratives are supported by evidence. Do not use him as a guide for what to build.