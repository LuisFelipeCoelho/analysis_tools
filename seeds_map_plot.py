import numpy as np
import ROOT

detector = 'pixel'
#detector = 'strip'

#ROOT.gROOT.SetStyle("ATLAS");

def setLegend(acts, athena, filter):
	legend = ROOT.TLegend(0.6,0.57,0.99,0.70)
	legend.AddEntry(acts ,"ACTS")
	legend.AddEntry(athena ,"Athena Master")
	legend.SetLineWidth(0)
	legend.SetFillStyle(0)
	legend.Draw("same")
	latex = ROOT.TLatex()
	latex.SetNDC()
	latex.SetTextSize(0.035)
	latex.DrawText(0.61, 0.78, "{} space points".format(detector))
	latex.DrawText(0.61, 0.83, "14 TeV ttbar")
	latex.DrawText(0.61, 0.73, filter)
	return legend
  
def setLegend2(h1, name):
  legend2.AddEntry(h1 , name)
  legend2.SetLineWidth(0)
  legend2.SetFillStyle(0)
  legend2.Draw("same")
  
def plotOptions(h1, h2, y_label):
	h1.GetYaxis().SetTitle(y_label)
	h1.GetYaxis().SetLabelSize(0.);
	h1.SetLineColor(95)
	h2.SetLineColor(60)
	h1.SetLineWidth(2)
	h1.GetYaxis().SetTitleSize(20)
	h1.GetYaxis().SetTitleFont(43)
	h1.GetYaxis().SetTitleOffset(3)
	h1.GetYaxis().SetLabelFont(43)
	h1.GetYaxis().SetLabelSize(15)
	h1.GetXaxis().SetLabelFont(43)
	h1.GetXaxis().SetLabelSize(15)
	h1.SetStats(0)
	h2.SetLineWidth(2)
	return h1, h2
  
def createPad1():
	pad1 = ROOT.TPad("pad1", "pad1", 0, 0.3, 1, 1.0);
	pad1.SetBottomMargin(0.05)
#	pad1.SetGridx()
	pad1.Draw()
	pad1.cd()
	return pad1
	
def createPad2():
	pad2 = ROOT.TPad("pad2", "pad2", 0, 0.08, 1, 0.3)
	pad2.SetTopMargin(0)
	pad2.SetBottomMargin(0.3)
#	pad2.SetGridx()
	pad2.Draw()
	pad2.cd()
	return pad2
	
def createCanvasPads():
	c = ROOT.TCanvas("c", "canvas", 800, 800)
	# Upper histogram plot is pad1
	pad1 = createPad1()
	# Lower ratio plot is pad2
	c.cd()
	pad2 = createPad2()
	return c, pad1, pad2

def plotRatio(h1, h2, x_label):

	# Define the ratio plot
	h3 = h1.Clone("h3")
	h3.SetTitle("")
	h3.SetLineColor(1)
	h3.SetMinimum(0.8)
	h3.SetMaximum(1.35)
	h3.SetMarkerStyle(21)
	h3.Sumw2()
	h3.SetStats(0)
	h3.Divide(h2)

	# Y axis h1 plot settings
	h1.GetYaxis().SetTitleSize(20)
	h1.GetYaxis().SetTitleFont(43)
	h1.GetYaxis().SetTitleOffset(1.6)
	
	# Y axis ratio plot settings
	h3.GetYaxis().SetTitle("")
	h3.GetYaxis().SetNdivisions(505)
	h3.GetYaxis().SetTitleSize(20)
	h3.GetYaxis().SetTitleFont(43)
	h3.GetYaxis().SetTitleOffset(1.6)
	h3.GetYaxis().SetLabelFont(43)
	h3.GetYaxis().SetLabelSize(15)
	
	# X axis ratio plot settings
	h3.GetXaxis().SetTitle(x_label)
	h3.GetXaxis().SetTitleSize(20)
	h3.GetXaxis().SetTitleFont(43)
	h3.GetXaxis().SetTitleOffset(4)
	h3.GetXaxis().SetLabelFont(43)
	h3.GetXaxis().SetLabelSize(15)
	
	return h3


acts_seeds_file = open("seedsMap_output_acts.txt", "r")
athena_seeds_file = open("seedsMap_output_athena.txt", "r")

h_acts_eta = ROOT.TH1F("acts_eta", "", 15, -0, 3)
h_athena_eta = ROOT.TH1F("athena_eta", "", 15, -0, 3)
h_acts_eta_filter1 = ROOT.TH1F("acts_eta", "", 15, -0, 3)
h_athena_eta_filter1 = ROOT.TH1F("athena_eta", "", 15, -0, 3)

h_acts_pt = ROOT.TH1F("acts_pt", "", 30, 0.8, 10)
h_athena_pt = ROOT.TH1F("athena_pt", "", 30, 0.8, 10)
h_acts_pt_filter1 = ROOT.TH1F("acts_pt", "", 30, 0.8, 2.7)
h_athena_pt_filter1 = ROOT.TH1F("athena_pt", "", 30, 0.8, 2.7)

h_acts_dscore = ROOT.TH1F("acts_dscore", "", 30, 0, 2)
h_athena_dscore = ROOT.TH1F("athena_dscore", "", 30, 0, 2)

h_acts_curvature = ROOT.TH1F("acts_curvature", "", 30, -0.0005/1.2, 0.0005/1.2)
h_athena_curvature = ROOT.TH1F("athena_curvature", "", 30, -0.0005/1.2, 0.0005/1.2)
h_acts_curvature_filter1 = ROOT.TH1F("acts_curvature", "", 30, -0.0005/1.2, 0.0005/1.2)
h_athena_curvature_filter1 = ROOT.TH1F("athena_curvature", "", 30, -0.0005/1.2, 0.0005/1.20)

h_acts_Im = ROOT.TH1F("acts_Im", "", 40, 0, 20)
h_athena_Im = ROOT.TH1F("athena_Im", "", 40, 0, 20)
h_acts_Im_filter1 = ROOT.TH1F("acts_Im", "", 35, 0, 20)
h_athena_Im_filter1 = ROOT.TH1F("athena_Im", "", 35, 0, 20)

h_acts_nSP = ROOT.TH1F("acts_nSP", "", 25, 0, 3010)
h_athena_nSP = ROOT.TH1F("athena_nSP", "", 25, 0, 3010)

h_acts_nSeeds = ROOT.TH1F("acts_nSeeds", "", 7, 1, 7)
h_athena_nSeeds = ROOT.TH1F("athena_nSeeds", "", 7, 1, 7)
h_acts_nSeeds_filter1 = ROOT.TH1F("acts_nSeeds", "", 7, 1, 7)
h_athena_nSeeds_filter1 = ROOT.TH1F("athena_nSeeds", "", 7, 1, 7)
h_acts_nSeeds_filter2 = ROOT.TH1F("acts_nSeeds", "", 10, 0, 10)
h_athena_nSeeds_filter2 = ROOT.TH1F("athena_nSeeds", "", 10, 0, 10)

h_acts_SPrVzMiddle = ROOT.TH2F("acts_SPrVz", "", 3000, -3000, 3000, 350, 0, 350)
h_athena_SPrVzMiddle = ROOT.TH2F("athena_SPrVz", "", 3000, -3000, 3000, 350, 0, 350)
h_acts_SPrVzBot = ROOT.TH2F("acts_SPrVz", "", 3000, -3000, 3000, 350, 0, 350)
h_athena_SPrVzBot = ROOT.TH2F("athena_SPrVz", "", 3000, -3000, 3000, 350, 0, 350)
h_acts_SPrVzTop = ROOT.TH2F("acts_SPrVz", "", 3000, -3000, 3000, 350, 0, 350)
h_athena_SPrVzTop = ROOT.TH2F("athena_SPrVz", "", 3000, -3000, 3000, 350, 0, 350)

h_athena_rminVz = ROOT.TH2F("athena_rminVz", "", 30, -3000, 3000, 30, -1, 350)
h_athena_rmaxVz = ROOT.TH2F("athena_rmaxVz", "", 30, -3000, 3000, 30, -1, 350)
h_athena_rminVeta = ROOT.TH2F("athena_rminVeta", "", 30, -10, 10, 30, -1, 350)
h_athena_rmaxVeta = ROOT.TH2F("athena_rmaxVeta", "", 30, -10, 10, 30, -1, 350)

string = "|Seeds Map {}| pT, eta, dScore, curvature, Im:".format(detector)
string2 = "|Seeds Map {}| m_RTmin, m_RTmax, eta, z:".format(detector)
string3 = "|Seeds Map {}| nSeeds, zBin, phiBin:".format(detector)
string4 = "|Seeds Map {}| nSeeds_test: ".format(detector)
string5 = "|Seeds Map {}| Seeds: rM, rB, rT, zM, zB, zT:".format(detector)
string6 = "|Seeds Map {}| nSeeds_filter, m_mapOneSeedsQ, m_mapOneSeeds: ".format(detector)
string6_2 = "|Seeds Map {}| nSeeds_filter: ".format(detector)
string7 = "|Seeds Map {}| pT_filter, eta_filter, dScore_filter, curvature_filter, Im_filter:".format(detector)

seedsDic = {"acts":[[],[]], "athena":[[],[]]}
filterSeed = {"acts":[[],[]], "athena":[[],[]]}
pt_val = [[],[]]
for file in [acts_seeds_file, athena_seeds_file]:
  evt = 0
  a = []
  b = []
  for line in file:
    if string in line:
      values = line[line.find(string):].replace(string,"").strip().split(" ")
#      print(values)
      pT = float(values[0])
#      eta = abs(float(values[1]))
#      print(eta)
      eta = float(values[1])
      dScore = float(values[2])
      curvature = float(values[3])
      Im = round(float(values[4]),6)
      if file==acts_seeds_file:
          h_acts_pt.Fill(pT)
          pt_val[0].append(pT)
          h_acts_eta.Fill(eta)
          h_acts_dscore.Fill(dScore)
          h_acts_curvature.Fill(curvature)
          h_acts_Im.Fill(Im)
          if h_acts_Im.GetXaxis().FindBin(Im) == 13:
             print("ACTS", h_acts_Im.GetXaxis().FindBin(Im), Im)
#          a.append("{}, {}, {}".format(round(Im,5), 0, 0))
      if file==athena_seeds_file:
          h_athena_pt.Fill(pT)
          pt_val[1].append(pT)
          h_athena_eta.Fill(eta)
          h_athena_dscore.Fill(dScore)
          h_athena_curvature.Fill(curvature)
          h_athena_Im.Fill(Im)
          if h_athena_Im.GetXaxis().FindBin(Im) == 13:
             print("ATHENA",  h_athena_Im.GetXaxis().FindBin(Im), Im)
#          a.append("{}, {}, {}".format(round(Im,5), 0, 0))
    if string7 in line:
      values = line[line.find(string7):].replace(string7,"").strip().split(" ")
      pT = float(values[0])
#      eta = abs(float(values[1]))
      eta = float(values[1])
      dScore = float(values[2])
      curvature = float(values[3])
      Im = float(values[4])
#      print(file, pT, Im)
      if file==acts_seeds_file:
          h_acts_pt_filter1.Fill(pT)
          h_acts_eta_filter1.Fill(abs(eta))
#          h_acts_dscore_filter1.Fill(dScore)
          h_acts_curvature_filter1.Fill(curvature)
          h_acts_Im_filter1.Fill(Im)
          if h_acts_Im_filter1.GetXaxis().FindBin(Im) == 13:
             print("ACTS", h_acts_Im_filter1.GetXaxis().FindBin(Im), Im)
#          if round(Im,3) != 0.824 or round(Im,3) != 5.515:
#          b.append(curvature)
      if file==athena_seeds_file:
          h_athena_pt_filter1.Fill(pT)
          h_athena_eta_filter1.Fill(abs(eta))
#          h_athena_dscore_filter1.Fill(dScore)
          h_athena_curvature_filter1.Fill(curvature)
          h_athena_Im_filter1.Fill(Im)
          if h_athena_Im_filter1.GetXaxis().FindBin(Im) == 13:
             print("ATHENA",  h_athena_Im_filter1.GetXaxis().FindBin(Im), Im)
#          if round(Im,3) != 0.824 or round(Im,3) != 5.515:
#          b.append(curvature)
    if string3 in line:
      values = line[line.find(string3):].replace(string3,"").strip().split(" ")
#      print(values)
      nSeeds = float(values[0])
      zBin = float(values[1])
      phiBin = float(values[2])
      if file==acts_seeds_file:
        h_acts_nSeeds.Fill(nSeeds)
        a.append("{}, {}, {}".format(nSeeds, zBin, phiBin))
      if file==athena_seeds_file:
        h_athena_nSeeds.Fill(nSeeds)
        a.append("{}, {}, {}".format(nSeeds, zBin, phiBin))
    if string6 in line or string6_2 in line:
      if file==acts_seeds_file:
      	values = line[line.find(string6_2):].replace(string6_2,"").strip().split(" ")
      if file==athena_seeds_file:
      	values = line[line.find(string6):].replace(string6,"").strip().split(" ")
      print(file, values)
      nSeeds_filter1 = float(values[0])
      nSeeds_filter2 = float(values[1])
#      print(file, nSeeds_filter1, nSeeds_filter2)
      if file==acts_seeds_file:
        h_acts_nSeeds_filter1.Fill(nSeeds_filter1)
        h_acts_nSeeds_filter2.Fill(nSeeds_filter2)
        b.append(nSeeds_filter1)
      if file==athena_seeds_file:
        h_athena_nSeeds_filter1.Fill(nSeeds_filter1)
        h_athena_nSeeds_filter2.Fill(nSeeds_filter2)
        b.append(nSeeds_filter1)
    if string5 in line:
      values = line[line.find(string5):].replace(string5,"").strip().split(" ")
      rM = float(values[0])
      rB = abs(float(values[1]))
      rT = float(values[2])
      zM = float(values[3])
      zB = float(values[4])
      zT = float(values[5])
      if file==acts_seeds_file:
        h_acts_SPrVzMiddle.Fill(zM, rM)
        h_acts_SPrVzTop.Fill(zT, rT)
        h_acts_SPrVzBot.Fill(zB, rB)
      if file==athena_seeds_file:
        h_athena_SPrVzMiddle.Fill(zM, rM)
        h_athena_SPrVzTop.Fill(zT, rT)
        h_athena_SPrVzBot.Fill(zB, rB)
    if '===========' in line and len(a) > 0:
      seedsDic["acts"][0].append(line)
      filterSeed["acts"][0].append(line)
      evt += 1
      seedsDic["acts"][1].append(a)
      filterSeed["acts"][1].append(b)
      a = []
      b = []
    if '===>>>  start processing event' in line and len(a) > 0:
      seedsDic["athena"][0].append(line)
      filterSeed["athena"][0].append(line)
      evt += 1
      seedsDic["athena"][1].append(a)
      filterSeed["athena"][1].append(b)
      a = []
      b = []
			

#for i in range(10):
#	print(pt_val[0][i],pt_val[1][i])

acts_seeds_file = open("seedsMap_output_acts.txt", "r")
athena_seeds_file = open("seedsMap_output_athena.txt", "r")
  
SP_list = {"acts":[], "athena":[], "lines1":[], "lines2":[], "SPtest_acts":[], "SPtest_athena":[]}
for file in [acts_seeds_file, athena_seeds_file]:
	SP = 0
	SP_test1 = 0
	SP_test2 = 0
	SP_test3 = 0
	for line in file:
		if 'Fill SP' in line or 'Fill bottom {} SP'.format(detector) in line or 'Fill top {} SP'.format(detector) in line:
			SP += 1
		if '================ E' in line or '===>>>  start processing event' in line:
			if file==acts_seeds_file and SP != 0:
				h_acts_nSP.Fill(SP)
				SP_list["acts"].append(SP)
				SP_list["lines1"].append(line)
#				print(line, SP)
			if file==athena_seeds_file and SP != 0:
				h_athena_nSP.Fill(SP)
				SP_list["athena"].append(SP)
				SP_list["lines2"].append(line)
#				print(line, SP)
			SP = 0
		if string4 in line:
			values = line[line.find(string4):].replace(string4,"").strip().split(" ")
#			print(line)
			SP_test1 += int(values[0])
			SP_test2 += int(values[1])
			SP_test3 += int(values[2])
			test_list = [SP_test1, SP_test2, SP_test3]
			if file==acts_seeds_file:
				SP_list["SPtest_acts"].append(test_list)
			if file==athena_seeds_file:
				SP_list["SPtest_athena"].append(test_list)
#	print(SP_test1,SP_test2,SP_test3)

# SP
#error = 0
#for i in range(0, len(SP_list["acts"])-3):
#	a = SP_list["acts"][i]
#	b = SP_list["athena"][i]
#	if a - b != 0:
#		print(SP_list["lines1"][i])
#		print(SP_list["lines2"][i])
#		print(i, a, b)
#		error += 1
#print(error)

# seedfinder errors
#error = 0
#for i in range(0, len(seedsDic["acts"][0])-2):
#	a = seedsDic["acts"][1][i]
#	b = seedsDic["athena"][1][i]
#	if len(list(set(a)-set(b))) != 0:
#		print(seedsDic["acts"][0][i])
#		print(seedsDic["athena"][0][i].replace("AthenaEventLoopMgr                                   INFO   ===>>>", ""))
#		print(list(set(a)-set(b)))
#		print(list(set(b)-set(a)))
#		print(a)
#		print(b)
#		error += 1
#print(error)

# seedfilter errors
h_acts_errors = ROOT.TH1F("mean errors strips ttbar", "", 40, 1, -1)
error = 0
print(len(filterSeed["acts"][0]), len(filterSeed["athena"][0]))
for i in range(0, len(filterSeed["acts"][0])):
	a = filterSeed["acts"][1][i]
	b = filterSeed["athena"][1][i]
	if len(list(set(a)-set(b))) != 0:
		print(filterSeed["acts"][0][i])
		print(filterSeed["athena"][0][i].replace("AthenaEventLoopMgr                                   INFO   ===>>>", ""))
		print(list(set(a)-set(b)))
		print(list(set(b)-set(a)))
#		a.sort()
#		b.sort()
		print(a)
		print(b)
		error += 1
	meanError = 0
	print(filterSeed["acts"][0][i])
	print(a)
	print(b)
	for j in range(len(a)):
		meanError += abs(a[j]-b[j])
	meanError /= len(a)
	h_acts_errors.Fill(meanError)
#	print(meanError)
print(error)
canvas = ROOT.TCanvas("c", "canvas", 500, 500)
pad1 = ROOT.TPad("pad1", "pad1", 0, 0, 1, 1);
pad1.SetBottomMargin(2)
pad1.Draw()
pad1.cd()
h_acts_errors.GetXaxis().SetTitle("|curvature[ACTS] - curvature[Athena]|")
h_acts_errors.Draw("h")
#pad1.SetLogx(1)
canvas.Print("seeds_plots_errors.png")
canvas.Clear()
	

#for i in range(len(filterSeed["acts"])):
#	if filterSeed["acts"][i] - filterSeed["athena"][i] != 0:
#		print(filterSeed["acts"][i], filterSeed["athena"][i])

athena_seeds_file = open("seedsMap_output_athena.txt", "r")

for line in athena_seeds_file:
		if string2 in line:
#			print(line)
			values = line[line.find(string2):].replace(string2,"").strip().split(" ")
#			print(values)
			RTmin = float(values[0])
			RTmax = float(values[1])
			eta = float(values[2])
			z = float(values[3])
#			print(z, eta)
			h_athena_rminVz.Fill(z, RTmin)
			h_athena_rmaxVz.Fill(z, RTmax)
			h_athena_rminVeta.Fill(eta, RTmin)
			h_athena_rmaxVeta.Fill(eta, RTmax)
			

histos = [h_acts_pt, h_acts_eta, h_athena_pt, h_athena_eta, h_acts_dscore, h_athena_dscore, h_acts_curvature, h_athena_curvature, h_acts_Im, h_athena_Im, h_athena_rminVz, h_athena_rmaxVz, h_athena_rminVeta, h_athena_rmaxVeta, h_acts_nSeeds, h_athena_nSeeds, h_acts_nSP, h_athena_nSP, h_acts_SPrVzMiddle, h_acts_SPrVzTop, h_acts_SPrVzBot, h_athena_SPrVzMiddle, h_athena_SPrVzTop, h_athena_SPrVzBot]
for h in histos:
  h.SetStats(0)

canvas = ROOT.TCanvas()
canvas.Print("seeds_plots.pdf[")
canvas.Clear()
# PT
h1, h2 = plotOptions(h_acts_pt, h_athena_pt, "Number of Seeds")
h3 = plotRatio(h1, h2, "p_{T} (GeV)")
canvas, pad1, pad2 = createCanvasPads()
pad1.cd()
h1.Draw("he")
h2.Draw("he same")
legend = setLegend(h1, h2, "before filter")
pad2.cd()
h3.Draw("he")
canvas.Print("seeds_plots.pdf")
canvas.Print("seeds_plots_pt.png")
canvas.Clear()

# PT
h1, h2 = plotOptions(h_acts_pt_filter1, h_athena_pt_filter1, "Number of Seeds")
h3 = plotRatio(h1, h2, "p_{T} (GeV)")
canvas, pad1, pad2 = createCanvasPads()
pad1.cd()
h1.Draw("he")
h2.Draw("he same")
legend = setLegend(h1, h2, "after filter")
pad2.cd()
h3.Draw("he")
canvas.Print("seeds_plots.pdf")
canvas.Print("seeds_plots_pt_filter1.png")
canvas.Clear()

# ETA
h1, h2 = plotOptions(h_acts_eta, h_athena_eta, "Number of Seeds")
h3 = plotRatio(h1, h2, "|#eta|")
canvas, pad1, pad2 = createCanvasPads()
pad1.cd()
h1.Draw("he")
h2.Draw("he same")
legend = setLegend(h1, h2, "before filter")
pad2.cd()
h3.Draw("he")
canvas.Print("seeds_plots.pdf")
canvas.Print("seeds_plots_eta.png")
canvas.Clear()

# ETA
h1, h2 = plotOptions(h_acts_eta_filter1, h_athena_eta_filter1, "Number of Seeds")
h3 = plotRatio(h1, h2, "|#eta|")
canvas, pad1, pad2 = createCanvasPads()
pad1.cd()
h1.Draw("he")
h2.Draw("he same")
legend = setLegend(h1, h2, "after filter")
pad2.cd()
h3.Draw("he")
canvas.Print("seeds_plots.pdf")
canvas.Print("seeds_plots_eta_filter1.png")
canvas.Clear()

# dScore
#h1, h2 = plotOptions(h_acts_dscore, h_athena_dscore, "Number of Seeds")
#h3 = plotRatio(h1, h2, "dScore")
#canvas, pad1, pad2 = createCanvasPads()
#pad1.cd()
#h1.Draw("he")
#h2.Draw("he same")
#legend = setLegend(h1, h2)
#pad2.cd()
#h3.Draw("he")
#canvas.Print("seeds_plots.pdf")
#canvas.Clear()

# Curvature
h1, h2 = plotOptions(h_acts_curvature, h_athena_curvature, "Number of Seeds")
h3 = plotRatio(h1, h2, "Curvature")
canvas, pad1, pad2 = createCanvasPads()
pad1.cd()
h1.Draw("he")
h2.Draw("he same")
legend = setLegend(h1, h2, "before filter")
pad2.cd()
h3.Draw("he")
canvas.Print("seeds_plots.pdf")
canvas.Print("seeds_plots_cruvature.png")
canvas.Clear()

# Curvature
h1, h2 = plotOptions(h_acts_curvature_filter1, h_athena_curvature_filter1, "Number of Seeds")
h3 = plotRatio(h1, h2, "Curvature")
canvas, pad1, pad2 = createCanvasPads()
pad1.cd()
h1.Draw("he")
h2.Draw("he same")
legend = setLegend(h1, h2, "after filter")
pad2.cd()
h3.Draw("he")
canvas.Print("seeds_plots.pdf")
canvas.Print("seeds_plots_cruvature_filter1.png")
canvas.Clear()

# Im
h1, h2 = plotOptions(h_acts_Im, h_athena_Im, "Number of Seeds")
h3 = plotRatio(h1, h2, "I_{m}")
canvas, pad1, pad2 = createCanvasPads()
pad1.cd()
h1.Draw("he")
h2.Draw("he same")
legend = setLegend(h1, h2, "before filter")
pad2.cd()
h3.Draw("he")
canvas.Print("seeds_plots.pdf")
canvas.Print("seeds_plots_Im.png")
canvas.Clear()

# Im
h1, h2 = plotOptions(h_acts_Im_filter1, h_athena_Im_filter1, "Number of Seeds")
h3 = plotRatio(h1, h2, "I_{m}")
canvas, pad1, pad2 = createCanvasPads()
pad1.cd()
h1.Draw("he")
h2.Draw("he same")
legend = setLegend(h1, h2, "after filter")
pad2.cd()
h3.Draw("he")
canvas.Print("seeds_plots.pdf")
canvas.Print("seeds_plots_Im_filter1.png")
canvas.Clear()

# nSP
h1, h2 = plotOptions(h_acts_nSP, h_athena_nSP, "")
h3 = plotRatio(h1, h2, "Number of SP")
canvas, pad1, pad2 = createCanvasPads()
pad1.cd()
h1.Draw("he")
h2.Draw("he same")
legend = setLegend(h1, h2, "")
pad2.cd()
h3.Draw("he")
canvas.Print("seeds_plots.pdf")
canvas.Print("seeds_plots_nSP.png")
canvas.Clear()

# nSeeds
h1, h2 = plotOptions(h_acts_nSeeds, h_athena_nSeeds, "")
h3 = plotRatio(h1, h2, "Number of seeds")
canvas, pad1, pad2 = createCanvasPads()
pad1.cd()
h1.Draw("he")
h2.Draw("he same")
legend = setLegend(h1, h2, "before filter")
pad2.cd()
h3.Draw("he")
canvas.Print("seeds_plots.pdf")
canvas.Print("seeds_plots_nSeeds.png")
canvas.Clear()

# nSeeds filter1
h1, h2 = plotOptions(h_acts_nSeeds_filter1, h_athena_nSeeds_filter1, "")
h3 = plotRatio(h1, h2, "Number of seeds")
canvas, pad1, pad2 = createCanvasPads()
pad1.cd()
h1.Draw("he")
h2.Draw("he same")
legend = setLegend(h1, h2, "after filter")
pad2.cd()
h3.Draw("he")
canvas.Print("seeds_plots.pdf")
canvas.Print("seeds_plots_nSeeds_filter1.png")
canvas.Clear()

# nSeeds filter2
#h1, h2 = plotOptions(h_athena_nSeeds_filter2, h_acts_nSeeds_filter2, "Number of Events")
#h3 = plotRatio(h1, h2, "Number of seeds after comparison")
#canvas, pad1, pad2 = createCanvasPads()
#pad1.cd()
#h1.Draw("he")
#h2.Draw("he same")
#legend = setLegend(h1, h2)
#pad2.cd()
#h3.Draw("he")
#canvas.Print("seeds_plots.pdf")
#canvas.Print("seeds_plots_nSeeds_filter2.png")
#canvas.Clear()

# ====================
# SPrVzMiddle
h_acts_SPrVzMiddle.GetYaxis().SetTitle("R Middle SP")
h_acts_SPrVzMiddle.GetXaxis().SetTitle("z (mm)")
h_acts_SPrVzMiddle.Draw("colz")
legend2 = ROOT.TLegend(0.7,0.8,0.9,0.9)
setLegend2(h_acts_SPrVzMiddle, "ACTS")
canvas.Print("seeds_plots.pdf")
canvas.Clear()

# SPrVzMiddle
h_athena_SPrVzMiddle.GetYaxis().SetTitle("R Middle SP")
h_athena_SPrVzMiddle.GetXaxis().SetTitle("z (mm)")
h_athena_SPrVzMiddle.Draw("colz")
legend2 = ROOT.TLegend(0.7,0.8,0.9,0.9)
setLegend2(h_athena_SPrVzMiddle, "Athena")
canvas.Print("seeds_plots.pdf")
canvas.Clear()

# SPrVzMiddle
h_acts_SPrVzBot.GetYaxis().SetTitle("R Bot SP")
h_acts_SPrVzBot.GetXaxis().SetTitle("z (mm)")
h_acts_SPrVzBot.Draw("colz")
legend2 = ROOT.TLegend(0.7,0.8,0.9,0.9)
setLegend2(h_acts_SPrVzBot, "ACTS")
canvas.Print("seeds_plots.pdf")
canvas.Clear()

# SPrVzMiddle
h_athena_SPrVzBot.GetYaxis().SetTitle("R Bot SP")
h_athena_SPrVzBot.GetXaxis().SetTitle("z (mm)")
h_athena_SPrVzBot.Draw("colz")
legend2 = ROOT.TLegend(0.7,0.8,0.9,0.9)
setLegend2(h_athena_SPrVzBot, "Athena")
canvas.Print("seeds_plots.pdf")
canvas.Clear()

# SPrVzMiddle
h_acts_SPrVzTop.GetYaxis().SetTitle("R Top SP")
h_acts_SPrVzTop.GetXaxis().SetTitle("z (mm)")
h_acts_SPrVzTop.Draw("colz")
legend2 = ROOT.TLegend(0.7,0.8,0.9,0.9)
setLegend2(h_acts_SPrVzTop, "ACTS")
canvas.Print("seeds_plots.pdf")
canvas.Clear()

# SPrVzMiddle
h_athena_SPrVzTop.GetYaxis().SetTitle("R Top SP")
h_athena_SPrVzTop.GetXaxis().SetTitle("z (mm)")
h_athena_SPrVzTop.Draw("colz")
legend2 = ROOT.TLegend(0.7,0.8,0.9,0.9)
setLegend2(h_athena_SPrVzTop, "Athena")
canvas.Print("seeds_plots.pdf")
canvas.Clear()
# ====================

h_acts_SPrVzMiddle.Add(h_acts_SPrVzBot)
h_acts_SPrVzMiddle.Add(h_acts_SPrVzTop)
h_acts_SPrVzMiddle.GetYaxis().SetTitle("R All SP")
h_acts_SPrVzMiddle.GetXaxis().SetTitle("z (mm)")
h_acts_SPrVzMiddle.Draw("colz")
canvas.Print("seeds_plots.pdf")
canvas.Clear()

h_athena_SPrVzMiddle.Add(h_athena_SPrVzBot)
h_athena_SPrVzMiddle.Add(h_athena_SPrVzTop)
h_athena_SPrVzMiddle.Divide(h_acts_SPrVzMiddle)
h_athena_SPrVzMiddle.GetYaxis().SetTitle("R Ratio SP")
h_athena_SPrVzMiddle.GetXaxis().SetTitle("z (mm)")
ROOT.gStyle.SetPalette(61)
h_athena_SPrVzMiddle.Draw("colz")
canvas.Print("seeds_plots.pdf")
canvas.Clear()

# ====================
# RTmin vs Z
h_athena_rminVz.GetYaxis().SetTitle("RT min")
h_athena_rminVz.GetXaxis().SetTitle("z (mm)")
h_athena_rminVz.Draw("colz")
canvas.Print("seeds_plots.pdf")
canvas.Clear()

# RTmax vs Z
h_athena_rmaxVz.GetYaxis().SetTitle("RT max")
h_athena_rmaxVz.GetXaxis().SetTitle("z (mm)")
h_athena_rmaxVz.Draw("colz")
canvas.Print("seeds_plots.pdf")
canvas.Clear()

# RT vs eta
h_athena_rminVeta.GetYaxis().SetTitle("RT min")
h_athena_rminVeta.GetXaxis().SetTitle("eta")
h_athena_rminVeta.Draw("colz")
canvas.Print("seeds_plots.pdf")
canvas.Clear()

# RT vs eta
h_athena_rmaxVeta.GetYaxis().SetTitle("RT max")
h_athena_rmaxVeta.GetXaxis().SetTitle("eta")
h_athena_rmaxVeta.Draw("colz")
canvas.Print("seeds_plots.pdf")
canvas.Clear()
#
canvas.Print("seeds_plots.pdf]")
