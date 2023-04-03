import numpy as np
import ROOT

# ROOT.gROOT.SetStyle("ATLAS");


def setLegend(acts, athena):
    legend = ROOT.TLegend(0.68, 0.78, 0.9, 0.9)
    legend.AddEntry(acts, "Main branch (no change)")
    legend.AddEntry(athena, "ITK changes")
    legend.SetLineWidth(0)
    legend.SetFillStyle(0)
    legend.Draw("same")
    return legend


def setLegend2(h1, name):
    legend2.AddEntry(h1, name)
    legend2.SetLineWidth(0)
    legend2.SetFillStyle(0)
    legend2.Draw("same")


def plotOptions(h1, h2, y_label):
    h1.GetYaxis().SetTitle(y_label)
    h1.GetYaxis().SetLabelSize(0.0)
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
    pad1 = ROOT.TPad("pad1", "pad1", 0, 0.3, 1, 1.0)
    pad1.SetBottomMargin(0.05)
    pad1.SetGridx()
    pad1.Draw()
    pad1.cd()
    return pad1


def createPad2():
    pad2 = ROOT.TPad("pad2", "pad2", 0, 0.08, 1, 0.3)
    pad2.SetTopMargin(0)
    pad2.SetBottomMargin(0.3)
    pad2.SetGridx()
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


h_eta_nochange = ROOT.TH1F("eta", "", 30, -2, 1.7)
h_eta_change = ROOT.TH1F("eta", "", 30, -2, 1.7)

h_pt_nochange = ROOT.TH1F("pt", "", 30, 0, 45)
h_pt_change = ROOT.TH1F("pt", "", 30, 0, 45)


path = "/private/var/folders/1f/kfh_x4md2jj9dq49v9dhf1yr0000gn/T/pytest-of-luiscoelho/"
fileChange = ROOT.TFile.Open(
    path + "pytest-0/test_seeding0/estimatedparams.root", "READ"
)
fileNoChange = ROOT.TFile.Open(
    path + "pytest-1/test_seeding0/estimatedparams.root", "READ"
)

treeChange = fileChange.Get("estimatedparams")
treeNoChange = fileNoChange.Get("estimatedparams")

for entryNum in range(0, treeChange.GetEntries()):
    treeChange.GetEntry(entryNum)
    pt = getattr(treeChange, "pt")
    eta = getattr(treeChange, "eta")
    h_pt_change.Fill(pt)
    h_eta_change.Fill(eta)

for entryNum in range(0, treeNoChange.GetEntries()):
    treeNoChange.GetEntry(entryNum)
    pt = getattr(treeNoChange, "pt")
    eta = getattr(treeNoChange, "eta")
    h_pt_nochange.Fill(pt)
    h_eta_nochange.Fill(eta)


# PT
h1, h2 = plotOptions(h_pt_nochange, h_pt_change, "")
h3 = plotRatio(h1, h2, "p_{T} (MeV)")
canvas, pad1, pad2 = createCanvasPads()
pad1.cd()
h1.Draw("he")
h2.Draw("he same")
legend = setLegend(h1, h2)
pad2.cd()
h3.Draw("he")
canvas.Print("plots_pt.png")
canvas.Clear()

# ETA
h1, h2 = plotOptions(h_eta_nochange, h_eta_change, "")
h3 = plotRatio(h1, h2, "#eta")
canvas, pad1, pad2 = createCanvasPads()
pad1.cd()
h1.Draw("he")
h2.Draw("he same")
legend = setLegend(h1, h2)
pad2.cd()
h3.Draw("he")
canvas.Print("plots_eta.png")
canvas.Clear()
