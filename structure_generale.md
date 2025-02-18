# Structure générale

## Hardware
- **RASP** : Raspbery pi 4  (4go Ram)
- **LAB** : Dell optiplex 3010 SFF (i5 + 8go Ram, upgraded to 16go) 
- **box** : Livebox grand public du fournisseur français Orange

## Nom de domaine
- J'utilise un nom de domaine loué chez OVH pour simplifier l'acces au services exposés du homelab depuis l'exterieur.
- La box à IP dynamique, j'ai donc du metre en place un DynDNS pour que la BOX puisse communiquer son IP à OVH.
- Par chance la box permet de s'interfacer avec OVH depuis l'interface graphique, ce qui m'a permis de ne pas avoir à mettre en place un script.

## Entry Point & Networking
- Subnet utilisé par la box : 172.25.50.0, mask : 255.255.255.0
- Les IP des machines sont fixe :
	- Rasp : 172.25.50.10
	- Lab : 172.25.50.11
- La box forward les ports suivants vers RASP :
 	- 25565 - Minecraft
 	- 51820 - Wireguard
 	- 1022 - SSH Gitea
 	- 22 - SSH
 	- 5657 - SSH Pufferpanel
	- 80:82 - HTTP
	- 443:445 - HTTPS
- Les requetes reçues par la box sur les ports 80 & 443 sont specifiquement redirigé vers les ports 82 & 445 de RASP.
Cela fait partie de la conf Treafik pour cacher la majorité de mes services derier un VPN en gardant quelques services accescible sur le web (Voir : [Configuration Traefik]())

- RASP gère ensuite tout le trafique entrant en le redirigeant vers les services correspondants sur les deux machines.

## Liens
- [Rasp](/rasp/index.md)
- [Lab](/lab/index.md)

