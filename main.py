import bySector as bs
import setup_ipeds_datasets as sid

# x  = sid.SetupIPEDSData()
# df = x.get_data()

# target_var = "ftretention_rate"
# bs.bySector(df).summary(target_var)

# data = bs.bySector(df).plot(target_var)

# print(data.groups)

import bubbleMap.Map as bm

bm.Mapper().write()