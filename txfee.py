import sys
from bitcoin.rpc import RawProxy

p = RawProxy()

transactionId = sys.argv[1]
transaction = p.getrawtransaction(transactionId, 1)

inputsTotal = 0
for output in transaction['vin']:
    itransaction = p.getrawtransaction(output['txid'], 1)
    voutIndex = output['vout']
    for index, ioutput in enumerate(itransaction['vout']):
        if (index == voutIndex):
            inputsTotal = inputsTotal + ioutput['value']
            break

outputsTotal = 0
for output in transaction['vout']:
    outputsTotal = outputsTotal + output['value']

print("Transaction: {0}", transactionId)
print("Transaction's fee: {0} BTC", inputsTotal - outputsTotal)