from newsscrapper import en
import pandas as pd

cnn = en.CNNSC()
df = pd.DataFrame(cnn)
df.to_json("cnn.json", index=False)