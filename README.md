# Clicksiem sigma rules

This is a github pipeline repository that runs every day the script `scripts/update.sh` to download latest sigma rules repository and convert to *clickdetect* format.

This will help users to easly migrate from others platforms to clicksiem.

- `clickhouse/`: Clicksiem rules for clickhouse
- `clickhouse/rules/`: Default sigma rules
- `clickhouse/rules-emerging-threats/`: Emerging threats
- `clickhouse/rules-threat-hunting/`: Threat hunting
