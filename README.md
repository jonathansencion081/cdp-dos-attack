# CDP DoS Attack Script
**Autor:** Jonathan Sención  
**Matrícula:** 20250851  
**Institución:** ITLA - Instituto Tecnológico de las Américas  

---

## Objetivo del Laboratorio
Demostrar cómo un atacante puede realizar un ataque de Denegación de Servicio (DoS) 
contra switches Cisco mediante el protocolo CDP (Cisco Discovery Protocol), saturando 
la tabla de vecinos CDP del switch hasta agotar su memoria y CPU.

---

## Objetivo del Script
Generar paquetes CDP malformados con MACs aleatorias hacia la dirección multicast CDP 
`01:00:0c:cc:cc:cc`, saturando la tabla CDP del switch víctima.

### Parámetros Usados
| Parámetro | Valor | Descripción |
|---|---|---|
| `dst` | `01:00:0c:cc:cc:cc` | Dirección multicast CDP |
| `src` | `RandMAC()` | MAC aleatoria por paquete |
| `iface` | `eth0` | Interfaz de red atacante |
| `OUI` | `0x00000c` | OUI de Cisco |
| `code` | `0x2000` | Código CDP |

### Requisitos
- Kali Linux
- Python 3
- Scapy (`sudo apt install python3-scapy`)
- Interfaz conectada a la misma red que el switch víctima
- Ejecutar como root (`sudo`)

---

## Funcionamiento del Script
1. Se construye un frame Ethernet con MAC destino multicast CDP
2. Se encapsula con LLC y SNAP usando el OUI de Cisco
3. Se genera un Device ID aleatorio por cada paquete
4. El switch recibe los paquetes y los procesa como vecinos CDP legítimos
5. La tabla CDP del switch se satura agotando recursos

---

## Topología de Red
[Kali Atacante] eth0 ──── e0/2 [SW1] e0/0 ──── e0/0 [SW2] e0/1 ──── eth0 [VPC1]
192.168.85.10                10.20.25.1              10.20.25.2         192.168.85.20
│
e0/1 └──── e0/0 [SW3] e0/1 ──── eth0 [VPC2]
10.20.25.3         192.168.51.20

### VLANs
| VLAN | Nombre | Red |
|---|---|---|
| VLAN 10 | VLAN10-20250851 | 192.168.85.0/24 |
| VLAN 20 | VLAN20-20280851 | 192.168.51.0/24 |
| Management | MGMT | 10.20.25.0/24 |

---

## Ejecución
```bash
sudo python3 cdp_dos.py
```

### Verificación del Ataque
En el switch víctima:
show cdp neighbors
show processes cpu

---

## Capturas de Pantalla
<img width="717" height="630" alt="image" src="https://github.com/user-attachments/assets/e315469c-7047-44a5-9f0f-c23eeec2b0c5" />

<img width="755" height="501" alt="image" src="https://github.com/user-attachments/assets/057efcf9-a611-44a8-9e82-4c4115e5756f" />

<img width="764" height="125" alt="image" src="https://github.com/user-attachments/assets/4aab0e2e-a208-400c-942c-f2946163ca36" />

---

## Contramedidas
### 1. Deshabilitar CDP globalmente
no cdp run
### 2. Deshabilitar CDP por interfaz
interface e0/2
no cdp enable
### 3. Habilitar solo en interfaces necesarias
CDP solo debe estar activo entre dispositivos Cisco de confianza, nunca en puertos 
de acceso hacia usuarios finales o dispositivos desconocidos.

---
