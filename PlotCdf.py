"""PlotCdf.ipynb
Automatically generated by Colaboratory.
Original file is located at
    https://colab.research.google.com/drive/1wgSA_SLzS5mTMmh77bpmoxBiwaJwBFOo
"""

#stampa1 :Stampa Packet Size senza considerare la direzione dello stream
import pandas as pd
import  seaborn as sns
import matplotlib.pyplot as plt
f, ax = plt.subplots(figsize=(7, 5))
path="midterm.csv"
df = pd.read_csv(path, delimiter=';')
sns.ecdfplot(data=df , x="PACKET_SIZE",hue="Activity")
sns.ecdfplot(data=df, x="PACKET_SIZE",color='black')
plt.xlabel("PACKET_SIZE[byte]")
plt.legend(labels=["MESSAGE","VIDEOCONFERENCE","CALL","SKYPE"])

#stampa2 :Stampa SIZE_MESSAGE senza considerare la direzione dello stream
import pandas as pd
import  seaborn as sns
import matplotlib.pyplot as plt
f, ax = plt.subplots(figsize=(7, 5))
path="midterm.csv"
df = pd.read_csv(path, delimiter=';')
sns.ecdfplot(data=df, x="SIZE_MESSAGE",hue="Activity")
sns.ecdfplot(data=df, x="SIZE_MESSAGE",color='black')
plt.xlabel("SIZE_MESSAGE[byte]")
plt.legend(labels=["MESSAGE","VIDEOCONFERENCE","CALL","SKYPE"])

#stampa3 :Stampa iat packet senza considerare la direzione dello stream
import pandas as pd
import  seaborn as sns
import matplotlib.pyplot as plt
f, ax = plt.subplots(figsize=(7, 5))
ax.set(xscale="log")
path="midterm.csv"
df = pd.read_csv(path, delimiter=';')
df["ARRIVAL_TIME_MSG"]=df["ARRIVAL_TIME_MSG"]*1000
sns.ecdfplot(data=df, x="ARRIVAL_TIME_PACKET",hue="Activity",ax=ax)
sns.ecdfplot(data=df, x="ARRIVAL_TIME_PACKET",color='black',ax=ax)
plt.xlabel("ARRIVAL_TIME_PACKET[ms]")
plt.legend(labels=["MESSAGE","VIDEOCONFERENCE","CALL","SKYPE"])

#stampa4 :Stampa iat msg senza considerare la direzione dello stream
import pandas as pd
import  seaborn as sns
f, ax = plt.subplots(figsize=(7, 5))
ax.set(xscale="log")
path="midterm.csv"
df = pd.read_csv(path, delimiter=';')
df["ARRIVAL_TIME_MSG"]=df["ARRIVAL_TIME_MSG"]*1000
sns.ecdfplot(data=df, x="ARRIVAL_TIME_MSG",hue="Activity",ax=ax)
sns.ecdfplot(data=df, x="ARRIVAL_TIME_MSG",color='black',ax=ax)
plt.xlabel("ARRIVAL_TIME_MSG[ms]")
plt.legend(labels=["MESSAGE","VIDEOCONFERENCE","CALL","SKYPE"])

#stampa1UpStream :Stampa Packet Size  considerare la direzione dello stream in questo caso Upstream
import pandas as pd
import  seaborn as sns
import matplotlib.pyplot as plt
f, ax = plt.subplots(figsize=(7, 5))
path="midterm.csv"
df = pd.read_csv(path, delimiter=';')
df_mask=df['TYPE_STREAM']==1
filtered_df = df[df_mask]
sns.ecdfplot(data=filtered_df , x="PACKET_SIZE",hue="Activity")
sns.ecdfplot(data=filtered_df , x="PACKET_SIZE",color='black')
plt.xlabel("PACKET_SIZE[byte]")
plt.legend(labels=["MESSAGE","VIDEOCONFERENCE","CALL","SKYPE"])

#stampa2UpStream :Stampa msg Size  considerare la direzione dello stream in questo caso Upstream
import pandas as pd
import  seaborn as sns
import matplotlib.pyplot as plt
f, ax = plt.subplots(figsize=(7, 5))
path="midterm.csv"
df = pd.read_csv(path, delimiter=';')
df_mask=df['TYPE_STREAM']==1
filtered_df = df[df_mask]
sns.ecdfplot(data=filtered_df , x="SIZE_MESSAGE",hue="Activity")
sns.ecdfplot(data=filtered_df , x="SIZE_MESSAGE",color='black')
plt.xlabel("SIZE_MESSAGE[byte]")
plt.legend(labels=["MESSAGE","VIDEOCONFERENCE","CALL","SKYPE"])

#stampa3UpStream :Stampa iatpkt  considerare la direzione dello stream in questo caso Upstream
import pandas as pd
import  seaborn as sns
f, ax = plt.subplots(figsize=(7, 5))
ax.set(xscale="log")
path="midterm.csv"
df = pd.read_csv(path, delimiter=';')
df["ARRIVAL_TIME_PACKET"]=df["ARRIVAL_TIME_PACKET"]*1000
df_mask=df['TYPE_STREAM']==1
filtered_df = df[df_mask]
sns.ecdfplot(data=filtered_df , x="ARRIVAL_TIME_PACKET",hue="Activity",ax=ax)
sns.ecdfplot(data=filtered_df , x="ARRIVAL_TIME_PACKET",color='black',ax=ax)
plt.xlabel("ARRIVAL_TIME_PACKET[ms]")
plt.legend(labels=["MESSAGE","VIDEOCONFERENCE","CALL","SKYPE"])

#stampa4UpStream :Stampa iat msg  considerare la direzione dello stream in questo caso Upstream
import pandas as pd
import  seaborn as sns
f, ax = plt.subplots(figsize=(7, 5))
ax.set(xscale="log")
path="midterm.csv"
df = pd.read_csv(path, delimiter=';')
df["ARRIVAL_TIME_MSG"]=df["ARRIVAL_TIME_MSG"]*1000
df_mask=df['TYPE_STREAM']==1
filtered_df = df[df_mask]
sns.ecdfplot(data=filtered_df , x="ARRIVAL_TIME_MSG",hue="Activity",ax=ax)
sns.ecdfplot(data=filtered_df , x="ARRIVAL_TIME_MSG",color='black',ax=ax)
plt.legend(labels=["MESSAGE","VIDEOCONFERENCE","CALL","SKYPE"])
plt.xlabel("ARRIVAL_TIME_MSG[ms]")

#stampa1DwnStream :Stampa Packet Size  considerare la direzione dello stream in questo caso Downstream
import pandas as pd
import  seaborn as sns
import matplotlib.pyplot as plt
f, ax = plt.subplots(figsize=(7, 5))
path="midterm.csv"
df = pd.read_csv(path, delimiter=';')
df_mask=df['TYPE_STREAM']==0
filtered_df = df[df_mask]
sns.ecdfplot(data=filtered_df , x="PACKET_SIZE",hue="Activity")
sns.ecdfplot(data=filtered_df , x="PACKET_SIZE",color='black')
plt.legend(labels=["MESSAGE","VIDEOCONFERENCE","CALL","SKYPE"])
plt.xlabel("PACKET_SIZE[byte]")

#stampa2DownStream :Stampa msg Size  considerare la direzione dello stream in questo caso Downstream
import pandas as pd
import  seaborn as sns
import matplotlib.pyplot as plt
f, ax = plt.subplots(figsize=(7, 5))
path="midterm.csv"
df = pd.read_csv(path, delimiter=';')
df_mask=df['TYPE_STREAM']==0
filtered_df = df[df_mask]
sns.ecdfplot(data=filtered_df , x="SIZE_MESSAGE",hue="Activity")
sns.ecdfplot(data=filtered_df , x="SIZE_MESSAGE",color='black')
plt.legend(labels=["MESSAGE","VIDEOCONFERENCE","CALL","SKYPE"])
plt.xlabel("SIZE_MESSAGE[byte]")

#stampa3DownStream :Stampa iatpkt  considerare la direzione dello stream in questo caso Downstream
import pandas as pd
import  seaborn as sns
import matplotlib.pyplot as plt
f, ax = plt.subplots(figsize=(7, 5))
ax.set(xscale="log")
path="midterm.csv"
df = pd.read_csv(path, delimiter=';')
df["ARRIVAL_TIME_PACKET"]=df["ARRIVAL_TIME_PACKET"]*1000
df_mask=df['TYPE_STREAM']==0
filtered_df = df[df_mask]
sns.ecdfplot(data=filtered_df , x="ARRIVAL_TIME_PACKET",hue="Activity",ax=ax)
sns.ecdfplot(data=filtered_df , x="ARRIVAL_TIME_PACKET",color='black',ax=ax)
plt.legend(labels=["MESSAGE","VIDEOCONFERENCE","CALL","SKYPE"])
plt.xlabel("ARRIVAL_TIME_PACKET[ms]")

#stampa4DownStream :Stampa iat msg  considerare la direzione dello stream in questo caso Downstream
import pandas as pd
import  seaborn as sns
import  seaborn as sns
f, ax = plt.subplots(figsize=(7, 5))
ax.set(xscale="log")
path="midterm.csv"
df = pd.read_csv(path, delimiter=';')
df["ARRIVAL_TIME_MSG"]=df["ARRIVAL_TIME_MSG"]*1000
df_mask=df['TYPE_STREAM']==0
filtered_df = df[df_mask]
sns.ecdfplot(data=filtered_df , x="ARRIVAL_TIME_MSG",hue="Activity",ax=ax)
sns.ecdfplot(data=filtered_df , x="ARRIVAL_TIME_MSG",color='black',ax=ax)
plt.legend(labels=["MESSAGE","VIDEOCONFERENCE","CALL","SKYPE"])
plt.xlabel("ARRIVAL_TIME_MSG[ms]")