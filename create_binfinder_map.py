software = 'acts'
software = 'athena'

#detector = 'pixel'
detector = 'strip'

layers = {
1:'mid',
2:'top',
3:'bottom'
}

phibins = 138
if detector == 'strip': phibins = 80
zbins = 11

if software=='athena' : event_string = '===>>>  start processing'
if software=='acts' : event_string = '================'

group_lines = [line for line in open('groups_output_{}.txt'.format(software)) if event_string in line or '|Groups {}|'.format(detector) in line]
map = list(filter(None,[lines[:].strip() for lines in group_lines]))
number_of_events = len([l for l in map if event_string in l]) 

event_list = []
event = []
for l in map:
	if '|Groups {}| n_group, n_mid, n_top, n_bot, phi_bin, z_bin:'.format(detector) in l:
		event.append(l.replace('|Groups {}| n_group, n_mid, n_top, n_bot, phi_bin, z_bin:'.format(detector),'').split(','))
	else:
		print(l)
		event_list.append(event)
		event = []

output_file = open('binfinder_map_{}_{}.txt'.format(software, detector), 'w')

for i_event, event_val in enumerate(event_list):
	output_file.write('========= Event {} ======== \n'.format(i_event))
	for i_layer, layer in layers.items():
		output_file.write('----> Layer {}: \n'.format(layer))
		map_list = [[0 for z in range(zbins)] for phi in range(phibins)]
		output_file.write(str(event_val)+' \n')
		for val in event_val:		
			map_list[int(val[4])][int(val[5])] = int(val[i_layer])
		map_string = ''
		for phi in range(phibins):
			output_file.write('({}) ==> |'.format(phi))
			for z in range(zbins):
				output_file.write('{}|'.format(map_list[phi][z]))
			output_file.write('\n')


