import factom
import sys
import json
import insurance_costs
script, chainId = sys.argv

#Get a list of all chain entries
entries = factom.chain_entries(chainId)
#TODO pagination doesnt work.
#print(entries)
cost = 5.0 # initial cost
interval = 2 #predetermined seconds per record

for e in entries['data']:
    print(e['entry_hash'])
    #TODO: This should be bulked to lower the amount of requests
    entry = factom.chain_get_entry(chainId,e['entry_hash'])
    entry = factom._decode(entry['data']['content'])
    print(entry)
    entry = json.loads(entry)
    recordType = entry['recordType']
    if(recordType != 'driveData'):
        continue
    roadType = entry['road_type']
    coordinates = entry['coordinates']
    speed = entry['speed']
    acceleration = entry['acceleration']
    timestamp = entry['timestamp']

    cost += insurance_costs._cost_per_mph(speed,interval)
    cost += insurance_costs._cost_per_road_type(roadType,speed,2)
    cost += insurance_costs._cost_per_mile(speed,interval)
print("Total Cost - $" + str(round(cost,2)))
