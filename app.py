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
                'short': 'Unlock insights', 
                'details': 'We analyze your data to discover trends and drive business decisions.',
                'icon': 'data_science.gif'
            },
            {
                'title': 'Machine Learning & AI', 
                'short': 'Move to the cloud', 
                'details': 'We help you transition to scalable, secure cloud environments.',
                'icon': 'machine_learning.gif'
            },
            {
                'title': 'Industry-Specific Analytics', 
                'short': 'Smarter solutions', 
                'details': 'We guide your AI initiatives from idea to deployment.',
                'icon': 'industry_specific_analytics.gif'
            },
            {
                'title': 'Business Intelligence & Reporting', 
                'short': 'Automation & CI/CD', 
                'details': 'Streamline your software delivery with best DevOps practices.',
                'icon': 'bi_reporting.gif'
            },
            {
                'title': 'Data Engineering', 
                'short': 'Stay protected', 
                'details': 'Risk assessments, vulnerability scanning, and incident response.',
                'icon': 'data_engineering.gif'
            },
            {
                'title': 'Data Infrastructure & Cloud Solutions', 
                'short': 'Modern web apps', 
                'details': 'Fast, responsive websites tailored to your business.',
                'icon': 'data_infra_cloud.gif'
            },
            {
                'title': 'Data Strategy & Governance', 
                'short': 'iOS & Android', 
                'details': 'Cross-platform mobile app design and development.',
                'icon': 'strategy.gif'
            },
            {
                'title': 'Training & Enablement', 
                'short': 'Make better decisions', 
                'details': 'Build dashboards and data visualizations for strategic insights.',
                'icon': 'trainings.gif'
            },
            {
                'title': 'R&D / Innovation', 
                'short': 'Efficiency boost', 
                'details': 'Use Robotic Process Automation to eliminate repetitive tasks.',
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
                'name': 'Vlad Statila',
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
