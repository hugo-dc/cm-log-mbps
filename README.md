# README

Get the average of Mgasps from the geth logs.

Used to compare geth performance using `--codemerkleization` flag and without using it.

Examples:

	# Get the average Mgasps for the geth log using --codemerkleization flag
	python analyze_log.py geth-log-cm.txt

	# Get the average Mgasps for the get log not using --codemerkleization flag
	python analyze_log.py geth-log-no-cm.txt

