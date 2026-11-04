import json
import os

# Load existing data/roles.json
with open('data/roles.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Real-world examples dictionary for all 18 roles
real_world_examples = {
    "ai-ml-engineer": [
        {
            "title": "Real-Time E-Commerce Recommendation Engine",
            "industry": "E-Commerce & Retail",
            "scenario": "An online marketplace with 15 million active products experienced high cart abandonment and low cross-selling rates during seasonal traffic spikes.",
            "whatTheyDo": "Trained a two-tower deep learning retrieval model and an approximate nearest-neighbor vector search index (Pinecone) using PyTorch; deployed the inference service via FastAPI on Kubernetes with automated drift monitoring in MLflow.",
            "impact": "Delivered sub-40ms personalized product recommendations, increasing average order value (AOV) by 14% and generating $6.2M in incremental annual revenue."
        },
        {
            "title": "Real-Time Credit Card Fraud Detection Pipeline",
            "industry": "Fintech & Banking",
            "scenario": "A digital banking app needed to evaluate transaction legitimacy in milliseconds without introducing noticeable latency to customer checkouts.",
            "whatTheyDo": "Engineered high-velocity feature stores using Feast, trained an ensemble gradient-boosted decision tree (XGBoost) model on historical fraudulent transactions, and deployed it into AWS SageMaker endpoints with autoscaling.",
            "impact": "Scored over 8,000 transactions per second in under 35 milliseconds, catching 92% of fraudulent attempts while reducing false positives by 28%."
        }
    ],
    "data-scientist": [
        {
            "title": "Predictive Customer Churn & Retention Strategy",
            "industry": "Telecommunications & SaaS",
            "scenario": "A subscription broadband provider was losing 3.8% of its subscriber base monthly without knowing which customers were at risk prior to cancellation.",
            "whatTheyDo": "Extracted and cleaned 3 years of customer billing, call center complaints, and network outage records with SQL and Pandas; built a random forest and logistic regression model that ranked high-risk customers 60 days before contract expiration.",
            "impact": "Identified top 15% high-risk accounts for proactive customer success outreach and targeted loyalty discounts, cutting churn by 18% and preserving $4.1M in annual recurring revenue."
        },
        {
            "title": "Hospital 30-Day Readmission Risk Scoring",
            "industry": "Healthcare Systems",
            "scenario": "A regional hospital network faced federal Medicare penalties for high 30-day readmission rates among post-surgical and chronic care patients.",
            "whatTheyDo": "Conducted statistical cohort analyses and survival modeling on anonymized Electronic Health Records (EHR) using Python (scikit-learn, lifelines); translated model outputs into an interactive Power BI risk dashboard for floor doctors and discharge coordinators.",
            "impact": "Reduced unplanned 30-day patient readmissions by 16% and avoided over $1.2M in federal Medicare reimbursement penalties."
        }
    ],
    "data-engineer": [
        {
            "title": "Streaming Fleet Telematics & Real-Time Logistics Pipeline",
            "industry": "Logistics & Supply Chain",
            "scenario": "A nationwide freight trucking carrier with 12,000 vehicles needed real-time GPS, fuel consumption, and engine diagnostic analytics to optimize delivery routes.",
            "whatTheyDo": "Designed an event-driven data streaming pipeline using Apache Kafka on AWS; processed incoming telemetry streams with PySpark on Databricks, partitioned raw data in Amazon S3, and populated live Snowflake analytical tables.",
            "impact": "Handled 25,000 events per second with sub-5-second latency, enabling dynamic rerouting that saved 1.2 million gallons of diesel fuel annually."
        },
        {
            "title": "Automated Enterprise Financial Reporting & Data Warehouse Migration",
            "industry": "Fintech & Enterprise SaaS",
            "scenario": "A fintech company's legacy relational database was crashing every morning during financial ledger reconciliations, delaying executive reporting by 6 hours.",
            "whatTheyDo": "Migrated legacy batch jobs to Apache Airflow DAGs; orchestrated modular dbt SQL models to transform raw transactional logs into star-schema dimension tables in Google BigQuery, implementing automated Great Expectations data quality tests.",
            "impact": "Reduced daily reporting ETL runtimes from 6 hours to 28 minutes, eliminated reporting discrepancies to 0%, and saved $80,000 in monthly database compute costs."
        }
    ],
    "cybersecurity-analyst": [
        {
            "title": "High-Severity Ransomware Phishing Triage & Containment",
            "industry": "Enterprise IT & Corporate Security",
            "scenario": "An employee in accounting opened an email attachment containing an obfuscated macro payload that began attempting lateral movement across corporate file shares.",
            "whatTheyDo": "Investigated anomalous network connection alerts in Splunk SIEM; isolated the infected host endpoint via CrowdStrike Falcon EDR within 9 minutes, analyzed the malware hash in a sandbox, and revoked compromised Active Directory credentials.",
            "impact": "Contained the threat before any files were encrypted or exfiltrated, preventing a multi-million-dollar ransomware extortion demand."
        },
        {
            "title": "Cloud Vulnerability Management & Compliance Remediation",
            "industry": "Healthcare SaaS",
            "scenario": "A health-tech platform preparing for SOC 2 Type II and HIPAA audits discovered untracked open ports and unpatched dependencies across its AWS environment.",
            "whatTheyDo": "Configured automated vulnerability scans with Tenable Nessus and AWS Security Hub; prioritized CVE vulnerabilities by CVSS severity score, worked with DevOps to patch open SSL vulnerabilities, and established a continuous CI/CD security audit trail.",
            "impact": "Remediated 100% of critical and high vulnerabilities within 14 days, achieving clean SOC 2 Type II and HIPAA certification without external auditor findings."
        }
    ],
    "cloud-engineer": [
        {
            "title": "Multi-Tier Legacy Banking Application Migration to AWS",
            "industry": "Banking & Financial Services",
            "scenario": "A commercial bank needed to migrate its core loan processing system off aging on-premises servers to comply with modern disaster recovery standards.",
            "whatTheyDo": "Authored Infrastructure as Code (IaC) in Terraform to provision a high-availability AWS architecture featuring multi-AZ VPCs, Application Load Balancers, autoscaling EC2 instances, and Amazon Aurora PostgreSQL with cross-region read replicas.",
            "impact": "Achieved 99.99% system availability, reduced failover recovery time from 4 hours to under 3 minutes, and passed strict OCC banking regulatory compliance."
        },
        {
            "title": "Enterprise FinOps & Cloud Cost Optimization",
            "industry": "High-Growth SaaS",
            "scenario": "A high-growth tech company's monthly cloud bill surged past $220,000 due to unmonitored development clusters, idle storage volumes, and unreserved compute.",
            "whatTheyDo": "Audited AWS Cost Explorer and CloudWatch metrics; transitioned unattached EBS volumes, moved 40 TB of static media to Amazon S3 Intelligent-Tiering, downsized over-provisioned EC2 instances, and purchased 1-year Savings Plans.",
            "impact": "Reduced monthly cloud expenditures by $68,000 (31% ongoing savings) without impacting production performance or developer velocity."
        }
    ],
    "devops-engineer": [
        {
            "title": "Automated Zero-Downtime Microservices CI/CD Pipeline",
            "industry": "E-Commerce & Digital Media",
            "scenario": "A retail website suffered 30-minute maintenance outages and frequent bug rollbacks during weekly deployment windows.",
            "whatTheyDo": "Built automated CI/CD pipelines in GitHub Actions and ArgoCD; packaged Node.js and Go microservices into Docker containers, orchestrated canary releases on Kubernetes (EKS), and configured Prometheus/Grafana automated rollbacks if HTTP 5xx error rates spiked above 0.5%.",
            "impact": "Increased deployment frequency from once a week to 15 times per day with zero customer downtime, reducing deployment rollback frequency by 80%."
        },
        {
            "title": "Disaster Recovery Automation & Infrastructure as Code",
            "industry": "Fintech Platform",
            "scenario": "A financial payments platform required automated cross-region disaster recovery to meet compliance requirements for payment processor licenses.",
            "whatTheyDo": "Codified 100% of cloud resources into modular Terraform and Ansible scripts; automated database replication between US-East and US-West, and scripted automated DNS failover drills via Route 53.",
            "impact": "Cut disaster recovery Recovery Time Objective (RTO) from 4 hours to 8 minutes, successfully passing annual third-party payment compliance audits."
        }
    ],
    "software-developer": [
        {
            "title": "Full-Stack Customer Self-Service Portal & Payment Integration",
            "industry": "Consumer Services & Fintech",
            "scenario": "A national utility service needed to replace an outdated desktop client with a modern, responsive web application for 2 million residential customers.",
            "whatTheyDo": "Engineered a front-end portal using React, TypeScript, and Tailwind CSS; built high-throughput RESTful backend endpoints in Java Spring Boot, integrated Stripe billing APIs with idempotent webhook processing, and wrote Jest unit tests.",
            "impact": "Handled 150,000 daily active users, boosted on-time digital bill payments by 26%, and cut call center customer billing inquiries by 40%."
        },
        {
            "title": "High-Performance Inventory API & Database Query Optimization",
            "industry": "Omnichannel Retail",
            "scenario": "An e-commerce order management system crashed under peak traffic spikes due to slow database queries and N+1 query loops.",
            "whatTheyDo": "Profiled API bottlenecks using APM tools; refactored slow SQL queries with composite indexes, replaced synchronous database lookups with a distributed Redis cache layer, and implemented asynchronous message queues in RabbitMQ.",
            "impact": "Reduced API response latency from 1,200ms to 45ms, enabling the platform to process 4,000 concurrent checkout requests during holiday flash sales without error."
        }
    ],
    "prompt-engineer": [
        {
            "title": "Automated Legal Contract Analysis & Risk Extraction Agent",
            "industry": "Enterprise Legal & Corporate Governance",
            "scenario": "In-house corporate attorneys spent 20 hours per week manually reviewing 80-page supplier agreements for non-standard indemnity and liability clauses.",
            "whatTheyDo": "Designed structured chain-of-thought prompts, JSON schema enforcement templates, and few-shot examples using OpenAI GPT-4; integrated a vector database (Chroma) for retrieval-augmented contract clause comparison and built automated accuracy evaluation scripts.",
            "impact": "Reduced contract first-pass review time from 4 hours to 12 minutes with 98.4% clause extraction precision, saving over 600 attorney hours per quarter."
        },
        {
            "title": "Multi-Turn Customer Support AI Agent with Guardrails",
            "industry": "E-Commerce & Consumer Brands",
            "scenario": "A global fashion retailer needed an automated chatbot to handle returns and order tracking without hallucinating fake policies or leaking internal company prompts.",
            "whatTheyDo": "Engineered multi-turn dialog state prompts with strict NeMo Guardrails and tool-calling parameters (OpenAI Function Calling); connected the LLM to inventory and shipping APIs while injecting security guardrails against jailbreaking.",
            "impact": "Autonomously resolved 62% of incoming support tickets on first contact, reduced agent response time to 15 seconds, and recorded zero brand-safety prompt injection incidents."
        }
    ],
    "civil-engineer": [
        {
            "title": "Highway Interchange Reconstruction & Stormwater Drainage Design",
            "industry": "Transportation & Municipal Infrastructure",
            "scenario": "A growing suburban corridor experienced severe traffic congestion and recurring localized flooding along a state highway junction.",
            "whatTheyDo": "Modeled 3D roadway corridors, superelevations, and grading surfaces in AutoCAD Civil 3D; conducted hydrological runoff calculations for 100-year storm events in HydroCAD, and designed detention ponds and culvert networks complying with Department of Transportation specs.",
            "impact": "Eliminated roadway flooding hazard, improved commuter travel times by 22%, and obtained environmental agency permit approval on the first submission."
        },
        {
            "title": "Commercial High-Rise Deep Foundation & Earth Retention Design",
            "industry": "Commercial Structural Engineering",
            "scenario": "A 28-story mixed-use commercial tower required deep foundation engineering in dense urban soil adjacent to an active subway line.",
            "whatTheyDo": "Analyzed soil boring reports and rock core samples; designed drilled shaft caissons, reinforced concrete foundation mats, and a soldier pile retention wall, verifying structural settlements using finite-element geotechnical modeling.",
            "impact": "Prevented ground subsidence adjacent to municipal transit tunnels and safely supported structural loads for a $110M skyscraper development."
        }
    ],
    "construction-manager": [
        {
            "title": "On-Schedule Hospital Surgical Wing Expansion ($55M Project)",
            "industry": "Healthcare Construction",
            "scenario": "A metropolitan hospital required a multi-story surgical wing expansion while adjacent emergency rooms and patient care floors remained 100% operational.",
            "whatTheyDo": "Built and maintained the project master schedule in Primavera P6; coordinated daily work across 18 trade subcontractors in Procore, managed strict infection-control barrier protocols (ICRA), and resolved mechanical clashes in field BIM coordination meetings.",
            "impact": "Delivered the $55M facility 2 weeks ahead of schedule with zero patient care disruptions and zero OSHA recordable safety incidents across 180,000 labor hours."
        },
        {
            "title": "320-Unit Mixed-Use Urban Apartment Complex Build",
            "industry": "Residential Multi-Family",
            "scenario": "A multi-family development faced severe material lead-time delays on structural timber and HVAC units, threatening delivery before tenant move-in dates.",
            "whatTheyDo": "Re-sequenced critical path trade schedules; negotiated alternative supply chains with local building distributors, managed daily field superintendent inspections, and controlled subcontractor change orders.",
            "impact": "Protected the developer's delivery schedule, completed municipal building inspections on time, and finished $380,000 under the approved contingency budget."
        }
    ],
    "mechanical-engineer": [
        {
            "title": "Thermal Management & Crash Enclosure for EV Battery Packs",
            "industry": "Automotive & Electric Vehicles",
            "scenario": "An electric vehicle startup needed a lightweight battery enclosure that could rapidly dissipate heat during fast charging and prevent thermal runaway in side-impact collisions.",
            "whatTheyDo": "Designed extruded aluminum tray structures and serpentine liquid cooling channels in SolidWorks; conducted finite element analysis (FEA) for structural impact and computational fluid dynamics (CFD) in ANSYS to optimize coolant flow distribution.",
            "impact": "Reduced battery pack mass by 12% while keeping battery cell temperatures below 35°C during rapid charging, passing all regulatory crash-safety certifications."
        },
        {
            "title": "High-Speed Automated Medical Device Packaging Machinery",
            "industry": "Medical Devices & Industrial Automation",
            "scenario": "A medical syringe manufacturer needed an automated packaging line that assembled, blister-packed, and laser-marked 300 units per minute with zero mechanical jamming.",
            "whatTheyDo": "Engineered servo-driven pick-and-place mechanisms, cam linkages, and pneumatic actuators in Creo; selected precision bearings, calculated motor torque requirements, and applied strict GD&T tolerances for CNC machining.",
            "impact": "Increased factory packaging throughput by 45%, reduced equipment downtime for seal adjustments by 60%, and met ISO 13485 medical device cleanroom standards."
        }
    ],
    "electrical-engineer": [
        {
            "title": "Industrial Substation Power Distribution & Arc Flash Safety Study",
            "industry": "Utility & Industrial Power Systems",
            "scenario": "A heavy manufacturing facility upgrading to automated machinery required a power distribution overhaul and updated safety labeling to prevent electrical flashover hazards.",
            "whatTheyDo": "Modeled the plant's 13.8kV to 480V electrical single-line distribution in ETAP; calculated short-circuit fault currents, designed protective relay time-current coordination curves (TCC), and generated NFPA 70E compliant arc flash safety warning labels.",
            "impact": "Eliminated nuisance circuit breaker tripping during high-demand motor starts and brought the entire 400,000 sq ft facility into full OSHA and NFPA 70E compliance."
        },
        {
            "title": "Automated Factory Robotics PLC & Control Panel Integration",
            "industry": "Industrial Automation & Robotics",
            "scenario": "An automotive tier-1 supplier needed an automated robotic welding line to communicate seamlessly with hydraulic presses and safety light curtains.",
            "whatTheyDo": "Designed electrical schematics and panel layouts in AutoCAD Electrical; programmed Allen-Bradley ControlLogix PLCs in ladder logic, integrated Fanuc robotic arms over EtherNet/IP, and built touchscreen operator HMIs in FactoryTalk View.",
            "impact": "Reduced weld cycle time by 18%, achieved 99.4% equipment reliability, and safeguarded machine operators with category-4 safety circuit interlocks."
        }
    ],
    "process-engineer": [
        {
            "title": "Petrochemical Distillation Column Yield & Energy Optimization",
            "industry": "Chemical Refining & Energy",
            "scenario": "A chemical refinery's distillation train was consuming excessive steam energy while losing valuable hydrocarbon product in the bottom residual stream.",
            "whatTheyDo": "Developed steady-state and dynamic process models in Aspen Plus; analyzed temperature and pressure profiles across column trays, optimized reflux ratios and feed preheating, and updated plant DCS operating setpoints.",
            "impact": "Increased high-purity chemical yield by 4.2% while reducing reboiler steam consumption by 11%, generating $2.1M in annual operating cost savings."
        },
        {
            "title": "Continuous Pharmaceutical Bioreactor Scale-Up & Debottlenecking",
            "industry": "Biotechnology & Pharmaceuticals",
            "scenario": "A biotech drug manufacturer needed to scale up an active monoclonal antibody therapy from a 50-liter pilot fermenter to a 2,000-liter commercial production bioreactor.",
            "whatTheyDo": "Calculated mass transfer coefficients, oxygen transfer rates (OTR), and mixing shear limits; updated Piping & Instrumentation Diagrams (P&IDs), selected hygienic sanitary valves, and tuned automated pH and dissolved oxygen control loops.",
            "impact": "Successfully scaled up commercial production batches with identical cellular growth yields, cutting batch cycle time by 14 hours and satisfying FDA cGMP requirements."
        }
    ],
    "validation-engineer": [
        {
            "title": "Sterile Autoclave & Lyophilizer Qualification (IQ/OQ/PQ)",
            "industry": "Pharmaceutical & Biologics",
            "scenario": "A commercial sterile injectable facility installed a new pharmaceutical steam autoclave and freeze-dryer that required complete qualification prior to clinical batch release.",
            "whatTheyDo": "Authored and executed Installation, Operational, and Performance Qualification protocols (IQ/OQ/PQ); placed 36 wireless temperature and pressure data loggers across the chamber to prove thermal uniformity and sterility kill kinetics (F0 values).",
            "impact": "Validated chamber temperature distribution within ±0.5°C across full loads, submitted deviation-free validation reports, and secured FDA pre-approval inspection clearance."
        },
        {
            "title": "Laboratory Information Management System (LIMS) Computer Validation",
            "industry": "Medical Diagnostics & Pharma Testing",
            "scenario": "A high-throughput QC testing laboratory transitioned from paper logbooks to a cloud-hosted LIMS software, requiring rigorous compliance with FDA 21 CFR Part 11 electronic records laws.",
            "whatTheyDo": "Created a User Requirements Specification (URS) and Traceability Matrix; executed software challenge tests for user privilege tiers, electronic signatures, time-stamped audit trails, and data backup disaster recovery protocols (GAMP 5).",
            "impact": "Validated 100% of regulatory requirements with full audit traceability, eliminating data integrity non-conformance risks and cutting QA batch release review time from 3 days to 4 hours."
        }
    ],
    "digital-marketing-specialist": [
        {
            "title": "High-Intent B2B Paid Search (Google Ads) & Conversion Optimization",
            "industry": "B2B SaaS & Tech",
            "scenario": "A cybersecurity software company was spending $60,000 per month on Google Ads with high click costs ($38/click) and poor lead quality that sales reps rejected.",
            "whatTheyDo": "Restructured campaigns by buyer intent and search themes; eliminated wasteful generic queries with extensive negative keyword lists, authored high-relevance Responsive Search Ads, and set up Google Tag Manager conversion triggers feeding into Google Analytics 4 (GA4).",
            "impact": "Decreased Cost Per Qualified Lead (CPL) by 41% while increasing monthly demo requests from 85 to 190, contributing $1.6M to the sales pipeline."
        },
        {
            "title": "Multi-Channel Paid Social (Meta & TikTok) E-Commerce Scaling",
            "industry": "Direct-to-Consumer (D2C) Retail",
            "scenario": "A sustainable apparel brand wanted to scale holiday sales across Meta (Instagram/Facebook) and TikTok without seeing return on ad spend (ROAS) collapse.",
            "whatTheyDo": "Tested 40 creative variations (UGC videos, product carousels); created custom lookalike and dynamic product retargeting audiences, and optimized bidding using Advantage+ shopping campaigns.",
            "impact": "Scaled monthly advertising spend from $20,000 to $95,000 while maintaining a 3.8x blended ROAS, generating $360,000 in monthly gross revenue."
        }
    ],
    "marketing-manager": [
        {
            "title": "National Omni-Channel Product Launch Strategy ($1.5M Budget)",
            "industry": "Consumer Packaged Goods (CPG)",
            "scenario": "A health beverage company needed a coordinated nationwide retail and digital marketing launch to achieve shelf placement across 2,500 target grocery stores.",
            "whatTheyDo": "Managed a $1.5M integrated launch budget; directed digital advertising, creator influencer partnerships, retail end-cap merchandising, and PR agency outreach while tracking customer acquisition costs (CAC) and brand sentiment.",
            "impact": "Achieved 120% of first-quarter retail sell-through targets, secured placement in major national chains (Target, Whole Foods), and boosted national brand awareness by 35%."
        },
        {
            "title": "Account-Based Marketing (ABM) Enterprise Demand Generation",
            "industry": "Enterprise Cloud Software",
            "scenario": "An enterprise HR software firm struggled to engage Fortune 500 decision-makers using traditional mass marketing email blasts.",
            "whatTheyDo": "Partnered with enterprise sales leaders to curate a target list of 250 strategic accounts; coordinated personalized LinkedIn InMail campaigns, tailored executive research briefs, and hosted invite-only VIP dinner roundtables.",
            "impact": "Generated 42 enterprise discovery meetings, added $5.2M in qualified sales opportunities, and shortened enterprise sales cycles by 28 days."
        }
    ],
    "product-manager": [
        {
            "title": "Mobile Banking App Onboarding Redesign & KYC Automation",
            "industry": "Fintech & Mobile Banking",
            "scenario": "A digital banking app experienced a 44% user drop-off rate during identity verification and document upload, losing prospective account holders.",
            "whatTheyDo": "Analyzed user session funnels in Mixpanel and conducted user research interviews; wrote technical PRDs and user stories, prioritized engineering sprints using the RICE framework, and integrated an automated AI identity verification SDK.",
            "impact": "Reduced onboarding completion time from 9 minutes to under 2 minutes, boosted account activation rates from 56% to 83%, and added 45,000 active new accounts in the first quarter."
        },
        {
            "title": "Enterprise Self-Service Billing & Admin Console Launch",
            "industry": "B2B SaaS",
            "scenario": "Corporate clients generated 35% of all customer support tickets asking for manual seat license additions, invoice downloads, and SSO configurations.",
            "whatTheyDo": "Defined product roadmap and wireframed intuitive self-service portal workflows with UX designers; led weekly agile scrum rituals with engineering, and launched the portal with in-app Pendo walkthroughs.",
            "impact": "Reduced billing support ticket volume by 48%, enabled instant self-service upgrades that drove $850,000 in net expansion revenue, and improved enterprise CSAT by 22 points."
        }
    ],
    "supply-chain-analyst": [
        {
            "title": "Multi-Warehouse Inventory Safety Stock & EOQ Optimization",
            "industry": "Retail & E-Commerce Logistics",
            "scenario": "A national home goods retailer suffered from recurring stockouts on high-velocity items while carrying millions of dollars in stagnant, slow-moving inventory across 5 regional distribution centers.",
            "whatTheyDo": "Extracted historical order lines and vendor lead times using SQL; performed ABC inventory classification, calculated optimal Economic Order Quantities (EOQ) and dynamic safety stock thresholds in Python and Excel, and automated weekly purchase reorder triggers.",
            "impact": "Decreased warehouse stockouts by 28% during peak season while reducing excess safety stock, unlocking $2.4M in cash flow."
        },
        {
            "title": "Global Ocean Carrier Freight Performance & Demurrage Analytics",
            "industry": "International Manufacturing & Logistics",
            "scenario": "A manufacturing importer faced unpredictable container arrival delays and surging demurrage detention penalties at West Coast container ports.",
            "whatTheyDo": "Aggregated shipping manifest and EDI carrier data into an interactive Power BI dashboard; tracked container dwell times, port congestion metrics, and on-time delivery rates across 8 global shipping lines to hold carriers accountable.",
            "impact": "Cut container demurrage detention fines by $340,000 annually and provided supply chain leadership with the data leverage needed to negotiate 12% lower ocean contract rates."
        }
    ]
}

# Define the complete Data Engineer role object
data_engineer_role = {
    "id": "data-engineer",
    "name": "Data Engineer",
    "category": "Tech & AI",
    "icon": "database",
    "oneLiner": "Designs, builds, and maintains the data pipelines and infrastructure that deliver clean, reliable data for analytics and AI.",
    "quickPitch": "A Data Engineer builds the digital plumbing of a company — extracting data from databases, apps, and logs, cleaning it, and loading it into data warehouses like Snowflake or BigQuery. They ensure data scientists and business analysts have fresh, accurate, and reliable data ready to use.",
    "dayToDay": [
        "Design, build, and maintain scalable ETL/ELT pipelines using tools like Apache Spark, Airflow, and dbt.",
        "Ingest data from diverse sources (APIs, transactional SQL databases, event streams like Kafka) into central data lakes or warehouses (Snowflake, BigQuery, Databricks).",
        "Optimize query performance, data partitioning, indexing, and storage costs across cloud platforms.",
        "Implement automated data quality checks, schema evolution tests, and monitoring alerts for pipeline failures.",
        "Collaborate with Data Scientists, Software Developers, and BI Analysts to provide production-ready tables and feature stores."
    ],
    "altTitles": [
        "Big Data Engineer",
        "Data Pipeline Engineer",
        "Analytics Engineer",
        "Data Platform Engineer",
        "ETL Developer",
        "Cloud Data Engineer",
        "Database Engineer"
    ],
    "keyTerms": [
        {
            "term": "ETL / ELT",
            "definition": "Extract, Transform, Load (or Extract, Load, Transform) — the process of copying data from sources, reshaping it, and loading it into an analytical warehouse."
        },
        {
            "term": "Data Pipeline",
            "definition": "An automated series of steps that moves data from where it's created to where it can be analyzed."
        },
        {
            "term": "Data Warehouse",
            "definition": "A centralized database optimized for fast business reporting and analytics (e.g., Snowflake, Google BigQuery, Amazon Redshift)."
        },
        {
            "term": "Data Lake",
            "definition": "A vast storage repository that holds raw, unstructured or semi-structured data in its native format until needed (e.g., AWS S3, Azure Data Lake)."
        },
        {
            "term": "Batch vs Streaming",
            "definition": "Batch processes data in scheduled chunks (e.g., nightly); streaming processes each record instantly in real-time as it occurs (e.g., Kafka)."
        },
        {
            "term": "Apache Spark",
            "definition": "A fast, distributed engine for processing massive datasets across clusters of computers."
        },
        {
            "term": "Airflow / Orchestration",
            "definition": "A workflow scheduler that manages when each data task runs, handles retries, and enforces task dependencies."
        },
        {
            "term": "dbt (data build tool)",
            "definition": "A tool that lets data teams transform raw warehouse data using simple SQL select statements and automated testing."
        },
        {
            "term": "Schema (Star / Snowflake)",
            "definition": "The architectural blueprint organizing warehouse tables into facts (numbers) and dimensions (context like dates, customers)."
        },
        {
            "term": "Data Quality / Lineage",
            "definition": "Tracking the origin and journey of data, and validating that rows are accurate, complete, and not duplicated."
        }
    ],
    "toolsSummary": "Python, SQL; Apache Spark, PySpark; Apache Airflow, Prefect, Dagster; Snowflake, Databricks, BigQuery, Amazon Redshift; dbt; Apache Kafka, AWS Kinesis; Docker, Kubernetes; AWS (S3, Glue, EMR), Azure (Data Factory, Synapse), GCP (BigQuery, Dataflow); Git.",
    "toolsList": [
        "Python, SQL",
        "Apache Spark, PySpark",
        "Apache Airflow, Prefect, Dagster",
        "Snowflake, Databricks, BigQuery, Amazon Redshift",
        "dbt",
        "Apache Kafka, AWS Kinesis",
        "Docker, Kubernetes",
        "AWS (S3, Glue, EMR)",
        "Azure (Data Factory, Synapse)",
        "GCP (BigQuery, Dataflow)",
        "Git"
    ],
    "certificationsSummary": "AWS Certified Data Engineer – Associate (DEA-C01), Databricks Certified Data Engineer Associate/Professional, Google Cloud Professional Data Engineer, Snowflake SnowPro Core, Microsoft Certified: Azure Data Engineer Associate (DP-203).",
    "certificationsList": [
        "AWS Certified Data Engineer – Associate (DEA-C01)",
        "Databricks Certified Data Engineer Associate/Professional",
        "Google Cloud Professional Data Engineer",
        "Snowflake SnowPro Core",
        "Microsoft Certified: Azure Data Engineer Associate (DP-203)"
    ],
    "roadmap": {
        "foundation": "Advanced SQL (window functions, CTEs, indexing), Python data structures and scripting, relational database design (PostgreSQL/MySQL), Git version control, Linux command line.",
        "jobReady": "Cloud data warehousing (Snowflake, BigQuery, or Redshift), distributed data processing with Apache Spark/PySpark, workflow orchestration (Apache Airflow), data modeling with dbt, building REST API connectors, Docker basics, 2–3 end-to-end pipeline portfolio projects on GitHub.",
        "advanced": "Real-time streaming architectures (Kafka, Flink), Lakehouse architecture (Delta Lake, Apache Iceberg), Infrastructure as Code (Terraform) for data infrastructure, CI/CD for data pipelines (DataOps), data governance, performance tuning at petabyte scale."
    },
    "background": "Computer Science, Information Systems, Software Engineering, Electrical Engineering, Mathematics, or transitions from Database Administrator (DBA), Software Developer, or Data Analyst.",
    "industries": [
        "Tech & SaaS",
        "Finance & Fintech",
        "Healthcare & Life Sciences",
        "E-commerce & Retail",
        "Telecommunications",
        "Media & Streaming",
        "Consulting"
    ],
    "industriesSummary": "Tech & SaaS, Finance & Fintech, Healthcare & Life Sciences, E-commerce & Retail, Telecommunications, Media & Streaming, Consulting.",
    "resumeKeywords": [
        "Python",
        "SQL (Advanced)",
        "Apache Spark / PySpark",
        "Snowflake / Databricks / BigQuery",
        "Airflow / ETL Pipelines",
        "dbt",
        "Kafka / Streaming",
        "Cloud (AWS / Azure / GCP)",
        "Pipeline optimization (\"reduced pipeline runtime by 45%\")"
    ],
    "resumeKeywordsSummary": "Python, SQL (Advanced), Apache Spark / PySpark, Snowflake / Databricks / BigQuery, Airflow / ETL Pipelines, dbt, Kafka / Streaming, Cloud (AWS / Azure / GCP), Pipeline optimization (\"reduced pipeline runtime by 45%\").",
    "crossQuestions": [
        {
            "q": "What is the difference between a Data Engineer, a Data Scientist, and a Data Analyst?",
            "a": "A Data Engineer builds and maintains the pipelines and databases that deliver clean data; a Data Analyst examines that data to answer business questions; and a Data Scientist builds machine learning models to predict future trends. We position your profile clearly around your pipeline building and infrastructure strengths."
        },
        {
            "q": "Is Big Data (Spark, Kafka) required for every Data Engineer role, or is SQL/dbt enough?",
            "a": "Many modern companies focus heavily on the Modern Data Stack (SQL + dbt + Snowflake/BigQuery) for business analytics; massive scale tech or streaming companies require Spark and Kafka. We highlight whichever stack you excel in to match the right job postings."
        },
        {
            "q": "Should I learn AWS, Azure, or GCP for Data Engineering?",
            "a": "AWS and Azure have the highest overall job volume, while GCP is prominent in startup and analytics-heavy environments. Mastering one primary cloud data stack (e.g. AWS S3 + Glue + Redshift, or Azure Data Factory + Synapse/Databricks) is what recruiters look for, and skills transfer easily."
        },
        {
            "q": "How do I make my resume stand out without 5+ years of experience?",
            "a": "Recruiters love measurable efficiency and scale: highlight the volume of data processed (e.g. 'processed 5M daily events'), cost savings on cloud warehouse compute, pipeline execution speedups (e.g. 'reduced ETL runtime from 4 hours to 45 minutes'), and include a public GitHub repo with an automated Airflow + dbt pipeline."
        }
    ],
    "relatedRoles": [
        "data-scientist",
        "cloud-engineer",
        "devops-engineer",
        "software-developer",
        "ai-ml-engineer"
    ],
    "salary": {
        "us": "$125,000 - $175,000 (Median ~$145,000)",
        "ca": "CAD $100,000 - $145,000",
        "source": "US Bureau of Labor Statistics (BLS) / Canada Job Bank",
        "asOf": "2026-10"
    },
    "quiz": [
        {
            "q": "What is the primary objective of an ETL or ELT pipeline built by a Data Engineer?",
            "options": [
                "To generate marketing copy and design visual logos.",
                "To extract data from source systems, transform it into a clean analytical format, and load it into a central warehouse.",
                "To write client-side CSS stylesheets for web applications.",
                "To configure local office Wi-Fi routers and printers."
            ],
            "answer": 1,
            "explanation": "ETL/ELT pipelines extract raw data from disparate operational systems, reshape/clean it, and load it into an analytical data warehouse for reporting and machine learning."
        },
        {
            "q": "Which tool is an industry standard workflow orchestration platform used by Data Engineers to schedule and monitor complex pipelines?",
            "options": [
                "Apache Airflow",
                "Figma",
                "AutoCAD",
                "Wireshark"
            ],
            "answer": 0,
            "explanation": "Apache Airflow (along with Prefect and Dagster) is the industry standard orchestration tool used to schedule, sequence, and monitor data pipeline DAGs."
        },
        {
            "q": "What is the difference between a Data Warehouse and a Data Lake?",
            "options": [
                "A Data Warehouse is only stored on USB flash drives; a Data Lake is an on-premises physical pond.",
                "A Data Warehouse stores structured, schema-on-write data optimized for fast SQL queries; a Data Lake stores vast amounts of raw data in various formats (structured, semi-structured, unstructured).",
                "A Data Warehouse is only used by human resources; a Data Lake is only used by civil engineers.",
                "There is no difference; the terms are 100% interchangeable in enterprise architecture."
            ],
            "answer": 1,
            "explanation": "Data warehouses (like Snowflake or BigQuery) enforce schemas for fast analytical SQL, whereas data lakes (like AWS S3) store raw files in native formats (Parquet, JSON, CSV) prior to transformation."
        },
        {
            "q": "What role does dbt (data build tool) play in modern data engineering?",
            "options": [
                "It replaces Python entirely for machine learning inference.",
                "It allows data teams to write modular SQL transformation logic directly inside the data warehouse, complete with version control and automated data tests.",
                "It is an optical character recognition tool for scanning paper documents.",
                "It is a network firewall used to block DDoS attacks."
            ],
            "answer": 1,
            "explanation": "dbt enables the 'T' in ELT by allowing engineers and analytics engineers to transform raw warehouse data using modular SQL SELECT queries, documentation, and automated assertions."
        },
        {
            "q": "What is Apache Spark primarily used for in Big Data engineering?",
            "options": [
                "Fast, distributed in-memory data processing across large clusters of machines for massive datasets.",
                "Editing vector graphics and company logos.",
                "Measuring electrical voltage in utility power grids.",
                "Sending bulk email marketing newsletters."
            ],
            "answer": 0,
            "explanation": "Apache Spark is a distributed computing engine that processes huge volumes of data in parallel memory across clusters, dramatically outperforming traditional MapReduce."
        }
    ],
    "realWorldExamples": real_world_examples["data-engineer"]
}

# 1. Update existing roles with realWorldExamples
for role in data['roles']:
    rid = role['id']
    if rid in real_world_examples:
        role['realWorldExamples'] = real_world_examples[rid]
        # Also ensure Data Engineer is added to relatedRoles where appropriate
        if rid in ["data-scientist", "cloud-engineer", "devops-engineer", "software-developer", "ai-ml-engineer"]:
            if "data-engineer" not in role['relatedRoles']:
                role['relatedRoles'].append("data-engineer")

# 2. Add Data Engineer role if not already present
de_exists = any(r['id'] == 'data-engineer' for r in data['roles'])
if not de_exists:
    # Insert right after Data Scientist (index 2)
    ds_idx = next((i for i, r in enumerate(data['roles']) if r['id'] == 'data-scientist'), 0)
    data['roles'].insert(ds_idx + 1, data_engineer_role)
    print("Added data-engineer role to roles list.")
else:
    # Update existing
    for i, r in enumerate(data['roles']):
        if r['id'] == 'data-engineer':
            data['roles'][i] = data_engineer_role
            print("Updated existing data-engineer role.")

# 3. Update categories: ensure 'data-engineer' is in Tech & AI
tech_cat = next((c for c in data['categories'] if c['id'] == 'tech-ai'), None)
if tech_cat and 'data-engineer' not in tech_cat['roles']:
    # Insert after data-scientist
    if 'data-scientist' in tech_cat['roles']:
        idx = tech_cat['roles'].index('data-scientist')
        tech_cat['roles'].insert(idx + 1, 'data-engineer')
    else:
        tech_cat['roles'].append('data-engineer')
    print("Added data-engineer to Tech & AI category roles list.")

# 4. Add comparison between Data Scientist and Data Engineer
de_comp_exists = any(c.get('pair') == "Data Scientist vs Data Engineer" for c in data.get('comparisons', []))
if not de_comp_exists:
    data['comparisons'].insert(1, {
        "pair": "Data Scientist vs Data Engineer",
        "roleA": "Data Scientist",
        "roleB": "Data Engineer",
        "difference": "Statistical models & predictive insights vs building scalable data pipelines & warehouse infrastructure."
    })
    print("Added Data Scientist vs Data Engineer comparison.")

# 5. Add Data Engineer key terms to glossary
existing_glossary_terms = {item['term'].lower(): item for item in data.get('glossary', [])}
for kt in data_engineer_role['keyTerms']:
    term_key = kt['term'].lower()
    if term_key not in existing_glossary_terms:
        data['glossary'].append({
            "term": kt['term'],
            "definition": kt['definition'],
            "roleId": "data-engineer",
            "roleName": "Data Engineer",
            "category": "Tech & AI"
        })
    else:
        # If term exists, make sure role tags mention Data Engineer if appropriate
        pass

# Re-sort glossary alphabetically by term
data['glossary'] = sorted(data['glossary'], key=lambda x: x['term'].lower())

# Save data/roles.json
with open('data/roles.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# Save data/roles-data.js
with open('data/roles-data.js', 'w', encoding='utf-8') as f:
    f.write('/** Auto-generated from PRD baseline content */\n')
    f.write('window.ROLES_DATA = ')
    json.dump(data, f, indent=2, ensure_ascii=False)
    f.write(';\n')

print(f"Update complete! Total roles: {len(data['roles'])}")
print(f"Tech & AI roles count: {len(tech_cat['roles'])}")
for r in data['roles']:
    print(f"- {r['name']}: {len(r.get('realWorldExamples', []))} real-world examples")
