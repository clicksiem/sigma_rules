uv run ./scripts/sigconvert.py -b clickhouse -d sigma/rules/
uv run ./scripts/sigconvert.py -b clickhouse -d sigma/rules-threat-hunting/
uv run ./scripts/sigconvert.py -b clickhouse -d sigma/rules-emerging-threats/

uv run ./scripts/sigconvert.py -b loki -d sigma/rules/
uv run ./scripts/sigconvert.py -b loki -d sigma/rules-threat-hunting/
uv run ./scripts/sigconvert.py -b loki -d sigma/rules-emerging-threats

git add clickhouse/
git commit -m 'ci(rules): update clickhouse sigma rules'

git add loki/
git commit -m 'ci(rules): update loki sigma rules'

git push origin
