import os, glob, re

os.chdir(os.path.expanduser("~/GitHub"))
m = glob.glob("ag*")
if not m: print("ERROR"); exit(1)
os.chdir(m[0])

# 1. FIX MONOGRAM PATH
mono_assets = os.path.exists("assets/ag-monogram.svg")
mono_root = os.path.exists("ag-monogram.svg")
print(f"Monogram in assets/: {mono_assets}, root: {mono_root}")

with open("index.html", "r") as f:
    html = f.read()

if mono_assets and 'src="ag-monogram' in html:
    html = html.replace('src="ag-monogram', 'src="assets/ag-monogram')
    print("Fixed: HTML now points to assets/ag-monogram")
elif not mono_assets and mono_root and 'src="assets/ag-monogram' in html:
    html = html.replace('src="assets/ag-monogram', 'src="ag-monogram')
    print("Fixed: HTML now points to root ag-monogram")
elif mono_assets:
    print("Monogram path looks OK (in assets/)")
elif mono_root:
    print("Monogram path looks OK (in root)")
else:
    print("ERROR: No monogram found!")

# 2. JSON-LD
jsonld_block = '<script type="application/ld+json">\n'
jsonld_block += '{\n'
jsonld_block += '  "@context": "https://schema.org",\n'
jsonld_block += '  "@graph": [\n'
jsonld_block += '    {\n'
jsonld_block += '      "@type": "Organization",\n'
jsonld_block += '      "@id": "https://autonomousgrowth.ai/#organization",\n'
jsonld_block += '      "name": "Autonomous Growth",\n'
jsonld_block += '      "url": "https://autonomousgrowth.ai",\n'
jsonld_block += '      "logo": "https://autonomousgrowth.ai/assets/ag-monogram.svg",\n'
jsonld_block += '      "description": "AI visibility and content systems partner for B2B SaaS companies. We build content and visibility systems that help B2B SaaS companies get found, recommended, and chosen in the AI era.",\n'
jsonld_block += '      "sameAs": ["https://www.linkedin.com/company/autonomousgrowth/"],\n'
jsonld_block += '      "knowsAbout": ["AI visibility","Answer Engine Optimization","AEO","B2B SaaS content strategy","Content systems","AI search optimization","LLM citation optimization","Structured data for AI","B2B SaaS growth","Content operations","Executive visibility"],\n'
jsonld_block += '      "areaServed": "Worldwide",\n'
jsonld_block += '      "priceRange": "$$$$"\n'
jsonld_block += '    },\n'
jsonld_block += '    {\n'
jsonld_block += '      "@type": "WebSite",\n'
jsonld_block += '      "@id": "https://autonomousgrowth.ai/#website",\n'
jsonld_block += '      "name": "Autonomous Growth",\n'
jsonld_block += '      "url": "https://autonomousgrowth.ai",\n'
jsonld_block += '      "publisher": {"@id": "https://autonomousgrowth.ai/#organization"},\n'
jsonld_block += '      "description": "Content and visibility systems that compound for B2B SaaS"\n'
jsonld_block += '    },\n'
jsonld_block += '    {\n'
jsonld_block += '      "@type": "ProfessionalService",\n'
jsonld_block += '      "@id": "https://autonomousgrowth.ai/#service",\n'
jsonld_block += '      "name": "Autonomous Growth",\n'
jsonld_block += '      "provider": {"@id": "https://autonomousgrowth.ai/#organization"},\n'
jsonld_block += '      "serviceType": "AI Visibility and Content Systems",\n'
jsonld_block += '      "description": "We help B2B SaaS teams build the systems that get them discovered and recommended where buyers are actually making decisions.",\n'
jsonld_block += '      "hasOfferCatalog": {\n'
jsonld_block += '        "@type": "OfferCatalog",\n'
jsonld_block += '        "name": "Engagement Options",\n'
jsonld_block += '        "itemListElement": [\n'
jsonld_block += '          {"@type":"Offer","name":"Visibility Sprint","description":"A focused 21-day engagement to assess AI and search visibility.","price":"3495","priceCurrency":"EUR"},\n'
jsonld_block += '          {"@type":"Offer","name":"Growth System","description":"Compounding content and visibility engine.","priceSpecification":{"@type":"UnitPriceSpecification","price":"4950","priceCurrency":"EUR","unitText":"month"}},\n'
jsonld_block += '          {"@type":"Offer","name":"Embedded Growth","description":"Deeper integration with dedicated resource allocation."}\n'
jsonld_block += '        ]\n'
jsonld_block += '      }\n'
jsonld_block += '    },\n'
jsonld_block += '    {\n'
jsonld_block += '      "@type": "FAQPage",\n'
jsonld_block += '      "@id": "https://autonomousgrowth.ai/#faq",\n'
jsonld_block += '      "mainEntity": [\n'
jsonld_block += '        {"@type":"Question","name":"What is AI visibility for B2B SaaS?","acceptedAnswer":{"@type":"Answer","text":"AI visibility is how well your brand, product, and content appear in AI-powered discovery channels like ChatGPT, Gemini, Claude, Perplexity, and other AI search and recommendation systems. As more B2B buyers use AI tools to research and shortlist software, the companies that show up in these AI-generated answers gain a significant competitive advantage."}},\n'
jsonld_block += '        {"@type":"Question","name":"What is Answer Engine Optimization (AEO)?","acceptedAnswer":{"@type":"Answer","text":"Answer Engine Optimization (AEO) is the practice of optimizing your content and digital presence so that AI systems like ChatGPT, Gemini, Perplexity, and Google AI Overviews can accurately find, understand, and cite your brand when users ask relevant questions. Unlike traditional SEO which focuses on ranking in search results, AEO focuses on being the answer that AI systems recommend."}},\n'
jsonld_block += '        {"@type":"Question","name":"Who does Autonomous Growth work with?","acceptedAnswer":{"@type":"Answer","text":"Autonomous Growth works with scaling B2B SaaS companies, typically Series B through Series D, who need to build sustainable content and visibility systems. Our primary clients are led by Heads of Content, VPs of Marketing, and marketing leaders at venture-backed technology companies."}},\n'
jsonld_block += '        {"@type":"Question","name":"How is Autonomous Growth different from an SEO agency?","acceptedAnswer":{"@type":"Answer","text":"Autonomous Growth is not an SEO agency. We are an AI visibility and content systems partner. We build systems that ensure your brand is discovered and recommended across AI search engines, LLM-powered recommendations, traditional search, and high-intent research workflows."}},\n'
jsonld_block += '        {"@type":"Question","name":"What does the Visibility Sprint include?","acceptedAnswer":{"@type":"Answer","text":"The Visibility Sprint is a focused 21-day engagement including an AI visibility audit across ChatGPT, Claude, Perplexity, and Google AI Overviews, content system assessment, competitive visibility analysis, answer modeling and entity mapping, gap analysis, and a prioritized 30-day action plan. It costs EUR 3,495 as a one-off engagement."}},\n'
jsonld_block += '        {"@type":"Question","name":"What is a content system?","acceptedAnswer":{"@type":"Answer","text":"A content system is an integrated set of processes, workflows, and infrastructure that allows a B2B SaaS company to consistently produce, optimize, and distribute content that compounds over time. Unlike ad-hoc content production, a content system builds lasting visibility across both traditional search and AI discovery channels."}}\n'
jsonld_block += '      ]\n'
jsonld_block += '    }\n'
jsonld_block += '  ]\n'
jsonld_block += '}\n'
jsonld_block += '</script>\n'

if "application/ld+json" not in html:
    html = html.replace("</head>", jsonld_block + "</head>")
    print("Added JSON-LD schema with Organization, Service, and FAQs")
else:
    print("JSON-LD already present")

with open("index.html", "w") as f:
    f.write(html)

# 3. SITEMAP
sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n'
sitemap += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
sitemap += '  <url>\n'
sitemap += '    <loc>https://autonomousgrowth.ai/</loc>\n'
sitemap += '    <changefreq>weekly</changefreq>\n'
sitemap += '    <priority>1.0</priority>\n'
sitemap += '  </url>\n'
sitemap += '</urlset>\n'
with open("sitemap.xml", "w") as f:
    f.write(sitemap)
print("Created sitemap.xml")

# 4. ROBOTS.TXT
robots = "User-agent: *\nAllow: /\nSitemap: https://autonomousgrowth.ai/sitemap.xml\n\n"
robots += "User-agent: GPTBot\nAllow: /\n\n"
robots += "User-agent: ChatGPT-User\nAllow: /\n\n"
robots += "User-agent: Google-Extended\nAllow: /\n\n"
robots += "User-agent: ClaudeBot\nAllow: /\n\n"
robots += "User-agent: PerplexityBot\nAllow: /\n\n"
robots += "User-agent: Applebot-Extended\nAllow: /\n"
with open("robots.txt", "w") as f:
    f.write(robots)
print("Created robots.txt (AI-friendly)")

# 5. LLMS.TXT
llms = "# Autonomous Growth\n\n"
llms += "> AI visibility and content systems partner for B2B SaaS. We build content and visibility systems that help B2B SaaS companies get found, recommended, and chosen in the AI era.\n\n"
llms += "Autonomous Growth helps scaling B2B SaaS companies (Series B through D) build durable content and visibility systems. We operate at the intersection of content strategy, AI search optimization (AEO), and systematic growth.\n\n"
llms += "Our buyers are typically Heads of Content, VPs of Marketing, and marketing leaders at venture-backed technology companies who need systems that compound rather than campaigns that expire.\n\n"
llms += "## What We Do\n\n"
llms += "- [Homepage](https://autonomousgrowth.ai/): Main site with positioning, services, and pricing\n"
llms += "- [Book a Call](https://calendar.google.com/calendar/appointments/schedules/AcZssZ3KRzBx-3jqwqCvSJIZaa9-cYLSKNVIgiRJNJzVREsaXpHnuAzo4vR979NyED0Jrs0bhc2fBepQ): Schedule a conversation about AI visibility and content systems\n\n"
llms += "## Services\n\n"
llms += "**Visibility Sprint** (EUR 3,495, one-off, 21 days): AI visibility audit across ChatGPT, Claude, Perplexity, and Google AI Overviews. Content system assessment, competitive visibility analysis, answer modeling and entity mapping, gap analysis, and a prioritized 30-day action plan.\n\n"
llms += "**Growth System** (from EUR 4,950/month): Compounding content and visibility engine including content and AI visibility strategy, editorial planning, SEO and AEO-optimized content production, structured data and schema for LLMs, content system design, AI-assisted production workflows, distribution cadence management, visibility tracking, and monthly strategy reviews.\n\n"
llms += "**Embedded Growth** (custom, scoped to needs): For teams needing deeper integration with embedded content operations, custom workflow and automation builds, executive and expert visibility systems, expanded content production, narrative and brand story management, and weekly strategy reviews.\n\n"
llms += "## Core Expertise\n\n"
llms += "- AI visibility and Answer Engine Optimization (AEO)\n"
llms += "- Content systems for B2B SaaS\n"
llms += "- LLM citation optimization\n"
llms += "- Structured data and schema for AI discovery\n"
llms += "- Editorial workflow design\n"
llms += "- AI-assisted content operations\n"
llms += "- Executive visibility systems\n"
llms += "- Competitive visibility analysis\n\n"
llms += "## Key Facts\n\n"
llms += "- Focus: B2B SaaS companies, Series B through D\n"
llms += "- Contracts: Month-to-month, no lock-in\n"
llms += "- Approach: Systems-led, not campaign-based\n"
llms += "- Category: AI visibility and content systems partner\n"
llms += "- Website: https://autonomousgrowth.ai\n"
llms += "- LinkedIn: https://www.linkedin.com/company/autonomousgrowth/\n\n"
llms += "## Optional\n\n"
llms += "- [LinkedIn Company Page](https://www.linkedin.com/company/autonomousgrowth/): Company updates and thought leadership\n"
with open("llms.txt", "w") as f:
    f.write(llms)
print("Created llms.txt")

print("\nAll done. Ready to commit.")
