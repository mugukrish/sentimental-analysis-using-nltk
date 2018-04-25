
from PIL import Image
import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt
plt.switch_backend('agg')
import MySQLdb
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


db = MySQLdb.connect("127.0.0.1","root","spiderman","feedback" )
cursor = db.cursor()
#cursor.execute("insert into nlpt_feedback values(user_input_feedback,(1 if ans="pos" else -1))")
cursor.execute("select feedback from nlpt_feedback where lab=1")
pos = cursor.fetchall()
pos = [x[0] for x in pos]

cursor.execute("select feedback from nlpt_feedback where lab=-1")
neg = cursor.fetchall()
neg = [x[0] for x in neg]
db.close()

postext = " ".join(pos)
negtext = " ".join(neg)
stopwords = set(STOPWORDS)

wc = WordCloud(background_color="white", random_state=42)
wc.generate(postext)
plt.figure()
plt.axis('off')
plt.imshow(wc, interpolation="bilinear")
plt.savefig('images/pos.png', bbox_inches='tight')

wc.generate(negtext)
plt.imshow(wc, interpolation="bilinear")
plt.savefig('images/neg.png', bbox_inches='tight')

db = MySQLdb.connect("127.0.0.1","root","spiderman","feedback" )
cursor = db.cursor()
cursor.execute("select feedback from nlpt_feedback where lab=1")
posdata = cursor.fetchall()
cursor.execute("select feedback from nlpt_feedback where lab=-1")
negdata = cursor.fetchall()

db.close()
explode = (0.02, 0.02)
plt.pie([len(posdata),len(negdata)],explode=explode,labels=["positive","negative"],autopct='%1.1f%%')
plt.savefig('images/pie.png', bbox_inches='tight')
with open("data/posdata.txt","w") as f:
    [f.write(x[0]+"\n") for x in posdata]

with open("data/negdata.txt","w") as f:
    [f.write(x[0]+"\n") for x in negdata]
