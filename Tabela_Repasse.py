import re

class TabelaRepasse():
    def __init__(self, ip='', prefixo=''):
        self.ip = ip
        self.prefixo = prefixo

        if self.ip == '':
            raise ValueError("Ip não enviado.");

        if self.ip_tem_prefixo():
            pass

    def ip_tem_prefixo(self):
        # 192.168.20.65/24
        ip_prefixo_regexp = re.compile('^[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}/[0-9]{1,2}$')

        if ip_prefixo_regexp(self.ip):
            print("tem")
            return True
        print("N tem")
        return False

if __name__ == '__main__':
    pepasse = TabelaRepasse()