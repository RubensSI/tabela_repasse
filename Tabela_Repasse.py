import re

class TabelaRepasse():
    def __init__(self, ip='', prefixo=''):
        self.ip = ip
        self.prefixo = prefixo

        if self.ip == '':
            raise ValueError("Ip não enviado.");

        self.ip_tem_prefixo()

        self.ip_decimal_binario(ip=self.ip)

    def ip_decimal_binario(self, ip=''):
        if not ip:
            ip = self.ip

        # A variável bloco_ip se refere ao bloco de endereço
        bloco_ip = ip.split('.')
        ip_bin = []

        for bloco in bloco_ip:
            binario = bin(int(bloco))
            binario = binario[2:].zfill(8)
            ip_bin.append(binario)

        ip_bin = '.'.join(ip_bin)
        return ip_bin

    def ip_tem_prefixo(self):
        # 192.168.20.65/24
        ip_prefixo_regexp = re.compile('^[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}/[0-9]{1,2}$')

        if not ip_prefixo_regexp.search(self.ip):
            return

        divide_ip = self.ip.split('/')
        self.ip = divide_ip[0]
        self.prefixo = divide_ip[1]


if __name__ == '__main__':
    pepasse = TabelaRepasse(ip='192.168.20.65/24')