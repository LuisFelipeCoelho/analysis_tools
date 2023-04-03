import numpy as np
import ROOT

acts_grid_file = open("acts_grid.txt", "r")
athena_grid_file = open("athena_grid.txt", "r")

pi2 = 2*3.14159265
zBins = 11
phiBins = 138

zBinEdges = np.array([-3000,-2500.,-1400.,-925.,-450.,-250.,250., 450,925.,1400.,2500,3000])
h_acts = ROOT.TH2F("acts_grid", "ACTS Grid", zBins, zBinEdges, phiBins, 0, pi2)
h_athena = ROOT.TH2F("athena_grid", "Athena Grid", zBins, zBinEdges, phiBins, 0, pi2)

for line in acts_grid_file:
    if "=======" not in line:
        phiBin = int(line.strip().split('|')[0].replace(") ==> ","").replace("(",""))
        zBin = 1
        for binValue in line.strip().split('|')[1:-1]:
            h_acts.SetBinContent(zBin, phiBin, float(binValue))
            #print(zBin, phiBin, binValue)
            zBin += 1

c = ROOT.TCanvas()
c.Draw()
h_acts.SetStats(0)
h_acts.Draw("colz")
c.SaveAs("h_acts.png")

for line in athena_grid_file:
    if "=======" not in line:
        phiBin = int(line.strip().split('|')[0].replace(") ===> ","").replace("(",""))
        zBin = 1
        for binValue in line.strip().split('|')[1:-1]:
            h_athena.SetBinContent(zBin, phiBin, float(binValue))
            #print(zBin, phiBin, binValue)
            zBin += 1

c.Draw()
h_athena.SetStats(0)
h_athena.Draw("colz")
c.SaveAs("h_athena.png")


h_Ratio = ROOT.TH2F("ratio", "Ratio Grid", zBins, zBinEdges, phiBins, 0, pi2)
for binx in range(h_athena.GetNbinsX()):
  for biny in range(h_athena.GetNbinsY()):
     if h_athena.GetBinContent(binx+1, biny+1) != 0:
         value = h_athena.GetBinContent(binx+1, biny+1)/h_acts.GetBinContent(binx+1, biny+1)
         if value != 1:
             print(h_athena.GetBinContent(binx+1, biny+1), h_acts.GetBinContent(binx+1, biny+1), binx+1, biny+1)
         h_Ratio.SetBinContent(binx+1, biny+1, value)

h_Ratio.SetMaximum(2)
h_Ratio.SetMinimum(0)
h_Ratio.SetStats(0)
h_Ratio.Draw("colz")
c.SaveAs("ratio.png")
