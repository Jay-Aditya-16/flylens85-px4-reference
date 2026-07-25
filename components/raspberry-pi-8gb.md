# Raspberry Pi 8 GB companion computer

**Sourced identity:** “Raspberry Pi 8 GB” can describe at least Raspberry Pi 4 Model B 8 GB or Raspberry Pi 5 8 GB.

## Candidate comparison

| Item | Raspberry Pi 4 Model B 8 GB | Raspberry Pi 5 8 GB |
|---|---|---|
| SoC | BCM2711, quad-core Cortex-A72 | BCM2712, quad-core Cortex-A76 at 2.4 GHz |
| Memory | 8 GB LPDDR4 | 8 GB LPDDR4X |
| Networking | Dual-band Wi-Fi, Bluetooth 5/BLE, Gigabit Ethernet | Dual-band Wi-Fi, Bluetooth 5/BLE, Gigabit Ethernet |
| USB | 2 × USB 3, 2 × USB 2 | 2 × USB 3, 2 × USB 2 |
| GPIO | 40-pin header | 40-pin header |
| Recommended supply capacity | 5 V/3 A | 5 V/5 A, 27 W USB-C supply recommended by Raspberry Pi |
| Typical bare-board active current in official power guidance | 600 mA | 800 mA |

## Identification fields

The board model string is available from Linux:

```sh
tr -d '\0' </proc/device-tree/model
```

Recordable technical fields include board revision, OS image, kernel version, bootloader version, storage type, cooling hardware, enabled interfaces, and attached peripherals.

## Primary sources

- [Raspberry Pi 4 Model B specifications](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/specifications/?variant=raspberry-pi-4-model-b-8gb)
- [Raspberry Pi 4 Model B datasheet](https://datasheets.raspberrypi.com/rpi4/raspberry-pi-4-datasheet.pdf)
- [Raspberry Pi 5 product page](https://www.raspberrypi.com/products/raspberry-pi-5/)
- [Raspberry Pi 5 product brief](https://datasheets.raspberrypi.com/rpi5/raspberry-pi-5-product-brief.pdf)
- [Raspberry Pi power-supply documentation](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#power-supply)
- [PX4 Raspberry Pi companion guide](https://docs.px4.io/v1.17/en/companion_computer/pixhawk_rpi)

Sources accessed 2026-07-25.
