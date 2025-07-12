from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    company_info = {
        'name': 'Cosman-IT',
        'core_values': ['Dedication', 'Innovation', 'Perseverence', 'Transparency'],
        'services': [
            {
                'title': 'Data Science & Advanced Analytics', 
                'short': 'Turn raw data into predictive insights that drive smarter business decisions', 
                'details': """
                🔍 1. Predictive Modeling<br>
                📈 2. Customer Segmentation<br>
                🧠 3. Natural Language Processing (NLP)<br>
                ⚙️ 4. Time Series Forecasting<br>
                💡 5. Anomaly Detection<br>
                """,
                'icon': 'data_science.gif'
            },
            {
                'title': 'Machine Learning & AI', 
                'short': 'Build intelligent systems with scalable, ethical, and business-ready AI solutions', 
                'details': """
                🔄 1. ML Models Auditing<br>
                🧠 2. AI-Powered Recommendation Systems<br>
                🗣️ 3. Conversational AI & Chatbots<br>
                🏗️ 4. ML Model Deployment & MLOps<br>
                🛡️ 5. Responsible AI & Model Explainability<br>
                🤖 6. RAG and Agents<br>
                """,
                'icon': 'machine_learning.gif'
            },
            {
                'title': 'Industry-Specific Analytics', 
                'short': "Deliver tailored analytics solutions to solve your industry's unique challenges", 
                'details': """
                🏦 1. Financial Services & Risk Analytics<br>
                🧱 2. Construction & Real Estate Analytics<br>
                🏃‍♂️ 3. Sports Analytics <br>
                🚚 4. Fleet & Vehicle Data Analytics<br>
                📦 5. Supply Chain & Logistics Optimization<br>
                """,
                'icon': 'industry_specific_analytics.gif'
            },
            {
                'title': 'Business Intelligence & Reporting', 
                'short': 'Transform data into actionable insights through dashboards, KPIs, and storytelling', 
                'details': """
                📊 1. Interactive Dashboard Development<br>
                🧩 2. KPI Design & Performance Tracking<br>
                📥 3. Automated Reporting Pipelines<br>
                💡 4. Storytelling & Insight Communication<br>
                ⚙️ 5. Dashboard Maintenance & Support<br>
                """,
                'icon': 'bi_reporting.gif'
            },
            {
                'title': 'Data Engineering', 
                'short': 'Build reliable, scalable data systems that power trusted business insights', 
                'details': """
                🧹 1. Data Cleaning & Transformation<br>
                📏 2. Data Quality & Validation Frameworks<br>
                🗃️ 3. Data Warehousing Solutions<br>
                🏗️ 4. Data Pipeline Design & Development<br>
                ⚙️ 5. Infrastructure Automation & DataOps<br>
                """,
                'icon': 'data_engineering.gif'
            },
            {
                'title': 'Data Infrastructure & Cloud Solutions', 
                'short': 'Empower your business with fast, secure, and scalable cloud infrastructure solutions', 
                'details': """
                ☁️ 1. Cloud Data Platform Architecture<br>
                🔁 2. Cloud Migration & Modernization<br>
                🧩 3. Hybrid & Multi-Cloud Integration<br>
                🛠️ 4. Monitoring & Reliability Engineering<br>
                """,
                'icon': 'data_infra_cloud.gif'
            },
            {
                'title': 'Data Strategy & Governance', 
                'short': 'Ensure trusted, high-quality, well-governed data through strategic control frameworks', 
                'details': """
                🧭 1. Enterprise Data Strategy Development<br>
                🏛️ 2. Data Governance Framework Design<br>
                📚 3. Data Cataloging & Lineage Mapping<br>
                🪪 4. Master Data Management (MDM)<br>
                📏 5. Data Quality Management<br>
                🔒 6. Access & Role-Based Permissions<br>
                """,
                'icon': 'strategy.gif'
            },
            {
                'title': 'Training & Enablement', 
                'short': 'Empower teams with skills to confidently use and govern data', 
                'details': """
                📈 1. Change Management & Data Literacy<br>
                💻 2. BI Tool Training (Power BI, Qlik, etc.)<br>
                📐 3. Governance & Compliance Training<br>
                🗂️ 4. Documentation & Knowledge Base<br>
                """,
                'icon': 'trainings.gif'
            },
            {
                'title': 'R&D / Innovation', 
                'short': 'Explore, prototype, and scale innovative data solutions using emerging technologies', 
                'details': """
                🧪 1. Data Innovation Labs<br>
                🤖 2. AI/ML Proof-of-Concept Development<br>
                🌐 3. Emerging Tech (LLMs, Graph, etc.)<br>
                🧠 4. Cognitive Services Integration<br>
                🧱 5. Data Product Design & Experimentation
                """,
                'icon': 'research.gif'
            },
        ],
        'team': [
            {
                'name': 'Tobias Lahtinen',
                'role': 'Data Scientist',
                'short': '@ Volvo Group',
                'photo': 'tobias_lahtinen.jpeg',
                'cv_file': 'tobias_lahtinen.pdf',
            },
            {
                'name': 'Jaime Munoz',
                'role': 'Data Scientist',
                'short': '@ Generali',
                'photo': 'jaime_munoz.jpeg',
                'cv_file': 'jaime_munoz.pdf'
            },
            {
                'name': 'Vadim Cosman',
                'role': 'Data Scientist',
                'short': '@ Volvo Group',
                'photo': 'vadim_cosman.jpeg',
                'cv_file': 'vadim_cosman.pdf',
            },
            {
                'name': 'Vlad Stratila',
                'role': 'Back-End Developer',
                'short': '@ CosmanIT',
                'photo': 'vlad_stratila.jpeg',
                'cv_file': 'vlad_statila.pdf',
            },
            {
                'name': 'Iulian Fosa',
                'role': 'Data + Software Engineer',
                'short': '@ CosmanIT',
                'photo': 'iulian_fosa.jpeg',
                'cv_file': 'iulian_fosa.pdf'
            },
            {
                'name': 'Daniil Klimenko',
                'role': 'Full-Stack Developer',
                'short': '@ CosmanIT',
                'photo': 'daniil_klimenko.jpeg',
                'cv_file': 'daniil_klimenko.pdf',
            },
        # Add 4 more team members similarly
        ],
        'contacts': {
            'email': 'team@cosman-it.com',
            'phone': '+123456789',
            'address': '123 Business St, City, Country'
        }
    }
    return render_template("index.html", company=company_info)


@app.route('/send-message', methods=['POST'])
def send_message():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # 🌐 Stub - later: send email using SendGrid
    print(f"Message from {name} <{email}>: {message}")
    flash("Your message has been sent successfully!")

    return redirect('/')


# Later: Add SendGrid Integration
# You’ll install SendGrid with:

# bash
# Copy
# Edit
# pip install sendgrid
# Then inside the send_message() route, replace the stub with:

# python
# Copy
# Edit
# sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
# email_message = Mail(
#     from_email='no-reply@yourdomain.com',
#     to_emails='your@email.com',
#     subject=f"New Contact Message from {name}",
#     html_content=f"<strong>From:</strong> {name} ({email})<br><br><strong>Message:</strong><br>{message}"
# )
# response = sg.send(email_message)


if __name__ == '__main__':
    app.run()
