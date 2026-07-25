# Project evidence

Keep project-specific measurements and configuration artifacts here. Suggested structure:

```text
evidence/
  identity/          labels and PCB photographs
  mechanical/        dimensioned drawings, mass, CG, sensor rotations
  electrical/        pin checks, rail/ripple/current/thermal measurements
  propulsion/        thrust-stand data and plots
  firmware/          PX4 board diff, artifact SHA-256, ESC and ELRS versions
  configuration/     sanitized PX4 and EdgeTX exports
  logs/              sanitized boot logs and ULogs
  test-reports/       dated acceptance records
```

Each record should include date, operator, hardware revision, firmware commit/tag, setup, instruments, units, environmental conditions, uncertainty where relevant, result, and pass/fail criterion. Preserve raw data beside derived plots.

Before publishing, remove serial numbers if sensitive, Wi-Fi credentials, API keys, ELRS binding phrases, personal information, exact home coordinates, and other operational secrets. Large ULogs/video should use Git LFS or a release/object store with immutable checksums rather than normal Git history.
