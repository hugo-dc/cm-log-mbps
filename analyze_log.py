import sys

def get_field(msg, field, next_field):
    soff = msg.find(field) + len(field)
    eoff = msg.find(next_field) - 1
    return msg[soff:eoff]

def analyze_message(msg):
    if msg == "Starting Geth on Ethereum mainnet...":
        return "CLIENT_START"
    if msg[:31] == "Loaded most recent local header":
        block_number = get_field(msg, "number=", "hash=")
        return "INITIAL_BLOCK_" + block_number
    if msg[:26] == "Imported new chain segment":
        mbps = get_field(msg, "mgasps=", "number=")
        block = get_field(msg, "number=", "hash=")
        return "MBPS_" + block + '_' + mbps
    return ""

def structure_data(line):
    words = line.split(' ')
    if len(words) <= 1:
        return {}

    message = ' '.join(words[2:])
    log_structure = {
            "log_type" : words[0],
            "timestamp" : words[1],
            "message" : message,
            "info" : analyze_message(message),
            }

    return log_structure


if __name__ == "__main__": 
    log_name = sys.argv[1]
    print("Reading", log_name, "...")

    input_log = open(log_name, 'r')

    c = 0
    total_mbps = 0
    results = []
    for line in input_log:
        log_object = structure_data(line)


        if log_object and log_object['info'][:4] == 'MBPS':
            data = log_object['info'].split('_')
            block = data[1]
            mbps = float(data[2])
            total_mbps += mbps
            results.append((block, mbps))
            
            c += 1

    print("total_results: ", c)
    print("~", total_mbps/c)

