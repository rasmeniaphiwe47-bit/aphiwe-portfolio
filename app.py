import streamlit as st
import json
import os

st.set_page_config(
    page_title="Aphiwe Rasmeni | Data Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .main { padding-top: 2rem; }
    section[data-testid="stSidebar"] { border-right: 1px solid #e6e6e6; }
    .profile-card {
        padding: 2rem; border-radius: 20px;
        background: linear-gradient(135deg, #0f172a, #1e293b);
        color: white; margin-bottom: 2rem;
    }
    .profile-name { font-size: 3rem; font-weight: 700; margin-bottom: 0.3rem; }
    .profile-title { font-size: 1.3rem; color: #cbd5e1; }
    .profile-description { font-size: 1.05rem; line-height: 1.7; color: #e2e8f0; margin-top: 1.2rem; }
    .section-title { font-size: 2rem; font-weight: 700; margin-top: 2rem; margin-bottom: 1rem; }
    .subsection-title { font-size: 1.3rem; font-weight: 700; margin-top: 1.5rem; margin-bottom: 0.5rem; color: #1e293b; }
    .project-card {
        padding: 1.5rem; border-radius: 16px; border: 1px solid #e2e8f0;
        background-color: white; min-height: 250px; margin-bottom: 1rem;
    }
    .project-title { font-size: 1.25rem; font-weight: 700; }
    .project-description { color: #475569; line-height: 1.6; }
    .skill {
        display: inline-block; padding: 0.45rem 0.8rem; margin: 0.25rem;
        border-radius: 20px; background-color: #e2e8f0; color: #0f172a; font-size: 0.9rem;
    }
    .exp-skill {
        display: inline-block; padding: 0.35rem 0.7rem; margin: 0.2rem;
        border-radius: 20px; background-color: #dbeafe; color: #1e40af; font-size: 0.85rem;
    }
    .timeline {
        border-left: 3px solid #334155; padding-left: 1.5rem; margin-bottom: 2rem;
        padding-bottom: 0.5rem;
    }
    .timeline-title { font-size: 1.2rem; font-weight: 700; }
    .timeline-org { font-size: 1rem; font-weight: 500; color: #334155; }
    .timeline-date { color: #64748b; font-size: 0.9rem; margin-bottom: 0.75rem; }
    .footer { text-align: center; padding: 3rem 0 1rem 0; color: #64748b; }
    .profile-photo img { border-radius: 16px; box-shadow: 0 4px 20px rgba(0,0,0,0.15); }
    .cert-card {
        padding: 1rem 1.25rem; border-radius: 12px; border: 1px solid #e2e8f0;
        background-color: white; margin-bottom: 0.75rem;
    }
</style>
""", unsafe_allow_html=True)

def load_projects():
    file_path = "data/projects.json"
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

projects = load_projects()

st.sidebar.title("APHIWE RASMENI")
st.sidebar.caption("Interactive Data Portfolio")

page = st.sidebar.radio(
    "Navigation",
    ["Home", "About", "Education", "Experience", "Skills", "Projects", "Certifications", "Contact"]
)

st.sidebar.markdown("---")
st.sidebar.caption("Junior Data Scientist | Data Engineer | Data Analyst")
st.sidebar.caption("📍 Cape Town, South Africa")

if page == "Home":
    col1, col2 = st.columns([1, 2])
    with col1:
        photo_path = "assets/profile.jpg"
        st.markdown('<div class="profile-photo">', unsafe_allow_html=True)
        if os.path.exists(photo_path):
            st.image(photo_path, width=280)
        else:
            st.markdown("""
            <div style="width:280px;height:280px;border-radius:50%;background:#e2e8f0;
            display:flex;align-items:center;justify-content:center;font-size:70px;
            font-weight:bold;color:#334155;">AR</div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="profile-card">
            <div class="profile-name">Aphiwe Rasmeni</div>
            <div class="profile-title">Junior Data Scientist | Data Engineer | Data Analyst</div>
            <div class="profile-description">
                Mathematics and Data Science professional passionate about transforming data
                into meaningful insights, predictive models and practical solutions.
                My work combines statistics, programming, machine learning, data analysis
                and data engineering.
            </div>
            <br>
            <div style="color:#94a3b8;font-size:0.9rem;">
                📧 rasmeniaphiwe47@gmail.com &nbsp;|&nbsp; 📍 Cape Town, South Africa
            </div>
        </div>
        """, unsafe_allow_html=True)
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            st.link_button("GitHub", "https://github.com/rasmeniaphiwe47-bit")
        with col_b:
            st.link_button("LinkedIn", "https://www.linkedin.com/in/aphiwe-rasmeni-b3a03227a")
        with col_c:
            st.button("Download CV", disabled=True)

    st.markdown('<div class="section-title">Featured Work</div>', unsafe_allow_html=True)
    if not projects:
        st.info("Project information will appear here.")
    else:
        featured_projects = projects[:3]
        cols = st.columns(3)
        for index, project in enumerate(featured_projects):
            with cols[index]:
                st.markdown(f"""
                <div class="project-card">
                    <div class="project-title">{project['title']}</div>
                    <br>
                    <div class="project-description">{project['description']}</div>
                    <br>
                    <b>Technologies</b><br>{project['technologies']}
                </div>
                """, unsafe_allow_html=True)

elif page == "About":
    st.markdown('<div class="section-title">About Me</div>', unsafe_allow_html=True)
    st.write("I am a Mathematical Sciences and Data Science professional interested in using mathematics, statistics, programming and technology to solve real-world problems. My interests span data analytics, machine learning, data science and data engineering. I enjoy working with data from the point where it is collected and transformed through to analysis, modelling and visualisation.")
    st.markdown("### Professional Interests")
    interests = ["Data Science", "Data Engineering", "Machine Learning", "Statistical Modelling", "Data Analytics", "Business Intelligence", "Cloud Technologies"]
    for interest in interests:
        st.markdown(f'<span class="skill">{interest}</span>', unsafe_allow_html=True)

elif page == "Education":
    st.markdown('<div class="section-title">Education</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="timeline">
    <div class="timeline-title">Cape Peninsula University of Technology</div>
    <div class="timeline-date">Diploma / Advanced Diploma in Mathematical Sciences</div>
    <br>
    Specialisation: <b>Data Science</b>
    <br><br>
    Relevant areas include:
    <ul>
        <li>Statistics</li>
        <li>Mathematical Modelling</li>
        <li>Data Science</li>
        <li>Programming</li>
        <li>Database Systems</li>
        <li>Machine Learning</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

elif page == "Experience":
    st.markdown('<div class="section-title">Experience</div>', unsafe_allow_html=True)

    experience_data = [
        {
            "title": "Student Researcher",
            "org": "UWC Bioinformatics Department & CPUT",
            "dates": "Jul 2026 – Present",
            "duties": [
                "Conducting research combining bioinformatics and data science methods on real-world biological datasets.",
                "Applying statistical and computational techniques to analyse and interpret research data.",
                "Collaborating across two institutions (UWC and CPUT) on ongoing research objectives.",
                "Documenting methodology, findings, and results for academic reporting.",
            ],
            "skills": ["Python", "Bioinformatics", "Statistical Analysis", "Research Methodology", "Data Interpretation"],
        },
        {
            "title": "Data Science Project Work",
            "org": "SaiKet Systems & Oasis Infobyte",
            "dates": "Apr 2026 – May 2026",
            "duties": [
                "Completed applied data science projects covering the full pipeline: data cleaning, exploratory analysis, modelling and evaluation.",
                "Built and validated machine learning models on real-world datasets as part of structured internship deliverables.",
                "Presented findings and technical work in a professional, project-based format.",
            ],
            "skills": ["Python", "Machine Learning", "Data Cleaning", "EDA", "Model Evaluation"],
        },
        {
            "title": "Retention Officer",
            "org": "Cape Peninsula University of Technology",
            "dates": "Sep 2026 – Dec 2026",
            "duties": [
                "Monitored and supported student retention initiatives using enrolment and performance data.",
                "Identified at-risk students through data tracking and coordinated appropriate intervention support.",
                "Maintained accurate records and reported on retention metrics to relevant stakeholders.",
            ],
            "skills": ["Data Tracking", "Reporting", "Stakeholder Communication", "Student Support Systems"],
        },
        {
            "title": "Data Analyst – WIL Placement",
            "org": "Statistics South Africa",
            "dates": "Jul 2025 – Dec 2025",
            "duties": [
                "Assisted with data collection, cleaning and processing of national statistical datasets.",
                "Performed exploratory data analysis to support statistical reporting and publications.",
                "Worked with structured data pipelines and validated data quality against national standards.",
                "Contributed to the preparation of statistical summaries and visualisations for internal review.",
            ],
            "skills": ["Data Analysis", "Data Cleaning", "SQL", "Statistical Reporting", "Data Quality Assurance"],
        },
        {
            "title": "Mathematics & Statistics Tutor",
            "org": "Cape Peninsula University of Technology",
            "dates": "Feb 2024 – Jun 2025",
            "duties": [
                "Delivered tutoring sessions in mathematics and statistics to undergraduate students across departments.",
                "Simplified complex mathematical and statistical concepts to improve student comprehension and pass rates.",
                "Prepared practice materials and worked examples aligned with course curricula.",
            ],
            "skills": ["Mathematics", "Statistics", "Teaching & Communication", "Curriculum Support"],
        },
        {
            "title": "Enumerator & Data Capturer",
            "org": "Golden Arrow Bus Service",
            "dates": "Aug 2024 – Nov 2024",
            "duties": [
                "Conducted field data collection through structured surveys and enumeration exercises.",
                "Captured and validated survey data for accuracy and completeness.",
                "Ensured data integrity during transfer from field forms into digital systems.",
            ],
            "skills": ["Data Collection", "Data Capturing", "Attention to Detail", "Field Research"],
        },
    ]

    for exp in experience_data:
        duties_html = "".join(f"<li>{d}</li>" for d in exp["duties"])
        skills_html = "".join(f'<span class="exp-skill">{s}</span>' for s in exp["skills"])
        st.markdown(f"""
        <div class="timeline">
        <div class="timeline-title">{exp['title']}</div>
        <div class="timeline-org">{exp['org']}</div>
        <div class="timeline-date">{exp['dates']}</div>
        <ul>{duties_html}</ul>
        <div style="margin-top:0.5rem;">{skills_html}</div>
        </div>
        """, unsafe_allow_html=True)

elif page == "Skills":
    st.markdown('<div class="section-title">Technical Skills</div>', unsafe_allow_html=True)
    skill_groups = {
        "Programming": ["Python", "R", "SQL", "MATLAB", "SAS"],
        "Data Science": ["Machine Learning", "Statistical Modelling", "Exploratory Data Analysis", "Predictive Modelling", "NLP"],
        "Data Engineering": ["ETL", "SQL", "SQLite", "Data Pipelines", "Data Warehousing", "Databricks", "Snowflake"],
        "Visualisation": ["Power BI", "Matplotlib", "Seaborn", "Plotly"],
        "Cloud": ["AWS", "Cloud Computing"],
        "Tools": ["Git", "GitHub", "Jupyter", "RStudio", "LaTeX"]
    }
    for category, skills in skill_groups.items():
        st.markdown(f"### {category}")
        for skill in skills:
            st.markdown(f'<span class="skill">{skill}</span>', unsafe_allow_html=True)
        st.write("")

elif page == "Projects":
    st.markdown('<div class="section-title">Projects</div>', unsafe_allow_html=True)
    st.write("Explore selected data science, machine learning and data engineering projects.")
    if not projects:
        st.info("Project information will appear here.")
    else:
        for project in projects:
            with st.container():
                st.markdown(f"""
                <div class="project-card">
                    <div class="project-title">{project['title']}</div>
                    <br>
                    <div class="project-description">{project['description']}</div>
                    <br>
                    <b>Technologies:</b> {project['technologies']}
                </div>
                """, unsafe_allow_html=True)
                col1, col2 = st.columns(2)
                with col1:
                    if project.get("github"):
                        st.link_button("View GitHub →", project["github"])
                with col2:
                    if project.get("demo"):
                        st.link_button("Live Demo →", project["demo"])
                st.divider()

elif page == "Certifications":
    st.markdown('<div class="section-title">Certifications</div>', unsafe_allow_html=True)
    st.write("Click 'View' next to any certificate to download and view the original PDF.")

    cert_dir = "assets/certificates"

    cert_groups = {
        "AWS Training & Certification / DataCamp": [
            ("AWS Cloud Practitioner (CLF-C02)", "aws_cloud_practitioner.pdf"),
            ("AWS Cloud Technology and Services Concepts", "aws_cloud_technology_services.pdf"),
            ("AWS Security and Cost Management Concepts", "aws_security_cost_management.pdf"),
            ("AWS Concepts", "aws_concepts.pdf"),
            ("Understanding Cloud Computing", "understanding_cloud_computing.pdf"),
            ("Understanding Data Engineering", "understanding_data_engineering.pdf"),
            ("Databricks Concepts", "databricks_concepts.pdf"),
            ("Introduction to Snowflake", "intro_snowflake.pdf"),
            ("Machine Learning Terminology and Process", "ml_terminology_process.pdf"),
            ("Practical Data Science with Amazon SageMaker", "practical_data_science_sagemaker.pdf"),
            ("Amazon RDS for SQL Server – Getting Started", "amazon_rds_sql_server.pdf"),
        ],
        "IBM / Coursera": [
            ("Databases and SQL for Data Science with Python", "databases_sql_data_science_python.pdf"),
            ("Python for Data Science, AI & Development", "python_data_science_ai_development.pdf"),
        ],
        "LinkedIn Learning / Microsoft": [
            ("Career Essentials in Data Analysis (Microsoft & LinkedIn)", "career_essentials_data_analysis.pdf"),
            ("Introduction to Career Skills in Data Analytics", "intro_career_skills_data_analytics.pdf"),
        ],
        "Cisco Networking Academy": [
            ("Introduction to Cybersecurity", "cisco_intro_cybersecurity.pdf"),
        ],
    }

    for group_name, certs in cert_groups.items():
        st.markdown(f'<div class="subsection-title">{group_name}</div>', unsafe_allow_html=True)
        for name, filename in certs:
            filepath = os.path.join(cert_dir, filename)
            col1, col2 = st.columns([5, 1])
            with col1:
                st.markdown(f'<div class="cert-card"><b>{name}</b></div>', unsafe_allow_html=True)
            with col2:
                if os.path.exists(filepath):
                    with open(filepath, "rb") as f:
                        st.download_button("View", f, file_name=filename, key=filename)
                else:
                    st.caption("Not uploaded yet")

elif page == "Contact":
    st.markdown('<div class="section-title">Let\'s Connect</div>', unsafe_allow_html=True)
    st.write("I am interested in opportunities involving data science, data engineering, data analytics and related technology roles.")

    st.markdown("### 📧 Email")
    st.markdown("**rasmeniaphiwe47@gmail.com**")

    st.markdown("### 🌐 Professional Links")
    col1, col2 = st.columns(2)
    with col1:
        st.link_button("💻 GitHub", "https://github.com/rasmeniaphiwe47-bit")
    with col2:
        st.link_button("🔗 LinkedIn", "https://www.linkedin.com/in/aphiwe-rasmeni-b3a03227a")

    st.markdown("### 📍 Location")
    st.markdown("**Cape Town, South Africa**")

    st.markdown("---")
    st.markdown("**Aphiwe Rasmeni**  \nJunior Data Scientist | Data Engineer | Data Analyst")

st.markdown("""
<div class="footer">
    © 2026 Aphiwe Rasmeni · Interactive Data Portfolio
    <br><span style="font-size:0.8rem;">Cape Town, South Africa</span>
</div>
""", unsafe_allow_html=True)
