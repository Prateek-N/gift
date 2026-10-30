# Script to ensure every role has >= 4 high-quality cross questions and regenerate data/roles.json and data/roles-data.js
import json

with open('data/roles.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

extra_cqs = {
    "data-scientist": {
        "q": "Do I need experience with Big Data tools like Spark or Hadoop for entry/mid roles?",
        "a": "For entry to mid-level roles, strong Python (Pandas/NumPy/scikit-learn) and advanced SQL are the core essentials; distributed big data tools like Spark or Databricks are usually valued bonuses or required for senior roles. We position your resume highlighting data analysis and measurable modeling impact."
    },
    "cybersecurity-analyst": {
        "q": "Can I get hired remotely as a cybersecurity analyst?",
        "a": "Yes, many Security Operations Centers (SOC) and threat analysis teams operate remote or hybrid monitoring shifts. However, roles involving classified government data or physical hardware usually require on-site presence. We target roles matching your work preferences."
    },
    "cloud-engineer": {
        "q": "Should I learn multi-cloud (AWS + Azure + GCP) right away?",
        "a": "It is much better to go deep in one primary cloud first (AWS or Azure) and earn an associate certification. Once you understand core architecture concepts, learning how other providers map those same services is much faster, and employers prefer deep mastery in their specific stack."
    },
    "devops-engineer": {
        "q": "How much application programming (Java/Python) do I need to know?",
        "a": "DevOps engineers don't usually write commercial application features from scratch; you need solid scripting skills (Python, Bash) to automate CI/CD pipelines, write test harnesses, and manage Infrastructure as Code (Terraform). We highlight your automation scripts prominently."
    },
    "software-developer": {
        "q": "Is full-stack better than specializing in just front-end or back-end?",
        "a": "Both paths have strong market demand. Early-stage companies and startups love full-stack developers for speed and versatility, while larger enterprises often hire specialized back-end (Java/Spring Boot, C#/.NET) or front-end (React) engineers. We market you toward whichever side your portfolio demonstrates best."
    },
    "prompt-engineer": {
        "q": "Will Prompt Engineering become obsolete as AI models improve?",
        "a": "The role is maturing into AI Systems and LLM Engineering — combining prompt optimization with Python APIs, evaluation frameworks, and RAG pipelines. Candidates who combine prompt design with coding and data retrieval skills have strong long-term career demand."
    },
    "civil-engineer": {
        "q": "How important is 3D BIM / Revit compared to traditional 2D AutoCAD?",
        "a": "2D AutoCAD remains standard for site planning and municipal permit drawings, but Revit and 3D BIM are increasingly required for commercial buildings and multi-disciplinary coordination. Highlighting any BIM modeling experience gives your profile a competitive edge."
    },
    "construction-manager": {
        "q": "Can I transition from a field superintendent or project engineer into construction management?",
        "a": "Yes, direct site and field experience is highly respected by General Contractors because you understand subcontractor coordination, real job site logistics, and OSHA safety standards. We highlight your completed project values ($), safety record, and scheduling software skills."
    },
    "mechanical-engineer": {
        "q": "Do I need simulation and FEA experience to get a product design role?",
        "a": "Core 3D CAD modeling (SolidWorks/Creo) and GD&T are the primary requirements for design engineers; FEA (ANSYS) is a major asset for specialized structural or thermal roles. We highlight whatever practical simulation and prototype testing you have done."
    },
    "electrical-engineer": {
        "q": "Is PLC automation or power systems analysis more in demand?",
        "a": "Both areas have high demand in different sectors: power distribution (ETAP, substations) is booming with utilities, renewable energy, and data center growth; PLC/controls automation (Rockwell, Siemens) is in high demand across manufacturing and robotics. We target the sector aligned with your background."
    },
    "process-engineer": {
        "q": "What industries pay the highest compensation for Process Engineers?",
        "a": "Pharmaceuticals, biotechnology, oil & gas, and semiconductor fabrication typically offer the highest compensation because their processes involve tight tolerances, expensive raw materials, and strict regulatory standards."
    },
    "validation-engineer": {
        "q": "Can I transition from general laboratory QA into Validation Engineering?",
        "a": "Yes, laboratory QA gives you strong grounding in GMP and documentation standards. Transitioning to validation involves executing equipment qualification protocols (IQ/OQ/PQ) or Computer System Validation (CSV), and we highlight your regulatory documentation skills to make this shift."
    },
    "digital-marketing-specialist": {
        "q": "Should I focus on B2B or B2C digital marketing?",
        "a": "Both are in demand. B2C emphasizes high-volume social advertising (Meta, TikTok), creative campaigns, and immediate e-commerce conversions; B2B focuses on Google Search, LinkedIn Ads, long sales funnels, and lead generation (MQLs). We highlight the audience type you have worked with."
    },
    "marketing-manager": {
        "q": "How do I demonstrate marketing ROI if I don't directly close deals?",
        "a": "We emphasize leading pipeline indicators on your resume: Marketing Qualified Leads (MQLs) generated, conversion rates, Customer Acquisition Cost (CAC) reduction, and overall sales pipeline contribution, proving to executive leadership that your campaigns fueled revenue."
    },
    "product-manager": {
        "q": "Do I need an engineering degree to become a Product Manager?",
        "a": "Not for general product roles. While Technical Product Managers (TPMs) often have engineering backgrounds, core product management prioritizes customer empathy, clear problem definition, prioritization frameworks (like RICE), and cross-functional leadership."
    },
    "supply-chain-analyst": {
        "q": "Is Python or R necessary for a Supply Chain Analyst?",
        "a": "Advanced Excel (lookups, pivot tables) and SQL are the non-negotiable fundamentals for 90% of roles. Python is an increasingly attractive bonus for automating demand forecasting and complex inventory optimization. We emphasize your quantitative toolset."
    }
}

for role in data['roles']:
    rid = role['id']
    if rid in extra_cqs:
        # Check if already added
        exists = any(cq['q'] == extra_cqs[rid]['q'] for cq in role['crossQuestions'])
        if not exists:
            role['crossQuestions'].append(extra_cqs[rid])

print("Updated cross-questions counts:")
for role in data['roles']:
    print(f"- {role['name']}: {len(role['crossQuestions'])} cross-questions")

# Save updated files
with open('data/roles.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

with open('data/roles-data.js', 'w', encoding='utf-8') as f:
    f.write('/** Auto-generated from PRD baseline content */\n')
    f.write('window.ROLES_DATA = ')
    json.dump(data, f, indent=2, ensure_ascii=False)
    f.write(';\n')

print("Saved updated data files successfully!")

