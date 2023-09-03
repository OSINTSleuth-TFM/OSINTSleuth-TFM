import whois
import dns.resolver
import requests
import re

def obtener_informacion_dominio(dominio):
    informacion = {}
    
    # Obtener información de Whois
    informacion_whois = whois.whois(dominio)
    informacion['Whois'] = informacion_whois.__dict__
    
    registros_dns = {}
    
    # Obtener registros DNS
    try:
        respuesta_dns = dns.resolver.resolve(dominio, 'A')
        registros_a = [str(r) for r in respuesta_dns]
        registros_dns['A'] = registros_a
    except dns.resolver.NoAnswer:
        registros_dns['A'] = []
    
    try:
        respuesta_dns = dns.resolver.resolve(dominio, 'MX')
        registros_mx = [str(r.exchange) for r in respuesta_dns]
        registros_dns['MX'] = registros_mx
    except dns.resolver.NoAnswer:
        registros_dns['MX'] = []
    
    try:
        respuesta_dns = dns.resolver.resolve(dominio, 'NS')
        registros_ns = [str(r) for r in respuesta_dns]
        registros_dns['NS'] = registros_ns
    except dns.resolver.NoAnswer:
        registros_dns['NS'] = []
    
    informacion['Registros DNS'] = registros_dns
    
    # Obtener información de encabezados HTTP
    try:
        respuesta = requests.get('http://' + dominio)
        informacion['Encabezados HTTP'] = respuesta.headers
        
    except requests.exceptions.RequestException:
        informacion['Encabezados HTTP'] = 'No se pudo obtener información de encabezados HTTP'
    
    # Obtener correos electrónicos del contenido de la página
    correos_electronicos = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', respuesta.text)
    informacion['Correos Electrónicos'] = correos_electronicos
    
    # Obtener cuentas de redes sociales
    cuentas_redes_sociales = obtener_cuentas_redes_sociales(dominio)
    informacion['Cuentas Redes Sociales'] = cuentas_redes_sociales

    return informacion

def obtener_cuentas_redes_sociales(dominio):
    cuentas_redes_sociales = {
        'Facebook': f'https://www.facebook.com/{dominio}',
        'Twitter': f'https://twitter.com/{dominio}',
        'Instagram': f'https://www.instagram.com/{dominio}',
        'LinkedIn': f'https://www.linkedin.com/company/{dominio}',
        'YouTube': f'https://www.youtube.com/{dominio}',
    }
    return cuentas_redes_sociales

# Solicitar el dominio al usuario
dominio = input("Ingrese el dominio que desea analizar: ")

# Obtener la información del dominio
informacion_dominio = obtener_informacion_dominio(dominio)

# Imprimir la información del dominio
for categoria, datos in informacion_dominio.items():
    print(f"{categoria}:")
    print(datos)
    print()

