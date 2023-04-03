import csv
import numpy as np
import matplotlib.pyplot as plt

binning_type = [
#"equidistant",
#"variable"
"tfirst",
"bfirst",
]

file_name = 'output_seeding_'
#file_name = 'output_atlas_ttbar_'

time_values = {"tfirst":[], "bfirst":[]}

for binning in binning_type:
  print(binning)
  for files in range(15):
    print('run'+str(files))
    tsv_file = open(file_name+binning+'/run'+str(files)+'/timing.tsv')
    read_tsv = csv.reader(tsv_file, delimiter="\t")
    for row in read_tsv:
      if row[0]=="Algorithm:SeedingAlgorithm":
        print("seeding time per event: "+str(row[2])+"s")
        time_values[binning].append(row[2])
    tsv_file.close()

print(time_values)

bins=np.histogram(np.hstack((np.array(time_values["tfirst"]).astype(np.float),np.array(time_values["bfirst"]).astype(np.float))), bins=40)[1]
n, bins, patches = plt.hist(x=np.array(time_values["tfirst"]).astype(np.float), bins=bins, alpha=0.5, rwidth=0.85)
n, bins, patches = plt.hist(x=np.array(time_values["bfirst"]).astype(np.float), bins=bins, alpha=0.5, rwidth=0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Time per event (s)')
plt.title('SeedingAlgorithm')
plt.text(0.00082, 19, r'50 runs of 1k singleMu events')
plt.text(0.00082, 18, r'Loop over top SP first: average time per event = '+str(np.average(np.array(time_values["tfirst"]).astype(np.float)))+' s', color='blue')
plt.text(0.00082, 17, r'Loop over bottom SP first: average time per event = '+str(np.average(np.array(time_values["bfirst"]).astype(np.float)))+' s', color='green')
maxfreq = n.max()
plt.ylim(ymax=np.ceil(maxfreq / 20) * 20 if maxfreq % 20 else maxfreq + 20)
plt.show()
