export const config = {
    developer: {
        name: "Sandipan",
        fullName: "Sandipan Chakraborty",
        title: "AI Backend &\nReal-Time Systems Engineer",
        description: "Architecting low-latency AI pipelines and distributed backend systems that run at scale in production."
    },
    social: {
        github: "sid0803",
        email: "chakrabortysandipan133@gmail.com",
        location: "Kolkata, India"
    },
    about: {
        title: "About Me",
        description: "Backend & AI Systems Engineer with experience designing and deploying real-time, low-latency AI pipelines, LLM-powered applications, and distributed backend systems. I've built production systems including async pipelines processing 1K–3K events/day (scalable to 10K+) and voice AI with ~120–180ms latency (p95 < 250ms). My focus is system design, fault-tolerant architecture, and end-to-end AI pipelines from input → processing → decision → response."
    },
    experiences: [
        {
            position: "AI & Automation Intern",
            company: "IndiiServe Solutions Pvt. Ltd.",
            period: "Feb 2026 – Present",
            location: "Kolkata",
            description: "Architecting and shipping production-grade AI systems, real-time voice pipelines, and async event infrastructure.",
            responsibilities: [
                "Architected production voice AI system (FastAPI + WebSockets + AWS Bedrock) achieving ~120–180ms latency, p95 < 250ms via Exotel telephony integration.",
                "Designed end-to-end system architecture for real-time AI pipeline (call → inference → response), including service decomposition, API contracts, and multi-tenant AWS EC2 deployment.",
                "Engineered OIE async pipeline processing 1K–3K events/day (scalable to 10K+) and WhatsApp Recovery System (Redis + Celery) with idempotent retries and Dead-Letter Queue.",
                "Implemented safety-critical routing for emergency escalation and tool-driven LLM architecture for structured retrieval.",
                "Built OCR-based data extraction pipelines converting unstructured documents into structured, queryable records."
            ],
            technologies: ["FastAPI", "AWS Bedrock", "WebSockets", "Redis", "Celery", "LLM", "OCR", "EC2", "Exotel"]
        },
        {
            position: "Machine Learning Intern",
            company: "LABMENTIX",
            period: "Aug 2025 – Oct 2025",
            location: "Remote",
            description: "Developed ML model serving APIs and improved prediction accuracy across data workflows.",
            responsibilities: [
                "Developed and deployed 3 RESTful APIs (FastAPI) for ML model serving, cutting manual data-processing time by ~40%.",
                "Trained and evaluated classification & regression models; applied feature engineering and cross-validation, improving prediction accuracy by ~15% over baseline."
            ],
            technologies: ["FastAPI", "Python", "Scikit-learn", "ML", "REST APIs"]
        }
    ],
    projects: [
        {
            id: 1,
            title: "Heartbeat System",
            category: "AI / LLM",
            technologies: "Python, FastAPI, LLM, SQLite, Chrome Extension, Multi-Source AI",
            image: "/heartbeat.png",
            description: "Privacy-first AI Chief-of-Staff for founders. Condenses 50+ daily notifications from Slack, Gmail, GitHub, and Calendar into 1 clear executive brief every 30 minutes using LLM summarization and priority scoring.",
            github: "https://github.com/sid0803/heartbeat-system"
        },
        {
            id: 2,
            title: "U-MEM",
            category: "Semantic Search / AI",
            technologies: "Python, Sentence Transformers, FAISS, OCR, SHA-256, HDBSCAN, Git",
            image: "/umem.png",
            description: "Universal Document Intelligence & Memory System. Enables sub-second semantic search across large document corpora via embedding → HDBSCAN clustering → FAISS index pipeline.",
            github: "https://github.com/sid0803/U-MEM-Universal-Document-Intelligence-Memory-System"
        },
        {
            id: 3,
            title: "Cloud Cost Knowledge Graph",
            category: "Graph / AI",
            technologies: "FastAPI, Neo4j, Streamlit, Sentence Transformers, Scikit-learn, LLM",
            image: "/kgraph.png",
            description: "Graph-powered cloud cost intelligence platform modeling 8.5K+ nodes and 43K+ relationships. Delivers LLM-assisted cost optimization via hybrid vector + graph + Cypher retrieval.",
            github: "https://github.com/sid0803/cloud-cost-knowledge-graph"
        }
    ],
    education: [
        {
            degree: "B.Tech in Computer Science & Business Systems",
            institution: "Techno International Newtown",
            period: "Aug 2022 – May 2026",
            location: "Kolkata, WB",
            details: "CGPA: 7.5"
        }
    ],
    contact: {
        email: "chakrabortysandipan133@gmail.com",
        github: "https://github.com/sid0803",
        linkedin: "https://linkedin.com/in/sandipan-chakraborty-",
        twitter: "https://x.com/",
        facebook: "https://facebook.com/",
        instagram: "https://instagram.com/"
    },
    skills: {
        develop: {
            title: "AI & BACKEND",
            description: "Building intelligent systems & production pipelines",
            details: "Specializing in real-time AI pipelines, LLM integration (RAG), semantic search, and distributed backend architectures using FastAPI, Redis, and AWS Bedrock.",
            tools: ["Python", "FastAPI", "AWS Bedrock", "LLMs", "RAG Pipelines", "FAISS", "Sentence Transformers", "Neo4j", "WebSockets", "Redis", "Celery", "OCR"]
        },
        design: {
            title: "INFRA & SYSTEMS",
            description: "Production-grade infrastructure & distributed systems",
            details: "Designing fault-tolerant, event-driven systems and deploying at scale using Docker, EC2, PostgreSQL, and async I/O patterns.",
            tools: ["Docker", "AWS EC2", "PostgreSQL", "SQLite", "Async I/O", "Event-Driven", "Microservices", "REST APIs", "C++", "Git", "Linux"]
        }
    }
};
