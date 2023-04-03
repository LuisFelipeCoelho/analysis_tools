import csv
import os

# detector = 'pixel'
detector = "strip"

fileName = "output_athena.txt"
log_file = open(fileName)
log_lines = [line for line in log_file if "t evtSP" in line or "Dumping" in line]
space_points = list(
    filter(
        None,
        [
            lines[lines.find("t evtSP") :].strip().replace("t evtSP", "")
            for lines in log_lines
        ],
    )
)
# print(space_points)


os.mkdir("CsvSpacePointsOutput")

# read evtSP
for event in range(int(space_points[-1].split(",")[0]) + 1):
    # print('measurement_id,sp_type,module_idhash,sp_x,sp_y,sp_z,sp_radius,sp_covr,sp_covz')
    name = str(event).zfill(9)
    csv_file_pixel = open(
        "CsvSpacePointsOutput/event" + name + "-spacepoints_pixel.csv", "w"
    )
    csv_file_strip = open(
        "CsvSpacePointsOutput/event" + name + "-spacepoints_strip.csv", "w"
    )
    # csv_file_pixel.write('measurement_id,sp_type,module_idhash,sp_x,sp_y,sp_z,sp_radius,sp_covr,sp_covz\n')
    csv_file_pixel.write(
        "measurement_id,sp_type,module_idhash,sp_x,sp_y,sp_z,sp_radius,sp_covr,sp_covz,sp_topHalfStripLength,sp_bottomHalfStripLength,sp_topStripDirection[0],sp_topStripDirection[1],sp_topStripDirection[2],sp_bottomStripDirection[0],sp_bottomStripDirection[1],sp_bottomStripDirection[2],sp_stripCenterDistance[0],sp_stripCenterDistance[1],sp_stripCenterDistance[2],sp_bottomStripCenterPosition[0],sp_bottomStripCenterPosition[1],sp_bottomStripCenterPosition[2]\n"
    )
    csv_file_strip.write(
        "measurement_id,sp_type,module_idhash,sp_x,sp_y,sp_z,sp_radius,sp_covr,sp_covz,sp_topHalfStripLength,sp_bottomHalfStripLength,sp_topStripDirection[0],sp_topStripDirection[1],sp_topStripDirection[2],sp_bottomStripDirection[0],sp_bottomStripDirection[1],sp_bottomStripDirection[2],sp_stripCenterDistance[0],sp_stripCenterDistance[1],sp_stripCenterDistance[2],sp_bottomStripCenterPosition[0],sp_bottomStripCenterPosition[1],sp_bottomStripCenterPosition[2]\n"
    )
    total_lines = 0
    for hit in space_points:
        # print(int(hit.split(',')[0]), event)
        if int(hit.split(",")[0]) == event:
            if int(hit.split(",")[2]) == 0:
                print_to_file = ""
                for i in hit.split(",")[1:]:
                    print_to_file += i + ","
                print_to_file = print_to_file[:-1]
                csv_file_pixel.write(print_to_file + "\n")
                total_lines += 1
                # print(print_to_file)
            if int(hit.split(",")[2]) == 1:
                print_to_file = ""
                for i in hit.split(",")[1:]:
                    print_to_file += i + ","
                print_to_file = print_to_file[:-1]
                csv_file_strip.write(print_to_file + "\n")
                total_lines += 1
                # print(print_to_file)
    # print('LEN'+str(total_lines))

"""

# read Grid Map
log_lines_grid = [line for line in open(fileName) if 'PIXEL MAP OF SPACEPOINTS' in line or 'STRIP MAP OF SPACEPOINTS' in line or '===>' in line or 'number of Phi bins' in line]
grid = list(filter(None,[lines[lines.find('INFO'):].strip().replace('INFO','') for lines in log_lines_grid]))
output_file = open('grid_output.txt', 'w')
for l in grid:
    output_file.write(l+'\n')

log_lines_grid = [line for line in open(fileName) if '===>>>' in line or '|Groups {}|'.format(detector) in line]
grid = list(filter(None,[lines[lines.find('INFO'):].strip().replace('INFO','') for lines in log_lines_grid]))
output_file = open('groups_output_athena.txt', 'w')
for l in log_lines_grid:
    output_file.write(l+'\n')

"""
