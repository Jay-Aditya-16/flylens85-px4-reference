# Contributing

Changes should make the platform easier to reproduce without turning assumptions into facts.

1. Open an issue describing the component, revision, or claim being changed.
2. Prefer the manufacturer, silicon vendor, PX4 source tree, or protocol project as the source.
3. Record the source URL, document title/version, access date, and the exact hardware revision it covers.
4. Mark reseller, mirror, forum, and measured claims clearly; do not silently merge conflicting values.
5. Put test evidence under `evidence/` using stable, descriptive filenames. Remove credentials, binding phrases, GPS home positions, serial numbers, and other sensitive information.
6. Run `python3 scripts/validate_repo.py` before committing.

For measurements, include the instrument, method, ambient conditions, firmware commit/tag, PX4 parameter export, and uncertainty where practical. For propulsion tests, include battery voltage, propeller manufacturer/model/orientation, ESC protocol and firmware, motor temperature, thrust, current, and test duration.
