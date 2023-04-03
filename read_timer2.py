import numpy as np
import ROOT
ROOT.gROOT.SetStyle("ATLAS")

software = [
'acts',
'athena',
]

sample = 'ttbar'
#sample = 'singleMu_100GeV'

event_name = "ttbar 14 TeV"
#event_name = "single Mu pT = 100 GeV"

string = '===>>>  done processing event'

log_lines_grid = [line.replace('|TIMER ACTS| ','') for line in open('output_{}.txt'.format(software[0]+'_'+sample)) if string in line or '|TIMER ACTS|' in line]
acts_values = list(filter(None,[lines[:].strip() for lines in log_lines_grid]))

log_lines_grid = [line.replace('|TIMER ATHENA| ','') for line in open('output_{}.txt'.format(software[1]+'_'+sample)) if string in line or '|TIMER ATHENA|' in line]
athena_values = list(filter(None,[lines[:].strip() for lines in log_lines_grid]))


h_acts_grid_time_PPP = ROOT.TH1F("h_acts_grid_time_PPP", "", 25, 0.0, 60)
h_athena_grid_time_PPP = ROOT.TH1F("h_athena_grid_time_PPP", "", 25, 0.0, 60)

h_acts_grid_time_SSS = ROOT.TH1F("h_acts_grid_time_SSS", "", 50, 0.0, 50)
h_athena_grid_time_SSS = ROOT.TH1F("h_athena_grid_time_SSS", "", 50, 0.0, 50)

h_acts_finder_time_PPP = ROOT.TH1F("h_acts_finder_time_PPP", "", 25, 0.0, 17)
h_athena_finder_time_PPP = ROOT.TH1F("h_athena_finder_time_PPP", "", 25, 0.0, 17)

h_acts_finder_time_SSS = ROOT.TH1F("h_acts_finder_time_SSS", "", 100, 0.0, -500)
h_athena_finder_time_SSS = ROOT.TH1F("h_athena_finder_time_SSS", "", 100, 0.0, -500)

h_acts_filter2_time_PPP = ROOT.TH1F("h_acts_finder_time_SSS", "", 25, 0.0, -100)
h_athena_filter2_time_PPP = ROOT.TH1F("h_athena_finder_time_SSS", "", 25, 0.0, -100)

h_acts_filter2_time_SSS = ROOT.TH1F("h_acts_finder_time_SSS", "", 50, 0.0, 17)
h_athena_filter2_time_SSS = ROOT.TH1F("h_athena_finder_time_SSS", "", 50, 0.0, 17)

h_acts_tri_time_PPP = ROOT.TH1F("h_acts_finder_time_SSS", "", 25, 0.0, 2300)
h_athena_tri_time_PPP = ROOT.TH1F("h_athena_finder_time_SSS", "", 25, 0.0, 2300)

h_acts_tri_time_SSS = ROOT.TH1F("h_acts_finder_time_SSS", "", 25, 0.0, -500)
h_athena_tri_time_SSS = ROOT.TH1F("h_athena_finder_time_SSS", "", 25, 0.0, -500)


for file in [acts_values, athena_values]:
  detector = ''
  a = 0
  b = 0
  event = 0
  for line in file:
    if event == 101:
      break
    if 'events processed so far' in line:
      print(event)
      event += 1
    #print(line)
    if 'This is PPP' in line:
      detector = 'PPP'
      #h_acts_finder_time_PPP.Fill(a/1000)
      #print(a/1000)
      a = 0
    if 'This is SSS' in line:
      detector = 'SSS'
      #h_acts_finder_time_SSS.Fill(b/1000)
      #print(b/1000)
      b = 0
    if 'duplets' in line:
      if file == acts_values:
        if detector == 'PPP':
          #print("h_acts_grid_time_PPP")
          h_acts_grid_time_PPP.Fill(float(line[line.find('duplets:'):].replace('duplets:', '').strip().split(" ")[0])/1000)
        elif detector == 'SSS':
          #print("h_acts_grid_time_SSS")
          h_acts_grid_time_SSS.Fill(float(line[line.find('duplets:'):].replace('duplets:', '').strip().split(" ")[0])/1000)
      elif file == athena_values:
        if detector == 'PPP':
          #print("h_athena_grid_time_PPP")
          h_athena_grid_time_PPP.Fill(float(line[line.find('duplets:'):].replace('duplets:', '').strip().split(" ")[0])/1000)
        elif detector == 'SSS':
          #print("h_athena_grid_time_SSS")
          h_athena_grid_time_SSS.Fill(float(line[line.find('duplets:'):].replace('duplets:', '').strip().split(" ")[0])/1000)
    elif 'filter 1' in line and 'triplets' not in line:
      if file == acts_values:
        if detector == 'PPP':
          #print("h_acts_finder_time_PPP")
          #print(float(line[line.find('filter 1:'):].replace('filter 1:', '').strip().split(" ")[0])/1000)
          h_acts_finder_time_PPP.Fill(float(line[line.find('filter 1:'):].replace('filter 1:', '').strip().split(" ")[0])/1000)
        elif detector == 'SSS':
          #print("h_acts_finder_time_SSS")
          h_acts_finder_time_SSS.Fill(float(line[line.find('filter 1:'):].replace('filter 1:', '').strip().split(" ")[0])/1000)
      elif file == athena_values:
        if detector == 'PPP':
          #print("h_athena_finder_time_PPP")
          #print(float(line[line.find('filter 1:'):].replace('filter 1:', '').strip().split(" ")[0])/1000)
          h_athena_finder_time_PPP.Fill(float(line[line.find('filter 1:'):].replace('filter 1:', '').strip().split(" ")[0])/1000)
        elif detector == 'SSS':
          #print("h_athena_finder_time_SSS")
          h_athena_finder_time_SSS.Fill(float(line[line.find('filter 1:'):].replace('filter 1:', '').strip().split(" ")[0])/1000)
    elif 'triplets + filter 1' in line:
      if file == acts_values:
        if detector == 'PPP':
          #print("h_acts_finder_time_PPP")
          #print(float(line[line.find('filter 1:'):].replace('filter 1:', '').strip().split(" ")[0])/1000)
          h_acts_tri_time_PPP.Fill(float(line[line.find('filter 1:'):].replace('filter 1:', '').strip().split(" ")[0])/1000)
        elif detector == 'SSS':
          #print("h_acts_finder_time_SSS")
          h_acts_tri_time_SSS.Fill(float(line[line.find('filter 1:'):].replace('filter 1:', '').strip().split(" ")[0])/1000)
      elif file == athena_values:
        if detector == 'PPP':
          #print("h_athena_finder_time_PPP")
          #print(float(line[line.find('filter 1:'):].replace('filter 1:', '').strip().split(" ")[0])/1000)
          h_athena_tri_time_PPP.Fill(float(line[line.find('filter 1:'):].replace('filter 1:', '').strip().split(" ")[0])/1000)
        elif detector == 'SSS':
          #print("h_athena_finder_time_SSS")
          h_athena_tri_time_SSS.Fill(float(line[line.find('filter 1:'):].replace('filter 1:', '').strip().split(" ")[0])/1000)
    elif 'filter 2' in line:
      if file == acts_values:
        if detector == 'PPP':
          #print("h_acts_finder_time_PPP")
          #print(float(line[line.find('filter 2:'):].replace('filter 2:', '').strip().split(" ")[0])/1000)
          h_acts_filter2_time_PPP.Fill(float(line[line.find('filter 2:'):].replace('filter 2:', '').strip().split(" ")[0])/1000)
        elif detector == 'SSS':
          #print("h_acts_finder_time_SSS")
          h_acts_filter2_time_SSS.Fill(float(line[line.find('filter 2:'):].replace('filter 2:', '').strip().split(" ")[0])/1000)
      elif file == athena_values:
        if detector == 'PPP':
          #print("h_athena_finder_time_PPP")
          #print(float(line[line.find('filter 2:'):].replace('filter 2:', '').strip().split(" ")[0])/1000)
          h_athena_filter2_time_PPP.Fill(float(line[line.find('filter 2:'):].replace('filter 2:', '').strip().split(" ")[0])/1000)
        elif detector == 'SSS':
          #print("h_athena_finder_time_SSS")
          h_athena_filter2_time_SSS.Fill(float(line[line.find('filter 2:'):].replace('filter 2:', '').strip().split(" ")[0])/1000)

def setLegend(acts, athena, filter, dec_name):
  legend = ROOT.TLegend(0.6,0.57,0.99,0.70)
  legend.AddEntry(acts ,"ACTS")
  legend.AddEntry(athena ,"Athena")
  legend.SetLineWidth(0)
  legend.SetFillStyle(0)
  legend.Draw("same")
  latex = ROOT.TLatex()
  latex.SetNDC()
  latex.SetTextSize(0.035)
  latex.DrawText(0.61, 0.78, "{} space points".format(dec_name))
  latex.DrawText(0.61, 0.83, event_name)
  latex.DrawText(0.61, 0.73, filter)
  return legend
  
def setLegend2(h1, h2, name1, name2, filter):
  legend2 = ROOT.TLegend(0.6,0.57,0.99,0.70)
  legend2.AddEntry(h1 , name1)
  legend2.AddEntry(h2 , name2)
  legend2.SetLineWidth(0)
  legend2.SetFillStyle(0)
  legend2.Draw("same")
  latex2 = ROOT.TLatex()
  latex2.SetNDC()
  latex2.SetTextSize(0.035)
  latex2.DrawText(0.61, 0.83, event_name)
  latex2.DrawText(0.61, 0.73, filter)
  return legend2
  
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
#  pad1.SetGridx()i
  pad1.SetLogy(1)
  pad1.Draw()
  pad1.cd()
  return pad1
  
def createPad2():
  pad2 = ROOT.TPad("pad2", "pad2", 0, 0.08, 1, 0.3)
  pad2.SetTopMargin(0)
  pad2.SetBottomMargin(0.3)
#  pad2.SetGridx()
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


canvas = ROOT.TCanvas()
canvas.Print("time_plots.pdf[")
canvas.Clear()



h1, h2 = plotOptions(h_acts_grid_time_PPP, h_athena_grid_time_PPP, "Events")
h3 = plotRatio(h1, h2, "Time (\mu s)")
canvas, pad1, pad2 = createCanvasPads()
pad1.cd()
h1.Draw("he")
h2.Draw("he same")
legend = setLegend(h1, h2, "duplets", "PPP")
pad2.cd()
h3.Draw("he")
canvas.Print("time_plots.pdf")
canvas.Print("time_duplets.root")
canvas.Clear()
'''
# GRID SSS
h1, h2 = plotOptions(h_acts_grid_time_SSS, h_athena_grid_time_SSS, "Events")
h3 = plotRatio(h1, h2, "Time (\mu s)")
canvas, pad1, pad2 = createCanvasPads()
pad1.cd()
h1.Draw("he")
h2.Draw("he same")
legend = setLegend(h1, h2, "duplets", "SSS")
pad2.cd()
h3.Draw("he")
canvas.Print("time_plots.pdf")
canvas.Print("time_grid_SSS.png")
canvas.Clear()
'''
# FINDER PPP
h1, h2 = plotOptions(h_acts_finder_time_PPP, h_athena_finder_time_PPP, "Events")
h3 = plotRatio(h1, h2, "Time (\mu s)")
canvas, pad1, pad2 = createCanvasPads()
pad1.cd()
h1.Draw("he")
h2.Draw("he same")
legend = setLegend(h1, h2, "newOneSeedWithCurvaturesComparisonPPP", "PPP")
pad2.cd()
h3.Draw("he")
canvas.Print("time_plots.pdf")
canvas.Print("time_filter1.root")
canvas.Clear()
'''
# FINDER SSS
h1, h2 = plotOptions(h_acts_finder_time_SSS, h_athena_finder_time_SSS, "Events")
h3 = plotRatio(h1, h2, "Time (\mu s)")
canvas, pad1, pad2 = createCanvasPads()
pad1.cd()
h1.Draw("he")
h2.Draw("he same")
legend = setLegend(h1, h2, "newOneSeedWithCurvaturesComparisonPPP", "SSS")
pad2.cd()
h3.Draw("he")
canvas.Print("time_plots.pdf")
canvas.Print("time_finder_SSS.png")
canvas.Clear()
'''
h1, h2 = plotOptions(h_acts_tri_time_PPP, h_athena_tri_time_PPP, "Events")
h3 = plotRatio(h1, h2, "Time (\mu s)")
canvas, pad1, pad2 = createCanvasPads()
pad1.cd()
h1.Draw("he")
h2.Draw("he same")
legend = setLegend(h1, h2, "triplets + newOneSeedWithCurvaturesComparisonPPP", "PPP")
pad2.cd()
h3.Draw("he")
canvas.Print("time_plots.pdf")
canvas.Print("time_triplets_filter1.root")
canvas.Clear()

h1, h2 = plotOptions(h_acts_filter2_time_PPP, h_athena_filter2_time_PPP, "Events")
h3 = plotRatio(h1, h2, "Time (\mu s)")
canvas, pad1, pad2 = createCanvasPads()
pad1.cd()
h1.Draw("he")
h2.Draw("he same")
legend = setLegend(h1, h2, "fillSeeds", "PPP")
pad2.cd()
h3.Draw("he")
canvas.Print("time_plots.pdf")
canvas.Print("time_filter2.root")
canvas.Clear()






canvas.Print("time_plots.pdf]")
