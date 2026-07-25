# Raspberry Pi 8 GB companion computer

**Identity:** unresolved. “Raspberry Pi 8 GB” can describe at least Raspberry Pi 4 Model B or Raspberry Pi 5. The distinction changes compute performance, connectors, cooling, power design, and integration risk.

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

Typical current is not a regulator-sizing value. Boot, CPU/GPU load, storage, radio, USB devices, camera/video work, regulator/cable loss, and transient behavior determine the actual supply.

## Identification

Run on the board:

```sh
tr -d '\0' </proc/device-tree/model
```

Also photograph the board markings and record the OS image, kernel, bootloader, storage, cooling, and enabled interfaces.

## Airframe integration

- Do not power a Pi 4/5 from the AIO's 5 V/2 A BEC. Use a dedicated, low-noise 5 V regulator sized and tested for the identified model.
- The UART GPIO uses 3.3 V logic. Cross TX/RX, share ground, and never connect RS-232 voltage levels.
- Use either MAVLink or uXRCE-DDS on the allocated FC port, not two services contending for the same UART.
- Disable unused radios/interfaces only after confirming operational needs; validate their effect on power and EMI.
- Provide storage retention, cooling, vibration isolation, and clean shutdown or a read-only/resilient filesystem.
- Measure the exact board and complete mounting mass; the official product briefs reviewed here do not provide a board mass suitable for this budget.

## Primary sources

- [Raspberry Pi 4 Model B specifications](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/specifications/?variant=raspberry-pi-4-model-b-8gb)
- [Raspberry Pi 4 Model B datasheet](https://datasheets.raspberrypi.com/rpi4/raspberry-pi-4-datasheet.pdf)
- [Raspberry Pi 5 product page](https://www.raspberrypi.com/products/raspberry-pi-5/)
- [Raspberry Pi 5 product brief](https://datasheets.raspberrypi.com/rpi5/raspberry-pi-5-product-brief.pdf)
- [Raspberry Pi power-supply documentation](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#power-supply)
- [PX4 Raspberry Pi companion guide](https://docs.px4.io/v1.17/en/companion_computer/pixhawk_rpi)

Sources accessed 2026-07-25.
