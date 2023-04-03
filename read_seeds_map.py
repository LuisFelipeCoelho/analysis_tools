
software = 'acts'
#software = 'athena'

detector = 'pixel'
#detector = 'strip'

if software == 'acts':
	string = '================'
else:
  string = '===>>>'

log_lines_grid = [line for line in open(f'output_{software}.txt') if string in line or '|Seeds Map {}|'.format(detector) in line or 'Fill SP' in line or "|seed filter 1| Q" in line]
grid = list(filter(None,[lines[:].strip() for lines in log_lines_grid]))
output_file = open(f'seedsMap_output_{software}.txt', 'w')
for l in grid:
    output_file.write(l+'\n')
