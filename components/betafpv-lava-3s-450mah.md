# BETAFPV LAVA 3S 450 mAh LiHV battery

- **Identity confidence:** high.
- **Quantity supplied:** two packs. Package quantity does not define electrical topology.

## Manufacturer specifications

| Item | 3S 450 mAh value |
|---|---|
| Chemistry | LiHV |
| Capacity / label | 450 mAh / 75C |
| Nominal voltage | 11.4 V |
| Maximum voltage | 13.05 V (4.35 V/cell) |
| Nominal energy | 5.13 Wh |
| Connector / lead | XT30, 16 AWG |
| Balance connector | JST-XH 2.54 |
| Dimensions | 63 × 15.5 × 21 mm |
| Mass | 37.8 g each |
| Vendor discharge floor | Do not discharge below 3.0 V/cell under load |
| Storage guidance | 3.8–3.9 V/cell |

## Current-rating caution

Multiplying the label gives 0.45 Ah × 75 C = 33.75 A. The product page does not identify whether 75C is a continuous or burst rating, its duration, allowable temperature, voltage-sag criterion, or end-of-life condition. It is not proof that one pack can supply a four-motor headline maximum. Use measured sag, temperature, connector loss, delivered capacity, and cell balance under the exact propulsion profile.

## Two-pack decision

- **Use one at a time** for initial work: 3S, 450 mAh, 5.13 Wh, 37.8 g.
- **Parallel** would remain 3S and become 900 mAh/10.26 Wh before losses, but requires intentionally matched packs, equal connection voltage, a reviewed current-sharing harness, and mass/CG revalidation.
- **Series is rejected:** it would be 6S LiHV, 26.1 V full. That is inside the original AIO's upper limit but outside the QPT motor's documented 3S/4S application.

Use a LiHV-capable balance charger, fire-resistant charging area, conservative charge rate, pack inspection, individual-cell monitoring, and a retirement rule for damage, swelling, imbalance, heat, or loss of capacity. Never parallel packs at unequal voltages or charge an assembled parallel system without a reviewed procedure.

## Primary source

- [BETAFPV LAVA 2S/3S/4S 450 mAh 75C battery product page](https://betafpv.com/products/lava-2s-3s-4s-450mah-75c-battery-2pcs)

Source accessed 2026-07-25.
