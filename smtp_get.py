import smtpd
import asyncore


class CustomSMTPServer(smtpd.SMTPServer):
    def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):
        print('Receiving message from:', peer)
        print('Message addressed from:', mailfrom)
        print('Message addressed to  :', rcpttos)
        print('Message length        :', len(data))
        print('\n\n', data)
        print('\n__________________________________________________________________________________\n')
        raise asyncore.ExitNow('Server is quitting!')


server = CustomSMTPServer(('192.168.10.12', 25), None)

asyncore.loop()
