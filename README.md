# FlyLens 85 PX4 development reference

Source-linked hardware documentation and bring-up guidance for a custom PX4 aircraft based on a Flywoo FlyLens 85 frame.

> [!CAUTION]
> This bill of materials is **not flight-ready as listed**. It combines an 85 mm, 2-inch frame with a full-size Raspberry Pi, a roughly 61 g camera/gimbal, and motors whose manufacturer specifies 2.5–4-inch propellers. Exact variants, mechanical fit, propulsion current, camera power, and the communications path must be verified before powered integration. Remove propellers for all bench work.

## Proposed bill of materials

| User-supplied name | Normalized identity | Verification | Main issue |
|---|---|---:|---|
| Flywoo Lens 85 | Flywoo **FlyLens 85** frame | High | Frame revision and motor-hole pattern must be measured |
| Raspberry Pi 8 GB | Raspberry Pi 4 Model B or Raspberry Pi 5 | Low | Both exist in 8 GB variants; model is not specified |
| Sky Droid C10 Pro | SkyDroid C10 Pro | Low | No dedicated current official C10 Pro datasheet was located; C10 and C10 Pro data conflict |
| Mico Air AG01 | MicoAir **MG-A01** GNSS/compass, provisionally | Medium | The manufacturer model is MG-A01, not AG01 |
| Mico Air 35 A 743 | MicoAir743-AIO-35A, original/discontinued revision | Medium | V1 and V2 use different PX4 targets and ESC firmware |
| Zero Drag ELRS | Zerodrag Nexus1 2.4 GHz ELRS receiver, provisionally | Medium | Confirm label and installed ExpressLRS major version |
| RadioMaster Pocket | Pocket ELRS or CC2500 variant | Low | Direct compatibility requires the ELRS version or an external ELRS module |
| QPT 1404.5 4500 KV | Quanteon QPT 1404.5 KV4500 | High | Published use is 2.5–4-inch props, not the frame's 2-inch class |
| Mico MTF01 | MicoAir MTF-01 optical-flow/range sensor | High | PX4 1.17 MAVLink protocol setting needs deliberate configuration |
| Lava LiHV 3S 450 mAh ×2 | BETAFPV LAVA 3S 450 mAh 75C, two-pack package | High | “×2” does not say one-at-a-time, parallel, or series; series is incompatible with the motor rating |

Identity confidence describes the match between the supplied name and the sourced product. It is not a safety or suitability rating.

## Read this first

1. Review the [compatibility assessment](docs/compatibility.md).
2. Close the identity and measurement items in [open questions](docs/open-questions.md).
3. Use the proposed [interfaces and wiring](docs/interfaces-and-wiring.md) only after checking every connector with the exact revision's diagram and a multimeter.
4. Recalculate the [power and mass budget](docs/power-and-mass-budget.md) with measured values.
5. Follow the staged [bring-up and test plan](docs/bringup-and-test-plan.md).
6. Configure the controller from the pinned [PX4 integration guide](docs/px4-integration.md).

## Repository map

- [`hardware.yaml`](hardware.yaml): machine-readable inventory, identity state, and key constraints.
- [`components/`](components/): one technical sheet per component, including primary sources and unresolved claims.
- [`docs/architecture.md`](docs/architecture.md): proposed system architecture and data paths.
- [`references/README.md`](references/README.md): datasheet/manual/source register, including document versions and source quality.
- [`evidence/README.md`](evidence/README.md): where maintainers should record photos, measurements, configurations, logs, and test results.

## Current engineering conclusion

The AIO has mainline PX4 support and its 25.5 × 25.5 mm mounting pattern is compatible with the frame's documented FC pattern. The remaining system is a development experiment, not a validated configuration:

- Published/provisional mass entries already total **156.49–157.99 g dry**, excluding the Pi, battery, props, regulators, mounts, wiring, fasteners, and cooling; this subtotal uses the secondary-source 61 g C10 Pro value.
- With one 37.8 g battery, that subtotal becomes **194.29–195.79 g** before those omitted items.
- With both batteries carried, it becomes **232.09–233.59 g**, leaving at most 17.91 g for the Pi and all integration hardware and therefore making this BOM incompatible with a sub-250 g target.
- The QPT motor's published maximum figures do not include enough test conditions to size this 2-inch system. A guarded thrust-stand test using the exact propeller and 3S supply is mandatory.
- A full-size Pi must use a dedicated, low-noise 5 V regulator. The flight controller's 5 V/2 A rail is not an adequate design supply for a Pi 4/5 plus peripherals.
- Camera control and video transport are not established by the listed parts. SkyDroid documents app/SDK control and does not claim direct control from an unrelated RC transmitter.

## Documentation policy

This repository links to vendor-hosted manuals rather than redistributing them. Claims are tagged by source quality, product-revision ambiguity is preserved, and measured evidence should supersede assumptions. The research snapshot date is **2026-07-25**; re-check upstream documents before a hardware or firmware change.

## License and safety

Original repository text and code are MIT-licensed. Linked manuals, drawings, trademarks, and product images remain the property of their respective owners. This is engineering documentation, not a certification, airworthiness determination, or substitute for applicable radio, battery, and aviation rules.
