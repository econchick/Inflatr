# parses inflation data downloaded from bls.gov
# to upload into sqlite3 inflationdata table.
# at ftp://ftp.bls.gov/pub/time.series/cu/cu.data.0.Current

from items import items
from area_names import names
import fileinput

counter = 0
for line in fileinput.input('/Users/lynnroot/desktop/cs50/project/myinflation/inflationdata/data.txt'):
    if fileinput.isfirstline():
        continue

    splitline = line.rstrip().split('\t')
    
    # BLS series id
    series = splitline[0]
    
    # decode BLS series id
    cu, s, r, area, item = series[0:2],series[2],series[3],series[4:8],series[8:]
    
    # strip extra white space for items
    item = item.strip()
    
    # regions
    area = names[area]
    
    # items measured
    if (item not in items):
        continue
    item = items[item]

    # other columns
    year = splitline[1]
    year = year.lstrip().rstrip()
    
    # decode BLS period
    # frequency = S = semiannual, = M = monthly
    period = splitline[2]  
    frequency, pointinyear = period[0],period[1:]
    
    
    value = splitline[3]
    value = value.lstrip().rstrip()

    counter += 1

    print ",".join([str(counter), item, area, year, frequency, pointinyear, value])