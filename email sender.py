from email.mime.application import MIMEApplication
from smtplib import SMTP_SSL  # 增加SSL验证,防止被截获
from email.mime.text import MIMEText  # 邮件文本
from email.mime.multipart import MIMEMultipart
from email.header import Header
from PyQt5.QtWidgets import QApplication, QFileDialog


def file_manager():
    app = QApplication([])
    file_dialog = QFileDialog()
    file_path = file_dialog.getOpenFileName()
    return file_path[0]


#  邮件构建
class SendEmail:
    def __init__(self, receiver):
        self.host_sever = 'smtp.163.com'  # 服务器地址
        self.sender = "jinxiaofengzhihome@163.com"  # 发送人
        self.receiver = receiver  # 收件人
        self.pass_word = 'ILXICMJDWTRDEZXE'  # 授权码

    def send_txt_email(self):
        mail_title, mail_content = '', ''
        while mail_title == '' or mail_content == '':  # 如果邮件标题和邮件内容有一个为空则要求重新输入
            mail_title = input("请输入邮件标题:")
            mail_content = input("请输入邮件文本:")
        message = MIMEMultipart()  # 实例化邮件封装方法
        message['subject'] = Header(mail_title, "utf-8")
        message['From'] = self.sender
        message['To'] = Header("我", 'utf-8')
        message.attach(MIMEText(mail_content, 'plain', 'utf-8'))

        answer = input("是否要附带附件: y/n")
        if answer == "y":
            folder_path = file_manager()
            attachment = MIMEApplication(open(folder_path, 'rb').read())
            attachment.add_header('Content-Disposition', 'attachment', filename=folder_path.split("/")[-1])
            message.attach(attachment)
        try:
            smtp = SMTP_SSL(self.host_sever)
            smtp.login(self.sender, self.pass_word)
            smtp.sendmail(self.sender, self.receiver, message.as_string())
            smtp.quit()
        except Exception as e:
            print(e)


class Run:
    def __init__(self, receiver):
        self.receiver = receiver
        self.sender = SendEmail(self.receiver)

    def send_txt_email(self):
        self.sender.send_txt_email()


while True:
    input_receiver = input("请输入收件人地址:")
    if input_receiver:
        break

if input_receiver:
    run_mod = Run(input_receiver)
    run_mod.send_txt_email()

else:
    print("请输入收件人地址!")



