<img width="1197" height="268" alt="VEICHI Header" src="https://github.com/user-attachments/assets/8c27f4cc-082f-4173-a9cd-b0d24bda7c32" />

# VEICHI AC10-70-300
- Intégration HACS pour piloter un variateur VEICHI model AC70, AC70 et AC300.
- Contrôle via le node Waveshare ETH Série RS485 Modbus RTU/TCP.

## Fonctionnalités
- Marche / Arrêt
- Sens de rotation
- Réglage fréquence 0–50 Hz
- Courant, puissance, température
- Config UI
- Diagnostics Home Assistant

## Installation
1. Ouvrir Home Assistant → HACS → Integrations → Custom repositories
2. Ajouter l’URL du dépôt dans HACS :
   ```
   https://github.com/SoFarSoGood86/veichi_ac70
   ```
3. Installer l'intégration, choisir **Category: Integration**
4. Configurer l'adresse IP (192.168.1.254)
5. Installer l’intégration et redémarrer HA

## Configuration Waveshare ETH/Série RS232 / RS485-422

- Renseigner les champs :

   * **IP du boîtier Waveshare** : ex. `192.168.1.254` (ou autre selon configuration)
   * **Port TCP** : ex. `23` (ou autre selon configuration)
   * **Mode physique** : RS485
   * **Slave Modbus** : ex. `1`(ou autre selon configuration)

- Valider et sauvegarder

## Lovelace - carte example :

#### Carte simple ( Entities )
```yaml
type: entities
title: VEICHI AC70
entities:
  - switch.ac70_marche
  - switch.ac70_sens_rotation
  - number.ac70_frequence
  - sensor.ac70_frequence_reelle
  - sensor.ac70_courant_moteur
  - sensor.ac70_puissance_moteur
  - sensor.ac70_temperature_variateur
```
#### Carte avancée ( Gauge + Buttons )
```yaml
type: vertical-stack
cards:
  - type: gauge
    entity: sensor.ac70_frequence_reelle
    min: 0
    max: 50
    name: Fréquence (Hz)

  - type: horizontal-stack
    cards:
      - type: button
        entity: switch.ac70_marche
        name: Marche
      - type: button
        entity: switch.ac70_sens_rotation
        name: Sens
```

#### Matériel compatible
- Waveshare Ethernet (poe) to RS232/485/422. [lien pdf](https://www.waveshare.com/wiki/RS232/485/422_TO_POE_ETH_(B))
- VEICHI AC10 [lien pdf](https://www.veichi.com/d/file/download/low-voltage-drives/ac10-series-frequency-inverter-manual-v1.pdf)
- VEICHI AC70 [Lien pdf](https://www.veichi.com/d/file/p/20180122/7824c2072d7575f857710d8a31bf2e25.pdf)
- VEICHI AC300 [Lien pdf](https://www.veichi.com/d/file/download/low-voltage-drives/veichi-ac300-technical-manual-v1-0.pdf)

## Avertissement

Cette intégration n'est **pas approuvée, associée ou supportée par VEICHI**. 

Le nom « VEICHI », les logos et toutes les marques de commerce et marques déposées présents dans ce dépôt sont la propriété de VEICHI.
L'utilisation de ces noms, marques de commerce et logos dans ce projet est uniquement à des fins d'identification et n'implique aucune approbation ou affiliation avec VEICHI.
