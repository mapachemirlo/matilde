#!/usr/bin/env python
#_*_coding: utf8 _*_
# MatildeInfo - Version 1
# Trae información de las cabeceras de un dominio o subdominio
# Autor: Claudio Herrera - claudioherrera@protonmail.ch
# Ejecutar con Python 3.*

import requests
import urllib.request
import argparse
import http.cookiejar as cookielib
import dns.resolver
import os, sys
import json
from progress.bar import Bar
from pyfiglet import Figlet
#reload(sys)
#sys.setdefaultencoding('utf8')

sis_op = sys.platform
sis_op = sis_op[:3]
if sis_op == 'lin':
    os.system('clear')
elif sis_op == 'win':
    os.system('cls')
else:
    pass

custom_fig = Figlet(font='slant')
print(custom_fig.renderText('MatildeInfo'))
print(' *** Informaciones varias ***\n --- Autor:Claudio Herrera - claudioherrera@protonmail.ch ---\n')
print(' Ejecutar con Python 3.*\n')
print('-----------------------------------------------------------------------------')

parser = argparse.ArgumentParser(description="Buscar cabeceras")
parser.add_argument('-d', '--dominio', help='Dominio')
parser = parser.parse_args()
user_agent = {'User-agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
cookie = cookielib.CookieJar()
global ip

def main():
    if parser.dominio:
        try:
            try:
                url_prot = ('https://'+ parser.dominio)
                get_url = requests.get(url=url_prot, headers=user_agent, timeout=2, cookies=cookie)
                prot = get_url.url
                codigo = get_url.status_code
                scrap = get_url.text #Me trae toda la web viva.
                
                #print("La web traida es: " + prot)
                bar = Bar(('Conectando a ... {}'.format(prot)), max=10)
                for e in range(10):
                    get_url = requests.get(url=url_prot, headers=user_agent, timeout=2, cookies=cookie)
                    bar.next()
                bar.finish()
            except:
                url_prot = ('http://'+ parser.dominio)
                get_url = requests.get(url=url_prot, headers=user_agent, timeout=2, cookies=cookie)
                prot = get_url.url
                codigo = get_url.status_code
                scrap = get_url.text #Me trae toda la web viva.
                
                #print("La web traida es: " + prot)
                bar = Bar(('Conectando a ... {}'.format(prot)), max=10)
                for e in range(10):
                    get_url = requests.get(url=url_prot, headers=user_agent, timeout=2, cookies=cookie)
                    bar.next()
                bar.finish()
        except:
            try:
                url_prot = ('http://www.' + parser.dominio)
                get_url = requests.get(url=url_prot, headers=user_agent, timeout=2, cookies=cookie)
                prot = get_url.url
                codigo = get_url.status_code
                scrap = get_url.text #Me trae toda la web viva.
                
                #print("la web traida es: " + prot)
                bar = Bar(('Conectando a ... {}'.format(prot)), max=10)
                for e in range(10):
                    get_url = requests.get(url=url_prot, headers=user_agent, timeout=2, cookies=cookie)
                    bar.next()
                bar.finish()
            except:  
                url_prot = ('https://www.' + parser.dominio)
                get_url = requests.get(url=url_prot, headers=user_agent, timeout=2, cookies=cookie)
                prot = get_url.url
                codigo = get_url.status_code
                scrap = get_url.text #Me trae toda la web viva.
                
                #print("la web traida es: " + prot)
                bar = Bar(('Conectando a ... {}'.format(prot)), max=10)
                for e in range(10):
                    get_url = requests.get(url=url_prot, headers=user_agent, timeout=2, cookies=cookie)
                    bar.next()
                bar.finish()
        			
        print('')
        print("Conectando a: " + prot + "\n")
        print("Estado de respuesta:{}".format(codigo) + " OK\n")
        print("Cookie: ", cookie)
        print("\n|============= CABECERAS =============|\n")
        cabec = dict(get_url.headers)
        for m in cabec.keys():
            print("{}:{}".format(m, cabec[m]))

        try:
            
            archiv = open('scrap.html', 'w')
            archiv.write(scrap)
            archiv.close()
            print('------------------------------------------------------')
            print("\n++ Archivo .html generado (puede contener errores)\n")
            print('------------------------------------------------------')
        except:
            print("\nNo se pudo generar el archivo html\n")
        
       
        print("\n|========== RESUELVE A','AAAA','NS','SOA','MX','MF','MD','TXT ===========|\n")
        consultas = ['A','AAAA','NS','SOA','MX','MF','MD','TXT'] #BUSCAR EN INTERNET CUALES MÁS TIPOS DE REGISTROS SE PUEDEN AGREGAR
        ip_dns = ['A']
        for cons in ip_dns:
            try:
                dn = dns.resolver.query(parser.dominio, cons) # Como 2do parámetro puede ir 'ANY', pero no anda
                for ip in dn: 
                    print("La IP del dominio {} es: {}\n".format(parser.dominio, ip))
            except:
                print("--- NO PUDO OBTENER LA IP ---")

        for cons in consultas:
            try:
                dn = dns.resolver.query(parser.dominio, cons) # Como 2do parámetro puede ir 'ANY', pero no anda
                for e in dn: 
                    print(e)
            except:
                print("--- NO PUDE OBTENER LA CONSULTA ---")

        print("\n|============== GEOLOCALIZACIÓN ==============|\n")
        try:
            geo = ("https://ipinfo.io/{}/json".format(ip))
            dat_url = urllib.request.urlopen(geo)
            js = json.loads(dat_url.read())

            for dato in js:
                print(dato + " : " + js[dato])
            print('')
        except:
            print("--- No se pudo obtener Geolocalización ---\n-- Ctrl+C para datener...--")
            

    else:
        print("\nNO pasó ningún dominio!, utilice: python matilde.py -d dominio\n")       

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrumpido por el usuario...")