def returns(c_today,c_tomo):
  return (c_tomo-c_today)/c_today

def momentum(c1,c5):
  return (c5-c1)/c1

def rel_vol(vol20_arr,curr_vol):
  total = 0
  for val in vol20_arr:
    total = total + val
  return curr_vol/(total/20)

def volatility(vola):
  return np.std(vola)

feature_matrix = []
acc_returns = []

for i in range(20,len(df)-20):

  acc_returns.append(returns(df["Close"].iloc[i].item(),df["Close"].iloc[i+1].item()))

  row = []
  c1 = df["Close"].iloc[i].item()
  c5 = df["Close"].iloc[i+4].item()
  row.append(momentum(c1,c5))

  vola = []

  for j in range(i,i+4):
    vola.append(returns(df["Close"].iloc[j].item(),df["Close"].iloc[j+1].item()))
  row.append(volatility(vola))

  rel_volu = []

  for k in range(i,i+20):
    v1 = df["Volume"].iloc[k].item()
    rel_volu.append(v1)

  curr = df["Volume"].iloc[i+19].item()
  row.append(rel_vol(rel_volu,curr))

  feature_matrix.append(row)

