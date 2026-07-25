# Zerodrag Nexus1 ExpressLRS receiver

- **Supplied name:** Zero Drag ELRS
- **Provisional match:** Zerodrag Nexus1 2.4 GHz receiver
- **Identity confidence:** medium; confirm the label and firmware target.

## Manufacturer specifications

| Item | Published value |
|---|---|
| RF band | 2.4 GHz ISM |
| Telemetry power | Up to 10 mW |
| Supply | 5 V |
| Receiver dimensions/mass | 20 × 13 mm; 1.2 g |
| T antenna mass | 2.29 g |
| RF connector | IPEX1 |
| Interface | Full-duplex CRSF on TX/RX |

The four electrical connections are GND, 5V, TX, and RX. Cross the data pair at the FC. Secure the IPEX connector without loading its socket and place the antenna away from carbon, batteries, high-current wiring, GNSS, and video hardware.

## PX4 warning

The vendor manual's “PX4 / ARDUPILOT” section shows an ArduPilot `SERIAL1_PROTOCOL=RCIN` setting. It is not a PX4 v1.17 setting. Full-duplex CRSF telemetry on PX4 uses the CRSF RC driver and `RC_CRSF_*` parameters described in [PX4 integration](../docs/px4-integration.md).

## ExpressLRS compatibility

- Transmitter module and receiver need compatible ExpressLRS major versions.
- The RadioMaster Pocket must be the internal ELRS variant or use an external compatible ELRS module in its nano bay.
- Regulatory domain/firmware options must match both devices and local rules.
- Record packet rate, telemetry ratio, dynamic-power settings, antenna, firmware target/version, and failsafe behavior. Do not publish the binding phrase.
- Perform range/link-quality and RF coexistence tests in the final layout.

## Primary sources

- [Zerodrag Nexus1 product page](https://zerodrag.in/products/express-lrs-receiver-2-4ghz-made-in-india)
- [Nexus1 User Manual v1.1 PDF](https://cdn.shopify.com/s/files/1/0567/9038/4729/files/Zerodrag_Nexus1_User_Manual_Version_1.1.pdf?v=1712646205)
- [ExpressLRS receiver wiring](https://www.expresslrs.org/quick-start/receivers/wiring-up/)
- [ExpressLRS firmware-version compatibility](https://www.expresslrs.org/quick-start/receivers/firmware-version/)
- [ExpressLRS firmware options](https://www.expresslrs.org/quick-start/firmware-options/)
- [PX4 CRSF telemetry guide](https://docs.px4.io/v1.17/en/telemetry/crsf_telemetry)

Sources accessed 2026-07-25.
