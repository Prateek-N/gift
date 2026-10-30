import re
import json
import os

with open('PRD_Job_Roles_Knowledge_Guide.md', 'r', encoding='utf-8') as f:
    text = f.read()

role_configs = [
    {
        "id": "ai-ml-engineer",
        "header": "4.1 AI / Machine Learning Engineer",
        "name": "AI / Machine Learning Engineer",
        "category": "Tech & AI",
        "icon": "cpu",
        "oneLiner": "Builds systems that learn from data and deploy AI/ML models to production at scale.",
        "relatedRoles": ["data-scientist", "prompt-engineer", "software-developer", "cloud-engineer"],
        "salary": {
            "us": "$135,000 - $190,000 (Median ~$155,000)",
            "ca": "CAD $110,000 - $160,000",
            "source": "US Bureau of Labor Statistics (BLS) / Canada Job Bank",
            "asOf": "2026-10"
        },
        "quiz": [
            {
                "q": "What is the key difference between a Data Scientist and an ML Engineer?",
                "options": [
                    "Data Scientists build and maintain hardware servers; ML Engineers write web pages.",
                    "Data Scientists focus on analyzing data and finding insights; ML Engineers focus on building and deploying models into scalable production software.",
                    "ML Engineers only work with spreadsheets, while Data Scientists only program in C++.",
                    "There is no difference; they are identical job titles with identical day-to-day tasks."
                ],
                "answer": 1,
                "explanation": "Data Scientists uncover insights and develop initial models, whereas ML Engineers take those models and engineer robust, production-ready software systems around them."
            },
            {
                "q": "What does RAG stand for in modern AI application development?",
                "options": [
                    "Random Automated Generation",
                    "Retrieval-Augmented Generation",
                    "Recursive Algorithm Gradients",
                    "Real-time Analytical Graphing"
                ],
                "answer": 1,
                "explanation": "Retrieval-Augmented Generation (RAG) grounds an LLM by pulling relevant knowledge/documents from a vector database before generating an answer."
            },
            {
                "q": "What is MLOps?",
                "options": [
                    "A brand of machine learning computer processors.",
                    "DevOps practices applied to machine learning: automating deployment, monitoring, and versioning of ML models.",
                    "A legal compliance document required for training neural networks in California.",
                    "An open-source spreadsheet used for manual data labeling."
                ],
                "answer": 1,
                "explanation": "MLOps applies continuous integration, deployment, and monitoring practices to ML models in production (e.g. using tools like MLflow, Kubeflow, SageMaker)."
            },
            {
                "q": "Which framework is currently the most widely used for training modern deep learning models?",
                "options": [
                    "PyTorch",
                    "jQuery",
                    "Ruby on Rails",
                    "Bootstrap"
                ],
                "answer": 0,
                "explanation": "PyTorch (along with TensorFlow) is the standard deep learning framework in research and modern AI production."
            },
            {
                "q": "How should a sales rep respond if a candidate asks: 'Is GenAI / LLM experience really necessary for ML roles today?'",
                "options": [
                    "Tell them GenAI is a fad and recruiters never ask about it.",
                    "Affirm that many modern postings emphasize LLMs and RAG, and assure them we'll prominently showcase any GenAI projects they have.",
                    "Advise them to change their entire career path to marketing immediately.",
                    "Promise them a $200k salary if they take one 10-minute online tutorial."
                ],
                "answer": 1,
                "explanation": "Acknowledging the industry surge in LLM/RAG requirements and reassuring the candidate that we highlight their practical projects builds confidence and credibility."
            }
        ]
    },
    {
        "id": "data-scientist",
        "header": "4.2 Data Scientist",
        "name": "Data Scientist",
        "category": "Tech & AI",
        "icon": "bar-chart-2",
        "oneLiner": "Uses data, statistics and machine learning to answer business questions and predict outcomes.",
        "relatedRoles": ["ai-ml-engineer", "software-developer", "supply-chain-analyst"],
        "salary": {
            "us": "$110,000 - $165,000 (Median ~$135,000)",
            "ca": "CAD $95,000 - $140,000",
            "source": "US Bureau of Labor Statistics (BLS) / Canada Job Bank",
            "asOf": "2026-10"
        },
        "quiz": [
            {
                "q": "What is the primary difference between a Data Analyst and a Data Scientist?",
                "options": [
                    "Data Analysts build deep neural networks; Data Scientists only write SQL queries.",
                    "Data Analysts primarily analyze past data and create reports/dashboards; Data Scientists use statistical modeling and ML to predict future outcomes.",
                    "Data Scientists do not use programming languages.",
                    "Data Analysts require a PhD, whereas Data Scientists need no degree."
                ],
                "answer": 1,
                "explanation": "Analysts focus on descriptive and diagnostic analytics (what happened), while Data Scientists use advanced predictive modeling and machine learning."
            },
            {
                "q": "What is 'Overfitting' in machine learning?",
                "options": [
                    "When a computer case is too small for the graphics card.",
                    "When a model memorizes training data so closely that it performs poorly on new, unseen data.",
                    "When a dataset has too many duplicate rows deleted.",
                    "When an algorithm finishes training in less than 5 minutes."
                ],
                "answer": 1,
                "explanation": "Overfitting happens when a model learns noise and specific details of the training set instead of generalized underlying patterns."
            },
            {
                "q": "Which two technical tools are fundamental prerequisites found on almost every Data Scientist job description?",
                "options": [
                    "Photoshop and Canva",
                    "Python and SQL",
                    "AutoCAD and SolidWorks",
                    "Ruby and Swift"
                ],
                "answer": 1,
                "explanation": "SQL is ubiquitous for querying and extracting data from relational warehouses, and Python is the standard for statistical analysis and machine learning."
            },
            {
                "q": "What is an A/B test?",
                "options": [
                    "A standardized typing test required during hiring.",
                    "A controlled experiment comparing two versions (A and B) to determine which produces better performance or user engagement.",
                    "An automated unit test checking code indentation.",
                    "A grading scale for data warehouse cleanliness."
                ],
                "answer": 1,
                "explanation": "A/B testing is the gold standard randomized experimentation method for evaluating product changes and feature impacts with statistical rigor."
            },
            {
                "q": "If an entry-level candidate worries they don't have a Master's degree for Data Science, what should the rep say?",
                "options": [
                    "Tell them without a Master's or PhD they can never get an interview.",
                    "Explain that while graduate degrees are common, strong end-to-end projects, solid SQL/Python skills, and relevant experience can bridge the gap.",
                    "Offer to forge educational credentials on their resume.",
                    "Advise them to apply only for administrative assistant roles."
                ],
                "answer": 1,
                "explanation": "Proven portfolio projects, Kaggle accomplishments, and strong practical problem-solving frequently open doors despite not having an advanced degree."
            }
        ]
    },
    {
        "id": "cybersecurity-analyst",
        "header": "4.3 Cybersecurity Analyst",
        "name": "Cybersecurity Analyst",
        "category": "Tech & AI",
        "icon": "shield",
        "oneLiner": "Protects company networks, endpoints and data from cyber threats and security incidents.",
        "relatedRoles": ["cloud-engineer", "devops-engineer"],
        "salary": {
            "us": "$95,000 - $145,000 (Median ~$120,000)",
            "ca": "CAD $85,000 - $125,000",
            "source": "US Bureau of Labor Statistics (BLS) / Canada Job Bank",
            "asOf": "2026-10"
        },
        "quiz": [
            {
                "q": "What is the primary function of a Security Operations Center (SOC)?",
                "options": [
                    "Managing payroll and employee onboarding.",
                    "Monitoring network traffic, system logs, and security alerts 24/7 to identify and respond to attacks.",
                    "Designing company logos and visual marketing material.",
                    "Writing business contracts for enterprise sales."
                ],
                "answer": 1,
                "explanation": "A SOC acts as a 24/7 centralized command post monitoring alerts, investigating telemetry, and stopping cyber intruders."
            },
            {
                "q": "What is a SIEM tool?",
                "options": [
                    "Security Information and Event Management software (e.g. Splunk, Sentinel) that aggregates and analyzes enterprise security logs.",
                    "A hardware cable used to connect monitors to computers.",
                    "An encrypted USB flash drive.",
                    "A regulatory law passed by the European Parliament."
                ],
                "answer": 0,
                "explanation": "SIEM systems ingest logs across servers, firewalls, and cloud environments to detect anomalies and trigger security alerts."
            },
            {
                "q": "Which certification is widely recognized as the top entry-level credential for Cybersecurity Analysts?",
                "options": [
                    "CISSP (requires 5 years verifiable experience)",
                    "CompTIA Security+",
                    "PMP (Project Management Professional)",
                    "Six Sigma Black Belt"
                ],
                "answer": 1,
                "explanation": "CompTIA Security+ is standard baseline proof of cybersecurity and networking fundamentals for entry and junior security roles."
            },
            {
                "q": "What does GRC stand for in enterprise information security?",
                "options": [
                    "General Routing Configuration",
                    "Governance, Risk, and Compliance",
                    "Global Resource Computation",
                    "Graphical Recovery Console"
                ],
                "answer": 1,
                "explanation": "GRC covers corporate governance, assessing security risks, and verifying compliance against regulatory frameworks like SOC 2, ISO 27001, and HIPAA."
            },
            {
                "q": "If a candidate without US citizenship asks about federal defense cybersecurity jobs, what must the rep explain?",
                "options": [
                    "Guarantee that they can bypass security clearance easily.",
                    "Clarify that US government and defense roles usually require security clearance restricted to US citizens, and recommend focusing on commercial/private sector roles.",
                    "Advise them to apply anyway and claim citizenship.",
                    "Tell them they can never work in tech in North America."
                ],
                "answer": 1,
                "explanation": "Honesty regarding security clearance restrictions protects the candidate's time and directs marketing efforts toward the thriving private enterprise sector."
            }
        ]
    },
    {
        "id": "cloud-engineer",
        "header": "4.4 Cloud Engineer",
        "name": "Cloud Engineer",
        "category": "Tech & AI",
        "icon": "cloud",
        "oneLiner": "Designs, provisions and runs scalable cloud infrastructure on AWS, Azure, and GCP.",
        "relatedRoles": ["devops-engineer", "cybersecurity-analyst", "software-developer"],
        "salary": {
            "us": "$115,000 - $165,000 (Median ~$130,000)",
            "ca": "CAD $95,000 - $140,000",
            "source": "US Bureau of Labor Statistics (BLS) / Canada Job Bank",
            "asOf": "2026-10"
        },
        "quiz": [
            {
                "q": "What is 'Infrastructure as Code' (IaC)?",
                "options": [
                    "Writing code on physical printouts kept in a binder.",
                    "Defining, provisioning, and managing IT infrastructure through code and configuration files (e.g. Terraform) rather than manual console clicking.",
                    "A coding boot camp program.",
                    "A network protocol for wireless printers."
                ],
                "answer": 1,
                "explanation": "IaC allows repeatable, automated, version-controlled cloud infrastructure deployment using tools like Terraform and CloudFormation."
            },
            {
                "q": "What is the primary difference between a Cloud Engineer and a DevOps Engineer?",
                "options": [
                    "Cloud Engineers build cloud servers, networks, and storage; DevOps Engineers focus specifically on automating the software CI/CD delivery lifecycle.",
                    "Cloud Engineers do not use computers.",
                    "DevOps Engineers only install physical fiber-optic cables.",
                    "There is no overlap whatsoever between the two domains."
                ],
                "answer": 0,
                "explanation": "Cloud Engineers specialize in cloud infrastructure and networking; DevOps Engineers emphasize automated building, testing, and deployment pipelines."
            },
            {
                "q": "Which cloud provider currently holds the highest enterprise adoption among organizations heavily invested in Microsoft environments?",
                "options": [
                    "AWS",
                    "Microsoft Azure",
                    "Google Cloud Platform (GCP)",
                    "DigitalOcean"
                ],
                "answer": 1,
                "explanation": "Microsoft Azure integrates seamlessly with Active Directory, Windows Server, Office 365, and enterprise .NET environments."
            },
            {
                "q": "What does a Virtual Private Cloud (VPC) provide?",
                "options": [
                    "A free online storage drive for personal photos.",
                    "An isolated, private virtual network within a public cloud provider where resources can run securely.",
                    "A virtual reality headset for developers.",
                    "A public web server open to all internet traffic by default."
                ],
                "answer": 1,
                "explanation": "A VPC provides network isolation, subnets, routing tables, and security gateways in the cloud."
            },
            {
                "q": "Which certification is widely considered the flagship benchmark for AWS cloud engineers?",
                "options": [
                    "AWS Certified Solutions Architect – Associate",
                    "Adobe Certified Professional",
                    "Certified Scrum Master",
                    "Google Ads Certification"
                ],
                "answer": 0,
                "explanation": "AWS Solutions Architect – Associate is the most recognized industry benchmark testing core AWS services, architecture, security, and cost efficiency."
            }
        ]
    },
    {
        "id": "devops-engineer",
        "header": "4.5 DevOps Engineer",
        "name": "DevOps Engineer",
        "category": "Tech & AI",
        "icon": "git-merge",
        "oneLiner": "Automates build, test, and release CI/CD pipelines to deliver software quickly and reliably.",
        "relatedRoles": ["cloud-engineer", "software-developer"],
        "salary": {
            "us": "$120,000 - $170,000 (Median ~$138,000)",
            "ca": "CAD $100,000 - $145,000",
            "source": "US Bureau of Labor Statistics (BLS) / Canada Job Bank",
            "asOf": "2026-10"
        },
        "quiz": [
            {
                "q": "What does CI/CD stand for in modern software engineering?",
                "options": [
                    "Continuous Integration / Continuous Delivery (or Deployment)",
                    "Centralized Intelligence / Customer Delivery",
                    "Code Inspection / Certified Development",
                    "Computer Interface / Cloud Device"
                ],
                "answer": 0,
                "explanation": "CI/CD automates the building, testing, and shipping of code updates safely and quickly to production."
            },
            {
                "q": "What is the primary benefit of containerization using Docker?",
                "options": [
                    "It physically shrinks the size of computer microchips.",
                    "It packages application code together with its libraries and dependencies so it executes identically in any environment.",
                    "It eliminates the need to ever write unit tests.",
                    "It translates Python code directly into assembly language."
                ],
                "answer": 1,
                "explanation": "Docker ensures environmental consistency from local developer laptops to testing staging and production clusters."
            },
            {
                "q": "What is Kubernetes (K8s)?",
                "options": [
                    "A specialized Linux text editor.",
                    "An open-source container orchestration engine that automates deploying, scaling, and managing containerized applications.",
                    "A relational database query engine.",
                    "A proprietary hardware router manufactured by Cisco."
                ],
                "answer": 1,
                "explanation": "Kubernetes is the industry-standard platform for clustering, auto-scaling, and healing containers in production."
            },
            {
                "q": "How does an SRE (Site Reliability Engineer) differ slightly from a traditional DevOps role?",
                "options": [
                    "SREs never touch code.",
                    "SRE applies software engineering principles specifically to operational reliability, defining SLAs/SLOs and error budgets.",
                    "DevOps engineers only work on mainframe computers.",
                    "SRE is exclusively a hardware repair role."
                ],
                "answer": 1,
                "explanation": "Originated at Google, SRE uses software engineering discipline to manage availability, latency, performance, and incident response."
            },
            {
                "q": "Which metric demonstrates the most impactful resume bullet for a DevOps Engineer?",
                "options": [
                    "'Read 15 books on technology.'",
                    "'Reduced deployment time from 2 hours to 15 minutes through automated Jenkins/GitHub Actions CI/CD pipelines.'",
                    "'Liked 500 LinkedIn posts about technology.'",
                    "'Attended daily team meetings on time.'"
                ],
                "answer": 1,
                "explanation": "Quantifiable engineering impact (speed of deployment, uptime improvement, error reduction) is what employers look for."
            }
        ]
    },
    {
        "id": "software-developer",
        "header": "4.6 Software Developer",
        "name": "Software Developer",
        "category": "Tech & AI",
        "icon": "code",
        "oneLiner": "Designs, writes, tests, and maintains applications and back-end services across tech stacks.",
        "relatedRoles": ["devops-engineer", "product-manager", "ai-ml-engineer"],
        "salary": {
            "us": "$105,000 - $160,000 (Median ~$127,000)",
            "ca": "CAD $85,000 - $130,000",
            "source": "US Bureau of Labor Statistics (BLS) / Canada Job Bank",
            "asOf": "2026-10"
        },
        "quiz": [
            {
                "q": "What is the distinction between Front-end and Back-end development?",
                "options": [
                    "Front-end is everything the user sees and interacts with (UI); Back-end handles data storage, business logic, and servers.",
                    "Front-end is only for graphic designers with no coding; Back-end requires no databases.",
                    "Front-end is written in C++; Back-end is written in HTML.",
                    "There is no distinction in modern software."
                ],
                "answer": 0,
                "explanation": "Front-end focuses on the client UI/browser interface, while Back-end handles business logic, database queries, and APIs."
            },
            {
                "q": "What is a REST API?",
                "options": [
                    "A tool that forces developers to take regular breaks.",
                    "An architectural style for network communication allowing applications to exchange data over HTTP using standard methods like GET, POST, PUT, DELETE.",
                    "A special brand of computer monitor.",
                    "An encryption algorithm used exclusively by banks."
                ],
                "answer": 1,
                "explanation": "REST APIs are the universal standard for client-server and microservice communication across the web."
            },
            {
                "q": "What does a Pull Request (PR) represent in Git collaboration?",
                "options": [
                    "A request to buy new computer hardware.",
                    "A proposal to merge code changes from one branch into another, inviting peer review and automated testing before inclusion.",
                    "An error notification indicating a crash.",
                    "A request to terminate a developer's contract."
                ],
                "answer": 1,
                "explanation": "Pull Requests allow peer review, discussion, automated linting, and continuous integration checks before merging changes."
            },
            {
                "q": "Why are Data Structures and Algorithms (DSA) frequently practiced on platforms like LeetCode?",
                "options": [
                    "They are legally mandated by the US Department of Labor.",
                    "Many US tech interviews include technical coding rounds that evaluate algorithmic problem solving and time/space complexity.",
                    "DSA is only used for video game graphics.",
                    "It replaces the need to learn SQL."
                ],
                "answer": 1,
                "explanation": "Technical coding screens at North American employers commonly test core algorithmic problem-solving and efficiency."
            },
            {
                "q": "Which programming languages represent the highest enterprise demand across US/Canada job boards?",
                "options": [
                    "COBOL and Fortran",
                    "Java, Python, JavaScript/TypeScript, and C#/.NET",
                    "Pascal and Visual Basic 6",
                    "Perl and ActionScript"
                ],
                "answer": 1,
                "explanation": "Java, Python, TypeScript/JavaScript, and C# dominate modern enterprise backend and full-stack software development postings."
            }
        ]
    },
    {
        "id": "prompt-engineer",
        "header": "4.7 Prompt Engineer",
        "name": "Prompt Engineer",
        "category": "Tech & AI",
        "icon": "message-square",
        "oneLiner": "Crafts instructions and evaluates workflows for Large Language Models to deliver reliable AI outputs.",
        "relatedRoles": ["ai-ml-engineer", "product-manager"],
        "salary": {
            "us": "$90,000 - $150,000 (Median ~$115,000)",
            "ca": "CAD $80,000 - $130,000",
            "source": "Emerging Role / Tech Salary Survey Data",
            "asOf": "2026-10"
        },
        "quiz": [
            {
                "q": "What is 'Hallucination' in the context of Large Language Models?",
                "options": [
                    "When the GPU overheats and shuts down.",
                    "When an AI model generates factually incorrect or fabricated information with high confidence.",
                    "When an AI model translates English into French.",
                    "When the user inputs non-English characters."
                ],
                "answer": 1,
                "explanation": "Hallucination refers to models generating confident, believable-sounding assertions that are completely untrue."
            },
            {
                "q": "What is the difference between Zero-shot and Few-shot prompting?",
                "options": [
                    "Zero-shot provides no prompt text; Few-shot provides ten paragraphs of code.",
                    "Zero-shot asks the model to perform a task without demonstration examples; Few-shot provides a few high-quality input-output examples in the prompt.",
                    "Zero-shot uses paid API tokens; Few-shot is always free.",
                    "Few-shot only works for image models."
                ],
                "answer": 1,
                "explanation": "Few-shot prompting provides context examples illustrating desired formatting and reasoning steps before asking the question."
            },
            {
                "q": "What is 'Chain-of-Thought' (CoT) prompting?",
                "options": [
                    "A technique that encourages the model to break down complex reasoning step-by-step before producing a final answer.",
                    "Linking multiple computers with physical cables.",
                    "A security protocol that encrypts prompt texts.",
                    "A method for training smaller models from scratch."
                ],
                "answer": 0,
                "explanation": "Asking a model to 'think step by step' forces it to output intermediate reasoning steps, drastically reducing errors in logic and math."
            },
            {
                "q": "Does a modern Prompt Engineer need programming skills?",
                "options": [
                    "No, writing English prompts in a browser interface is all that is ever required.",
                    "Yes, practical roles typically require basic Python and API scripting to run automated evaluations, connect vector stores, and build workflows.",
                    "Only assembly language is useful.",
                    "Only hardware electrical soldering."
                ],
                "answer": 1,
                "explanation": "Enterprise AI roles expect Python integration with APIs, LangChain, LlamaIndex, and systematic test harnesses."
            },
            {
                "q": "How does a sales rep market a candidate targeting Prompt Engineering?",
                "options": [
                    "Market them exclusively with the narrow title 'Prompt Writer'.",
                    "Position them broadly across GenAI Engineer, AI Solutions Specialist, and AI Product roles while highlighting prompt evaluation and RAG workflows as core skills.",
                    "Tell them to abandon AI and learn manual bookkeeping.",
                    "Guarantee them an immediate VP role at an AI lab."
                ],
                "answer": 1,
                "explanation": "Broadening target titles into GenAI Engineer and AI Solutions Specialist dramatically increases interview opportunities."
            }
        ]
    },
    {
        "id": "civil-engineer",
        "header": "5.1 Civil Engineer",
        "name": "Civil Engineer",
        "category": "Engineering, Construction & Manufacturing",
        "icon": "hard-hat",
        "oneLiner": "Designs and oversees physical infrastructure including roads, bridges, buildings, and water systems.",
        "relatedRoles": ["construction-manager"],
        "salary": {
            "us": "$85,000 - $130,000 (Median ~$95,000)",
            "ca": "CAD $78,000 - $115,000",
            "source": "US Bureau of Labor Statistics (BLS) / Canada Job Bank",
            "asOf": "2026-10"
        },
        "quiz": [
            {
                "q": "What is the key difference between a Civil Engineer and a Construction Manager?",
                "options": [
                    "Civil Engineers work only in banks; Construction Managers work only in chemical laboratories.",
                    "Civil Engineers primarily focus on design calculations, plans, and compliance; Construction Managers focus on physical site execution, scheduling, workers, and budgets.",
                    "There is no difference between design and execution.",
                    "Civil Engineers do not need a degree."
                ],
                "answer": 1,
                "explanation": "Civil engineers design and calculate structural/site systems; construction managers execute the physical build on site."
            },
            {
                "q": "What do the FE and PE designations mean in the United States?",
                "options": [
                    "Federal Employee and Private Employee",
                    "Fundamentals of Engineering (yielding EIT status) and Professional Engineer (legal license to stamp drawings)",
                    "Factory Electrician and Plant Electrician",
                    "Foreman Exam and Project Exam"
                ],
                "answer": 1,
                "explanation": "The FE exam qualifies graduates as Engineers-in-Training (EIT); the PE exam and required experience grant the license to stamp engineering drawings."
            },
            {
                "q": "What is BIM in modern infrastructure and building design?",
                "options": [
                    "Basic Industrial Material",
                    "Building Information Modeling — 3D intelligent model-based process (e.g. Autodesk Revit) for architecture, engineering, and construction.",
                    "Bridge Inspection Manual",
                    "Building Insurance Metric"
                ],
                "answer": 1,
                "explanation": "BIM tools like Revit create intelligent 3D models containing rich geometric and specification data."
            },
            {
                "q": "What CAD software is standard for land development, grading, and civil infrastructure?",
                "options": [
                    "Adobe Photoshop",
                    "Autodesk Civil 3D",
                    "Microsoft Paint",
                    "Canva"
                ],
                "answer": 1,
                "explanation": "Autodesk Civil 3D is the industry standard for civil grading, corridor design, pipe networks, and surveying."
            },
            {
                "q": "Can a candidate with an overseas civil engineering degree get a job in North America before completing the PE license?",
                "options": [
                    "No, it is strictly illegal to touch engineering drawings without a PE license.",
                    "Yes, many work successfully as EITs, Designers, or Project Engineers under the direct supervision of licensed PEs while pursuing licensure.",
                    "Only if they retake an undergraduate degree from scratch.",
                    "Only in federal government positions."
                ],
                "answer": 1,
                "explanation": "Junior and mid-level engineers work under licensed P.E. supervision while completing state credential evaluations and exam requirements."
            }
        ]
    },
    {
        "id": "construction-manager",
        "header": "5.2 Construction Manager",
        "name": "Construction Manager",
        "category": "Engineering, Construction & Manufacturing",
        "icon": "briefcase",
        "oneLiner": "Plans, coordinates, and manages construction builds from start to finish on time and within budget.",
        "relatedRoles": ["civil-engineer"],
        "salary": {
            "us": "$90,000 - $145,000 (Median ~$105,000)",
            "ca": "CAD $85,000 - $130,000",
            "source": "US Bureau of Labor Statistics (BLS) / Canada Job Bank",
            "asOf": "2026-10"
        },
        "quiz": [
            {
                "q": "What does an RFI stand for in construction project management?",
                "options": [
                    "Ready For Inspection",
                    "Request for Information — a formal written inquiry from the contractor to the architect/engineer clarifying drawings or specifications.",
                    "Required Field Invoice",
                    "Rebar Foundation Installation"
                ],
                "answer": 1,
                "explanation": "An RFI formally documents questions or gaps in blueprints and architectural specs."
            },
            {
                "q": "What is a 'Change Order'?",
                "options": [
                    "A request to switch worker shifts.",
                    "An approved, legally binding modification to the contract scope, budget, or completion date.",
                    "An order to return defective lumber.",
                    "A tool used to measure soil density."
                ],
                "answer": 1,
                "explanation": "Change orders capture alterations in project scope, materials, or unforeseen conditions that adjust schedule and billing."
            },
            {
                "q": "Which project management software is widely recognized as the market leader on commercial job sites?",
                "options": [
                    "Procore",
                    "Final Cut Pro",
                    "Audacity",
                    "Notepad"
                ],
                "answer": 0,
                "explanation": "Procore is the dominant cloud construction management platform connecting field supervisors, GCs, and subs."
            },
            {
                "q": "What is OSHA 30 certification in the US?",
                "options": [
                    "A 30-day driving test.",
                    "A 30-hour comprehensive training course on occupational safety and hazard recognition for construction supervisors.",
                    "A certification for crane operators only.",
                    "An environmental tax certificate."
                ],
                "answer": 1,
                "explanation": "OSHA 30 is the industry-standard safety credential required for superintendents, foremen, and project engineers on job sites."
            },
            {
                "q": "What is a 'Punch List' in construction?",
                "options": [
                    "A list of punches thrown during workplace disputes.",
                    "A list of minor deficiencies, repairs, and incomplete items compiled at near-completion before final payment and handover.",
                    "A daily attendance sheet for manual laborers.",
                    "A list of equipment parts to purchase."
                ],
                "answer": 1,
                "explanation": "The punch list ensures every detail, finish, and fixture meets contract quality before substantial completion."
            }
        ]
    },
    {
        "id": "mechanical-engineer",
        "header": "5.3 Mechanical Engineer",
        "name": "Mechanical Engineer",
        "category": "Engineering, Construction & Manufacturing",
        "icon": "settings",
        "oneLiner": "Designs, models, and tests mechanical devices, machines, thermal systems, and equipment.",
        "relatedRoles": ["process-engineer", "electrical-engineer"],
        "salary": {
            "us": "$85,000 - $135,000 (Median ~$99,000)",
            "ca": "CAD $75,000 - $118,000",
            "source": "US Bureau of Labor Statistics (BLS) / Canada Job Bank",
            "asOf": "2026-10"
        },
        "quiz": [
            {
                "q": "What is FEA (Finite Element Analysis)?",
                "options": [
                    "Federal Energy Assessment",
                    "A computerized simulation method (e.g. using ANSYS) to predict how physical parts react to forces, vibration, heat, and stress.",
                    "Final Expense Accounting",
                    "Factory Electrical Audit"
                ],
                "answer": 1,
                "explanation": "FEA breaks down complex geometries into mesh elements to analyze stress, deformation, and thermal performance."
            },
            {
                "q": "What is GD&T (Geometric Dimensioning and Tolerancing)?",
                "options": [
                    "A programming language for robotics.",
                    "A standardized system of symbols and rules on engineering drawings defining the allowable variation in geometric characteristics.",
                    "A brand of carbon fiber composite.",
                    "A legal patent document."
                ],
                "answer": 1,
                "explanation": "GD&T specifies exact manufacturing tolerances and datum references to ensure parts fit together reliably."
            },
            {
                "q": "What does DFM stand for in product development?",
                "options": [
                    "Design for Manufacturing — designing components so they can be produced easily and cost-effectively.",
                    "Direct Frequency Modulation",
                    "Data File Management",
                    "Differential Fluid Movement"
                ],
                "answer": 0,
                "explanation": "DFM optimizes part geometry, tooling, and materials to lower fabrication costs and prevent production defects."
            },
            {
                "q": "Which CAD modeling software is most prevalent in mid-sized product design and manufacturing companies?",
                "options": [
                    "SolidWorks",
                    "Microsoft Word",
                    "GIMP",
                    "VLC Media Player"
                ],
                "answer": 0,
                "explanation": "Dassault Systèmes SolidWorks is the industry workhorse for 3D mechanical modeling, assemblies, and drafting."
            },
            {
                "q": "What is a Bill of Materials (BOM)?",
                "options": [
                    "A monthly electricity bill.",
                    "A comprehensive list of raw materials, assemblies, components, and quantities required to manufacture an end product.",
                    "A certificate of hazardous waste disposal.",
                    "A shipping manifest for export customs."
                ],
                "answer": 1,
                "explanation": "The BOM is the master recipe detailing every screw, plate, sub-assembly, and drawing part number needed to assemble a machine."
            }
        ]
    },
    {
        "id": "electrical-engineer",
        "header": "5.4 Electrical Engineer",
        "name": "Electrical Engineer",
        "category": "Engineering, Construction & Manufacturing",
        "icon": "zap",
        "oneLiner": "Designs and tests electrical distribution systems, power grids, circuits, and industrial controls.",
        "relatedRoles": ["mechanical-engineer", "process-engineer"],
        "salary": {
            "us": "$90,000 - $140,000 (Median ~$106,000)",
            "ca": "CAD $80,000 - $125,000",
            "source": "US Bureau of Labor Statistics (BLS) / Canada Job Bank",
            "asOf": "2026-10"
        },
        "quiz": [
            {
                "q": "What is a PLC (Programmable Logic Controller)?",
                "options": [
                    "A personal laptop computer.",
                    "An industrial digital computer ruggedized for controlling manufacturing processes, assembly lines, and robotic equipment.",
                    "A type of high-voltage circuit breaker.",
                    "A solar panel inverter."
                ],
                "answer": 1,
                "explanation": "PLCs (from Rockwell/Allen-Bradley, Siemens) run deterministic automation logic in factories and plants."
            },
            {
                "q": "What code governs safe electrical installations and inspections in the United States?",
                "options": [
                    "The National Electrical Code (NEC / NFPA 70)",
                    "The Uniform Commercial Code",
                    "The International Roadway Code",
                    "The Digital Millennium Copyright Act"
                ],
                "answer": 0,
                "explanation": "The NEC (National Electrical Code) is the benchmark standard adopted across US states and municipalities for electrical safety."
            },
            {
                "q": "What software tool is the standard for power system design, load flow, and short circuit analysis?",
                "options": [
                    "ETAP or SKM PowerTools",
                    "Adobe InDesign",
                    "Audacity",
                    "WordPress"
                ],
                "answer": 0,
                "explanation": "ETAP and SKM are the recognized standard simulation packages for power distribution, arc flash studies, and load calculations."
            },
            {
                "q": "What is the difference between power systems engineering and electronics engineering?",
                "options": [
                    "Power focuses on high-voltage generation, transmission grids, and building distribution; Electronics focuses on low-voltage circuits, microchips, and PCBs.",
                    "Power engineers never work with electricity.",
                    "Electronics engineers only install power poles.",
                    "There is no difference."
                ],
                "answer": 0,
                "explanation": "Power deals with megawatts, substations, and utilities, while electronics centers on microchips, circuit boards, and signal processing."
            },
            {
                "q": "What does an Arc Flash study evaluate?",
                "options": [
                    "The brightness of welding torches.",
                    "The thermal energy and boundary distances released during an electrical fault to determine safety PPE for technicians.",
                    "The battery life of smartphones.",
                    "The speed of light in optical cables."
                ],
                "answer": 1,
                "explanation": "Arc flash studies analyze blast energy and calculate safe approach boundaries and PPE ratings required to protect electricians."
            }
        ]
    },
    {
        "id": "process-engineer",
        "header": "5.5 Process Engineer",
        "name": "Process Engineer",
        "category": "Engineering, Construction & Manufacturing",
        "icon": "activity",
        "oneLiner": "Optimizes chemical, industrial, and manufacturing processes for yield, safety, and efficiency.",
        "relatedRoles": ["mechanical-engineer", "validation-engineer"],
        "salary": {
            "us": "$88,000 - $135,000 (Median ~$102,000)",
            "ca": "CAD $80,000 - $120,000",
            "source": "US Bureau of Labor Statistics (BLS) / Canada Job Bank",
            "asOf": "2026-10"
        },
        "quiz": [
            {
                "q": "What does a P&ID represent in chemical and industrial processing?",
                "options": [
                    "Personal & Identification Document",
                    "Piping and Instrumentation Diagram — a detailed schematic showing piping, valves, instrumentation, and control loops.",
                    "Plant & Inventory Directory",
                    "Project & Invoice Detail"
                ],
                "answer": 1,
                "explanation": "P&IDs show the interconnected piping, sensors, pumps, heat exchangers, and control loops that run a plant."
            },
            {
                "q": "What does DMAIC stand for in Six Sigma process improvement?",
                "options": [
                    "Define, Measure, Analyze, Improve, Control",
                    "Design, Market, Assemble, Inspect, Clean",
                    "Divide, Multiply, Add, Integrate, Calculate",
                    "Direct, Manage, Audit, Investigate, Check"
                ],
                "answer": 0,
                "explanation": "DMAIC is the standard data-driven improvement methodology for eliminating process defects and reducing variability."
            },
            {
                "q": "What is SPC (Statistical Process Control)?",
                "options": [
                    "A secret company formula.",
                    "Using statistical methods and control charts to monitor and control process parameters within acceptable limits.",
                    "A federal environmental tax.",
                    "An inventory management barcode format."
                ],
                "answer": 1,
                "explanation": "SPC tracks critical process variables over time using control charts to identify and correct deviations before defects occur."
            },
            {
                "q": "What is a HAZOP study?",
                "options": [
                    "Hazard and Operability study — a structured systematic examination of a planned process to identify safety hazards and operational risks.",
                    "Hardware Allocation Zone Operation",
                    "Hazardous Operations Permit",
                    "Hourly Assembly Zone Optimization"
                ],
                "answer": 0,
                "explanation": "A HAZOP analyzes potential guide words (more flow, less pressure, reverse) to prevent industrial disasters."
            },
            {
                "q": "What is 'Scale-up' in process engineering?",
                "options": [
                    "Weighing raw materials on an electronic scale.",
                    "Transitioning a chemical or biochemical process from laboratory/pilot bench scale to commercial manufacturing volume.",
                    "Hiring additional operators for a night shift.",
                    "Adding more columns to an Excel worksheet."
                ],
                "answer": 1,
                "explanation": "Scale-up solves heat and mass transfer challenges when expanding a 5-liter lab recipe into a 10,000-liter commercial reactor."
            }
        ]
    },
    {
        "id": "validation-engineer",
        "header": "5.6 Validation Engineer",
        "name": "Validation Engineer",
        "category": "Engineering, Construction & Manufacturing",
        "icon": "check-circle",
        "oneLiner": "Documents and tests equipment, processes, and systems to ensure compliance with FDA/GMP standards.",
        "relatedRoles": ["process-engineer"],
        "salary": {
            "us": "$85,000 - $130,000 (Median ~$98,000)",
            "ca": "CAD $78,000 - $115,000",
            "source": "US Bureau of Labor Statistics (BLS) / Canada Job Bank",
            "asOf": "2026-10"
        },
        "quiz": [
            {
                "q": "What does the qualification lifecycle sequence 'IQ / OQ / PQ' stand for?",
                "options": [
                    "Inspection Quality, Output Quality, Production Quality",
                    "Installation Qualification, Operational Qualification, Performance Qualification",
                    "Internal Query, Official Query, Public Query",
                    "Initial Quote, Order Quote, Price Quote"
                ],
                "answer": 1,
                "explanation": "IQ verifies correct installation; OQ tests operational limits; PQ proves repeatable performance in simulated production conditions."
            },
            {
                "q": "What does FDA 21 CFR Part 11 regulate?",
                "options": [
                    "Food labeling on cereal boxes.",
                    "Criteria under which electronic records and electronic signatures are considered trustworthy, reliable, and equivalent to paper records.",
                    "The speed of packaging machinery.",
                    "Import duties on medical plastics."
                ],
                "answer": 1,
                "explanation": "21 CFR Part 11 establishes FDA requirements for audit trails, user authentication, and data integrity in computerized systems."
            },
            {
                "q": "What is GAMP 5?",
                "options": [
                    "A video gaming console.",
                    "Good Automated Manufacturing Practice guideline — a risk-based approach to compliant GxP computerized systems.",
                    "A medical diagnostic machine.",
                    "An emergency evacuation procedure."
                ],
                "answer": 1,
                "explanation": "GAMP 5 (by ISPE) is the premier international framework for validating life-sciences software and computer systems."
            },
            {
                "q": "What is a CAPA in pharmaceutical quality management?",
                "options": [
                    "Capacity Planning Analysis",
                    "Corrective and Preventive Action — systemic actions taken to investigate and resolve non-conformances and prevent recurrence.",
                    "Capital Asset Purchase Agreement",
                    "Certified Analytical Pharmacy Assistant"
                ],
                "answer": 1,
                "explanation": "CAPA is a mandatory regulatory process for systematically investigating defects and preventing future failures."
            },
            {
                "q": "What is the core distinction between Verification and Validation?",
                "options": [
                    "Verification tests: 'Did we build the system right according to specification?'; Validation tests: 'Did we build the right system that consistently meets its intended use in production?'",
                    "Verification is only done by accountants; Validation is done by sales reps.",
                    "There is no difference; they are exact synonyms.",
                    "Verification is only done after a product has already expired."
                ],
                "answer": 0,
                "explanation": "Verification checks technical specifications; validation provides documented evidence that the process reliably achieves intended clinical/quality results."
            }
        ]
    },
    {
        "id": "digital-marketing-specialist",
        "header": "6.1 Digital Marketing (Specialist / Executive)",
        "name": "Digital Marketing Specialist",
        "category": "Business, Marketing & Operations",
        "icon": "trending-up",
        "oneLiner": "Drives traffic, customer acquisition, and sales through SEO, paid ads, content, and analytics.",
        "relatedRoles": ["marketing-manager", "product-manager"],
        "salary": {
            "us": "$60,000 - $95,000 (Median ~$72,000)",
            "ca": "CAD $55,000 - $85,000",
            "source": "US Bureau of Labor Statistics (BLS) / Canada Job Bank",
            "asOf": "2026-10"
        },
        "quiz": [
            {
                "q": "What is the difference between SEO and SEM/PPC?",
                "options": [
                    "SEO optimizes content to earn organic (free) rankings on Google; SEM/PPC involves paying for ads to appear in search results.",
                    "SEO is only for mobile phones; SEM is for computers.",
                    "SEO requires coding in C++; SEM requires no internet.",
                    "There is no difference."
                ],
                "answer": 0,
                "explanation": "SEO drives organic traffic over time through optimization; SEM (PPC) purchases ad placements on search engines instantly."
            },
            {
                "q": "What does ROAS stand for in paid advertising?",
                "options": [
                    "Rate of Automated Sales",
                    "Return on Ad Spend — revenue generated divided by the dollars spent on advertising.",
                    "Relevance of Audience Segmentation",
                    "Return on Account Sponsorship"
                ],
                "answer": 1,
                "explanation": "ROAS (e.g. 4x or 400%) measures financial returns directly attributed to specific marketing advertising expenditure."
            },
            {
                "q": "What is GA4?",
                "options": [
                    "General Assembly meeting number 4.",
                    "Google Analytics 4 — the event-based web and app analytics platform used to track user behavior and conversions.",
                    "A new version of graphic design software.",
                    "A social media advertising network."
                ],
                "answer": 1,
                "explanation": "GA4 is Google's modern analytics platform tracking cross-platform event streams, engagement, and conversion paths."
            },
            {
                "q": "What does CTR measure in digital campaigns?",
                "options": [
                    "Computer Telephony Response",
                    "Click-Through Rate — the percentage of people who click on a link or ad after viewing it.",
                    "Cost to Refund",
                    "Conversion Tracking Ratio"
                ],
                "answer": 1,
                "explanation": "CTR = (Clicks / Impressions) * 100%, indicating how engaging the ad creative and headline are."
            },
            {
                "q": "What is the most critical item employers look for on a Digital Marketer's resume?",
                "options": [
                    "A list of high school awards.",
                    "Quantifiable campaign achievements: ROAS achieved, lead volume generated, CAC reduction, and budget sizes managed.",
                    "10 pages of social media screenshots.",
                    "A certificate of typing speed."
                ],
                "answer": 1,
                "explanation": "Marketing hiring managers want hard performance numbers demonstrating commercial return on spend."
            }
        ]
    },
    {
        "id": "marketing-manager",
        "header": "6.2 Marketing Manager",
        "name": "Marketing Manager",
        "category": "Business, Marketing & Operations",
        "icon": "target",
        "oneLiner": "Leads overall brand strategy, campaign planning, go-to-market execution, and marketing budgets.",
        "relatedRoles": ["digital-marketing-specialist", "product-manager"],
        "salary": {
            "us": "$100,000 - $160,000 (Median ~$135,000)",
            "ca": "CAD $85,000 - $135,000",
            "source": "US Bureau of Labor Statistics (BLS) / Canada Job Bank",
            "asOf": "2026-10"
        },
        "quiz": [
            {
                "q": "What is the key difference between a Marketing Manager and a Digital Marketing Specialist?",
                "options": [
                    "The Specialist focuses on hands-on tactical channel execution; the Manager owns overall strategy, budgets, brand positioning, and team coordination.",
                    "The Specialist has higher salary and manages all directors.",
                    "Marketing Managers do not use digital media.",
                    "There is no difference in seniority or responsibility."
                ],
                "answer": 0,
                "explanation": "Marketing Managers lead cross-functional strategy, budget allocation, and team/agency management."
            },
            {
                "q": "What is a 'Go-To-Market' (GTM) strategy?",
                "options": [
                    "A roadmap for opening a grocery store.",
                    "A comprehensive action plan specifying how a company will launch a product to customers to achieve competitive advantage and revenue.",
                    "An internal human resources policy.",
                    "A software patch deployment script."
                ],
                "answer": 1,
                "explanation": "A GTM strategy defines target audiences, marketing channels, pricing, sales enablement, and launch messaging."
            },
            {
                "q": "What does CAC to LTV ratio evaluate in business marketing?",
                "options": [
                    "Computer Access Code to Local Terminal Velocity.",
                    "Customer Acquisition Cost compared to Customer Lifetime Value — evaluating long-term profitability of marketing investments.",
                    "Click Algorithm Calculation to Lead Tracking Volume.",
                    "Corporate Asset Class to Loan Total Value."
                ],
                "answer": 1,
                "explanation": "A healthy LTV:CAC ratio (typically 3:1 or higher) proves that marketing generates profitable, sustainable customer relationships."
            },
            {
                "q": "What is the distinction between an MQL and an SQL?",
                "options": [
                    "Marketing Qualified Lead (deemed likely to buy by marketing based on engagement) vs Sales Qualified Lead (vetted and accepted by sales for direct outreach).",
                    "MQL is a database language; SQL is a spreadsheet.",
                    "MQL is a manager role; SQL is a specialist role.",
                    "They are identical terms."
                ],
                "answer": 0,
                "explanation": "MQLs enter the top of the funnel via marketing activities; sales reps review and qualify them into SQLs for pipeline deals."
            },
            {
                "q": "What role does a Product Marketing Manager (PMM) play compared to a core Product Manager (PM)?",
                "options": [
                    "The PMM decides how to position, message, and sell the product to the market; the PM defines what features get built with software engineers.",
                    "The PMM writes all software code; the PM runs Facebook ads.",
                    "PMM is an entry-level intern role; PM is the CEO.",
                    "Both roles only write technical documentation."
                ],
                "answer": 0,
                "explanation": "PMMs drive market positioning, customer persona research, competitive analysis, and sales enablement; PMs build the product with engineering."
            }
        ]
    },
    {
        "id": "product-manager",
        "header": "6.3 Product Manager",
        "name": "Product Manager",
        "category": "Business, Marketing & Operations",
        "icon": "layers",
        "oneLiner": "Defines product vision, requirements, and roadmaps to bridge customer needs and engineering.",
        "relatedRoles": ["software-developer", "marketing-manager"],
        "salary": {
            "us": "$115,000 - $175,000 (Median ~$140,000)",
            "ca": "CAD $95,000 - $150,000",
            "source": "US Bureau of Labor Statistics (BLS) / Canada Job Bank",
            "asOf": "2026-10"
        },
        "quiz": [
            {
                "q": "What is the primary distinction between a Product Manager and a Project Manager?",
                "options": [
                    "Product Managers determine WHAT to build and WHY (customer problems, value, vision); Project Managers coordinate HOW and WHEN it gets delivered (schedules, resources).",
                    "Project Managers are in charge of code architecture; Product Managers only handle finances.",
                    "They are the exact same title in every company.",
                    "Product Managers do not talk to engineers."
                ],
                "answer": 0,
                "explanation": "Product Managers own the product strategy and value proposition; Project Managers ensure timely, on-budget delivery of commitments."
            },
            {
                "q": "What is an MVP (Minimum Viable Product)?",
                "options": [
                    "Most Valuable Player in an office game.",
                    "The simplest version of a product that can be released to early customers to validate hypotheses and collect learning with least effort.",
                    "A product that has zero features.",
                    "A completed product after 5 years of development."
                ],
                "answer": 1,
                "explanation": "An MVP delivers core value quickly to test assumptions in the market without over-investing in unnecessary bells and whistles."
            },
            {
                "q": "What does a PRD stand for in tech product teams?",
                "options": [
                    "Public Relations Department",
                    "Product Requirements Document — the document defining the purpose, user stories, requirements, and metrics for a product feature.",
                    "Personnel Review Directory",
                    "Production Release Diagnostic"
                ],
                "answer": 1,
                "explanation": "A PRD details the user problems, functional requirements, success metrics, and release scope for the engineering and design teams."
            },
            {
                "q": "What is the RICE scoring model used for?",
                "options": [
                    "Cooking lunch in the cafeteria.",
                    "Prioritizing features based on Reach, Impact, Confidence, and Effort.",
                    "Calculating annual software license costs.",
                    "Screening employee resumes."
                ],
                "answer": 1,
                "explanation": "RICE helps Product Managers objectively score backlog ideas based on Reach * Impact * Confidence / Effort."
            },
            {
                "q": "Can a Business Analyst transition into a Product Manager role?",
                "options": [
                    "No, it is an entirely forbidden career shift.",
                    "Yes, it is one of the most common transition paths, leveraging shared competencies in requirements gathering, data analysis, and stakeholder alignment.",
                    "Only if they obtain a medical doctorate first.",
                    "Only after working 15 years as an accountant."
                ],
                "answer": 1,
                "explanation": "BAs naturally share strong analytical, requirements, and stakeholder skills with PMs, making it a very frequent and successful career leap."
            }
        ]
    },
    {
        "id": "supply-chain-analyst",
        "header": "6.4 Supply Chain Analyst",
        "name": "Supply Chain Analyst",
        "category": "Business, Marketing & Operations",
        "icon": "truck",
        "oneLiner": "Forecasts customer demand, optimizes inventory turnover, and streamlines logistics data.",
        "relatedRoles": ["data-scientist"],
        "salary": {
            "us": "$70,000 - $110,000 (Median ~$85,000)",
            "ca": "CAD $65,000 - $95,000",
            "source": "US Bureau of Labor Statistics (BLS) / Canada Job Bank",
            "asOf": "2026-10"
        },
        "quiz": [
            {
                "q": "What is 'Safety Stock'?",
                "options": [
                    "Shares of stock purchased in a safe company.",
                    "A buffer of surplus inventory held to mitigate the risk of stockouts caused by unpredictable demand spikes or supplier delays.",
                    "Fireproof shelving inside a warehouse.",
                    "First aid equipment stored in delivery trucks."
                ],
                "answer": 1,
                "explanation": "Safety stock cushions unexpected supply disruptions and surges in customer orders to preserve service levels."
            },
            {
                "q": "What is S&OP (Sales and Operations Planning)?",
                "options": [
                    "Standard & Ordinary Procedure",
                    "An integrated monthly business management process that aligns sales demand forecasts with supply chain and manufacturing capabilities.",
                    "Shipping and Overnight Postage",
                    "Safety and OSHA Protection"
                ],
                "answer": 1,
                "explanation": "S&OP harmonizes the commercial sales plan with inventory, production, and procurement capacity."
            },
            {
                "q": "Which enterprise software suite is the gold standard for global supply chain, inventory, and materials management?",
                "options": [
                    "SAP (ERP / SCM / IBP)",
                    "Adobe Illustrator",
                    "Spotify",
                    "Audacity"
                ],
                "answer": 0,
                "explanation": "SAP is the global market leader in enterprise resource planning, warehouse management, and supply chain logistics."
            },
            {
                "q": "What does a 3PL refer to in logistics?",
                "options": [
                    "Third-Party Logistics provider — a specialized external firm outsourced to manage transportation, warehousing, and freight fulfillment.",
                    "3-Phase Power Line",
                    "Triple Product Line",
                    "Three Point Lighting"
                ],
                "answer": 0,
                "explanation": "A 3PL handles fulfillment, ocean/air shipping, and regional distribution for businesses without their own fleet."
            },
            {
                "q": "What does Lead Time signify in procurement and supply chain?",
                "options": [
                    "The time a sales lead spends in the CRM.",
                    "The latency elapsed from the moment a purchase order is placed until the goods are received and ready for use.",
                    "The hours a warehouse manager works each week.",
                    "The expiration date of canned goods."
                ],
                "answer": 1,
                "explanation": "Lead time dictates how far in advance replenishment orders must be dispatched to avoid running out of materials."
            }
        ]
    }
]

print("Starting role extraction from PRD...")

roles_data = []
all_glossary_terms = {}

for idx, conf in enumerate(role_configs):
    rid = conf["id"]
    h = conf["header"]
    p1 = text.find('### ' + h)
    if p1 == -1:
        raise Exception(f"Header not found: {h}")
    
    if idx + 1 < len(role_configs):
        next_h = '### ' + role_configs[idx+1]["header"]
        p2 = text.find(next_h, p1)
    else:
        p2 = text.find('## 7. Shared content pages', p1)
    
    sec = text[p1:p2]

    # 1. Quick Pitch
    m_pitch = re.search(r'\*\*Quick Pitch:\*\*\s*(.*?)(?=\n\n\*\*Day-to-day|\n\*\*Day-to-day)', sec, re.DOTALL)
    quick_pitch = m_pitch.group(1).strip() if m_pitch else ""

    # 2. Day to day
    m_day = re.search(r'\*\*Day-to-day\*\*\s*(.*?)(?=\n\n\*\*Alternate titles|\n\*\*Alternate titles)', sec, re.DOTALL)
    day_to_day = []
    if m_day:
        for line in m_day.group(1).strip().split('\n'):
            line = line.strip()
            if line.startswith('- '):
                day_to_day.append(line[2:].strip())

    # 3. Alternate titles
    m_alt = re.search(r'\*\*Alternate titles:\*\*\s*(.*?)(?=\n\n\*\*Key terms|\n\*\*Key terms)', sec, re.DOTALL)
    alt_titles = []
    if m_alt:
        alt_str = m_alt.group(1).strip().rstrip('.')
        alt_titles = [t.strip() for t in alt_str.split(',') if t.strip()]

    # 4. Key terms
    m_terms = re.search(r'\*\*Key terms\*\*\s*\n\| Term \| Plain-English meaning \|\s*\n\|---\|---\|\s*\n(.*?)(?=\n\n\*\*Tools|\n\*\*Tools)', sec, re.DOTALL)
    key_terms = []
    if m_terms:
        for row in m_terms.group(1).strip().split('\n'):
            parts = [p.strip() for p in row.split('|')]
            if len(parts) >= 3 and parts[1] and parts[2]:
                t = parts[1]
                d = parts[2]
                key_terms.append({"term": t, "definition": d})
                # Add to global glossary
                if t not in all_glossary_terms:
                    all_glossary_terms[t] = {
                        "term": t,
                        "definition": d,
                        "roles": [conf["name"]],
                        "category": conf["category"]
                    }
                else:
                    if conf["name"] not in all_glossary_terms[t]["roles"]:
                        all_glossary_terms[t]["roles"].append(conf["name"])

    # 5. Tools & tech
    m_tools = re.search(r'\*\*Tools & tech:\*\*\s*(.*?)(?=\n\n\*\*Certifications|\n\*\*Certifications)', sec, re.DOTALL)
    tools_tech_str = m_tools.group(1).strip() if m_tools else ""
    tools_list = [item.strip() for item in tools_tech_str.split(';') if item.strip()]

    # 6. Certifications
    m_certs = re.search(r'\*\*Certifications(?:/licences)?:\*\*\s*(.*?)(?=\n\n\*\*Roadmap|\n\*\*Roadmap)', sec, re.DOTALL)
    certs_str = m_certs.group(1).strip() if m_certs else ""
    certs_list = [c.strip() for c in certs_str.split(',') if c.strip()]

    # 7. Roadmap
    m_road = re.search(r'\*\*Roadmap\*\*\s*(.*?)(?=\n\n\*\*Background|\n\*\*Background)', sec, re.DOTALL)
    roadmap = {"foundation": "", "jobReady": "", "advanced": ""}
    if m_road:
        r_text = m_road.group(1).strip()
        m_f = re.search(r'-\s*\*Foundation:\*\s*([^\n]+)', r_text)
        m_j = re.search(r'-\s*\*Job-ready(?:\s*\([^)]*\))?:\*\s*([^\n]+)', r_text)
        m_a = re.search(r'-\s*\*Advanced(?:\s*\([^)]*\))?:\*\s*([^\n]+)', r_text)
        if m_f: roadmap["foundation"] = m_f.group(1).strip()
        if m_j: roadmap["jobReady"] = m_j.group(1).strip()
        if m_a: roadmap["advanced"] = m_a.group(1).strip()

    # 8. Background
    m_bg = re.search(r'\*\*Background:\*\*\s*(.*?)(?=\n\n\*\*Industries|\n\*\*Industries)', sec, re.DOTALL)
    background = m_bg.group(1).strip() if m_bg else ""

    # 9. Industries
    m_ind = re.search(r'\*\*Industries:\*\*\s*(.*?)(?=\n\n\*\*Resume keywords|\n\*\*Resume keywords)', sec, re.DOTALL)
    industries_str = m_ind.group(1).strip() if m_ind else ""
    industries = [i.strip() for i in industries_str.split(',') if i.strip()]

    # 10. Resume keywords
    m_res = re.search(r'\*\*Resume keywords:\*\*\s*(.*?)(?=\n\n\*\*Cross-questions|\n\*\*Cross-questions)', sec, re.DOTALL)
    resume_keywords_str = m_res.group(1).strip() if m_res else ""
    resume_keywords = [k.strip() for k in resume_keywords_str.split(',') if k.strip()]

    # 11. Cross-questions
    m_cross = re.search(r'\*\*Cross-questions\*\*\s*(.*)', sec, re.DOTALL)
    cross_questions = []
    if m_cross:
        cq_text = m_cross.group(1).strip()
        # Find lines like - *"question?"* — answer
        # Using regex to capture each bullet
        raw_items = re.findall(r'-\s+\*\"([^\"]+)\"\*\s+[—–-]\s+([^\n]+(?:\n(?!\s*-\s+\*\")[^\n]+)*)', cq_text)
        for q, a in raw_items:
            cross_questions.append({
                "q": q.strip(),
                "a": " ".join(a.strip().split())
            })

    role_obj = {
        "id": conf["id"],
        "name": conf["name"],
        "category": conf["category"],
        "icon": conf["icon"],
        "oneLiner": conf["oneLiner"],
        "quickPitch": quick_pitch,
        "dayToDay": day_to_day,
        "altTitles": alt_titles,
        "keyTerms": key_terms,
        "toolsSummary": tools_tech_str,
        "toolsList": tools_list,
        "certificationsSummary": certs_str,
        "certificationsList": certs_list,
        "roadmap": roadmap,
        "background": background,
        "industries": industries,
        "industriesSummary": industries_str,
        "resumeKeywords": resume_keywords,
        "resumeKeywordsSummary": resume_keywords_str,
        "crossQuestions": cross_questions,
        "relatedRoles": conf["relatedRoles"],
        "salary": conf["salary"],
        "quiz": conf["quiz"],
        "lastReviewed": "2026-10-30"
    }

    roles_data.append(role_obj)
    print(f"Parsed {conf['name']}: {len(key_terms)} terms, {len(cross_questions)} cross-questions, {len(conf['quiz'])} quiz questions.")

# Now parse Compare Roles (Section 7.1)
m_comp = re.search(r'### 7\.1 Compare-roles page \(required comparisons\)\s*\n.*?\n\| Commonly confused \| One-line difference \|\s*\n\|---\|---\|\s*\n(.*?)(?=\n### 7\.2|\n\n### 7\.2)', text, re.DOTALL)
comparisons = []
if m_comp:
    for row in m_comp.group(1).strip().split('\n'):
        parts = [p.strip() for p in row.split('|')]
        if len(parts) >= 3 and parts[1] and parts[2]:
            roles_pair = parts[1]
            diff = parts[2]
            # Try to map to IDs
            p_split = roles_pair.split(' vs ')
            comparisons.append({
                "pair": roles_pair,
                "roleA": p_split[0].strip(),
                "roleB": p_split[1].strip() if len(p_split) > 1 else "",
                "difference": diff
            })

print(f"Extracted {len(comparisons)} role comparisons.")

# Convert glossary to sorted list
glossary_list = sorted(list(all_glossary_terms.values()), key=lambda x: x["term"].lower())
print(f"Compiled {len(glossary_list)} glossary terms.")

# US & Canada job market basics from 7.3
job_market_basics = {
    "ats": {
        "title": "ATS (Applicant Tracking System)",
        "summary": "Software employers and recruiters use to collect, parse, filter, and score resumes against job descriptions before a human ever looks at them.",
        "keyPoints": [
            "Keyword matching: Resumes must accurately incorporate the exact technical phrases (e.g. 'CI/CD', 'ETAP', '21 CFR Part 11', 'GA4') found in the job specification.",
            "Formatting hygiene: Single column, clear standard headings, standard PDF/Word formats, avoiding tables, text boxes, and complex graphics that scramble parser extraction.",
            "Why it matters on a call: Explains why our tailored profile marketing produces dramatically higher response rates than blasting one generic resume."
        ]
    },
    "resumeNorms": {
        "title": "US & Canada Resume Standards",
        "summary": "Standard business conventions and legal norms in North American professional hiring.",
        "keyPoints": [
            "Length: Strictly 1 to 2 pages (max 2 pages for experienced candidates; 1 page for junior).",
            "Privacy & anti-discrimination: Strictly NO photograph, NO date of birth, NO age, NO marital or family status, NO nationality or religion.",
            "Quantifiable achievements: Bullet points must follow the Google X-Y-Z formula: 'Accomplished [X], as measured by [Y], by doing [Z]' with numbers, dollar savings, and percentage gains."
        ]
    },
    "linkedin": {
        "title": "LinkedIn Recruiter Presence",
        "summary": "The primary platform where 85%+ of US and Canadian corporate and technical recruiters source active and passive talent.",
        "keyPoints": [
            "Headline: Must state target job title and top 3-4 specialized competencies (not just 'Aspiring Software Engineer' or 'Seeking Opportunities').",
            "About section: First 3 lines hook the reader before the 'see more' fold, followed by a crisp narrative and a categorized 'Core Competencies' block.",
            "Skills inventory: Pinning and ordering top skills so they align with LinkedIn Recruiter search algorithms."
        ]
    },
    "jobTypes": {
        "title": "North American Employment Types",
        "summary": "How jobs are structured from tax, contract, and employer perspectives.",
        "usTypes": [
            {"type": "W-2 (Full-Time / Direct Hire)", "detail": "Permanent or contract employee on the payroll of the employer or agency with standard tax withholdings and benefits."},
            {"type": "C2C (Corp-to-Corp)", "detail": "B2B contract between the client and the candidate's registered corporation (LLC or Inc.). Common for senior contractors and visa holders through third-party vendors."},
            {"type": "1099 (Independent Contractor)", "detail": "Direct freelance agreement without taxes withheld. Less common for foreign national candidates."},
            {"type": "Contract-to-Hire (C2H)", "detail": "Starts on a 3 to 12 month contract with a scheduled evaluation for conversion to full-time permanent W-2."}
        ],
        "caTypes": [
            {"type": "Permanent (T4 Full-time)", "detail": "Standard Canadian permanent salaried role with statutory holiday, CPP, and EI deductions."},
            {"type": "Contract (T4 Employee)", "detail": "Fixed-term staffing contract with statutory tax deductions handled by the placement firm."},
            {"type": "Incorporated Contractor", "detail": "B2B billing via a Canadian federal or provincial incorporated business (Inc./Corp.), similar to US C2C."}
        ]
    },
    "hiringStages": [
        {"stage": "1. Application & ATS Filter", "desc": "Resume parsed and ranked by automated screening algorithms."},
        {"stage": "2. Recruiter Screening Call", "desc": "15–30 minute conversational screen checking communication, salary expectations, role fit, and work authorization."},
        {"stage": "3. Hiring Manager Screen", "desc": "30–45 minute conversation testing domain depth, previous projects, and team culture fit."},
        {"stage": "4. Technical Assessment / Take-home", "desc": "Coding test (LeetCode / HackerRank), design problem, or take-home case study."},
        {"stage": "5. Onsite / Final Loop Panel", "desc": "3–5 consecutive rounds (System Design, Deep Technical, Behavioral / STAR method, Leadership)."},
        {"stage": "6. Offer & Background Check", "desc": "Formal written offer followed by employment history, education, and criminal background verification (e.g. via HireRight or Sterling)."}
    ],
    "workAuth": {
        "title": "Work Authorization Terminology (Awareness Only)",
        "disclaimer": "CRITICAL: The sales team does NOT provide legal or immigration advice. This section is strictly to recognize candidate terminology and position their profile correctly.",
        "usTerms": [
            {"code": "OPT", "name": "Optional Practical Training", "detail": "12-month post-graduation work authorization for F-1 student visa holders."},
            {"code": "STEM OPT", "name": "STEM OPT Extension", "detail": "Additional 24-month extension (total 36 months) for graduates of qualifying STEM degree programs."},
            {"code": "CPT", "name": "Curricular Practical Training", "detail": "Authorization allowing enrolled F-1 students to work in an internship or co-op integral to their curriculum."},
            {"code": "H-1B", "name": "Specialty Occupation Visa", "detail": "Employer-sponsored temporary work visa subject to an annual lottery (April) with a 6-year general cap (unless I-140 approved)."},
            {"code": "L-1", "name": "Intracompany Transferee", "detail": "Visa for employees transferring from an overseas branch to a US office (L-1A executive / L-1B specialized knowledge)."},
            {"code": "Green Card (PR)", "name": "Permanent Resident", "detail": "Permanent legal status with unrestricted employment authorization across all private US employers."},
            {"code": "US Citizen", "name": "Citizen", "detail": "Required for most high-level security clearance and defense/aerospace federal contract positions."}
        ],
        "caTerms": [
            {"code": "PGWP", "name": "Post-Graduation Work Permit", "detail": "Open work permit granted to international students graduating from designated Canadian learning institutions (up to 3 years)."},
            {"code": "Open Work Permit", "name": "Open Work Permit", "detail": "Authorizes employment for any Canadian employer without needing a specific job offer or LMIA (e.g. spousal open work permit)."},
            {"code": "Closed Work Permit", "name": "Employer-Specific Permit", "detail": "Tied to a specific sponsoring employer who obtained an LMIA or LMIA exemption."},
            {"code": "LMIA", "name": "Labour Market Impact Assessment", "detail": "Document a Canadian employer must obtain proving no Canadian citizen or PR was available for the job."},
            {"code": "PR", "name": "Permanent Resident", "detail": "Full permanent status allowing unrestricted employment in any province or territory."}
        ],
        "officialLinks": [
            {"name": "US Citizenship and Immigration Services (USCIS)", "url": "https://www.uscis.gov"},
            {"name": "Immigration, Refugees and Citizenship Canada (IRCC)", "url": "https://www.canada.ca/en/immigration-refugees-citizenship.html"}
        ]
    }
}

# Cross questions call guidelines & compliance guardrails from 7.4
cross_questions_guide = {
    "techniqueSteps": [
        {
            "step": 1,
            "title": "Listen & Mirror",
            "desc": "Listen actively without interrupting. Repeat back their specific role and specializations in their exact terminology so they feel heard."
        },
        {
            "step": 2,
            "title": "Deliver the Quick Pitch & Keywords",
            "desc": "Use the 30-second Quick Pitch and 1–2 key industry terms naturally in your response. Sound knowledgeable, but never lecture."
        },
        {
            "step": 3,
            "title": "The Honest Deferral Script",
            "desc": "If a candidate asks an ultra-specific or deeply technical question you aren't sure about, say: 'That is a great, specific question — let me confirm with our technical/marketing specialist and get back to you today.' Never guess or bluff."
        },
        {
            "step": 4,
            "title": "Re-anchor to Value",
            "desc": "Transition the conversation back to our core service: positioning their profile for ATS compliance, optimizing resume impact, and reaching hiring decision-makers."
        }
    ],
    "complianceGuardrails": {
        "mustNotSay": [
            "NEVER guarantee a job, guaranteed interviews, hiring timeline, or specific salary outcome.",
            "NEVER give legal or immigration advice. If asked about visa sponsorship or filings, refer them to a licensed immigration attorney or official USCIS/IRCC channels.",
            "NEVER suggest, recommend, or allow inflating or falsifying experience, dates, qualifications, or work status on a resume.",
            "NEVER quote salary ranges without citing the verified official source and review date from the guide."
        ],
        "approvedResponses": [
            {
                "candidateSays": "Can you guarantee I'll get interviews within 30 days?",
                "repResponse": "We cannot guarantee specific interview offers or hiring timelines because final hiring decisions always rest with the employer. What we guarantee is a rigorous, proven profile marketing process: optimizing your resume to pass ATS filters, highlighting your verified projects and technical strengths, and putting your profile directly in front of targeted recruiters."
            },
            {
                "candidateSays": "Will you help me get an H-1B or Canadian LMIA work permit?",
                "repResponse": "We are a candidate profile marketing firm, not an immigration law practice. We assist you in finding and marketing your profile to employers who have historically sponsored or are open to your authorization status, but we do not file petitions or give legal advice."
            },
            {
                "candidateSays": "I only have 3 months of experience, can we put 2 years on my resume?",
                "repResponse": "We adhere to strict integrity standards: we never falsify or exaggerate experience, because background verification checks (HireRight, Sterling) will fail and damage your reputation with employers. Instead, we highlight your verified technical projects, certifications, and skills to present your real qualifications in the strongest possible light."
            }
        ]
    }
}

full_data = {
    "version": "1.0",
    "lastUpdated": "2026-10-30",
    "categories": [
        {
            "id": "tech-ai",
            "name": "Tech & AI",
            "badgeColor": "blue",
            "description": "Software engineering, artificial intelligence, data science, cybersecurity, and modern cloud infrastructure.",
            "roles": ["ai-ml-engineer", "data-scientist", "cybersecurity-analyst", "cloud-engineer", "devops-engineer", "software-developer", "prompt-engineer"]
        },
        {
            "id": "engineering",
            "name": "Engineering, Construction & Manufacturing",
            "badgeColor": "amber",
            "description": "Physical infrastructure, mechanical systems, high-voltage electrical, chemical process optimization, and regulatory validation.",
            "roles": ["civil-engineer", "construction-manager", "mechanical-engineer", "electrical-engineer", "process-engineer", "validation-engineer"]
        },
        {
            "id": "business",
            "name": "Business, Marketing & Operations",
            "badgeColor": "emerald",
            "description": "Digital marketing channels, product management roadmaps, brand leadership, and global supply chain logistics.",
            "roles": ["digital-marketing-specialist", "marketing-manager", "product-manager", "supply-chain-analyst"]
        }
    ],
    "roles": roles_data,
    "comparisons": comparisons,
    "glossary": glossary_list,
    "jobMarketBasics": job_market_basics,
    "crossQuestionsGuide": cross_questions_guide
}

# Ensure data directory exists
os.makedirs('data', exist_ok=True)

# Write roles.json
with open('data/roles.json', 'w', encoding='utf-8') as f:
    json.dump(full_data, f, indent=2, ensure_ascii=False)

# Write roles-data.js for standalone browser support
with open('data/roles-data.js', 'w', encoding='utf-8') as f:
    f.write('/** Auto-generated from PRD baseline content */\n')
    f.write('window.ROLES_DATA = ')
    json.dump(full_data, f, indent=2, ensure_ascii=False)
    f.write(';\n')

print("Successfully generated data/roles.json and data/roles-data.js!")
