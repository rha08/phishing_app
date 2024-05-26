import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


myfile = open("names.txt","r")

count = 0
for email in myfile:
    if count == 0:
        survey_ID = email
    elif count == 1:
        source = email
    else:
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"

        sender_email = "rhearam3571@gmail.com"
        password = "dubs vrgz hkgw cbjj"

        message = MIMEMultipart("alternative")
        message["Subject"] = "multipart test"
        message["From"] = sender_email
        message["To"] = email
        message["Bcc"] = email

        html = f"""\
        <html>
        <body>
            <p>Hi,<br>
            How are you?<br>
            <a href="http://127.0.0.1:5000/add_url_data?email={email}&source={source}&surveyID={survey_ID}">blah blah</a>
            has many great tutorials.
            </p>
        </body>
        </html>
        """

        # text part
        text_part = MIMEText(html, "html")
        message.attach(text_part)

        # file part
        filename = "names.txt"

        # Open PDF file in binary mode
        with open(filename, "rb") as attachment:
            file_part = MIMEBase("application", "octet-stream")
            file_part.set_payload(attachment.read())

        # Encode file in ASCII characters to send by email
        encoders.encode_base64(file_part)

        # Add header as key/value pair to attachment part
        file_part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )

        message.attach(file_part)
        text = message.as_string()

        # sending the email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, email, message.as_string())
    count = count + 1
