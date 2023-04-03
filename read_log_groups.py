#detector = 'pixel'
detector = 'strip'

log_lines_grid = [line for line in open('output_acts.txt') if '================' in line or '|Groups {}|'.format(detector) in line]
grid = list(filter(None,[lines[:].strip() for lines in log_lines_grid]))
output_file = open('groups_output_acts.txt', 'w')
for l in grid:
    output_file.write(l+'\n')
