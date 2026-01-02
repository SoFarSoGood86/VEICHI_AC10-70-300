<img width="1197" height="268" alt="VEICHI Header" src="https://github.com/user-attachments/assets/8c27f4cc-082f-4173-a9cd-b0d24bda7c32" />

# VEICHI AC10-70-300
- Intégration HACS de contrôle pour variateurs de vitesse de fréquence pour les séries VEICHI AC10, AC70 et AC300.
- Protocole de controle Modbus RTU/TCP -> Waveshare ETH Serial node RS232-RS485/422.

## Fonctions :
- Marche / Arrêt
- Sens de Rotation
- Réglage fréquence 0–50 Hz
- Courant, puissance, température
- Config UI
- Diagnostics Home Assistant

<img width="1197" height="21" alt="Baner" src="https://github.com/user-attachments/assets/f3ae4b2b-d0ec-4efd-9821-147d31e2c54b" />

## Installation :
1. Ouvrir Home Assistant → HACS → Integrations → Custom repositories.
2. Ajouter l’URL du dépôt dans HACS :
   ```
   https://github.com/SoFarSoGood86/veichi_ac10_70_300.git
   ```
3. Installer l'intégration, choisir **Category: Integration**.
4. Configurer l'adresse IP `192.168.1.70`.
5. Installer l’intégration et redémarrer Home Assistant.

## Configuration du node Waveshare ETH to Serial RS232 / RS485-422 :

- Renseigner les champs :

   * **IP du boîtier Waveshare** : ex. `192.168.1.70` (ou autre selon configuration)
   * **Port TCP** : ex. `502` (ou autre selon configuration)
   * **Mode physique** : RS485
   * **Slave Modbus** : ex. `1`(ou autre selon configuration)

- Valider et sauvegarder

<img width="1197" height="21" alt="Baner" src="https://github.com/user-attachments/assets/f3ae4b2b-d0ec-4efd-9821-147d31e2c54b" />

## Configuration yaml :

#### VEICHI AC10 :

```yaml
modbus:
  - name: veichi_ac10
    type: tcp
    host: 192.168.1.70    # Ou autre IP selon configuration
    port: 502             # Ou autre Port selon configuration 
    delay: 1
    timeout: 5

    En cours...
```

#### VEICHI AC70 :

```yaml
modbus:
  - name: veichi_ac70
    type: tcp
    host: 192.168.1.70    # Ou autre IP selon configuration
    port: 502             # Ou autre Port selon configuration
    delay: 1
    timeout: 5

    switches:
      - name: "AC70 Marche"
        slave: 1
        address: 0x2000
        write_type: holding
        command_on: 1      # Marche
        command_off: 0     # Arrêt

      - name: "AC70 Sens rotation"
        slave: 1
        address: 0x2002     # Sens de rotation
        write_type: holding
        command_on: 1       # Avant
        command_off: 0      # Arrière

    numbers:
      - name: "AC70 Fréquence consigne"
        slave: 1
        address: 0x2001
        write_type: holding
        unit_of_measurement: "Hz"
        min: 0
        max: 50
        step: 0.1
        scale: 0.01
        precision: 2

    sensors:
      - name: "AC70 Fréquence actuelle"
        slave: 1
        address: 0x2103
        input_type: holding
        unit_of_measurement: "Hz"
        scale: 0.01
        precision: 2

      - name: "AC70 Courant moteur"
        slave: 1
        address: 0x2104
        input_type: holding
        unit_of_measurement: "A"
        scale: 0.1
        precision: 1

      - name: "AC70 Puissance moteur"
        slave: 1
        address: 0x2106
        input_type: holding
        unit_of_measurement: "kw"
        scale: 0.1
        precision: 1

      - name: "AC70 Température variateur"
        slave: 1
        address: 0x2107
        input_type: holding
        unit_of_measurement: "°C"
        scale: 1
        precision: 0
```

#### VEICHI AC300 :

```yaml
modbus:
  - name: veichi_ac300
    type: tcp
    host: 192.168.1.70    # Ou autre IP selon configuration
    port: 502             # Ou autre Port selon configuration 
    delay: 1
    timeout: 5

    En cours...
```
<img width="1197" height="21" alt="Baner" src="https://github.com/user-attachments/assets/f3ae4b2b-d0ec-4efd-9821-147d31e2c54b" />

## Lovelace - carte example :

#### Configuration HA :
1. Sur le tableau de bord, aller dans "Modifier tableau de bord" en haut à droite
2. "Ajouter au tableau de bord" puis selectionner "Manuel"
3. Copier les codes ci-dessous
4. Coller manuellement le code YAML

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

<img width="1197" height="21" alt="Baner" src="https://github.com/user-attachments/assets/f3ae4b2b-d0ec-4efd-9821-147d31e2c54b" />

## Matériel compatible
- Waveshare Ethernet (poe) to RS232/485/422. [pdf](https://www.waveshare.com/wiki/RS232/485/422_TO_POE_ETH_(B))
- VEICHI AC10 [pdf](https://www.veichi.com/d/file/download/low-voltage-drives/ac10-series-frequency-inverter-manual-v1.pdf)
- VEICHI AC70 [pdf](https://www.veichi.com/d/file/p/20180122/7824c2072d7575f857710d8a31bf2e25.pdf)
- VEICHI AC300 [pdf](https://www.veichi.com/d/file/download/low-voltage-drives/veichi-ac300-technical-manual-v1-0.pdf)

<img width="1197" height="21" alt="Baner" src="https://github.com/user-attachments/assets/f3ae4b2b-d0ec-4efd-9821-147d31e2c54b" />

## Avertissement

Cette intégration n'est **pas approuvée, associée ou supportée par VEICHI**. 

Le nom « VEICHI », les logos et toutes les marques de commerce et marques déposées présents dans ce dépôt sont la propriété de VEICHI.
L'utilisation de ces noms, marques de commerce et logos dans ce projet est uniquement à des fins d'identification et n'implique aucune approbation ou affiliation avec VEICHI.

