uv run ./scripts/sigconvert.py -w clickhouse/
git add clickhouse/
git commit -m 'ci(rules): update clickhouse sigma rules'
git push origin
