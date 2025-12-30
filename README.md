<img width="1197" height="417" alt="VEICHI Header" src="https://github.com/user-attachments/assets/9b6fccda-1099-43cb-bcc5-1732d246eb9e" />

# VEICHI AC70
Intégration HACS pour piloter un variateur VEICHI AC70 via Waveshare ETH RS485 Modbus RTU/TCP.

## Fonctionnalités
- Marche / Arrêt
- Sens de rotation
- Réglage fréquence 0–50 Hz
- Courant, puissance, température
- Config UI
- Diagnostics Home Assistant

## Installation
1. Ajouter le dépôt GitHub dans HACS
2. Installer l'intégration
3. Configurer l'adresse IP (192.168.1.254)

## Lovelace card example :

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
