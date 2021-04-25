import os
import smtplib
import ssl
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from signals import EMASignal, BBSignal, RSISignal


def FireEmail(stock, signal, sender, receiver):
    global server
    try:
        # Creating body of email
        message = MIMEMultipart()
        message["From"] = sender
        message["To"] = receiver
        message["Subject"] = f"Hey! The price of {stock} just triggered an alert!"

        body = f"""\
        <html>
    <body>
    <p>Hi There!
        <br/>
        <hr/>
    </p>
    <p>
        The stock price of <strong>{stock}</strong> just triggered an alert!
        <br/>
        <br/>
        The program is giving a <strong>{signal}</strong> signal.
        <br/>
        <br/>
        The parameter signals were passing:
        <ul>
            <li>EMA: {EMASignal(stock)}</li>
            <li>Bollinger Bands: {BBSignal(stock)}</li>
            <li>RSI: {RSISignal(stock)}</li>
        </ul>
        <br/>
        <br/>
    </p>
    <p>
        <em>Attached are the images of the signals plotted</em>
    </p>
    </body>
    </html>
        """

        message.attach(MIMEText(body, "html"))

        directory = f'image/{stock}'
        for f in os.listdir(directory):
            img_data = open(os.path.join(directory, f), 'rb').read()
            image = MIMEImage(img_data, name=os.path.basename(f))
            message.attach(image)

        text = message.as_string()

        # Initializing smtp server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        context = ssl.create_default_context()
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()

        server.login(user='analysis.technical.in@gmail.com', password=os.getenv('GMAIL_KEY'))
        server.sendmail(sender, receiver, text)
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.close()
