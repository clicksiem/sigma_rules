uv run ./scripts/sigconvert.py -w clickhouse/ -d sigma/rules/
uv run ./scripts/sigconvert.py -w clickhouse/ -d sigma/rules-threat-hunting/
uv run ./scripts/sigconvert.py -w clickhouse/ -d sigma/rules-emerging-threats/
git add clickhouse/
git commit -m 'ci(rules): update clickhouse sigma rules'
git push origin
