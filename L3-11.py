# delete the item ‘Indian’ created in the dictionary for L3_10


theDict = dict()

theDict['Indian'] = 'Charles Bronson'
theDict['1'] = 'Airplane'
theDict['2'] = 'Car'
theDict['3'] = 'Boat'

print('theDict before: ', theDict)

# now delete the item

del theDict['Indian']

print('theDict after: ', theDict)
