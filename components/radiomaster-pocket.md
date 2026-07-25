# RadioMaster Pocket transmitter

**Identity:** unresolved RF variant. RadioMaster sells Pocket versions with internal 2.4 GHz ExpressLRS or CC2500 multiprotocol hardware.

## Manufacturer specifications

| Item | Published value |
|---|---|
| Firmware | EdgeTX |
| RF variants | 2.4 GHz ELRS or CC2500; FCC/LBT choices |
| Frequency | 2.400–2.480 GHz |
| Channels | Up to 16, receiver/model dependent |
| Battery | 2 × 18650 cells, not included |
| Operating voltage | 6.6–8.4 V DC |
| Charging | USB-C |
| Gimbals | Hall-effect |
| Expansion | Nano module bay |
| Dimensions | 156.6 × 65.1 × 125.3 mm folded; 156.6 × 73.1 × 154.8 mm unfolded |
| Mass | 288 g |

## Compatibility decision

- **Pocket ELRS:** can bind directly to a compatible Nexus1 after matching the ExpressLRS major version, regulatory domain, and binding method.
- **Pocket CC2500:** cannot directly transmit ExpressLRS. Fit a compatible 2.4 GHz ELRS nano module and configure EdgeTX to use the external module.

The manual recommends dynamic power and notes that packet rates no higher than 500 Hz help battery life and heat. Packet rate is an RF/control tradeoff; choose it from link testing and required control latency rather than the maximum available value.

Create an EdgeTX model with deliberate channel order, arm/mode switches, output ranges, warnings, and a model-specific checklist. Validate every channel and failsafe in QGroundControl with propellers removed. SkyDroid states that third-party remote controllers cannot directly control its gimbals, so do not assign camera/gimbal channels until a documented companion/SDK adapter exists.

## Primary sources

- [RadioMaster Pocket product page](https://radiomasterrc.com/products/pocket-radio-controller-m2)
- [RadioMaster Pocket user manual PDF](https://cdn.shopify.com/s/files/1/0701/8066/7584/files/Pocket_A1.8.pdf?v=1770617495)
- [ExpressLRS quick start](https://www.expresslrs.org/quick-start/getting-started/)

Sources accessed 2026-07-25.
