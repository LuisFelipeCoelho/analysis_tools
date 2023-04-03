import sys
import numpy as np
import ROOT
import os

ROOT.gROOT.SetStyle("ATLAS");

# --> inputs: [orthogonal_file] [acts_file] [sample_type] [energy] [detector] [peliUp] [eventsNTotal] [pT]
#
#     [sample_type] can be 'singleMu' or 'ttbar' or '100Mu'
#     [energy] can be '{value}GeV' or '{value}TeV' or 'None'
#     [detector] can be 'PPP' or 'SSS'
#     [pileUp] can be '{value}' or 'None'
#		  [eventsNTotal] can be '{value}'
#     [pT] in GeV can be '{value}' or '{value}:{value}' or 'None'
#

if len(sys.argv) != 9:
	raise Exception('ERROR len input != 5')

path = ''

file_acts = path + sys.argv[1]
file_orthogonal = path + sys.argv[2]
sample_type = sys.argv[3]
energy = sys.argv[4]
detector = sys.argv[5]
pileUp = sys.argv[6]
eventsNTotal = sys.argv[7]
pT = sys.argv[8]


time_orthogonal = ""
time_default = ""

sample_type_plot = sample_type
if sample_type == "ttbar": sample_type_plot = rf"\text{{ }}" + r"t\bar{t}"
if sample_type == "100Mu": sample_type_plot = rf"\text{{100-}} \mu"
if sample_type == "200Mu": sample_type_plot = rf"\text{{200-}} \mu"
if sample_type == "singleMu": sample_type_plot = rf"single- \mu"
nEventTotal = str(eventsNTotal) + " events"
if detector == "PPP": seedType = 1
if detector == "SSS": seedType = 0

outPath = "ITkSeeding_"+sample_type
text_plot = " "

if energy != "None":
	text_plot += energy.replace('GeV', ' GeV ').replace('TeV', ' \\text{TeV} ')
	outPath += "_"+energy
	
text_plot += sample_type_plot

if pT != "None" and ':'not in pT: text_plot += ' p_{T}=' + pT + ' GeV'
if pT != "None" and ':'in pT: text_plot += rf'\text{{ (}}' + pT.split(':')[0] + '<p_{T}<' + pT.split(':')[1] + rf'\text{{) GeV}}'

if pileUp != "None":
	text_plot += ' < \mu>=' + pileUp
	outPath += "_mu"+pileUp

outPath +="_"+detector+"/"
outName = outPath[:-1]

def createDir(dirName):
	try: 
		os.mkdir(dirName) 
	except OSError as error: 
        	print(error)

def setLegend(acts, orthogonal, right="rightTop"):
	if right=="rightTop":	legend = ROOT.TLegend(0.6,0.65,0.95,0.72)
	elif right=="leftTop":  legend = ROOT.TLegend(0.2,0.65,0.55,0.72)
	elif right=="leftBot":  legend = ROOT.TLegend(0.2,0.15,0.55,0.22)
	elif right=="rightBot": legend = ROOT.TLegend(0.6,0.15,0.95,0.22)
	legend.AddEntry(acts ,"ACTS reference"+time_default)
	legend.AddEntry(orthogonal ,"ACTS monitored"+time_orthogonal)
	legend.SetTextSize(0.035)
	legend.SetLineWidth(0)
	legend.SetFillStyle(0)
	legend.Draw("same")
	latex = ROOT.TLatex()
	latex.SetNDC()
	latex.SetTextSize(0.035)
	if right=="rightTop":
		latex.DrawText(0.61, 0.80, " ITk {} configuration".format(detector))
		latex.DrawLatex(0.61, 0.85, text_plot)
		latex.DrawText(0.61, 0.75, nEventTotal)
	elif right=="leftTop":
		latex.DrawText(0.21, 0.80, " ITk {} configuration".format(detector))
		latex.DrawLatex(0.21, 0.85, text_plot)
		latex.DrawText(0.21, 0.75, nEventTotal)	
	elif right=="leftBot":
		latex.DrawText(0.21, 0.30, " ITk {} configuration".format(detector))
		latex.DrawLatex(0.21, 0.35, text_plot)
		latex.DrawText(0.21, 0.25, nEventTotal)	
	elif right=="rightBot":
		latex.DrawText(0.61, 0.30, " ITk {} configuration".format(detector))
		latex.DrawLatex(0.61, 0.35, text_plot)
		latex.DrawText(0.61, 0.25, nEventTotal)	
	return legend

def setLegend2(h1, name):
	legend2.AddEntry(h1 , name)
	legend2.SetLineWidth(0)
	legend2.SetFillStyle(0)
	legend2.Draw("same")
        
def plotOptions(h1, h2, y_label, yMin=-1, yMax=-1):
	h1.GetYaxis().SetTitle(y_label)
	h1.GetYaxis().SetLabelSize(0.);
	h1.SetLineColor(206)
	h2.SetLineColor(62)
	h1.SetLineWidth(2)
	h1.SetMarkerStyle(0);
	h2.SetMarkerStyle(0);
	h1.GetYaxis().SetTitleSize(20)
	h1.GetYaxis().SetTitleFont(43)
	h1.GetYaxis().SetTitleOffset(3)
	h1.GetYaxis().SetLabelFont(43)
	h1.GetYaxis().SetLabelSize(15)
	h1.GetXaxis().SetLabelFont(43)
	h1.GetXaxis().SetLabelSize(15)
	h2.GetXaxis().SetRange(1,40)
	h1.GetXaxis().SetRange(1,40)
	if yMin != -1:
		h1.GetYaxis().SetRangeUser(yMin,yMax)
		h2.GetYaxis().SetRangeUser(yMin,yMax)
	h1.SetStats(0)
	h2.SetLineWidth(2)
	return h1, h2

def createPad1():
	pad1 = ROOT.TPad("pad1", "pad1", 0, 0.3, 1, 1.0);
	pad1.SetBottomMargin(0.05)
	#pad1.SetGridx()
#	pad1.SetLogy()
	pad1.Draw()
	pad1.cd()
	return pad1

def createPad2():
	pad2 = ROOT.TPad("pad2", "pad2", 0, 0.08, 1, 0.3)
	pad2.SetTopMargin(0)
	pad2.SetBottomMargin(0.3)
	#pad2.SetGridx()
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
	h3.GetXaxis().SetTitleOffset(1)
	h3.GetXaxis().SetLabelFont(43)
	h3.GetXaxis().SetLabelSize(15)

	return h3

createDir(outPath)

pixel_param = {
# variable_name:[bins, xMin, xMax, label, yMin]
'trackeff_vs_eta':[40, -4, 4, "#eta", 0.75, 1.01],
#'trackeff_vs_pT':[40, 0, 100, "p_{T} (GeV)", 0.96, 1.01],
'nDuplicated_vs_eta':[40, -4, 4, "#eta", 0, 24.1],
#'nDuplicated_vs_pT':[40, 0, 100, "p_{T} (GeV)", 6, 13.5],
}

strip_param = {
# variable_name:[bins, xMin, xMax]
'trackeff_vs_eta':[40, -4, 4],
#'trackeff_vs_pT':[40, 0, 100],
'duplicationRate_vs_eta':[40, -4, 4],
#'duplicationRate_vs_pT':[40, 0, 100],
}

if detector == 'PPP':
	p = pixel_param 
elif detector == 'SSS':
	p = strip_param 

hist_list_default = []
hist_list_orthogonal = []
for key in pixel_param:
	hist_list_default.append(ROOT.TH1F(key, "", p[key][0], p[key][1], p[key][2]))
	hist_list_orthogonal.append(ROOT.TH1F(key, "", p[key][0], p[key][1], p[key][2]))

# canvas
canvas = ROOT.TCanvas()

for i_key, key in enumerate(pixel_param):
	TTree_name = {
	file_orthogonal:key,
	file_acts:key,
	}

	n_i = 0
	for file in [file_orthogonal, file_acts]:
		print("read TFile " + file)
		read_file = ROOT.TFile.Open(file, "READ")
		print("read TEff " + TTree_name[file])
		eff = read_file.Get(TTree_name[file])
		for bin in range(1, p[key][0]+1):
			# print(eff.GetEfficiency(bin))
			if "trackeff" in key:
				title = "Efficiency"
				eff_per_bin = float(eff.GetEfficiency(bin))
			else:
				title = "N duplicates"
				eff_per_bin = float(eff.GetBinContent(bin))
			if file == file_orthogonal:
				hist_list_orthogonal[i_key].SetBinContent(bin, eff_per_bin)
			if file == file_acts:
				hist_list_default[i_key].SetBinContent(bin, eff_per_bin)

	# plot
	canvas.Clear()
	h1, h2 = plotOptions(hist_list_default[i_key], hist_list_orthogonal[i_key], title, yMin=p[key][4], yMax=p[key][5])
	h3 = plotRatio(h1, h2, p[key][3])
	canvas, pad1, pad2 = createCanvasPads()
	pad1.cd()
	h1.Draw("h")
	h2.Draw("h same")
	legend = setLegend(h1, h2, "leftBot")
	pad2.cd()
	h3.Draw("h")
	canvas.Print(outPath+outName+"_"+key+".png")
