<img width="1197" height="268" alt="VEICHI Header" src="https://github.com/user-attachments/assets/8c27f4cc-082f-4173-a9cd-b0d24bda7c32" />

# VEICHI AC70
Intégration HACS pour piloter un variateur VEICHI AC70 via Waveshare ETH Série RS485 Modbus RTU/TCP.

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

## Lovelace card example :

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
- Waveshare RS485 Ethernet
- VEICHI AC70
