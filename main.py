import bySector as bs
import setup_ipeds_datasets as sid

x  = sid.SetupIPEDSData()
df = x.get_data()

a_obj = bs.bySector(df)

target_var = "ftretention_rate"

print(a_obj.summary(target_var))

a_obj.plot(target_var)
