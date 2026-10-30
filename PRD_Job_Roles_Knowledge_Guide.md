# PRD: Job Roles Knowledge Guide — Static Webpage for the Sales Team

| Field | Detail |
|---|---|
| Document type | Product Requirements Document (PRD) |
| Product | "Role Ready" — internal static knowledge website |
| Audience of this PRD | Sales leadership, content owner, web developer/designer |
| End users of the product | New sales executives who call job-seeking candidates (US & Canada market) |
| Version | 1.0 (Draft) |
| Date | 30 Oct 2026 |
| Status | Ready for review |

---

## 1. Overview

### 1.1 Background
Our company provides candidate marketing services: we help job seekers in the US and Canada market their profiles to employers and recruiters. Our sales team reaches out to candidates by phone, explains our services, and converts them into clients.

### 1.2 Problem statement
The sales team is new and does not yet understand the job roles our candidates are targeting. When a candidate asks a technical or career question ("Do you market Data Engineers too, or only Data Scientists?", "Which cloud certification should I put first on my resume?", "Is Prompt Engineering even a real job?"), the rep cannot answer confidently. This causes:

- Loss of credibility in the first 2–3 minutes of the call.
- Lower conversion rates, because candidates feel we "don't understand their field".
- Over-reliance on senior staff for basic questions.
- Inconsistent (and sometimes incorrect) information being given to candidates.

### 1.3 Proposed solution
A simple, fast, static website that works as a **quick-reference knowledge guide**. For each of the 17 job roles we support, it explains in plain English: what the role is, what the person does, the core technical terms, the tools and certifications, a skills roadmap (beginner → job-ready → senior), and ready-made answers to common candidate cross-questions. The site is designed to be read during onboarding and to be glanced at **during a live call**.

### 1.4 Goals
1. Every sales rep can explain each of the 17 roles in 30 seconds, in plain language.
2. Every rep can recognise and correctly use the top 8–10 technical terms for each role.
3. Every rep can answer the most common candidate cross-questions without escalating.
4. Reduce onboarding time for new reps on "domain knowledge" from weeks to days.
5. Give the whole team one consistent, approved source of truth.

### 1.5 Non-goals
- Not a technical training course; reps are not expected to become engineers.
- Not a CRM, dialer, or lead-management tool.
- Not a public, candidate-facing marketing website (v1 is internal only).
- No login system, database, or backend in v1.
- Not a source of legal or immigration advice (see Section 7.4).

### 1.6 Success metrics

| Metric | Target | How measured |
|---|---|---|
| Rep knowledge quiz score after onboarding | ≥ 80% average | Built-in self-quiz + manager-run quiz |
| Calls escalated to senior staff for role questions | −50% in 60 days | Sales manager tracking |
| Time to "call-ready" for a new rep | ≤ 5 working days | Onboarding checklist |
| Call-to-conversion rate | +10–15% in 90 days | CRM report |
| Page usage | Each rep opens the guide ≥ 3×/week in month 1 | Simple privacy-friendly analytics |

---

## 2. Users and use cases

### 2.1 Personas

**Persona A — "New Rep Neha" (primary).** Joined 2 weeks ago, non-technical background (commerce/BBA), good communicator. Needs simple definitions and confidence. Uses the guide heavily during onboarding and keeps it open in a browser tab during calls.

**Persona B — "Experienced Rep Arjun" (secondary).** 6+ months in sales, knows the tech roles but weak on engineering/construction roles. Uses search to jump straight to a role or term mid-call.

**Persona C — "Sales Manager / Trainer" (secondary).** Uses the guide to run training sessions, role-plays and quizzes. Needs a printable version and a clear structure.

### 2.2 Key use cases

| # | Use case | Requirement it drives |
|---|---|---|
| UC1 | Rep studies a role before starting calls for that segment | Full role pages with clear structure |
| UC2 | Candidate asks "What's the difference between X and Y?" during a live call | Search, "Quick Pitch" box at top, comparison table |
| UC3 | Candidate uses a term the rep doesn't know (e.g. "Kubernetes", "IQ/OQ/PQ") | Global glossary + search that covers terms |
| UC4 | Candidate asks what they should learn/certify next | Roadmap and certifications per role |
| UC5 | Candidate questions visa/work-authorisation or "guaranteed job" | Common FAQ + compliance guardrails |
| UC6 | Manager runs a training session | Print-friendly pages + self-quiz |

---

## 3. Scope, site structure and page template

### 3.1 Site map

```
Home (index)
├── How to use this guide (incl. "On a live call? Read this")
├── Role categories
│   ├── Tech & AI
│   │   ├── AI / Machine Learning Engineer
│   │   ├── Data Scientist
│   │   ├── Cybersecurity Analyst
│   │   ├── Cloud Engineer
│   │   ├── DevOps Engineer
│   │   ├── Software Developer
│   │   └── Prompt Engineer
│   ├── Engineering, Construction & Manufacturing
│   │   ├── Civil Engineer
│   │   ├── Construction Manager
│   │   ├── Mechanical Engineer
│   │   ├── Electrical Engineer
│   │   ├── Process Engineer
│   │   └── Validation Engineer
│   └── Business, Marketing & Operations
│       ├── Digital Marketing (Specialist/Executive)
│       ├── Marketing Manager
│       ├── Product Manager
│       └── Supply Chain Analyst
├── Compare roles (side-by-side table of commonly confused roles)
├── Glossary (A–Z, all terms across all roles)
├── US & Canada job-market basics (ATS, resume, work authorisation overview)
├── Handling cross-questions (call scripts + compliance do's and don'ts)
└── Self-quiz
```

### 3.2 Standard role-page template (every role page MUST follow this)

1. **Quick Pitch (30-second explanation)** — highlighted box at the top, 2–3 sentences a rep can almost read aloud.
2. **What they do day-to-day** — 4–6 bullet points.
3. **Common job titles / alternate names** — so the rep recognises the role when the candidate uses a different title.
4. **Key terms to know** — 8–10 terms, each with a one-line plain-English definition.
5. **Tools & technologies** — grouped list.
6. **Popular certifications** — what they are and who they suit.
7. **Skills roadmap** — three stages: *Foundation*, *Job-ready (entry/mid)*, *Advanced (senior)*.
8. **Typical background / education** — what degrees and prior roles usually lead here.
9. **Industries that hire** — where the jobs are.
10. **What employers look for on a resume** — keywords and proof points.
11. **Candidate cross-questions & suggested answers** — 4–6 Q&A pairs.
12. **Related roles** — links to neighbouring roles (and the Compare page).
13. **Salary range (US / CA)** — placeholder field; to be filled and dated by the content owner from official sources (see 8.3). Never hard-coded without a source and date.

Sections 4–6 below contain the **approved v1 content** for every role, in this template (sections 12–13 are generated by the site / content owner).

---

## 4. Content — Tech & AI roles

### 4.1 AI / Machine Learning Engineer

**Quick Pitch:** An ML Engineer builds systems that learn from data and make predictions or decisions — like fraud detection, recommendation engines ("customers also bought…"), or chatbots. They take models from experiments and turn them into reliable software running in production.

**Day-to-day**
- Collect and prepare data for training models.
- Train, test and improve machine learning / deep learning models.
- Deploy models into apps and APIs so real users can use them.
- Monitor model accuracy over time and retrain when performance drops.
- Increasingly: build applications on top of Large Language Models (LLMs) such as GPT, Claude, Llama.

**Alternate titles:** ML Engineer, AI Engineer, Deep Learning Engineer, MLOps Engineer, Applied Scientist, GenAI Engineer, NLP Engineer, Computer Vision Engineer.

**Key terms**
| Term | Plain-English meaning |
|---|---|
| Machine Learning (ML) | Software that learns patterns from data instead of being hand-coded with rules. |
| Model | The "trained brain" produced by learning from data. |
| Training / Inference | Training = teaching the model; inference = using it to make a prediction. |
| Supervised vs Unsupervised | Supervised learns from labelled examples; unsupervised finds patterns in unlabelled data. |
| Deep Learning / Neural Network | ML using layered networks loosely inspired by the brain; powers image, speech and language AI. |
| LLM | Large Language Model — AI trained on huge text data to understand and generate language. |
| NLP / Computer Vision | AI for text/language / AI for images and video. |
| RAG | Retrieval-Augmented Generation — giving an LLM access to company documents so it answers using them. |
| MLOps | DevOps practices applied to ML: deploying, versioning and monitoring models. |
| Fine-tuning | Further training an existing model on specific data to specialise it. |

**Tools & tech:** Python; PyTorch, TensorFlow, scikit-learn; Hugging Face; LangChain/LlamaIndex; MLflow, Kubeflow; Docker, Kubernetes; AWS SageMaker, Azure ML, Google Vertex AI; vector databases (Pinecone, FAISS); SQL.

**Certifications:** AWS Certified Machine Learning (Specialty/Engineer–Associate), Google Professional Machine Learning Engineer, Microsoft Azure AI Engineer Associate (AI-102), TensorFlow / DeepLearning.AI course certificates.

**Roadmap**
- *Foundation:* Python, statistics & probability, linear algebra basics, data handling (Pandas, NumPy), SQL.
- *Job-ready:* classic ML algorithms (regression, decision trees, clustering), scikit-learn, one deep learning framework (PyTorch), model evaluation, Git, building APIs (Flask/FastAPI), Docker, one cloud ML platform, 2–3 portfolio projects on GitHub.
- *Advanced:* LLMs, RAG, fine-tuning, MLOps pipelines, Kubernetes, distributed training, model monitoring, system design for ML.

**Background:** CS/IT, Data Science, Math, Statistics, Electronics; often moves up from Software Developer or Data Scientist.

**Industries:** Tech, finance/banking, healthcare, e-commerce, insurance, automotive, consulting.

**Resume keywords:** Python, PyTorch/TensorFlow, model deployment, MLOps, LLM, RAG, AWS/Azure/GCP, measurable impact ("improved accuracy by 12%").

**Cross-questions**
- *"What's the difference between an ML Engineer and a Data Scientist?"* — A Data Scientist mainly analyses data and builds models to find insights; an ML Engineer focuses on building and deploying those models into production software at scale. There's overlap, and we position your profile based on which side your experience leans.
- *"Is GenAI/LLM experience important now?"* — Yes, many current AI job descriptions mention LLMs, RAG or GenAI. If you've built anything with them, we'll highlight it prominently.
- *"I only have academic projects."* — That's common for entry-level candidates. Strong GitHub projects with clear results, plus a cloud ML certification, help close the gap.
- *"Do you know MLOps?"* — It's the practice of reliably deploying, versioning and monitoring ML models — basically DevOps for machine learning, with tools like MLflow, Kubeflow and SageMaker.

---

### 4.2 Data Scientist

**Quick Pitch:** A Data Scientist uses data, statistics and programming to answer business questions and predict outcomes — for example, which customers might cancel, or how much stock to order. They turn raw data into insights and recommendations.

**Day-to-day**
- Gather and clean data from databases and files.
- Explore data to find trends and patterns (EDA).
- Build statistical and machine learning models to predict outcomes.
- Run experiments such as A/B tests.
- Present findings through dashboards and presentations to business teams.

**Alternate titles:** Data Analyst (more junior/reporting-focused), Data Scientist, Applied Scientist, Decision Scientist, Quantitative Analyst, Analytics Engineer (related), Research Scientist.

**Key terms**
| Term | Plain-English meaning |
|---|---|
| EDA | Exploratory Data Analysis — first look at data to understand it. |
| Data cleaning / wrangling | Fixing missing, wrong or messy data. |
| Regression / Classification | Predicting a number (price) / predicting a category (yes/no, spam/not spam). |
| A/B testing | Comparing two versions to see which performs better. |
| Hypothesis testing / p-value | Statistical way to check if a result is real or chance. |
| Feature engineering | Creating useful input variables for a model. |
| Overfitting | When a model memorises training data and fails on new data. |
| Data visualisation | Charts and dashboards that explain data. |
| Big Data | Data too large for normal tools; handled with Spark, Hadoop. |
| Data Engineer (related) | Builds the pipelines that move and store data; Data Scientists use that data. |

**Tools & tech:** Python (Pandas, NumPy, scikit-learn), R, SQL, Jupyter, Tableau, Power BI, Excel, Spark, Databricks, Snowflake, cloud (AWS/Azure/GCP).

**Certifications:** IBM Data Science Professional Certificate, Google Data Analytics / Advanced Data Analytics, Microsoft Power BI Data Analyst (PL-300), Azure Data Scientist Associate (DP-100), Databricks certifications.

**Roadmap**
- *Foundation:* Excel, SQL, statistics basics, Python basics, data visualisation.
- *Job-ready:* Pandas, EDA, ML with scikit-learn, Tableau/Power BI, A/B testing, storytelling with data, 2–3 end-to-end projects (e.g., Kaggle).
- *Advanced:* deep learning, big data (Spark), cloud data platforms, experiment design, causal inference, mentoring, business strategy influence.

**Background:** Statistics, Math, CS, Economics, Engineering, Physics; many have a Master's.

**Industries:** Every industry — tech, banking, retail, healthcare, insurance, telecom, consulting.

**Resume keywords:** Python, SQL, machine learning, statistics, Tableau/Power BI, A/B testing, business impact numbers.

**Cross-questions**
- *"Data Analyst vs Data Scientist?"* — Analysts focus on reporting and explaining what happened (SQL, Excel, dashboards). Scientists go further, predicting what will happen using statistics and ML. Many candidates target both titles, and we can market you for both if your skills fit.
- *"Do I need a Master's?"* — It's common but not mandatory; strong projects, SQL/Python skills and relevant experience can compensate.
- *"Which is more important, Python or SQL?"* — Both. SQL appears in almost every data job description; Python is standard for analysis and modelling.

---

### 4.3 Cybersecurity Analyst

**Quick Pitch:** A Cybersecurity Analyst protects a company's computers, networks and data from hackers. They monitor for attacks, investigate alerts, fix weaknesses and respond when something goes wrong.

**Day-to-day**
- Monitor security alerts and logs, often in a Security Operations Center (SOC).
- Investigate suspicious activity and respond to incidents.
- Run vulnerability scans and help fix weak points.
- Ensure systems follow security policies and compliance rules.
- Train employees on threats like phishing.

**Alternate titles:** SOC Analyst (L1/L2/L3), Information Security Analyst, Security Engineer, Incident Responder, Threat Analyst, Penetration Tester (ethical hacker), GRC Analyst, IAM Analyst.

**Key terms**
| Term | Plain-English meaning |
|---|---|
| SOC | Security Operations Center — the team watching for attacks 24/7. |
| SIEM | Software that collects and analyses security logs (e.g., Splunk, Microsoft Sentinel). |
| Firewall | Barrier controlling what network traffic is allowed in/out. |
| Phishing | Fake emails/messages tricking people into giving access or data. |
| Malware / Ransomware | Malicious software / malware that locks data and demands payment. |
| Vulnerability / Patch | A weakness / the fix for it. |
| Penetration testing | Authorised simulated hacking to find weaknesses. |
| IAM | Identity & Access Management — who can access what. |
| Incident response | Steps taken to contain and recover from an attack. |
| GRC / Compliance | Governance, Risk & Compliance — meeting standards like NIST, ISO 27001, SOC 2, HIPAA, PCI-DSS. |

**Tools & tech:** Splunk, Microsoft Sentinel, QRadar; CrowdStrike, Microsoft Defender (EDR); Wireshark; Nessus, Qualys; Burp Suite, Metasploit (pentest); Okta, Azure AD/Entra ID; Linux, networking (TCP/IP).

**Certifications:** CompTIA Security+ (most common entry cert), CompTIA CySA+, CEH, CISSP (senior, requires experience), CISM, OSCP (penetration testing), Google Cybersecurity Certificate, cloud security certs (AWS Security Specialty, AZ-500).

**Roadmap**
- *Foundation:* networking basics (IP, DNS, ports), operating systems (Windows/Linux), CompTIA Network+/Security+.
- *Job-ready:* SIEM tools, log analysis, incident handling, vulnerability scanning, basic scripting (Python/PowerShell), home lab / TryHackMe / HackTheBox.
- *Advanced:* threat hunting, cloud security, pentesting, security architecture, CISSP/CISM, leadership.

**Background:** IT, CS, Networking; many move up from IT Help Desk or System Administrator roles.

**Industries:** Banking, government/defence, healthcare, consulting, tech, any company with data.

**Resume keywords:** SIEM (Splunk/Sentinel), incident response, Security+, NIST, vulnerability management, EDR, cloud security.

**Cross-questions**
- *"Is Security+ enough to get a job?"* — It's the most common entry-level certification and often appears in job requirements, especially government-related roles. Combined with hands-on lab experience, it strengthens a profile a lot.
- *"Do government jobs need clearance?"* — Many US government and defence roles require security clearance, which generally requires US citizenship. We'd focus your profile on private-sector roles if that applies.
- *"SOC Analyst vs Security Engineer?"* — SOC analysts monitor and respond to alerts; security engineers design and build the security systems.

---

### 4.4 Cloud Engineer

**Quick Pitch:** A Cloud Engineer builds and manages a company's IT systems on cloud platforms like AWS, Microsoft Azure and Google Cloud, instead of physical servers in an office. They make systems scalable, secure and cost-efficient.

**Day-to-day**
- Set up and manage cloud servers, storage, databases and networks.
- Migrate applications from on-premise data centres to the cloud.
- Automate infrastructure using code (Infrastructure as Code).
- Monitor performance, security and costs.
- Troubleshoot outages and issues.

**Alternate titles:** Cloud Engineer, Cloud Architect (senior), AWS Engineer, Azure Engineer, Cloud Administrator, Cloud Infrastructure Engineer, Site Reliability Engineer (related), Cloud Security Engineer.

**Key terms**
| Term | Plain-English meaning |
|---|---|
| AWS / Azure / GCP | The three biggest cloud providers (Amazon, Microsoft, Google). |
| IaaS / PaaS / SaaS | Renting servers / renting a platform to build on / using ready software (e.g., Gmail). |
| Virtual Machine (EC2) | A computer running in the cloud. |
| Object storage (S3) | Cloud storage for files. |
| VPC | Virtual Private Cloud — a private network in the cloud. |
| Infrastructure as Code (IaC) | Creating servers and networks with code; tools Terraform, CloudFormation. |
| Serverless (Lambda) | Running code without managing servers. |
| Containers / Kubernetes | Packaged apps / the system that runs many containers. |
| Auto-scaling / Load balancer | Adding servers when traffic rises / spreading traffic across servers. |
| Cloud migration | Moving systems into the cloud. |

**Tools & tech:** AWS, Azure, GCP; Terraform, CloudFormation, ARM/Bicep; Linux; Docker, Kubernetes (EKS/AKS/GKE); Python, Bash, PowerShell; CloudWatch, Azure Monitor; Git.

**Certifications:** AWS Solutions Architect – Associate (very popular), AWS SysOps Administrator, Azure Administrator (AZ-104), Azure Solutions Architect (AZ-305), Google Associate Cloud Engineer, HashiCorp Terraform Associate, CKA (Kubernetes).

**Roadmap**
- *Foundation:* Linux, networking basics, one cloud's fundamentals (AWS Cloud Practitioner / AZ-900).
- *Job-ready:* core services (compute, storage, networking, IAM), Terraform, scripting, Docker, an associate-level cert, hands-on projects.
- *Advanced:* multi-cloud, Kubernetes, cloud security, cost optimisation (FinOps), architecture design, professional-level certs.

**Background:** IT/CS; often moves up from System Administrator, Network Engineer, or Support roles.

**Industries:** Almost all — tech, finance, healthcare, retail, consulting, government.

**Resume keywords:** AWS/Azure/GCP, Terraform, IaC, migration, Kubernetes, IAM, cost optimisation, certification names.

**Cross-questions**
- *"Should I learn AWS or Azure?"* — AWS has the largest market share overall; Azure is very strong in large enterprises that use Microsoft. Many job postings ask for either; one deep plus basic knowledge of the other is a good position.
- *"Cloud Engineer vs DevOps Engineer?"* — Cloud Engineers focus on building and running cloud infrastructure; DevOps Engineers focus on automating how software is built, tested and released. The roles overlap heavily and many job postings blend them.
- *"Are certifications enough without experience?"* — They help get shortlisted, but employers want hands-on proof — projects or lab work strengthen the profile.

---

### 4.5 DevOps Engineer

**Quick Pitch:** A DevOps Engineer helps software teams release code faster and more reliably by automating building, testing and deployment. They bridge the gap between developers (who write code) and operations (who run systems).

**Day-to-day**
- Build and maintain CI/CD pipelines (automatic build, test, deploy).
- Manage containers and Kubernetes clusters.
- Automate infrastructure with code.
- Set up monitoring and alerting.
- Respond to production issues and improve reliability.

**Alternate titles:** DevOps Engineer, Site Reliability Engineer (SRE), Platform Engineer, Build & Release Engineer, DevSecOps Engineer, Infrastructure Engineer.

**Key terms**
| Term | Plain-English meaning |
|---|---|
| CI/CD | Continuous Integration / Continuous Delivery — automatically testing and releasing code. |
| Pipeline | The automated sequence of build → test → deploy steps. |
| Docker / container | Packaging an app with everything it needs to run anywhere. |
| Kubernetes (K8s) | System that runs and manages many containers. |
| Infrastructure as Code | Creating infrastructure using code (Terraform, Ansible). |
| Configuration management | Keeping servers set up consistently (Ansible, Chef, Puppet). |
| Monitoring / Observability | Watching system health using metrics, logs and traces. |
| Git / Version control | Tracking code changes; GitHub/GitLab/Bitbucket. |
| SRE | Site Reliability Engineering — Google's approach to running reliable systems. |
| DevSecOps | Adding security checks into the DevOps pipeline. |

**Tools & tech:** Git, GitHub Actions, Jenkins, GitLab CI, Azure DevOps; Docker, Kubernetes, Helm; Terraform, Ansible; AWS/Azure/GCP; Prometheus, Grafana, Datadog, ELK; Linux, Bash, Python.

**Certifications:** AWS DevOps Engineer – Professional, Azure DevOps Engineer Expert (AZ-400), CKA / CKAD (Kubernetes), HashiCorp Terraform Associate, Docker Certified Associate.

**Roadmap**
- *Foundation:* Linux, networking, Git, scripting (Bash/Python), one cloud.
- *Job-ready:* CI/CD tool (Jenkins/GitHub Actions), Docker, Kubernetes basics, Terraform, monitoring tools, end-to-end pipeline project.
- *Advanced:* Kubernetes at scale, SRE practices (SLOs), DevSecOps, platform engineering, architecture.

**Background:** CS/IT; often from System Admin, Software Developer or Cloud roles.

**Industries:** Tech/SaaS, finance, e-commerce, telecom, consulting.

**Resume keywords:** CI/CD, Jenkins/GitHub Actions, Docker, Kubernetes, Terraform, AWS/Azure, monitoring, automation results ("reduced deployment time from 2 hours to 15 minutes").

**Cross-questions**
- *"Is DevOps a role or a culture?"* — Both. It started as a way of working between dev and ops teams, and now it's also a widely used job title.
- *"DevOps vs SRE?"* — Very similar toolsets; SRE puts more emphasis on reliability targets and on-call operations, while DevOps emphasises delivery automation.
- *"Do DevOps engineers need coding?"* — Yes, scripting (Python, Bash) and writing pipeline/infrastructure code are core skills, though usually less application coding than a software developer.

---

### 4.6 Software Developer

**Quick Pitch:** A Software Developer writes the code that builds apps, websites and systems — from mobile banking apps to the back-end systems that process orders. They design, code, test and maintain software.

**Day-to-day**
- Write and review code for new features.
- Fix bugs and improve performance.
- Write tests to make sure code works.
- Work with product managers and designers in Agile sprints.
- Use Git to collaborate with other developers.

**Alternate titles:** Software Engineer, Software Developer, Front-end Developer, Back-end Developer, Full-stack Developer, Java Developer, .NET Developer, Python Developer, Mobile (iOS/Android) Developer, SDE I/II/III.

**Key terms**
| Term | Plain-English meaning |
|---|---|
| Front-end / Back-end / Full-stack | What users see (UI) / server, logic and databases / both. |
| Programming language | Java, Python, C#, JavaScript/TypeScript, Go, C++. |
| Framework | Ready-made toolkit: React, Angular (front-end); Spring Boot, .NET, Django, Node.js (back-end). |
| API / REST | A way for software systems to talk to each other. |
| Database (SQL / NoSQL) | Where data is stored — MySQL, PostgreSQL / MongoDB. |
| Microservices | Building an app as many small independent services. |
| Agile / Scrum / Sprint | Iterative way of working in 1–2 week cycles. |
| Git / Pull Request | Version control / proposing code changes for review. |
| Unit testing | Automatic tests for small pieces of code. |
| Data structures & algorithms (DSA) | Core CS concepts heavily tested in US tech interviews. |

**Tools & tech:** Java/Spring Boot, C#/.NET, Python/Django/FastAPI, JavaScript/TypeScript, React, Angular, Node.js; SQL & NoSQL databases; Git; Docker; AWS/Azure; Jira; VS Code, IntelliJ.

**Certifications:** Less important than skills and projects. Useful extras: AWS Developer Associate, Azure Developer (AZ-204), Oracle Java certifications, Meta Front-End/Back-End certificates.

**Roadmap**
- *Foundation:* one language deeply (Java, Python or JavaScript), programming basics, Git, SQL.
- *Job-ready:* one framework stack (e.g., React + Node, or Java + Spring Boot), REST APIs, databases, testing, DSA practice (LeetCode), deployed portfolio projects.
- *Advanced:* system design, microservices, cloud, performance, mentoring, architecture.

**Background:** CS/IT/Engineering degrees, bootcamps, self-taught.

**Industries:** Every industry.

**Resume keywords:** language + framework names, REST APIs, microservices, cloud, Agile, testing, quantified impact.

**Cross-questions**
- *"Which stack is most in demand?"* — Java, Python and JavaScript/TypeScript (React, Node) appear very frequently in postings, along with C#/.NET in enterprises. We market you for the stack where your experience is strongest.
- *"Software Developer vs Software Engineer?"* — Mostly used interchangeably in job postings; "Engineer" is the more common title at larger tech companies.
- *"Do I need LeetCode?"* — Many US tech interviews include coding/DSA rounds, so practice is strongly recommended, especially for larger companies.

---

### 4.7 Prompt Engineer

**Quick Pitch:** A Prompt Engineer designs the instructions ("prompts") given to AI models like ChatGPT or Claude so they produce accurate, useful, safe results — and builds and tests AI-powered workflows for businesses. It's a newer role that often blends with AI Engineer and AI product roles.

**Day-to-day**
- Write, test and refine prompts for AI tasks (summaries, support bots, content, data extraction).
- Build evaluation sets to measure AI output quality.
- Connect AI models to company data and tools (RAG, APIs).
- Reduce errors such as "hallucinations".
- Document best practices and train teams to use AI.

**Alternate titles:** Prompt Engineer, AI Prompt Specialist, Generative AI Engineer, LLM Engineer, Conversational AI Designer, AI Solutions Specialist, AI Trainer / Content Specialist.

**Key terms**
| Term | Plain-English meaning |
|---|---|
| Prompt | The instruction or input given to an AI model. |
| LLM | Large Language Model (GPT, Claude, Gemini, Llama). |
| Zero-shot / Few-shot | Asking without examples / giving a few examples in the prompt. |
| Chain-of-thought | Encouraging the model to reason step by step. |
| System prompt | Background instructions that set the AI's role and rules. |
| Hallucination | When AI confidently makes up wrong information. |
| Token / Context window | Unit of text the model processes / how much text it can consider at once. |
| RAG | Giving the AI relevant documents so it answers from them. |
| Evaluation (evals) | Systematic testing of AI output quality. |
| Temperature | Setting that controls how creative vs predictable outputs are. |

**Tools & tech:** OpenAI, Anthropic, Google APIs; LangChain, LlamaIndex; Python; prompt-testing/eval tools; vector databases; Zapier/Make for automation; Jupyter.

**Certifications:** No single standard yet. Relevant: DeepLearning.AI short courses, vendor courses from OpenAI/Anthropic/Google, Azure AI Engineer (AI-102), AWS AI Practitioner.

**Roadmap**
- *Foundation:* how LLMs work at a high level, prompting techniques, strong writing and logical thinking.
- *Job-ready:* Python basics, calling AI APIs, RAG basics, building evaluations, a portfolio of AI workflows with before/after results.
- *Advanced:* agent/tool-use design, fine-tuning, AI safety and guardrails, AI product strategy.

**Background:** Mixed — CS, linguistics, writing, data, domain experts (legal, healthcare, marketing).

**Industries:** Tech, AI startups, consulting, marketing agencies, customer-support platforms, enterprises adopting AI.

**Resume keywords:** LLM, prompt design, RAG, evals, Python, API integration, GenAI, measurable outcomes.

**Cross-questions**
- *"Is Prompt Engineer a real, lasting job?"* — Pure "prompt-only" titles are fewer than broader GenAI/AI Engineer roles, so we usually market these candidates for the broader AI titles too, highlighting prompt design as a key skill.
- *"Do I need coding?"* — It helps a lot. Most roles expect at least basic Python and API skills alongside prompt design.
- *"How do I prove my skills?"* — A portfolio showing problems solved with AI, how you tested quality, and results.

---

## 5. Content — Engineering, Construction & Manufacturing roles

### 5.1 Civil Engineer

**Quick Pitch:** A Civil Engineer designs and oversees construction of infrastructure — roads, bridges, buildings, water and sewer systems, dams and airports — making sure they are safe, durable and meet codes.

**Day-to-day**
- Design structures and infrastructure using software (AutoCAD, Civil 3D, Revit).
- Perform calculations for loads, materials and drainage.
- Prepare drawings, specifications and cost estimates.
- Visit sites to inspect work and solve problems.
- Ensure compliance with building codes and environmental rules.

**Alternate titles:** Civil Engineer, Structural Engineer, Transportation Engineer, Geotechnical Engineer, Water Resources Engineer, Site/Land Development Engineer, Project Engineer, EIT (Engineer in Training).

**Key terms**
| Term | Plain-English meaning |
|---|---|
| Structural engineering | Designing the "skeleton" of buildings and bridges so they stand safely. |
| Geotechnical | Study of soil and rock to design foundations. |
| Transportation engineering | Roads, highways, traffic and transit design. |
| Hydraulics / Stormwater | Managing water flow and drainage. |
| AutoCAD / Civil 3D | Drafting and civil design software. |
| BIM | Building Information Modelling — 3D digital models of buildings (Revit). |
| Building codes | Legal safety rules (e.g., IBC in US, National Building Code in Canada). |
| FE / PE exams (US) | Fundamentals of Engineering exam → EIT; Professional Engineer licence after experience. |
| P.Eng (Canada) | Professional Engineer licence via provincial bodies (e.g., PEO in Ontario). |
| Site inspection | Checking construction work matches design and codes. |

**Tools & tech:** AutoCAD, Civil 3D, Revit, STAAD.Pro, SAP2000, ETABS, MicroStation, HEC-RAS, ArcGIS, MS Project, Excel.

**Certifications/licences:** FE exam / EIT, PE licence (US); EIT then P.Eng (Canada); PMP (for project-focused roles); LEED (green building).

**Roadmap**
- *Foundation:* civil engineering degree, mechanics, materials, AutoCAD.
- *Job-ready:* Civil 3D/Revit, one analysis tool (STAAD/ETABS), codes knowledge, FE/EIT, internship or site experience.
- *Advanced:* PE / P.Eng licence, project management, design lead, specialisation (structural, geotechnical, water).

**Background:** B.E./B.Tech/B.Sc. in Civil Engineering; Master's common for structural.

**Industries:** Consulting engineering firms, government (DOTs, municipalities), construction companies, real estate developers, utilities.

**Resume keywords:** AutoCAD/Civil 3D, structural analysis, site development, codes (IBC/ACI/AASHTO), EIT/PE, project values.

**Cross-questions**
- *"Is my overseas degree valid?"* — Licensing (PE/P.Eng) has specific credential-evaluation steps through the state board or provincial engineering body. Many candidates work as EIT/Project Engineers while pursuing licensure.
- *"Do I need PE to get a job?"* — Not for entry-level; it becomes important for senior roles where you sign/stamp drawings.
- *"Civil vs Structural Engineer?"* — Structural is a specialisation within civil, focused on buildings and bridges.

---

### 5.2 Construction Manager

**Quick Pitch:** A Construction Manager plans and runs construction projects from start to finish — managing schedule, budget, workers, subcontractors, safety and quality — so a building or infrastructure project is delivered on time and on budget.

**Day-to-day**
- Plan project schedules and budgets.
- Coordinate subcontractors, suppliers and site teams.
- Track progress and handle change orders.
- Enforce safety (OSHA in US) and quality standards.
- Communicate with clients, architects and engineers.

**Alternate titles:** Construction Manager, Project Manager (Construction), Site Manager, Superintendent, Project Engineer, Assistant Project Manager, Construction Coordinator.

**Key terms**
| Term | Plain-English meaning |
|---|---|
| General Contractor (GC) | Main company responsible for the build. |
| Subcontractor | Specialist hired for parts (electrical, plumbing). |
| RFI | Request for Information — formal question to designers. |
| Submittals | Documents/samples sent for approval before use. |
| Change order | Approved change to scope, cost or time. |
| Gantt chart / Critical path | Schedule visual / the sequence of tasks that determines the end date. |
| Bid / Estimate | Price proposal / cost calculation. |
| Punch list | Final list of items to fix before completion. |
| OSHA | US workplace safety rules (OSHA 30 is a common certificate). |
| Commercial vs Residential vs Infrastructure | Office/retail / homes / roads, bridges, utilities. |

**Tools & tech:** Procore, Primavera P6, MS Project, Bluebeam, AutoCAD (reading drawings), PlanGrid/Autodesk Build, Excel.

**Certifications:** PMP, CCM (Certified Construction Manager), OSHA 30, LEED AP, Gold Seal (Canada).

**Roadmap**
- *Foundation:* reading drawings, construction methods, materials, safety basics.
- *Job-ready:* scheduling (P6/MS Project), cost control, Procore, contracts basics, OSHA 30, site experience as Project Engineer/APM.
- *Advanced:* full project ownership, large budgets, client management, PMP/CCM.

**Background:** Civil Engineering, Construction Management, Architecture, or site experience.

**Industries:** General contractors, real estate developers, infrastructure, energy, government.

**Resume keywords:** project size ($ value), Procore, P6, scheduling, cost control, safety record, OSHA 30, PMP.

**Cross-questions**
- *"Is my overseas site experience counted?"* — Yes, experience counts; we highlight project scale, type and responsibilities. US/Canada-specific safety and software knowledge (OSHA, Procore) strengthens the profile.
- *"Construction Manager vs Civil Engineer?"* — Civil engineers mainly design; construction managers mainly execute and manage the building process.
- *"Do I need PMP?"* — Helpful and often preferred, not always mandatory.

---

### 5.3 Mechanical Engineer

**Quick Pitch:** A Mechanical Engineer designs, builds and tests machines and mechanical systems — engines, HVAC systems, robots, medical devices, manufacturing equipment — anything that moves or uses energy.

**Day-to-day**
- Design parts and products in CAD software.
- Run calculations and simulations (stress, heat, fluid flow).
- Build and test prototypes.
- Work with manufacturing to make designs producible.
- Improve existing products for cost, quality or performance.

**Alternate titles:** Mechanical Engineer, Design Engineer, Mechanical Design Engineer, HVAC Engineer, Product Development Engineer, Manufacturing Engineer, R&D Engineer.

**Key terms**
| Term | Plain-English meaning |
|---|---|
| CAD | Computer-Aided Design — SolidWorks, AutoCAD, CATIA, Creo, NX. |
| FEA | Finite Element Analysis — simulating stress/strain on parts (ANSYS). |
| CFD | Simulating fluid and air flow. |
| GD&T | Standard symbols on drawings defining allowed tolerances. |
| Thermodynamics / Heat transfer | Science of energy and heat movement. |
| HVAC | Heating, ventilation and air conditioning systems. |
| Prototype | Early working model for testing. |
| DFM | Design for Manufacturing — designing parts that are easy and cheap to make. |
| BOM | Bill of Materials — list of all parts. |
| PLM | Product Lifecycle Management software (Windchill, Teamcenter). |

**Tools & tech:** SolidWorks, AutoCAD, CATIA, Creo, Siemens NX, ANSYS, MATLAB, Revit MEP (for HVAC), Windchill/Teamcenter, Excel.

**Certifications:** CSWA/CSWP (SolidWorks), FE/PE or EIT/P.Eng, Six Sigma Green Belt, GD&T certification (ASME).

**Roadmap**
- *Foundation:* mechanics, thermodynamics, materials, CAD basics.
- *Job-ready:* SolidWorks/Creo proficiency, GD&T, FEA basics, DFM, internship/project experience.
- *Advanced:* system design, advanced simulation, leading product development, PE/P.Eng.

**Background:** Mechanical Engineering degree.

**Industries:** Automotive, aerospace, manufacturing, HVAC/building services, energy, medical devices, consumer products.

**Resume keywords:** SolidWorks/CATIA, GD&T, FEA/ANSYS, product design, prototyping, DFM, industry name.

**Cross-questions**
- *"Mechanical vs Manufacturing Engineer?"* — Mechanical/design engineers create the product design; manufacturing engineers figure out how to produce it efficiently in the factory.
- *"Which CAD software matters?"* — SolidWorks is very common in mid-size companies; CATIA and NX are common in automotive/aerospace; Creo in industrial equipment. We highlight what you've used.
- *"Is GD&T important?"* — Yes, it's commonly listed in design-engineering job descriptions.

---

### 5.4 Electrical Engineer

**Quick Pitch:** An Electrical Engineer designs and maintains systems that generate, distribute and use electricity — from power grids and building electrical systems to circuit boards inside electronic devices.

**Day-to-day**
- Design electrical systems, circuits or power distribution.
- Create schematics and wiring diagrams.
- Perform load calculations and select equipment.
- Test, troubleshoot and commission systems.
- Ensure compliance with electrical codes (NEC in US, CEC in Canada).

**Alternate titles:** Electrical Engineer, Power Systems Engineer, Electrical Design Engineer, Controls Engineer, Electronics/Hardware Engineer, Substation Engineer, Instrumentation Engineer, PCB Design Engineer.

**Key terms**
| Term | Plain-English meaning |
|---|---|
| Power vs Electronics | Large-scale electricity (grids, buildings) vs small circuits (devices, chips). |
| AC / DC | Alternating current / direct current. |
| Schematic | Diagram of an electrical circuit. |
| PLC | Programmable Logic Controller — computer controlling machines in factories. |
| SCADA | Software to monitor and control industrial/utility systems. |
| Load calculation | Working out how much power a system needs. |
| Substation / Switchgear | Facility that changes voltage / equipment that controls and protects circuits. |
| NEC / CEC | National Electrical Code (US) / Canadian Electrical Code. |
| PCB | Printed Circuit Board. |
| Arc flash / Short circuit study | Electrical safety and fault analysis studies. |

**Tools & tech:** AutoCAD Electrical, ETAP, SKM PowerTools, MATLAB/Simulink, PLC software (Rockwell/Allen-Bradley, Siemens TIA Portal), Altium/OrCAD (PCB), Revit MEP.

**Certifications/licences:** FE/PE (US), EIT/P.Eng (Canada), PLC vendor certifications, NETA (testing).

**Roadmap**
- *Foundation:* circuit theory, electromagnetics, power systems basics, AutoCAD.
- *Job-ready:* specialisation tools (ETAP for power, PLC programming for controls, Altium for electronics), codes (NEC/CEC), internship/project.
- *Advanced:* system design leadership, protection studies, renewable/grid integration, PE/P.Eng.

**Background:** Electrical/Electronics Engineering degree.

**Industries:** Utilities, renewable energy, construction/MEP consulting, manufacturing, semiconductors, automotive (EVs), data centres.

**Resume keywords:** power distribution, ETAP, NEC, PLC/SCADA, AutoCAD Electrical, substation, renewable, PE/EIT.

**Cross-questions**
- *"Power or controls — which is in demand?"* — Both are in demand in different sectors: power with utilities, renewables and data centres; controls/PLC with manufacturing and automation. We target based on your experience.
- *"Electrical vs Electronics Engineer?"* — Electrical often means power and building systems; electronics means circuit boards and devices.
- *"Do I need to know NEC?"* — For US building/power roles, it's frequently required; for Canada, the CEC.

---

### 5.5 Process Engineer

**Quick Pitch:** A Process Engineer designs, runs and improves the processes used to make products at scale — in chemical plants, oil & gas, pharma, food, semiconductors or manufacturing — making them safer, faster, cheaper and higher quality.

**Day-to-day**
- Monitor production processes and analyse data.
- Troubleshoot quality or yield problems.
- Design improvements and run trials.
- Create process flow diagrams and standard operating procedures (SOPs).
- Apply Lean and Six Sigma methods to cut waste and variation.

**Alternate titles:** Process Engineer, Chemical Process Engineer, Manufacturing Process Engineer, Process Improvement Engineer, Continuous Improvement Engineer, Production Engineer.

**Key terms**
| Term | Plain-English meaning |
|---|---|
| PFD / P&ID | Process Flow Diagram / Piping & Instrumentation Diagram. |
| Yield | Percentage of good output from input. |
| Lean | Method to remove waste from processes. |
| Six Sigma / DMAIC | Data-driven method to reduce defects (Define, Measure, Analyse, Improve, Control). |
| SPC | Statistical Process Control — monitoring processes with control charts. |
| Root Cause Analysis (RCA) | Finding the true cause of a problem (5 Whys, fishbone). |
| SOP | Standard Operating Procedure — written step-by-step instructions. |
| Scale-up | Moving a process from lab/pilot to full production. |
| HAZOP | Structured safety study of a process. |
| Kaizen | Continuous small improvements. |

**Tools & tech:** Aspen HYSYS/Plus, Minitab, JMP, MATLAB, AutoCAD/P&ID tools, SAP, Excel, PLC/SCADA basics, Power BI.

**Certifications:** Lean Six Sigma Green/Black Belt, PE/P.Eng, PMP, industry-specific safety certifications.

**Roadmap**
- *Foundation:* chemical/mechanical engineering fundamentals, mass & energy balance, reading P&IDs.
- *Job-ready:* Lean/Six Sigma tools, SPC, Minitab, RCA, plant/internship experience.
- *Advanced:* process design, scale-up, capital projects, Black Belt, leading improvement programs.

**Background:** Chemical, Mechanical, Industrial or Materials Engineering.

**Industries:** Oil & gas, chemicals, pharmaceuticals, food & beverage, semiconductors, automotive, plastics.

**Resume keywords:** process optimisation, yield improvement %, Lean Six Sigma, SPC, RCA, P&ID, Aspen, cost savings $.

**Cross-questions**
- *"Process vs Manufacturing Engineer?"* — Very similar. Process engineers focus on the process (often continuous, like chemical plants); manufacturing engineers often focus on assembly lines and equipment.
- *"Is Six Sigma important?"* — It's frequently listed as preferred and helps prove improvement skills with data.
- *"I worked in a plant in India — relevant?"* — Yes; we highlight the process type, improvements made and measurable results.

---

### 5.6 Validation Engineer

**Quick Pitch:** A Validation Engineer proves — with documented testing — that equipment, processes, software and facilities consistently produce products that meet quality and regulatory requirements. It's a key role in highly regulated industries like pharma, biotech and medical devices.

**Day-to-day**
- Write validation protocols (test plans) and reports.
- Execute IQ/OQ/PQ testing on equipment and processes.
- Validate computer systems (CSV) used in production and labs.
- Document deviations and work with Quality Assurance.
- Support audits by the FDA (US) or Health Canada.

**Alternate titles:** Validation Engineer, Validation Specialist, CQV Engineer (Commissioning, Qualification & Validation), Computer System Validation (CSV) Engineer, Process Validation Engineer, Quality Engineer (related).

**Key terms**
| Term | Plain-English meaning |
|---|---|
| GMP / cGMP | (current) Good Manufacturing Practice — rules for making safe medicines/devices. |
| FDA / Health Canada | US / Canadian regulators. |
| IQ / OQ / PQ | Installation Qualification (installed correctly) / Operational (works across ranges) / Performance (works consistently in real use). |
| CQV | Commissioning, Qualification & Validation. |
| CSV / CSA | Computer System Validation / Computer Software Assurance (newer risk-based FDA approach). |
| 21 CFR Part 11 | FDA rule on electronic records and signatures. |
| GAMP 5 | Industry guide for validating computerised systems. |
| Protocol / Deviation | Test plan / documented departure from plan. |
| CAPA | Corrective and Preventive Action. |
| Cleaning validation | Proving equipment cleaning removes residues. |

**Tools & tech:** Kneat, ValGenesis (digital validation), TrackWise, Veeva, MasterControl (QMS), SAP, LIMS, Kaye validators (temperature mapping), MS Office.

**Certifications:** ASQ CQE (Certified Quality Engineer), Six Sigma, ISPE/GAMP training, ASQ CQA.

**Roadmap**
- *Foundation:* GMP basics, life-science or engineering fundamentals, technical writing.
- *Job-ready:* IQ/OQ/PQ execution, protocol writing, 21 CFR Part 11, GAMP 5, deviation/CAPA handling.
- *Advanced:* validation master plans, CSA, leading CQV projects, audit leadership.

**Background:** Chemical, Mechanical, Biomedical, Electrical Engineering; Pharmacy; Biotechnology.

**Industries:** Pharmaceuticals, biotech, medical devices, food, CDMOs, engineering consultancies serving pharma.

**Resume keywords:** IQ/OQ/PQ, CQV, CSV, GMP, 21 CFR Part 11, GAMP 5, FDA audits, Kneat/ValGenesis.

**Cross-questions**
- *"Validation vs Verification?"* — Verification checks "did we build it right" against specs; validation checks "does it consistently meet the intended use" — in regulated industries, validation is formal and documented.
- *"Validation vs QA?"* — QA oversees the overall quality system; validation engineers do the technical testing and documentation that QA reviews.
- *"Is CSV experience separate?"* — Yes, Computer System Validation is a specialisation; candidates with both equipment and CSV experience can target more roles.

---

## 6. Content — Business, Marketing & Operations roles

### 6.1 Digital Marketing (Specialist / Executive)

**Quick Pitch:** A Digital Marketer promotes a company's products online — through Google search, social media, email, ads and websites — to attract customers, generate leads and increase sales, and measures results with data.

**Day-to-day**
- Run paid ad campaigns (Google Ads, Meta/LinkedIn Ads).
- Improve website ranking on Google (SEO).
- Create and schedule social media and email campaigns.
- Track performance in Google Analytics and report results.
- Run A/B tests on ads, emails and landing pages.

**Alternate titles:** Digital Marketing Specialist/Executive, SEO Specialist, PPC/SEM Specialist, Paid Media Specialist, Social Media Manager, Performance Marketer, Email Marketing Specialist, Growth Marketer, Content Marketer.

**Key terms**
| Term | Plain-English meaning |
|---|---|
| SEO | Search Engine Optimisation — ranking higher in free Google results. |
| SEM / PPC | Search Engine Marketing / Pay-Per-Click ads. |
| CTR | Click-Through Rate — % of people who click. |
| Conversion / Conversion rate | Desired action (purchase, sign-up) / % who do it. |
| CPC / CPA / ROAS | Cost per click / cost per acquisition / return on ad spend. |
| Funnel | Customer journey: awareness → consideration → purchase. |
| Landing page | Page built specifically for a campaign. |
| Marketing automation | Software sending targeted emails automatically (HubSpot, Marketo). |
| GA4 | Google Analytics 4 — website analytics tool. |
| KPI | Key Performance Indicator — main success metric. |

**Tools & tech:** Google Ads, Meta Ads Manager, LinkedIn Ads, GA4, Google Tag Manager, SEMrush, Ahrefs, HubSpot, Mailchimp, Hootsuite, Canva, WordPress, Looker Studio.

**Certifications:** Google Ads certifications, Google Analytics certification, HubSpot Inbound/Content Marketing, Meta Certified Digital Marketing Associate, SEMrush Academy.

**Roadmap**
- *Foundation:* marketing basics, funnel, content, social media, GA4 basics.
- *Job-ready:* run real campaigns (even small budgets), Google Ads + Meta Ads, SEO basics, email marketing, reporting, free Google/HubSpot certs.
- *Advanced:* performance strategy, budget ownership, marketing automation, CRO, team leadership.

**Background:** Marketing, Business, Communications, or any degree with practical campaign experience.

**Industries:** E-commerce, agencies, SaaS/tech, retail, healthcare, education.

**Resume keywords:** SEO, PPC, Google Ads, GA4, ROAS, conversion rate %, budget managed, leads generated.

**Cross-questions**
- *"Do certifications matter?"* — Free Google and HubSpot certs are helpful supporting proof, but employers care most about campaign results (budgets handled, leads, ROAS).
- *"Specialist vs Generalist?"* — Larger companies hire specialists (SEO, PPC); smaller companies prefer generalists. We can position your profile either way.
- *"Is AI replacing digital marketing?"* — AI tools are changing how content and ads are produced; marketers who use AI tools effectively are increasingly valued.

---

### 6.2 Marketing Manager

**Quick Pitch:** A Marketing Manager plans and leads a company's overall marketing strategy — deciding target customers, messaging, channels and budgets — and manages the team and agencies that execute campaigns to grow the business.

**Day-to-day**
- Create marketing plans and budgets.
- Define target audience, positioning and messaging.
- Oversee campaigns across digital, events, PR and content.
- Manage team members and agencies.
- Report on results (pipeline, revenue, ROI) to leadership.

**Alternate titles:** Marketing Manager, Brand Manager, Product Marketing Manager (PMM), Growth Marketing Manager, Demand Generation Manager, Marketing Communications Manager.

**Key terms**
| Term | Plain-English meaning |
|---|---|
| Go-to-market (GTM) | Plan for launching a product to customers. |
| Positioning | How the product is described vs competitors. |
| Brand awareness | How well people know the brand. |
| Demand generation | Creating interest that leads to sales. |
| MQL / SQL | Marketing-qualified lead / sales-qualified lead. |
| CAC / LTV | Customer acquisition cost / customer lifetime value. |
| Marketing ROI | Return generated per marketing dollar. |
| Segmentation / Persona | Grouping customers / profile of an ideal customer. |
| B2B vs B2C | Selling to businesses vs consumers. |
| Attribution | Working out which marketing activity led to a sale. |

**Tools & tech:** HubSpot, Salesforce, Marketo, GA4, Google/Meta Ads, Asana/Monday, Tableau/Looker, SEMrush.

**Certifications:** Google/HubSpot certifications, PMI or Pragmatic Institute (product marketing), AMA PCM, MBA (common but not required).

**Roadmap**
- *Foundation:* marketing fundamentals, digital channels, analytics.
- *Job-ready (manager):* 3–5+ years of execution, campaign ownership, budget management, CRM, team/agency coordination.
- *Advanced:* strategy, brand, multi-channel leadership, Director/CMO track.

**Background:** Marketing, Business, MBA; usually grows from Digital Marketing or Marketing Specialist roles.

**Industries:** All — tech, FMCG/CPG, healthcare, finance, retail, B2B services.

**Resume keywords:** strategy, budget ($), team size, pipeline/revenue growth %, GTM launches, B2B/B2C.

**Cross-questions**
- *"Marketing Manager vs Digital Marketing Specialist?"* — The specialist executes campaigns; the manager owns strategy, budget and people.
- *"Product Marketing Manager vs Product Manager?"* — PMM handles how a product is positioned and launched to the market; PM decides what the product should be and builds it with engineering.
- *"Do I need an MBA?"* — Helpful for some larger companies, but proven results and leadership experience matter most.

---

### 6.3 Product Manager

**Quick Pitch:** A Product Manager decides what a product should do and why — balancing customer needs, business goals and technical feasibility — then works with engineers and designers to build and launch it. Often described as the "CEO of the product", though without direct authority over the team.

**Day-to-day**
- Talk to customers and analyse data to find problems worth solving.
- Define the product vision and roadmap.
- Write requirements (PRDs, user stories) and prioritise the backlog.
- Work daily with engineering and design in Agile sprints.
- Launch features and measure success with metrics.

**Alternate titles:** Product Manager, Associate PM (APM), Senior PM, Technical Product Manager (TPM), Product Owner, Group PM, Product Lead.

**Key terms**
| Term | Plain-English meaning |
|---|---|
| Product roadmap | Plan of what will be built and when. |
| PRD | Product Requirements Document (like this one!). |
| User story | "As a [user], I want [goal] so that [benefit]." |
| Backlog / Prioritisation | List of work to do / deciding order (RICE, MoSCoW). |
| MVP | Minimum Viable Product — simplest version to test an idea. |
| Product-market fit | Product clearly meets a strong market need. |
| Agile / Scrum / Sprint | Iterative development in short cycles. |
| KPIs (DAU, retention, churn) | Daily active users, users who return, users who leave. |
| Stakeholder | Anyone affected by or influencing the product. |
| Product Owner | Scrum role managing the backlog; overlaps with PM. |

**Tools & tech:** Jira, Confluence, Figma, Productboard, Aha!, Amplitude, Mixpanel, GA4, SQL (helpful), Miro, Notion.

**Certifications:** CSPO (Certified Scrum Product Owner), PSPO, Pragmatic Institute, AIPMM CPM, Product School certificates.

**Roadmap**
- *Foundation:* product thinking, Agile/Scrum, user research basics, basic data analysis.
- *Job-ready:* writing PRDs/user stories, prioritisation frameworks, Jira, metrics, SQL basics, case studies of products shipped.
- *Advanced:* product strategy, P&L ownership, leading multiple teams, AI product knowledge.

**Background:** Engineering, Business, MBA, Design, Data; common transitions from Developer, Business Analyst, Consultant.

**Industries:** Tech/SaaS, fintech, e-commerce, healthcare tech, enterprise software.

**Resume keywords:** roadmap, launched [feature], metrics improved %, Agile, cross-functional leadership, user research.

**Cross-questions**
- *"Product Manager vs Project Manager?"* — The Product Manager decides *what* to build and *why*; the Project Manager manages *how and when* it gets delivered (timelines, resources).
- *"Product Manager vs Product Owner?"* — Product Owner is a Scrum role focused on the backlog; in many companies one person does both.
- *"Can a Business Analyst move into PM?"* — Yes, it's a common path; we highlight requirement-gathering, stakeholder management and product decisions.

---

### 6.4 Supply Chain Analyst

**Quick Pitch:** A Supply Chain Analyst uses data to improve how products move from suppliers to warehouses to customers — forecasting demand, managing inventory, reducing costs and avoiding stock-outs or delays.

**Day-to-day**
- Analyse inventory, shipping and supplier data.
- Forecast demand and plan inventory levels.
- Track KPIs like on-time delivery and inventory turnover.
- Identify cost-saving opportunities in logistics and procurement.
- Build reports and dashboards for operations teams.

**Alternate titles:** Supply Chain Analyst, Demand Planner, Inventory Analyst, Logistics Analyst, Procurement Analyst, Materials Planner, Operations Analyst, S&OP Analyst.

**Key terms**
| Term | Plain-English meaning |
|---|---|
| Supply chain | Full flow: suppliers → manufacturing → warehouse → customer. |
| Demand forecasting | Predicting how much customers will buy. |
| Inventory turnover | How fast stock is sold and replaced. |
| Lead time | Time from order to delivery. |
| Safety stock | Extra stock kept to avoid running out. |
| ERP | Enterprise Resource Planning software (SAP, Oracle) running core operations. |
| MRP | Material Requirements Planning — planning materials needed. |
| S&OP | Sales & Operations Planning — aligning sales forecasts with supply. |
| Procurement / Sourcing | Buying goods / choosing suppliers. |
| 3PL / Logistics | Third-party logistics provider / transport and warehousing. |

**Tools & tech:** Excel (advanced), SQL, SAP (MM/SD/APO/IBP), Oracle SCM, Tableau, Power BI, Python (helpful), Kinaxis, Blue Yonder.

**Certifications:** APICS/ASCM CSCP, CPIM, CLTD; Six Sigma Green Belt; SAP certifications.

**Roadmap**
- *Foundation:* supply chain basics, Excel (pivot tables, VLOOKUP/XLOOKUP), basic statistics.
- *Job-ready:* SQL, Power BI/Tableau, ERP experience (SAP), forecasting methods, KPI reporting.
- *Advanced:* network optimisation, S&OP leadership, Python modelling, CSCP/CPIM, managerial roles.

**Background:** Supply Chain, Industrial Engineering, Business, Operations, Economics.

**Industries:** Retail, e-commerce, manufacturing, pharma, CPG, logistics companies, automotive.

**Resume keywords:** forecasting accuracy %, inventory reduction, SAP, Excel, SQL, Power BI, cost savings $, KPIs.

**Cross-questions**
- *"Is SAP experience required?"* — Many postings list SAP or another ERP; any ERP experience is valuable and we highlight it.
- *"Supply Chain Analyst vs Data Analyst?"* — Similar tools (Excel, SQL, BI), but supply chain analysts apply them specifically to inventory, logistics and procurement.
- *"Which certification helps most?"* — ASCM/APICS certifications (CPIM, CSCP) are the best-known in the field.

---

## 7. Shared content pages

### 7.1 Compare-roles page (required comparisons)
A single table page answering the most frequent "difference between" questions, each in one or two lines, linking to both role pages:

| Commonly confused | One-line difference |
|---|---|
| Data Scientist vs ML Engineer | Insights & models vs deploying models in production. |
| Data Scientist vs Data Analyst | Prediction & ML vs reporting what happened. |
| Cloud Engineer vs DevOps Engineer | Building cloud infrastructure vs automating software delivery. |
| DevOps vs SRE | Delivery automation vs reliability targets & operations. |
| Prompt Engineer vs AI/ML Engineer | Designing AI instructions & workflows vs building/training models. |
| Civil Engineer vs Construction Manager | Designing vs managing construction. |
| Mechanical vs Process Engineer | Designing products/machines vs designing/improving production processes. |
| Validation Engineer vs QA | Technical testing & documentation vs overall quality oversight. |
| Product Manager vs Project Manager | What & why vs how & when. |
| Marketing Manager vs Digital Marketer | Strategy, budget & team vs channel execution. |
| Supply Chain Analyst vs Data Analyst | Same tools, applied to inventory/logistics. |

### 7.2 Glossary
- Auto-generated A–Z from all "Key terms" tables (≈ 170 terms), each tagged with the role(s) it belongs to.
- Searchable and filterable by category.

### 7.3 US & Canada job-market basics (for reps)
Plain-language explainers the rep can use in conversation:
- **ATS (Applicant Tracking System):** software employers use to filter resumes by keywords — the reason keyword-matched resumes matter.
- **US/Canada resume norms:** 1–2 pages, no photo, no date of birth/marital status, achievement-focused bullets with numbers.
- **LinkedIn:** heavily used by recruiters in both countries; a complete, keyword-rich profile matters.
- **Job types:** Full-time (W-2 in US), contract (C2C/1099 in US), contract-to-hire; in Canada, permanent vs contract/T4 vs incorporated contractor.
- **Common hiring stages:** application → recruiter screen → technical/hiring-manager interviews → case/assessment → offer → background check.
- **Work authorisation terms (awareness only):** US — OPT, STEM OPT, CPT, H-1B, Green Card, US Citizen; Canada — PGWP, open/closed work permit, Permanent Resident, LMIA. The site lists these as *terms to recognise*, with a "last verified" date, and links to official sources (USCIS, IRCC). Rules change frequently.

### 7.4 Handling cross-questions — call guidelines & compliance guardrails
**Call technique (displayed as a short card):**
1. Listen, then repeat the candidate's role in their words.
2. Use the Quick Pitch and one or two key terms naturally — don't lecture.
3. If you don't know: *"That's a great, specific question — let me confirm with our [technical/marketing] specialist and get back to you today."* Never guess.
4. Bring the conversation back to how our service helps (profile positioning, resume keywords, reaching recruiters).

**Must NOT say (compliance):**
- Never guarantee a job, interview count, salary or visa outcome.
- Never give immigration or legal advice — refer to an immigration attorney / licensed consultant (RCIC in Canada) or official sources.
- Never suggest misrepresenting experience, skills, education or work authorisation on a resume.
- Never quote salary figures that aren't from the dated, sourced salary field.

These guardrails appear on every role page footer and on the Handling Cross-Questions page. (Legal/compliance team to review wording before launch.)

### 7.5 Self-quiz
- 5–10 multiple-choice questions per role (e.g., "What does IQ/OQ/PQ refer to?"), plus a mixed "random 20" mode.
- Score shown instantly; no data stored on any server in v1 (optional local browser storage for "last score").
- Question bank stored in the same JSON content file as role data.

---

## 8. Requirements

### 8.1 Functional requirements

| ID | Requirement | Priority |
|---|---|---|
| FR-1 | Home page shows all 17 roles as cards grouped into 3 categories, each with role name, icon and one-line description. | Must |
| FR-2 | Each role has its own page following the standard template (Section 3.2). | Must |
| FR-3 | Quick Pitch box is visually highlighted and appears at the top of every role page. | Must |
| FR-4 | Global search (client-side) across role names, alternate titles, key terms, tools and certifications, with instant results as you type. | Must |
| FR-5 | Searching an alternate title (e.g., "SRE", "Product Owner", "SOC Analyst") returns the parent role. | Must |
| FR-6 | Sticky in-page navigation (table of contents) on role pages to jump between sections. | Must |
| FR-7 | Compare-roles page (Section 7.1). | Must |
| FR-8 | A–Z glossary page generated from role data. | Must |
| FR-9 | Cross-questions sections displayed as expandable Q&A (accordion). | Must |
| FR-10 | "Live Call Mode" toggle: hides everything except Quick Pitch, key terms and cross-questions for fast scanning. | Should |
| FR-11 | Print-friendly CSS (one role per printed page set) and "Print this role" button. | Should |
| FR-12 | Self-quiz page (Section 7.5). | Should |
| FR-13 | Keyboard shortcut "/" focuses search. | Could |
| FR-14 | "Copy" button next to each Quick Pitch. | Could |
| FR-15 | Each page shows "Content last reviewed: [date]" in the footer. | Must |
| FR-16 | Salary field shows value, source and date, or "Pending verification". | Must |
| FR-17 | Feedback link ("Something wrong or missing?") opening a pre-filled email/form to the content owner. | Should |

### 8.2 Non-functional requirements

| ID | Requirement |
|---|---|
| NFR-1 | **Static only**: plain HTML/CSS/JS or a static-site generator output; no server or database. |
| NFR-2 | **Performance**: first page load < 2 seconds on a standard office connection; search results < 100 ms. |
| NFR-3 | **Responsive**: works on desktop (primary, used beside dialer), tablet and mobile. |
| NFR-4 | **Accessibility**: WCAG 2.1 AA — readable contrast, keyboard navigable, proper headings. |
| NFR-5 | **Readability**: content written at roughly a Grade 8–10 reading level; every technical term explained in plain English. |
| NFR-6 | **Maintainability**: all role content stored in one structured data file (JSON/YAML/Markdown) separate from layout, so non-developers can update content. |
| NFR-7 | **Access control**: internal use only — hosted behind company SSO/VPN, IP allow-list, or a simple access gate provided by the hosting platform. Pages set `noindex`. |
| NFR-8 | **Browser support**: latest Chrome, Edge, Firefox, Safari. |
| NFR-9 | **Light and dark mode** following system preference. |

### 8.3 Content requirements
- Content in Sections 4–7 is the approved v1 baseline.
- Each role page must have: Quick Pitch ≤ 60 words, 8–10 key terms, ≥ 4 cross-questions, 3-stage roadmap.
- Salary data: sourced only from official/reputable sources (US Bureau of Labor Statistics Occupational Outlook Handbook; Canada's Job Bank wage data) with source name and date displayed; reviewed every 6 months.
- Certification names and exam codes verified against vendor sites before launch and each quarterly review (vendors retire/rename exams).
- Work-authorisation terminology reviewed quarterly against USCIS/IRCC and approved by compliance.

### 8.4 Suggested data model (per role)

```json
{
  "id": "cloud-engineer",
  "name": "Cloud Engineer",
  "category": "Tech & AI",
  "icon": "cloud",
  "oneLiner": "Builds and runs company systems on AWS, Azure and Google Cloud.",
  "quickPitch": "...",
  "dayToDay": ["..."],
  "altTitles": ["AWS Engineer", "Azure Engineer", "Cloud Architect"],
  "keyTerms": [{ "term": "IaC", "definition": "..." }],
  "tools": { "Cloud": ["AWS", "Azure", "GCP"], "IaC": ["Terraform"] },
  "certifications": [{ "name": "AWS Solutions Architect – Associate", "level": "Associate", "note": "..." }],
  "roadmap": { "foundation": ["..."], "jobReady": ["..."], "advanced": ["..."] },
  "background": "...",
  "industries": ["..."],
  "resumeKeywords": ["..."],
  "crossQuestions": [{ "q": "...", "a": "..." }],
  "relatedRoles": ["devops-engineer", "cybersecurity-analyst"],
  "salary": { "us": null, "ca": null, "source": null, "asOf": null },
  "quiz": [{ "q": "...", "options": ["..."], "answer": 0 }],
  "lastReviewed": "2026-10-30"
}
```

### 8.5 Design & UX guidelines
- Clean, professional, high-contrast layout; one accent colour per category (Tech & AI, Engineering, Business).
- Role cards with simple icons; no stock photos.
- Generous spacing, max text width ~75 characters for readability.
- Tables scroll horizontally on small screens.
- Quick Pitch in a coloured callout; cross-questions in accordions; roadmap shown as a 3-step horizontal timeline (stacked on mobile).

### 8.6 Recommended tech stack (any equivalent is acceptable)
- **Option A (simplest):** hand-built HTML/CSS/vanilla JS + one `roles.json`; client-side search with Fuse.js.
- **Option B (recommended for maintainability):** static-site generator (Astro, Eleventy, Hugo or Docusaurus) with Markdown/JSON content files and built-in search (e.g., Pagefind).
- **Hosting:** Netlify, Vercel, Cloudflare Pages, GitHub Pages (private + access control), or internal company server/SharePoint.
- **Analytics (optional):** privacy-friendly page-view analytics (e.g., Plausible), no personal data.

---

## 9. Delivery plan

### 9.1 Milestones

| Phase | Deliverable | Duration |
|---|---|---|
| 1. Content finalisation | Review/approve Sections 4–7; verify certifications; add salary data with sources; compliance review of 7.4 | Week 1–2 |
| 2. Design | Wireframes: home, role page, Live Call Mode, compare, glossary; design sign-off | Week 2 |
| 3. Build | Data file, templates, search, glossary generation, compare page | Week 3–4 |
| 4. Quiz & polish | Self-quiz, print CSS, accessibility pass, dark mode | Week 4–5 |
| 5. UAT | 3–5 sales reps test on real call scenarios; fix issues | Week 5 |
| 6. Launch & training | Launch, 60-minute team walkthrough, onboarding checklist updated | Week 6 |

### 9.2 Acceptance criteria
- All 17 role pages live, each passing the content checklist in 8.3.
- Searching any alternate title or key term listed in the content returns the correct role within the top 3 results.
- A new rep can find the answer to any of 10 randomly chosen cross-questions in under 20 seconds (tested in UAT).
- Site passes automated accessibility check (Lighthouse accessibility ≥ 90) and performance target in NFR-2.
- Compliance has signed off on Section 7.4 wording.
- Access is restricted to company users; pages are not indexed by search engines.

### 9.3 Roles & responsibilities

| Role | Responsibility |
|---|---|
| Product owner (Sales Head) | Final approval, priorities, success tracking |
| Content owner (Sales Trainer / SME) | Content accuracy, quarterly reviews, feedback inbox |
| Technical reviewers (internal/external SMEs) | Verify tech & engineering content per category |
| Web developer / designer | Build, hosting, accessibility |
| Compliance / Legal | Approve guardrails and work-authorisation wording |

### 9.4 Maintenance
- **Quarterly** content review (tools, certifications, cross-questions from real calls).
- **Every 6 months** salary data refresh.
- **Ongoing**: reps submit new candidate questions via the feedback link; the content owner adds the best ones to the relevant role.
- Changelog page listing updates so reps know what's new.

### 9.5 Risks & mitigations

| Risk | Mitigation |
|---|---|
| Outdated content (tools/certs change fast, esp. AI and cloud) | Quarterly review, "last reviewed" dates, feedback link |
| Reps over-promise using technical talk | Compliance guardrails on every page; training on "don't guess" script |
| Incorrect immigration information shared | Terms-only, links to official sources, compliance approval |
| Low adoption | Live Call Mode, fast search, manager-led quizzes in onboarding |
| Content too technical for new reps | Plain-English rule, Quick Pitch first, UAT with newest reps |
| Internal content exposed publicly | Access control + noindex |

### 9.6 Future enhancements (v2+)
- Add more roles (Data Engineer, Business Analyst, QA/Test Engineer, Project Manager, Network Engineer, SAP consultant, Healthcare IT).
- AI-powered "Ask the guide" search assistant.
- Call-script generator per role.
- Integration with CRM for role-tagged leads.
- Hindi/regional-language explanations for training sessions.
- Candidate-facing public version (with marketing review).
