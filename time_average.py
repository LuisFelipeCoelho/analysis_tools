import os
import time

start_time = time.time()
runs = 2

i = 0
while i <= runs:
    #  os.system("acts_build/bin/ActsExampleSeedingTGeo \
    #     -n1000 -j1 \
    #     --mat-input-file=run/material-maps-ITk-HGTD.json \
    #     --input-dir=data/sim_atlas/ttbar/ \
    #     --output-dir=output_atlas_ttbar/run"+str(i)+" \
    #     --input-csv=1 --bf-constant-tesla=0:0:2 --response-file=run/tgeo-atlas-itk-hgtd.response \
    #     --digi-config-file=run/itk-pixel-digitization.json \
    #     --geo-selection-config-file run/geoSelection-openDataDetector.json > tmp")
    #  os.system("./acts_build/bin/ActsExampleSeedingITk --input-dir=data/CsvSpacePointsOutput_2 --output-dir=output_grid_test/run"+str(i)+" --bf-constant-tesla=0:0:2 --loglevel=2 -j1 >> tmp")
    os.system(
        "python3 acts/Examples/Scripts/Python/full_chain_itk.py"
    )
    print("-------", i, "-------")
    a = open("/Users/luiscoelho/lcoelho/acts2/itk_output/timing.tsv", "r").read()
    print(a)
    file = open("/Users/luiscoelho/lcoelho/acts2/itk_othogonal_comp/itk_orthogonal_comp_3/output_timer_test/run" + str(i) + "_timing.tsv", "w")
    file.write(a)
#    os.system("rm tmp")
    print("-------")
    if "Algorithm:SeedingAlgorithm" in a:
        i += 1
    if i >= runs:
      break
#    if time.time() - start_time > 2 and i == 0:
#        print("ERROR")
#        break


print("--- %s seconds ---" % ((time.time() - start_time) / runs))
