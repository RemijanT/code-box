from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models import (DBSession,)
from sqlalchemy import *
from sqlalchemy.orm import mapper, sessionmaker, clear_mappers
from sqlalchemy.ext.declarative import declarative_base
    
from .functions import common_functions_basic as php

import re, os.path, time, math, sys, unicodedata
		
@view_config(route_name='home', renderer='templates/splat_home_basic.pt')
def vanity_of_bananas(request):
	print request
	
	base = os.path.dirname(__file__)
	
	file_path = base + '/templates/query_submitted_basic.pt'
	mdate = time.ctime(os.path.getmtime(file_path))
	
	#print mdate
	dict = {
		#'json' : javascript,
		'modifieddate' : mdate
	}
    
	return {'retval': dict }
	
	
def tokenise_species(spec=''):
	if spec is None or spec == '':
		return False
	
	tok = re.sub(r'([0-9]+)', r'<sub>\g<1></sub>', spec)
	tok = re.sub(r'<sub>([0-9]+)</sub>,', r'\g<1>,', tok)
	tok = re.sub(r'<sub>([0-9]+)</sub>\)', r'\g<1>)', tok)
	tok = re.sub(r'=<sub>([0-9]+)</sub>', r'=\g<1>', tok)
	tok = re.sub(r'_plus', '<sup>+</sup>', tok)
	return tok

def map_frequency_color(frequency, measfreq, row):
	if (frequency >=31300 and frequency <=45000) or (measfreq >=31300 and measfreq <=45000):
		if row % 2 == 1:
			return "#ff99cc"
		else:
			return "#ffa9dc"
	
	if (frequency >= 67000 and frequency <= 90000) or (measfreq >= 67000 and measfreq <= 90000): 
		if row % 2 == 1: 
			return "#ff9933"
		else:
			return "#ffa943"
		
	if (frequency >= 86000 and frequency <= 116000) or (measfreq >= 86000 and measfreq <= 116000): 
		if row % 2 == 1: 
			return "#6699ff"
		else:
			return "#76a9ff"
		
	if (frequency >= 125000 and frequency <= 163000) or (measfreq >= 125000 and measfreq <= 163000): 
		if row % 2 == 1: 
			return "#66cc66"
		else:
			return "#76dc76"
		
	if (frequency >= 163000 and frequency <= 211000) or (measfreq >= 163000 and measfreq <= 211000): 
		if row % 2 == 1: 
			return "#efef33"
		else:
			return "#ffff43"

	if (frequency >= 211000 and frequency <= 275000) or (measfreq >= 211000 and measfreq <= 275000): 
		if row % 2 == 1: 
			return "#bcbcef"
		else:
			return "#ccccff"
		
	if (frequency >= 275000 and frequency <= 373000) or (measfreq >= 275000 and measfreq <= 373000): 
		if row % 2 == 1: 
			return "#99ffcc"
		else:
			return "#a9ffdc"
		
	if (frequency >= 385000 and frequency <= 500000) or (measfreq >= 385000 and measfreq <= 500000): 
		if row % 2 == 1: 
			return "#9966ff"
		else:
			return "#a976ff"
		
	if (frequency >= 602000 and frequency <= 720000) or (measfreq >= 602000 and measfreq <= 720000): 
		if row % 2 == 1: 
			return "#99ccff"
		else:
			return "#a9dcff"
		
	if (frequency >= 787000 and frequency <= 950000) or (measfreq >= 787000 and measfreq <= 950000): 
		if row % 2 == 1: 
			return "#999900"
		else:
			return "#a9a920"
	
	if row % 2 == 1:
		return "#d0d0d0"
	
	return "#e0e0e0"
	
def map_frequency_almaband(frequency, measfreq):
	if (frequency >=31300 and frequency <=45000) or (measfreq >=31300 and measfreq <=45000):
		return "ALMA BAND 1"
	
	if (frequency >= 67000 and frequency <= 90000) or (measfreq >= 67000 and measfreq <= 90000): 
		return "ALMA BAND 2"
		
	if (frequency >= 86000 and frequency <= 116000) or (measfreq >= 86000 and measfreq <= 116000): 
		return "ALMA BAND 3"
		
	if (frequency >= 125000 and frequency <= 163000) or (measfreq >= 125000 and measfreq <= 163000): 
		return "ALMA BAND 4"
		
	if (frequency >= 163000 and frequency <= 211000) or (measfreq >= 163000 and measfreq <= 211000): 
		return "ALMA BAND 5"

	if (frequency >= 211000 and frequency <= 275000) or (measfreq >= 211000 and measfreq <= 275000): 
		return "ALMA BAND 6"
		
	if (frequency >= 275000 and frequency <= 373000) or (measfreq >= 275000 and measfreq <= 373000): 
		return "ALMA BAND 7"
		
	if (frequency >= 385000 and frequency <= 500000) or (measfreq >= 385000 and measfreq <= 500000): 
		return "ALMA BAND 8"
		
	if (frequency >= 602000 and frequency <= 720000) or (measfreq >= 602000 and measfreq <= 720000): 
		return "ALMA BAND 9"
		
	if (frequency >= 787000 and frequency <= 950000) or (measfreq >= 787000 and measfreq <= 950000): 
		return "ALMA BAND 10"
	
	return ""
	
def has_value(value):
	if (value == '' or value is None):
		return False
	return True
	
def array_push(array, string):
	return array.append(string)
	
def array_map(function, list):
	m_list = dir(sys.modules[__name__])
	result = []
	for m in m_list:
		if m == function:
			for s in list:
				result.append(globals()[m](s))
			return result
	
def has_number(str):
	if str is None:
		return False
	if type(str) is float:
		return True
	if type(str) is int:
		return True
	if type(str) is long:
		return True
	
def set_if_has_value(original, yes, no=""):
	if original is None or original == "":
		original = no
	else:
		original = yes

def array_push_if(array, value, condition):
	
	if array:
		for i in array:
			print i	
		if condition == True:
			array.append(value)
			return array
		return array
	else:
		array = []
		array.append(value)
		return array
		
def mysql_real_escape_string(string):
	if type(string) is not string:
		return string
	
	if "\\x00" in string:
		string = string.replace("\\x00","\\\\x00")
	if "\\n" in string:
		string = string.replace("\\n","\\\\n")
	if "\\r" in string:
		string = string.replace("\\r","\\\\r")
	if "\\" in string:
		string = string.replace("\\","\\\\")
	if "'" in string:
		string = string.replace("'","\\'")
	if "\"" in string:
		string = string.replace("\"","\\\"")
	if "\\x1a" in string:
		string = string.replace("\\x1a","\\\\x1a")
	#string = string + 'eblu sok'
	return string

def map_line_list(ll_id):
	
	if ll_id == 10: return "CDMS"
	if ll_id == 11: return "Lovas"
	if ll_id == 12: return "JPL"
	if ll_id == 14: return "SLAIM"
	if ll_id == 15: return "Recomb"
	if ll_id == 16: return "ToyaMA"
	if ll_id == 17: return "OSU"
	if ll_id == 18: return "TopModel"
	if ll_id == 19: return "RFI"
	
	return ""

def describe_results(req, name, amount, start,end):	

	#print req['energy_range_type'] == "eu_k"
	found = "Found " + amount
	if line['sid'] is not None and line['sid'] != '':
		found += """&nbsp<a class="norm" href="javascript:void(0)" onclick="info_window('species_metadata_displayer_basic.php?species_id=""" + str(line['sid']) + """')">name</a>"""
	
	found += ' lines'
	
	if (req['from'] != '' and req['to'] == ''):
		found += ' above ' + str(req['from']) + ' ' + str(req['frequency_units'])
	
	if (req['from'] == '' and req['to'] != ''):
		found += ' above ' + str(req['to']) + ' ' + str(req['frequency_units'])
		
	if (req['from'] != '' and req['to'] != ''):
		found += ' above ' + str(req['from']) + ' - ' + str(req['to']) + ' ' + str(req['frequency_units'])
	
	if (req["from"] != "" and req["to"] == "") or (req['from'] == "" and req['to'] != ""):
		print "<P><p><h2>Splatalogue input error!<p> Please click back button in your browser and enter missing <font color=red>Min/Max</font> value(s) in the frequency range!"
		return
	

	for i in range(2, 21): 
		fromi = "from" + str(i)
		toi = "to" + str(i)
		try:
			if ((req[fromi] != "" and req[toi] == "" and req['from'] != "" or req['to'] != "")):
				print "<P><p><h2>Splatalogue input error!<p> Please click back button in your browser and enter missing <font color=red>Min/Max</font> value(s) in the frequency range!"
				return
		except:
			print 'req[from' + str(i) + '] not found'
		
	
	for i in range(2, 21): 
		fromi = "from" + str(i)
		toi = "to" + str(i)
		try:
			if ((req[fromi] == "" and req[toi] != "" and req['from'] != "" or req['to'] != "")):
				print "<P><p><h2>Splatalogue input error!<p> Please click back button in your browser and enter missing <font color=red>Min/Max</font> value(s) in the frequency range!"
				return
		except:
			print 'req[from' + str(i) + '] not found'
	
	for i in range(2, 21): 
		fromi = "from" + str(i)
		toi = "to" + str(i)
		try:
			if (req[fromi] != "" and req[toi] == ""):
				found += ", from " + str(req[fromi]) + " - " + str(req[toi]) + " " + str(req["frequency_units"])
		except:
			print 'req[from' + str(i) + '] not found'
	
	
	if (req['band'] != "any" and req['from'] == "" and req['to'] == ""):
		if (req['band'] == "alma3"): 
			found = found + " in ALMA Band 3 (84-116 GHz)"
		
		elif (req['band'] == "alma4"): 
			found = found + " in ALMA Band 4 (125-163 GHz)"
		
		elif (req['band'] == "alma5"): 
			found = found + " in ALMA Band 5 (163-211 GHz)"
		
		elif (req['band'] == "alma6"): 
			found = found + " in ALMA Band 6 (211-275 GHz)"
		
		elif (req['band'] == "alma7"): 
			found = found + " in ALMA Band 7 (275-373 GHz)"
		
		elif (req['band'] == "alma8"): 
			found = found + " in ALMA Band 8 (385-500 GHz)"
		
		elif (req['band'] == "alma9"): 
			found = found + " in ALMA Band 9 (602-720 GHz)"
		
		elif (req['band'] == "alma10"): 
			found = found + " in ALMA Band 10 (787-950 GHz)"
		
		elif (req['band'] == "pf1"): 
			found = found + " in GBT PF1 (0.29-0.92 GHz)"
		
		elif (req['band'] == "pf2"): 
			found = found + " in GBT PF2 (0.91-1.23 GHz)"
		
		elif (req['band'] == "l"): 
			found = found + " in GBT/VLA L (1-2 GHz)"
		
		elif (req['band'] == "s"): 
			found = found + " in GBT/VLA S (1.7-4 GHz)"
		
		elif (req['band'] == "c"): 
			found = found + " in GBT/VLA C (3.9-8 GHz)"
		
		elif (req['band'] == "x"): 
			found = found + " in GBT/VLA X (8-12 GHz)"
		
		elif (req['band'] == "ku"): 
			found = found + " in GBT/VLA Ku (12-18 GHz)"
		
		elif (req['band'] == "kfpa"): 
			found = found + " in GBT KFPA (18-27.5 GHz)"
		
		elif (req['band'] == "k"): 
			found = found + " in VLA K (18-26.5 GHz)"
		
		elif (req['band'] == "ka"): 
			found = found + " in GBT/VLA Ka (26-40 GHz)"
		
		elif (req['band'] == "q"): 
			found = found + " in GBT/VLA Q (38-50 GHz)"
		
		elif (req['band'] == "w"): 
			found = found + " in GBT W (67-93.3 GHz)"
		
		elif (req['band'] == "mustang"): 
			found = found + " in GBT/VLA Mustang (80-100 GHz)"
		
		else:
			pass
		
		if (req['energy_range_type'] == "el_cm1" and req['energy_range_from'] != "" and req['energy_range_to'] == ""):
			found = found + ", with E<sub>L</sub> >= " + req['energy_range_from'] + " cm<sup>-1</sup>"
		
		if (req['energy_range_type'] == "el_cm1" and req['energy_range_from'] == "" and req['energy_range_to'] != ""): 
			found = found + ", with E<sub>L</sub> <= " + req['energy_range_to'] + " cm<sup>-1</sup>"
		
		if (req['energy_range_type'] == "el_cm1" and req['energy_range_from'] != "" and req['energy_range_to'] != ""): 
			found = found + ", with " + req['energy_range_from'] + " <= E<sub>L</sub> <= " + req['energy_range_to'] + " cm<sup>-1</sup>"
		

		if (req['energy_range_type'] == "eu_cm1" and req['energy_range_from'] != "" and req['energy_range_to'] == ""): 
			found = found + ", with E<sub>U</sub> >= " + req['energy_range_from'] + " cm<sup>-1</sup>"
		
		if (req['energy_range_type'] == "eu_cm1" and req['energy_range_from'] == "" and req['energy_range_to'] != ""): 
			found = found + ", with E<sub>U</sub> <= " + req['energy_range_to'] + " cm<sup>-1</sup>"
		
		if (req['energy_range_type'] == "eu_cm1" and req['energy_range_from'] != "" and req['energy_range_to'] != ""): 
			found = found + ", with " + req['energy_range_from'] + " <= E<sub>U</sub> <= " + req['energy_range_to'] + " cm<sup>-1</sup>"
		

		if (req['energy_range_type'] == "el_k" and req['energy_range_from'] != "" and req['energy_range_to'] == ""): 
			found = found + ", with E<sub>L</sub> >= " + req['energy_range_from'] + " K"
		
		if (req['energy_range_type'] == "el_k" and req['energy_range_from'] == "" and req['energy_range_to'] != ""): 
			found = found + ", with E<sub>L</sub> <= " + req['energy_range_to'] + " K"
		
		if (req['energy_range_type'] == "el_k" and req['energy_range_from'] != "" and req['energy_range_to'] != ""): 
			found = found + ", with " + req['energy_range_from'] + " <= E<sub>L</sub> <= " + req['energy_range_to'] + " K"
		

		if (req['energy_range_type'] == "eu_k" and req['energy_range_from'] != "" and req['energy_range_to'] == ""): 
			found = found + ", with E<sub>U</sub> >= " + req['energy_range_from'] + " K"
		
		if (req['energy_range_type'] == "eu_k" and req['energy_range_from'] == "" and req['energy_range_to'] != ""): 
			found = found + ", with E<sub>U</sub> <= " + req['energy_range_to'] + " K"
		
		if (req['energy_range_type'] == "eu_k" and req['energy_range_from'] != "" and req['energy_range_to'] != ""): 
			found = found + ", with " + req['energy_range_from'] + " <= E<sub>U</sub> <= " + req['energy_range_to'] + " K"
		
		if (end != -1):
			found = found + ", showing " + str(int(start) + 1) + " - " + str(int(end) + 1)
		else:
			found = found + ", showing " + str(start) + " - " + str(int(end) + 1)
		
		#print req['energy_range_type'] == "eu_k"
		return found

@view_config(route_name='query_submitted_basic', renderer='templates/query_submitted_basic.pt')
def build_query(request, offset = 0, limit = 4294967296):
	
	select_where = []
	select_fields = []
	lines = []
	lower_limits = []

	#print request.params
	
	req_show_unres_qn = ''
	req_show_upper_degeneracy = ''
	req_show_molecule_tag = ''
	req_show_qn_code = ''
	
	tran = ''
	bias = ''
	
	req_il = ''
	req_intl = '' 
	
	req_no_probable = ''
	req_known = ''
	req_fel = ''
	req_noHFS = ''
	req_trans = ''
	
	# 23 Quick Picker checkboxes
	
	quick_picker = []
	exec "try:\n if request.params['sid_204'] == '204': quick_picker.append('204') \nexcept: pass"
	exec "try:\n if request.params['sid_4'] == '4': quick_picker.append('4') \nexcept: pass"
	exec "try:\n if request.params['sid_226'] == '226': quick_picker.append('226') \nexcept: pass"
	exec "try:\n if request.params['sid_245'] == '245': quick_picker.append('245') \nexcept: pass"
	exec "try:\n if request.params['sid_55'] == '55': quick_picker.append('55') \nexcept: pass"
	exec "try:\n if request.params['sid_194'] == '194': quick_picker.append('194') \nexcept: pass"
	exec "try:\n if request.params['sid_258'] == '258': quick_picker.append('258') \nexcept: pass"
	exec "try:\n if request.params['sid_82'] == '82': quick_picker.append('82') \nexcept: pass"
	exec "try:\n if request.params['sid_137'] == '137': quick_picker.append('137') \nexcept: pass"
	exec "try:\n if request.params['sid_255'] == '255': quick_picker.append('255') \nexcept: pass"
	exec "try:\n if request.params['sid_23'] == '23': quick_picker.append('23') \nexcept: pass"
	exec "try:\n if request.params['sid_15'] == '15': quick_picker.append('15') \nexcept: pass"
	exec "try:\n if request.params['sid_6'] == '6': quick_picker.append('6') \nexcept: pass"
	exec "try:\n if request.params['sid_38'] == '38': quick_picker.append('38') \nexcept: pass"
	exec "try:\n if request.params['sid_638'] == '638': quick_picker.append('638') \nexcept: pass"
	exec "try:\n if request.params['sid_125'] == '125': quick_picker.append('125') \nexcept: pass"
	exec "try:\n if request.params['sid_1364'] == '1364': quick_picker.append('1364') \nexcept: pass"
	exec "try:\n if request.params['sid_1367'] == '1367': quick_picker.append('1367') \nexcept: pass"
	exec "try:\n if request.params['sid_1368'] == '1368': quick_picker.append('1368') \nexcept: pass"
	exec "try:\n if request.params['sid_1366'] == '1366': quick_picker.append('1366') \nexcept: pass"
	exec "try:\n if request.params['sid_418'] == '418': quick_picker.append('418') \nexcept: pass"
	exec "try:\n if request.params['sid_472'] == '472': quick_picker.append('472') \nexcept: pass"
	exec "try:\n if request.params['sid_20'] == '20': quick_picker.append('20') \nexcept: pass"
	in_list = ','.join(quick_picker)
	select_where.append('m.species_id in (' + in_list + ')')


	# Search text input box
	
	if request.params['chemical_name'] == "Cyanobutadiyne (HC5N v11 = 1)": select_where.append(species_id = '1')
	if request.params['chemical_name'] == "Formic Acid (t-H(13)COOH)": select_where.append(species_id = '3')
	if request.params['chemical_name'] == "Carbon Monoxide ((13)CO v=0)": select_where.append(species_id = '4')		
	if request.params['chemical_name'] == "Carbon Monosulfide ((13)C(34)S v=0)": select_where.append(species_id = '5')
	if request.params['chemical_name'] == "Carbon Monosulfide (CS v=0)": select_where.append(species_id = '6')
	if request.params['chemical_name'] == "Formylium (D(13)CO+)": select_where.append(species_id = '7')
	if request.params['chemical_name'] == "Atomic Carbon ((13)C)": select_where.append(species_id = '10')	 
	if request.params['chemical_name'] == "Silicon tetracarbide (SiC4)": select_where.append(species_id = '12')
	if request.params['chemical_name'] == "Carbon Monoxide ((13)C(18)O)": select_where.append(species_id = '14')
	if request.params['chemical_name'] == "Ketenimine (H2CCNH)": select_where.append(species_id = '17')		
	if request.params['chemical_name'] == "Silicon Monoxide (SiO v=0)": select_where.append(species_id = '20')
	if request.params['chemical_name'] == "Ethylene Oxide (c-H2COCH2)": select_where.append(species_id = '21')
	if request.params['chemical_name'] == "Carbon Monophosphide (CP)": select_where.append(species_id = '22')
	if request.params['chemical_name'] == "Hydrogen Cyanide (DCN v=0)": select_where.append(species_id = '23')
	if request.params['chemical_name'] == "Sulfur Monoxide ((34)SO)": select_where.append(species_id = '24')	
	if request.params['chemical_name'] == "Cyanobutadiyne (HCC(13)CCCN)": select_where.append(species_id = '27')	
	if request.params['chemical_name'] == "Carbon Monosulfide (C(36)S v = 0)": select_where.append(species_id = '30')
	if request.params['chemical_name'] == "Silicon Mononitride (SiN)": select_where.append(species_id = '33')
	if request.params['chemical_name'] == "Cyanoacetylene (HC3N v7=1)": select_where.append(species_id = '36')
	if request.params['chemical_name'] == "Formylium (H(13)CO+)": select_where.append(species_id = '38')	
	if request.params['chemical_name'] == "Cyanide Radical (CN v=0)": select_where.append(species_id = '40')
	if request.params['chemical_name'] == "Ammonia (ND3)": select_where.append(species_id = '41')
	if request.params['chemical_name'] == "Ketene (H2CCO)": select_where.append(species_id = '44')			
	if request.params['chemical_name'] == "Propadienylidene (l-H2CCC)": select_where.append(species_id = '45')	
	if request.params['chemical_name'] == "Cyanoacetylene (HC3N v6=1,v7=1)": select_where.append(species_id = '46')
	if request.params['chemical_name'] == "Trihydrogen ion (H2D+)": select_where.append(species_id = '47')	
	if request.params['chemical_name'] == "Sodium Chloride (NaCl v=0)": select_where.append(species_id = '51')
	if request.params['chemical_name'] == "Propynylidyne (l-C3H v=0)": select_where.append(species_id = '52')
	if request.params['chemical_name'] == "Methanol (CH3OH vt=0)": select_where.append(species_id = '55')			
	if request.params['chemical_name'] == "2,4,6-Heptatriynenitrile (HC7N v=0)": select_where.append(species_id = '58')
	if request.params['chemical_name'] == "Diazenylium (N2D+)": select_where.append(species_id = '59')	
	if request.params['chemical_name'] == "Sulfur Dioxide ((33)SO2)": select_where.append(species_id = '60')			
	if request.params['chemical_name'] == "Silicon Isocyanide (SiNC 2P1/2)": select_where.append(species_id = '61')	
	if request.params['chemical_name'] == "1,3-Butadiynyl radical (C(13)CCCH)": select_where.append(species_id = '63')
	if request.params['chemical_name'] == "1,3,5-Hexatriynyl (C6H)": select_where.append(species_id = '64')	
	if request.params['chemical_name'] == "Cyanide Radical ((13)CN)": select_where.append(species_id = '65')
	if request.params['chemical_name'] == "Thioformaldehyde (D2CS)": select_where.append(species_id = '68')
	if request.params['chemical_name'] == "Nitrosyl cyanide (ONCN)": select_where.append(species_id = '75')
	if request.params['chemical_name'] == "Ammonia (NH2D)": select_where.append(species_id = '77')				
	if request.params['chemical_name'] == "Sulfur Dioxide ((34)SO2 v=0)": select_where.append(species_id = '78')	
	if request.params['chemical_name'] == "Iminomethylium (HCNH+)": select_where.append(species_id = '79')	
	if request.params['chemical_name'] == "Sulfur dioxide (SO2 v=0)": select_where.append(species_id = '80')		
	if request.params['chemical_name'] == "Hydrogen Isocyanide (HNC v=0)": select_where.append(species_id = '82')
	if request.params['chemical_name'] == "Cyanoethynyl (CC(13)CN)": select_where.append(species_id = '85')	
	if request.params['chemical_name'] == "2,4-Pentadiynylidyne (l-C5H)": select_where.append(species_id = '92')
	if request.params['chemical_name'] == "Formaldehyde (D2CO)": select_where.append(species_id = '94')			
	if request.params['chemical_name'] == "1,3-Butadiynyl radical (C4H v=0)": select_where.append(species_id = '96')	
	if request.params['chemical_name'] == "Magnesium Isocyanide (MgNC v = 0)": select_where.append(species_id = '100')
	if request.params['chemical_name'] == "Silicon Monoxide ((29)SiO v=0)": select_where.append(species_id = '103')	
	if request.params['chemical_name'] == "Aluminum Isocyanitrile (AlNC)": select_where.append(species_id = '107')
	if request.params['chemical_name'] == "1,3,5-Hexatriynyl anion (C6H-)": select_where.append(species_id = '108')	
	if request.params['chemical_name'] == "Formaldehyde (HDCO)": select_where.append(species_id = '109')					
	if request.params['chemical_name'] == "2,4,6,8,10-Undecapentaynenitrile (HC11N)": select_where.append(species_id = '110')
	if request.params['chemical_name'] == "Fluoromethyliumylidene (CF+ v=0)": select_where.append(species_id = '115')
	if request.params['chemical_name'] == "Silicon Monoxide (Si(18)O v = 0)": select_where.append(species_id = '116')
	if request.params['chemical_name'] == "Carbon Monosulfide (C(34)S v=0)": select_where.append(species_id = '117')
	if request.params['chemical_name'] == "Carbon monosulfide (CS v=1-0)": select_where.append(species_id = '1249')
	if request.params['chemical_name'] == "Ethylene Glycol (g'Ga-(CH2OH)2)": select_where.append(species_id = '121')
	if request.params['chemical_name'] == "Atomic Carbon (C)": select_where.append(species_id = '125')			
	if request.params['chemical_name'] == "Silicon Cyanide (SiCN 2P1/2)": select_where.append(species_id = '127')	
	if request.params['chemical_name'] == "2,4,6-Heptatriynylidyne (C7H)": select_where.append(species_id = '129')
	if request.params['chemical_name'] == "Cyanoacetylene (HC(13)CCN v6=1)": select_where.append(species_id = '130')	
	if request.params['chemical_name'] == "4-Cyano-1,3-Butadiynyl (C5N)": select_where.append(species_id = '133')
	if request.params['chemical_name'] == "Cyclopropenone (c-H2C3O)": select_where.append(species_id = '136')	
	if request.params['chemical_name'] == "Hydrogen Cyanide (H(13)CN v=0)": select_where.append(species_id = '137')	
	if request.params['chemical_name'] == "Isothiocyanic acid (HNCS a-type)": select_where.append(species_id = '138')
	if request.params['chemical_name'] == "Thioformaldehyde (HDCS)": select_where.append(species_id = '139')	
	if request.params['chemical_name'] == "Formylium (HC(17)O+)": select_where.append(species_id = '141')		
	if request.params['chemical_name'] == "Carbon Monosulfide ((13)CS v=0)": select_where.append(species_id = '142')	
	if request.params['chemical_name'] == "Methyl diacetylene (CH3C4H)": select_where.append(species_id = '146')	
	if request.params['chemical_name'] == "Cyanoacetylene (HC3N v6=1)": select_where.append(species_id = '147')	
	if request.params['chemical_name'] == "Diazenylium (N2H+ v=0)": select_where.append(species_id = '148')	
	if request.params['chemical_name'] == "Sulfur Dioxide (OS(18)O)": select_where.append(species_id = '149')		
	if request.params['chemical_name'] == "Potassium chloride (K(37)Cl v = 0)": select_where.append(species_id = '150')	
	if request.params['chemical_name'] == "Formaldehyde (H2C(18)O)": select_where.append(species_id = '155')			
	if request.params['chemical_name'] == "Glycolaldehyde (cis-CH2OHCHO v=0)": select_where.append(species_id = '156')	
	if request.params['chemical_name'] == "2-Butynenitrile (CH3C3N)": select_where.append(species_id = '158')		
	if request.params['chemical_name'] == "Hydroxymethylidyne (HOC+ v = 0)": select_where.append(species_id = '160')	
	if request.params['chemical_name'] == "Formic Acid (t-HCOOH)": select_where.append(species_id = '163')			
	if request.params['chemical_name'] == "Protonate 2-proynenitrile (HC3NH+)": select_where.append(species_id = '170')	
	if request.params['chemical_name'] == "Trihydrogen ion (HD2+)": select_where.append(species_id = '172')				
	if request.params['chemical_name'] == "2,4,6,8-Nonatetraynenitrile (HC9N)": select_where.append(species_id = '173')	
	if request.params['chemical_name'] == "Carbonyl Sulfide ((18)OCS)": select_where.append(species_id = '174')		
	if request.params['chemical_name'] == "1,3-Butadiynyl radical (C4D)": select_where.append(species_id = '175')	
	if request.params['chemical_name'] == "Molecular Hydrogen (HD v=0)": select_where.append(species_id = '178')	
	if request.params['chemical_name'] == "Carbonyl Sulfide (O(13)CS)": select_where.append(species_id = '179')	
	if request.params['chemical_name'] == "Ethynyl (CCD)": select_where.append(species_id = '182')		
	if request.params['chemical_name'] == "Methylene (CH2)": select_where.append(species_id = '185')		
	if request.params['chemical_name'] == "Methylidyne (CH 2P1/2)": select_where.append(species_id = '189')			
	if request.params['chemical_name'] == "Potassium chloride (KCl v = 0)": select_where.append(species_id = '193')	
	if request.params['chemical_name'] == "Formaldehyde (H2CO)": select_where.append(species_id = '194')			
	if request.params['chemical_name'] == "Hydrogen Cyanide (DCN v2=1)": select_where.append(species_id = '196')			
	if request.params['chemical_name'] == "3-Cyano-1,2-propadienylidene (l-HC4N)": select_where.append(species_id = '198')	
	if request.params['chemical_name'] == "Cyanoacetylene (HCCC(15)N)": select_where.append(species_id = '203')		
	if request.params['chemical_name'] == "Carbon Monoxide (CO v=0)": select_where.append(species_id = '204')	
	if request.params['chemical_name'] == "Methyl Acetylene (CH3CCD)": select_where.append(species_id = '209')	
	if request.params['chemical_name'] == "Thioformaldehyde (H2CS)": select_where.append(species_id = '210')	
	if request.params['chemical_name'] == "Cyanoethynyl (CCCN v=0)": select_where.append(species_id = '212')	
	if request.params['chemical_name'] == "Vinyl Alcohol (a-H2CCHOH)": select_where.append(species_id = '214')	
	if request.params['chemical_name'] == "Cyanobutadiyne (HCCCC(13)CN)": select_where.append(species_id = '215')	
	if request.params['chemical_name'] == "Methylcyanodiacetylene (CH3C5N)": select_where.append(species_id = '220')	
	if request.params['chemical_name'] == "Phosphaethyne (HCP v=0)": select_where.append(species_id = '221')			
	if request.params['chemical_name'] == "Cyanoacetylene (HC(13)CCN v7 = 1)": select_where.append(species_id = '222')	
	if request.params['chemical_name'] == "Cyanoformaldehyde (CNCHO)": select_where.append(species_id = '223')	
	if request.params['chemical_name'] == "Hydroxymethylium ion (H2COH+)": select_where.append(species_id = '224')	
	if request.params['chemical_name'] == "Cyanoacetylene (HCC(13)CN)": select_where.append(species_id = '225')	
	if request.params['chemical_name'] == "Carbon Monoxide (C(17)O)": select_where.append(species_id = '226')
	if request.params['chemical_name'] == "Formylium (HC(18)O+)": select_where.append(species_id = '227')	
	if request.params['chemical_name'] == "Thioformaldehyde (H2(13)CS)": select_where.append(species_id = '228')	
	if request.params['chemical_name'] == "Sulfur Monoxide ((33)SO)": select_where.append(species_id = '232')
	if request.params['chemical_name'] == "Diazenylium ((15)NNH+)": select_where.append(species_id = '234')		
	if request.params['chemical_name'] == "Cyanoacetylene (HC3N v4=1,v7=1)": select_where.append(species_id = '242')	
	if request.params['chemical_name'] == "Cyanoacetylene (H(13)CCCN)": select_where.append(species_id = '244')	
	if request.params['chemical_name'] == "Carbon Monoxide (C(18)O)": select_where.append(species_id = '245')	
	if request.params['chemical_name'] == "Thioformylium (HCS+)": select_where.append(species_id = '247')	
	if request.params['chemical_name'] == "Thioxoethenylidene (CCS)": select_where.append(species_id = '251')	
	if request.params['chemical_name'] == "Cyanoacetylene (HC(13)CCN v7=2)": select_where.append(species_id = '252')	
	if request.params['chemical_name'] == "Hydrogen Cyanide (HC(15)N v=0)": select_where.append(species_id = '255')	
	if request.params['chemical_name'] == "Formylium (DCO+ v=0)": select_where.append(species_id = '256')	
	if request.params['chemical_name'] == "Hydrogen Cyanide (HCN v=0)": select_where.append(species_id = '258')	
	if request.params['chemical_name'] == "Cyanobutadiyne (HCCC(13)CCN)": select_where.append(species_id = '260')	
	if request.params['chemical_name'] == "Silicon Monocarbide (SiC v=0)": select_where.append(species_id = '261')	
	if request.params['chemical_name'] == "Carbon Monoxide ((13)C(17)O)": select_where.append(species_id = '264')	
	if request.params['chemical_name'] == "Ethynyl ((13)CCH)": select_where.append(species_id = '268')		
	if request.params['chemical_name'] == "Carbonyl Sulfide (OC(34)S)": select_where.append(species_id = '270')	
	if request.params['chemical_name'] == "Cyanobutadiyne (H(13)CCCCCN)": select_where.append(species_id = '272')	
	if request.params['chemical_name'] == "Cyanoacetylene (DC3N)": select_where.append(species_id = '273')			
	if request.params['chemical_name'] == "1,3-Butadiynyl radical (CCC(13)CH)": select_where.append(species_id = '275')	
	if request.params['chemical_name'] == "Sulfur Monoxide (SO 3Sigma v=0)": select_where.append(species_id = '279')		
	if request.params['chemical_name'] == "1,3-Butadiynyl radical ((13)CCCCH)": select_where.append(species_id = '280')	
	if request.params['chemical_name'] == "Ethynyl (CCH v=0)": select_where.append(species_id = '282')			
	if request.params['chemical_name'] == "Ammonia (NHD2)": select_where.append(species_id = '285')			
	if request.params['chemical_name'] == "1,3,5,7-Octatetraynyl (C8H)": select_where.append(species_id = '286')				
	if request.params['chemical_name'] == "1,3-Butadiynyl radical (C4H v7 = 2 l=0)": select_where.append(species_id = '289')	
	if request.params['chemical_name'] == "Sulfur Monoxide (S(18)O)": select_where.append(species_id = '291')	
	if request.params['chemical_name'] == "Silicon Monoxide ((30)SiO v=0)": select_where.append(species_id = '293')	
	if request.params['chemical_name'] == "Cyanoacetylene (HC3N v=0)": select_where.append(species_id = '294')	
	if request.params['chemical_name'] == "Hydrogen Isocyanide (DNC)": select_where.append(species_id = '296')	
	if request.params['chemical_name'] == "Cyanoethynyl ((13)CCCN)": select_where.append(species_id = '299')			
	if request.params['chemical_name'] == "Carbon Monosulfide   (C(33)S v=0)": select_where.append(species_id = '300')	
	if request.params['chemical_name'] == "Cyanoacetylene (HC(13)CCN)": select_where.append(species_id = '304')	
	if request.params['chemical_name'] == "Copper hydride ((65)CuH)": select_where.append(species_id = '305')	
	if request.params['chemical_name'] == "Methyl Acetylene (CH2DCCH)": select_where.append(species_id = '308')	
	if request.params['chemical_name'] == "Hydrogen Cyanide (HCN v2=1)": select_where.append(species_id = '309')	
	if request.params['chemical_name'] == "Methyl Acetylene (CH3CCH v=0)": select_where.append(species_id = '311')	
	if request.params['chemical_name'] == "Cyanobutadiyne (DCCCCCN)": select_where.append(species_id = '312')	
	if request.params['chemical_name'] == "Cyanoacetylene (H(13)CCCN v7=2)": select_where.append(species_id = '316')	
	if request.params['chemical_name'] == "Carbonyl Sulfide (OCS v=0)": select_where.append(species_id = '317')	
	if request.params['chemical_name'] == "Methanol ((13)CH3OH vt=0)": select_where.append(species_id = '319')		
	if request.params['chemical_name'] == "Cyanoacetylene (H(13)CCCN v7 = 1)": select_where.append(species_id = '321')	
	if request.params['chemical_name'] == "Cyanoallene (H2CCCHCN)": select_where.append(species_id = '323')	
	if request.params['chemical_name'] == "Formaldehyde (H2(13)CO)": select_where.append(species_id = '324')	
	if request.params['chemical_name'] == "Cyanoacetylene (HC3N v7=2)": select_where.append(species_id = '326')	
	if request.params['chemical_name'] == "Carbon trimer (C3)": select_where.append(species_id = '330')			
	if request.params['chemical_name'] == "Hydrogen Cyanide (H(13)CN v2=1)": select_where.append(species_id = '332')	
	if request.params['chemical_name'] == "Cyanobutadiyne (HC5N)": select_where.append(species_id = '337')			
	if request.params['chemical_name'] == "1,3-Butadiynyl radical (CC(13)CCH)": select_where.append(species_id = '339')	
	if request.params['chemical_name'] == "Methylene amidogen (H2CN)": select_where.append(species_id = '341')	
	if request.params['chemical_name'] == "Amidogen (NH2)": select_where.append(species_id = '351')					
	if request.params['chemical_name'] == "3-Oxo-1,2-Propadienylidene (CCCO)": select_where.append(species_id = '352')	
	if request.params['chemical_name'] == "3-Thioxo-1,2-Propadieylidene (CCCS)": select_where.append(species_id = '353')	
	if request.params['chemical_name'] == "Ethynyl (C(13)CH)": select_where.append(species_id = '355')		
	if request.params['chemical_name'] == "Sulfur Dioxide (OS(17)O)": select_where.append(species_id = '356')	
	if request.params['chemical_name'] == "Diazenylium (N(15)NH+)": select_where.append(species_id = '360')	
	if request.params['chemical_name'] == "Cyanoacetylene (HC3N v4=1)": select_where.append(species_id = '368')		
	if request.params['chemical_name'] == "1,3-Butadiynyl radical (C4H v7 = 1)": select_where.append(species_id = '369')	
	if request.params['chemical_name'] == "Cyanide Radical (C(15)N)": select_where.append(species_id = '371')	
	if request.params['chemical_name'] == "Cyanoethynyl (C(13)CCN)": select_where.append(species_id = '372')						
	if request.params['chemical_name'] == "3-Silanetetrayl-1,2-Propadienylidene  (c-SiC3)": select_where.append(species_id = '374')
	if request.params['chemical_name'] == "Hexatrienyl (l-C6H2)": select_where.append(species_id = '375')	
	if request.params['chemical_name'] == "Vinyl Alcohol (s-H2CCHOH)": select_where.append(species_id = '379')
	if request.params['chemical_name'] == "Butatrienylidene (l-C4H2)": select_where.append(species_id = '385')	
	if request.params['chemical_name'] == "Thioformaldehyde (H2C(34)S)": select_where.append(species_id = '387')	
	if request.params['chemical_name'] == "Methyltriacetylene (CH3C6H)": select_where.append(species_id = '388')
	if request.params['chemical_name'] == "Hydrochloric acid (H(37)Cl)": select_where.append(species_id = '392')
	if request.params['chemical_name'] == "Methyl Formate (CH3OCHO v=0)": select_where.append(species_id = '393')
	if request.params['chemical_name'] == "Formic Acid (t-HCOOD)": select_where.append(species_id = '400')	
	if request.params['chemical_name'] == "Methyl Cyanide (CH3(13)CN)": select_where.append(species_id = '401')
	if request.params['chemical_name'] == "Hydrogen sulfide (HDS)": select_where.append(species_id = '402')		
	if request.params['chemical_name'] == "Aluminum Monofluoride (AlF v=0)": select_where.append(species_id = '403')	
	if request.params['chemical_name'] == "Cyclopropenylidene (c-HCC(13)CH)": select_where.append(species_id = '410')	
	if request.params['chemical_name'] == "Water (H2O v=0)": select_where.append(species_id = '418')					
	if request.params['chemical_name'] == "Protonated Carbon Dioxide (HOCO+)": select_where.append(species_id = '430')	
	if request.params['chemical_name'] == "Aluminum Monochloride (Al(37)Cl v=0)": select_where.append(species_id = '431')	
	if request.params['chemical_name'] == "trans-Ethanol (t-CH3CH2OH)": select_where.append(species_id = '436')
	if request.params['chemical_name'] == "Methyl isocyanide (CH3NC)": select_where.append(species_id = '445')
	if request.params['chemical_name'] == "Cyanamide (NH2CN)": select_where.append(species_id = '449')		
	if request.params['chemical_name'] == "Magnesium Cyanide (MgCN)": select_where.append(species_id = '451')
	if request.params['chemical_name'] == "Nitrous Oxide (N2O v=0)": select_where.append(species_id = '453')
	if request.params['chemical_name'] == "Oxoethenylidene (CCO)": select_where.append(species_id = '454')	
	if request.params['chemical_name'] == "Lithium Hydride (LiH v=0)": select_where.append(species_id = '463')	
	if request.params['chemical_name'] == "Isocyanic Acid (DNCO)": select_where.append(species_id = '468')	
	if request.params['chemical_name'] == "Methyliumylidene (CH+)": select_where.append(species_id = '469')	
	if request.params['chemical_name'] == "Water (HDO)": select_where.append(species_id = '472')					
	if request.params['chemical_name'] == "Hydrogen Isocyanide (HN(13)C)": select_where.append(species_id = '473')	
	if request.params['chemical_name'] == "Phosphorous nitride (PN v=0)": select_where.append(species_id = '482')
	if request.params['chemical_name'] == "Methyl Acetylene (CH3C(13)CH)": select_where.append(species_id = '484')
	if request.params['chemical_name'] == "Ammonia ((15)NH3)": select_where.append(species_id = '485')			
	if request.params['chemical_name'] == "Methyl Acetylene ((13)CH3CCH)": select_where.append(species_id = '486')	
	if request.params['chemical_name'] == "Hydrogen Isocyanide (H(15)NC)": select_where.append(species_id = '489')	
	if request.params['chemical_name'] == "Molecular oxygen (O2 v=0)": select_where.append(species_id = '490')	
	if request.params['chemical_name'] == "Ammonia (NH3 v2=1)": select_where.append(species_id = '491')		
	if request.params['chemical_name'] == "Silicon Carbide (SiC2 v=0)": select_where.append(species_id = '492')		
	if request.params['chemical_name'] == "Cyclopropenylidene (c-HCCCH v=0)": select_where.append(species_id = '493')	
	if request.params['chemical_name'] == "Dimethyl ether (CH3OCH3)": select_where.append(species_id = '495')		
	if request.params['chemical_name'] == "Silicon monosulfide (Si(34)S v=0)": select_where.append(species_id = '497')	
	if request.params['chemical_name'] == "Sulfur Monoxide ion (SO+)": select_where.append(species_id = '504')	
	if request.params['chemical_name'] == "Cyclopropenylidene (c-HCCCD)": select_where.append(species_id = '507')	
	if request.params['chemical_name'] == "Aluminum Monochloride (AlCl v=0)": select_where.append(species_id = '521')	
	if request.params['chemical_name'] == "Hydroxyl (OH v=0)": select_where.append(species_id = '523')					
	if request.params['chemical_name'] == "3-Imino-1,2 Propadienylidene (HNCCC)": select_where.append(species_id = '528')	
	if request.params['chemical_name'] == "Acetaldehyde (CH3CHO vt=0)": select_where.append(species_id = '529')	
	if request.params['chemical_name'] == "Hydrogen fluoride (HF)": select_where.append(species_id = '535')	
	if request.params['chemical_name'] == "Phosphorus Monoxide (PO)": select_where.append(species_id = '541')	
	if request.params['chemical_name'] == "Sulfur dioxide (SO2 v2=1)": select_where.append(species_id = '546')	
	if request.params['chemical_name'] == "Ethyl Cyanide (CH3CH2CN v=0)": select_where.append(species_id = '547')	
	if request.params['chemical_name'] == "Ethyl Cyanide ((13)CH3CH2CN)": select_where.append(species_id = '549')	
	if request.params['chemical_name'] == "Vinyl Cyanide  ((13)CH2CHCN)": select_where.append(species_id = '551')	
	if request.params['chemical_name'] == "Thioxoethenylidene (C(13)CS)": select_where.append(species_id = '558')	
	if request.params['chemical_name'] == "Ethyne Isocyanide (HCCNC v=0)": select_where.append(species_id = '564')	
	if request.params['chemical_name'] == "Formamide (NH2CHO)": select_where.append(species_id = '573')			
	if request.params['chemical_name'] == "Cyanobutadiyne (HC(13)CCCCN)": select_where.append(species_id = '578')	
	if request.params['chemical_name'] == "Hydrogen sulfide (H2S)": select_where.append(species_id = '582')			
	if request.params['chemical_name'] == "Silicon monosulfide   ((29)SiS v=0)": select_where.append(species_id = '586')
	if request.params['chemical_name'] == "2,4-Pentadiynylidyne (l-C5D)": select_where.append(species_id = '589')	
	if request.params['chemical_name'] == "Nitric sulfide (NS, v=0)": select_where.append(species_id = '595')		
	if request.params['chemical_name'] == "Silicon monosulfide ((30)SiS v=0)": select_where.append(species_id = '598')	
	if request.params['chemical_name'] == "Methyl Cyanide (CH3CN v=0)": select_where.append(species_id = '606')	
	if request.params['chemical_name'] == "Nitric sulfide (N(34)S)": select_where.append(species_id = '607')	
	if request.params['chemical_name'] == "Nitrosyl hydride (HNO)": select_where.append(species_id = '618')	
	if request.params['chemical_name'] == "Methyl Cyanide (CH3C(15)N)": select_where.append(species_id = '619')	
	if request.params['chemical_name'] == "Water (H2(18)O v=0)": select_where.append(species_id = '620')			
	if request.params['chemical_name'] == "Thioxoethenylidene ((13)CCS)": select_where.append(species_id = '624')	
	if request.params['chemical_name'] == "Ethyl Cyanide (CH3CH2(13)CN)": select_where.append(species_id = '631')	
	if request.params['chemical_name'] == "Water (H2O v2=1)": select_where.append(species_id = '637')		
	if request.params['chemical_name'] == "Ammonia (NH3 v=0)": select_where.append(species_id = '638')			
	if request.params['chemical_name'] == "Vinyl Cyanide  (CH2(13)CHCN)": select_where.append(species_id = '646')	
	if request.params['chemical_name'] == "Methyl Cyanide ((13)CH3CN)": select_where.append(species_id = '651')	
	if request.params['chemical_name'] == "Silicon monosulfide   (SiS v=0)": select_where.append(species_id = '652')	
	if request.params['chemical_name'] == "Hydrochloric acid (HCl)": select_where.append(species_id = '655')
	if request.params['chemical_name'] == "Methanimine (CH2NH)": select_where.append(species_id = '664')	
	if request.params['chemical_name'] == "Hydroxyl (18OH)": select_where.append(species_id = '665')			
	if request.params['chemical_name'] == "Isocyanic Acid (HNCO v=0)": select_where.append(species_id = '673')		
	if request.params['chemical_name'] == "Cyclopropenylidene (c-H(13)CCCH)": select_where.append(species_id = '682')	
	if request.params['chemical_name'] == "Thioxoethenylidene (CC(34)S)": select_where.append(species_id = '685')	
	if request.params['chemical_name'] == "Atomic Deuterium (D)": select_where.append(species_id = '697')	
	if request.params['chemical_name'] == "Atomic Hydrogen (H)": select_where.append(species_id = '699')	
	if request.params['chemical_name'] == "Formic Acid (t-DCOOH)": select_where.append(species_id = '706')		
	if request.params['chemical_name'] == "Vinyl Cyanide  (CH2CH(13)CN)": select_where.append(species_id = '707')	
	if request.params['chemical_name'] == "Carbon Monoxide Ion (CO+)": select_where.append(species_id = '709')	
	if request.params['chemical_name'] == "Nitric oxide (NO)": select_where.append(species_id = '713')			
	if request.params['chemical_name'] == "Ethyl Cyanide (CH3(13)CH2CN)": select_where.append(species_id = '717')	
	if request.params['chemical_name'] == "Formyl Radical (HCO)": select_where.append(species_id = '727')	
	if request.params['chemical_name'] == "2-Propynal (HCCCHO)": select_where.append(species_id = '729')		
	if request.params['chemical_name'] == "Sodium Cyanide (NaCN/NaNC)": select_where.append(species_id = '736')	
	if request.params['chemical_name'] == "Cyanomethyl (CH2CN)": select_where.append(species_id = '748')			
	if request.params['chemical_name'] == "Vinyl Cyanide (CH2CHCN v=0)": select_where.append(species_id = '758')	
	if request.params['chemical_name'] == "Hydrogen sulfide (H2(34)S)": select_where.append(species_id = '776')	
	if request.params['chemical_name'] == "Silicon Carbide (Si(13)CC)": select_where.append(species_id = '791')
	if request.params['chemical_name'] == "Hydroxyl ((17)OH)": select_where.append(species_id = '801')			
	if request.params['chemical_name'] == "Hydrogen Isocyanide (D(15)NC)": select_where.append(species_id = '808')		
	if request.params['chemical_name'] == "Methanol (CH3OD)": select_where.append(species_id = '813')		
	if request.params['chemical_name'] == "Acetone ((CH3)2CO v=0)": select_where.append(species_id = '819')	
	if request.params['chemical_name'] == "Methylamine (CH3NH2)": select_where.append(species_id = '828')			
	if request.params['chemical_name'] == "Silicon monosulfide (Si(33)S v=0)": select_where.append(species_id = '833')	
	if request.params['chemical_name'] == "Methyl Mercaptan (CH3SH v=0)": select_where.append(species_id = '841')
	if request.params['chemical_name'] == "Silicon Carbide ((30)SiC2)": select_where.append(species_id = '849')
	if request.params['chemical_name'] == "Propenal (t-CH2CHCHO)": select_where.append(species_id = '853')	
	if request.params['chemical_name'] == "Silicon Carbide ((29)SiC2)": select_where.append(species_id = '872')
	if request.params['chemical_name'] == "Methanol (CH2DOH)": select_where.append(species_id = '874')	
	if request.params['chemical_name'] == "Formamide (NH2(13)CHO)": select_where.append(species_id = '875')			
	if request.params['chemical_name'] == "Magnesium Isocyanide ((26)MgNC)": select_where.append(species_id = '885')	
	if request.params['chemical_name'] == "Methanol (CH3(18)OH)": select_where.append(species_id = '892')		
	if request.params['chemical_name'] == "Methyl Cyanide (CH3CN v8=1)": select_where.append(species_id = '1041')	
	if request.params['chemical_name'] == "Methanol (CHD2OH)": select_where.append(species_id = '906')						
	if request.params['chemical_name'] == "Silicon monosulfide   ((30)Si(34)S v=0)": select_where.append(species_id = '934')	
	if request.params['chemical_name'] == "Acetic Acid (CH3COOH v=0)": select_where.append(species_id = '941')	
	if request.params['chemical_name'] == "Methylidyne (CH 2P3/2)": select_where.append(species_id = '963')	
	if request.params['chemical_name'] == "Carbon Monosulfide (CS v=1)": select_where.append(species_id = '994')
	if request.params['chemical_name'] == "Hydrogen Cyanide (HCN v2=2)": select_where.append(species_id = '964')
	if request.params['chemical_name'] == "Hydrogen Cyanide (HCN v3=1)": select_where.append(species_id = '966')
	if request.params['chemical_name'] == "Hydrogen Cyanide (HCN v1=1)": select_where.append(species_id = '967')	
	if request.params['chemical_name'] == "Hydrogen Isocyanide (HNC v2=1)": select_where.append(species_id = '971')		
	if request.params['chemical_name'] == "Hydrogen Recombination Line (H(alpha))": select_where.append(species_id = '1154')
	if request.params['chemical_name'] == "Methanol (CH3OH vt=1)": select_where.append(species_id = '984')	
	if request.params['chemical_name'] == "Methanol ((13)CH3OH vt=1)": select_where.append(species_id = '985')
	if request.params['chemical_name'] == "Methanol (CD3OH)": select_where.append(species_id = '986')	
	if request.params['chemical_name'] == "Carbon Monoxide (CO v=1)": select_where.append(species_id = '990')	
	if request.params['chemical_name'] == "Carbon Monosulfide (C(34)S v=1)": select_where.append(species_id = '1001')
	if request.params['chemical_name'] == "Acetaldehyde (CH3CHO vt=1)": select_where.append(species_id = '1042')	
	if request.params['chemical_name'] == "Acetaldehyde (CH3CHO vt=2)": select_where.append(species_id = '1043')	
	if request.params['chemical_name'] == "gauche-Ethanol (g-CH3CH2OH)": select_where.append(species_id = '1044')
	if request.params['chemical_name'] == "Cyanoacetylene (HC3N v7=3)": select_where.append(species_id = '1045')	
	if request.params['chemical_name'] == "Cyanoacetylene (HC3N v5=1)": select_where.append(species_id = '1046')	
	if request.params['chemical_name'] == "Vinyl Cyanide (CH2CHCN v11=1)": select_where.append(species_id = '1048')
	if request.params['chemical_name'] == "Vinyl Cyanide (CH2CHCN v11=2)": select_where.append(species_id = '1049')
	if request.params['chemical_name'] == "Vinyl Cyanide (CH2CHCN v15=1)": select_where.append(species_id = '1050')
	if request.params['chemical_name'] == "Ethyl Cyanide (CH3CH2CN v=1)": select_where.append(species_id = '1052')
	if request.params['chemical_name'] == "Propanal (CH3CH2CHO)": select_where.append(species_id = '1053')		
	if request.params['chemical_name'] == "1,3-Butadiynyl anion (C4H-)": select_where.append(species_id = '1055')	
	if request.params['chemical_name'] == "1,3,5,7-Octatetraynyl anion (C8H-)": select_where.append(species_id = '1057')	
	if request.params['chemical_name'] == "Hydrogen sulfide (D2S)": select_where.append(species_id = '1076')		
	if request.params['chemical_name'] == "Silicon Monoxide (SiO v=1)": select_where.append(species_id = '1089')		
	if request.params['chemical_name'] == "Silicon Monoxide (SiO v=2)": select_where.append(species_id = '1090')
	if request.params['chemical_name'] == "Silicon Monoxide (SiO v=3)": select_where.append(species_id = '1091')
	if request.params['chemical_name'] == "Silicon Monoxide (SiO v=4)": select_where.append(species_id = '1092')
	if request.params['chemical_name'] == "Silicon Monoxide (SiO v=5)": select_where.append(species_id = '1093')
	if request.params['chemical_name'] == "Silicon Monoxide (SiO v=6)": select_where.append(species_id = '1094')	
	if request.params['chemical_name'] == "Silicon Monoxide ((29)SiO v=1)": select_where.append(species_id = '1095')
	if request.params['chemical_name'] == "Silicon Monoxide ((29)SiO v=2)": select_where.append(species_id = '1096')
	if request.params['chemical_name'] == "Silicon Monoxide ((30)SiO v=1)": select_where.append(species_id = '1100')
	if request.params['chemical_name'] == "Silicon Monoxide ((30)SiO v=2)": select_where.append(species_id = '1101')
	if request.params['chemical_name'] == "Silicon monosulfide (SiS v=1)": select_where.append(species_id = '1112')
	if request.params['chemical_name'] == "Silicon monosulfide (SiS v=2)": select_where.append(species_id = '1113')
	if request.params['chemical_name'] == "Silicon monosulfide (SiS v=3)": select_where.append(species_id = '1114')
	if request.params['chemical_name'] == "Acetamide (CH3CONH2)": select_where.append(species_id = '1173')				
	if request.params['chemical_name'] == "Hydrogen Recombination Line (H(beta))": select_where.append(species_id = '1155')
	if request.params['chemical_name'] == "Hydrogen Recombination Line (H(gamma))": select_where.append(species_id = '1156')
	if request.params['chemical_name'] == "Hydrogen Recombination Line (H(delta))": select_where.append(species_id = '1157')	
	if request.params['chemical_name'] == "Hydrogen Recombination Line (H(epsilon))": select_where.append(species_id = '1158')
	if request.params['chemical_name'] == "Hydrogen Recombination Line (H(zeta))": select_where.append(species_id = '1159')
	if request.params['chemical_name'] == "Helium Recombination Line (He(alpha))": select_where.append(species_id = '1160')
	if request.params['chemical_name'] == "Helium Recombination Line (He(beta))": select_where.append(species_id = '1161')
	if request.params['chemical_name'] == "Helium Recombination Line (He(gamma))": select_where.append(species_id = '1162')
	if request.params['chemical_name'] == "Helium Recombination Line (He(delta))": select_where.append(species_id = '1163')
	if request.params['chemical_name'] == "Carbon Recombination Line (C(alpha))": select_where.append(species_id = '1164')
	if request.params['chemical_name'] == "Carbon Recombination Line (C(beta))": select_where.append(species_id = '1165')
	if request.params['chemical_name'] == "Carbon Recombination Line (C(gamma))": select_where.append(species_id = '1166')
	if request.params['chemical_name'] == "Hydrogen Cyanide (HCN v2=4)": select_where.append(species_id = '1179')		
	if request.params['chemical_name'] == "Hydrogen Cyanide (HCN v2=1^1-v2=4^0)": select_where.append(species_id = '1180')
	if request.params['chemical_name'] == "Formylium (HCO+ v=0)": select_where.append(species_id = '15')				
	if request.params['chemical_name'] == "Cyanoacetylene (HC3N v5=1,v7=1)": select_where.append(species_id = '1198')
	if request.params['chemical_name'] == "Cyanoacetylene (HC3N v6=1, v7=2)": select_where.append(species_id = '1199')
	if request.params['chemical_name'] == "Cyanoacetylene (HC3N v6=2)": select_where.append(species_id = '1201')	
	if request.params['chemical_name'] == "Cyanoacetylene (HC3N v7=4)": select_where.append(species_id = '1202')
	if request.params['chemical_name'] == "Isocyanic Acid (HNCO v4=1)": select_where.append(species_id = '1244')
	if request.params['chemical_name'] == "Isocyanic Acid (HNCO v5=1)": select_where.append(species_id = '1245')
	if request.params['chemical_name'] == "Isocyanic Acid (HNCO v6=1)": select_where.append(species_id = '1246')
	if request.params['chemical_name'] == "Cyanoethynylide ion (C3N-)": select_where.append(species_id = '1264')
	if request.params['chemical_name'] == "Silicon Carbide (SiC2 v3=1)": select_where.append(species_id = '1268')
	if request.params['chemical_name'] == "Phosphapropynylidyne (CCP)": select_where.append(species_id = '1274')	
	if request.params['chemical_name'] == "Aminoacetonitrile (H2NCH2CN)": select_where.append(species_id = '1277')
	if request.params['chemical_name'] == "Acetone ((CH3)2CO vt=1)": select_where.append(species_id = '1281')		
	if request.params['chemical_name'] == "Cyanobutadiynylide anion (C5N-)": select_where.append(species_id = '1308')
	if request.params['chemical_name'] == "Methyl Formate (CH3OCHO v=1)": select_where.append(species_id = '1333')	
	if request.params['chemical_name'] == "Fulminic acid (HCNO)": select_where.append(species_id = '1352')		
	if request.params['chemical_name'] == "Cyanic acid (HOCN)": select_where.append(species_id = '1353')	
	if request.params['chemical_name'] == "Atomic Carbon (CII)": select_where.append(species_id = '1364')	
	if request.params['chemical_name'] == "Atomic Helium (3He+)": select_where.append(species_id = '1365')	
	if request.params['chemical_name'] == "Atomic Nitrogen (NII)": select_where.append(species_id = '1366')	
	if request.params['chemical_name'] == "Atomic Oxygen (OI)": select_where.append(species_id = '1367')	
	if request.params['chemical_name'] == "Atomic Oxygen (OIII)": select_where.append(species_id = '1368')	
	if request.params['chemical_name'] == "Atomic Carbon (13CII(13))": select_where.append(species_id = '1378')	
	if request.params['chemical_name'] == "ortho-Oxidaniumyl (o-H2O+)": select_where.append(species_id = '1397')	
	if request.params['chemical_name'] == "para-Oxidaniumyl (p-H3O+)": select_where.append(species_id = '1398')	
	if request.params['chemical_name'] == "Propynylidynium (C3H+)": select_where.append(species_id = '1413')		
	if request.params['chemical_name'] == "Cyanomethanimine (E-HNCHCN)": select_where.append(species_id = '1416')
	
	
	req_chemical_name = request.params['chemical_name']
	req_chemical_name = req_chemical_name.lower()

	if req_chemical_name == "h2o": 
		select_where.append("chemical_name = 'Water'")
	
	if req_chemical_name == "carbon": 
		select_where.append("chemical_name = 'atomic carbon'")
	
	if req_chemical_name == "nitrogen": 
		select_where.append("chemical_name = 'atomic nitrogen'")
	
	if req_chemical_name == "oxygen": 
		select_where.append("chemical_name = 'atomic oxygen'")
	
	if req_chemical_name == "co": 
		select_where.append("chemical_name = 'carbon monoxide'")
	
	if req_chemical_name == "nh3": 
		select_where.append("chemical_name = 'ammonia'")
	
	if req_chemical_name == "ch3oh": 
		select_where.append("chemical_name = 'methanol'")
	
	if req_chemical_name == "o2": 
		select_where.append("chemical_name = 'molecular oxygen'")
	
	if req_chemical_name == "h": 
		select_where.append("chemical_name = 'hydrogen recombination line'")
	
	if req_chemical_name == "hcn" or req_chemical_name == "dcn": 
		select_where.append("chemical_name = 'hydrogen cyanide'")
	
	if req_chemical_name == "hco+" or req_chemical_name == "dco+": 
		select_where.append("chemical_name = 'formylium'")
	
	if req_chemical_name == "cs": 
		select_where.append("chemical_name = 'carbon monosulfide'")
	
	if req_chemical_name == "oh": 
		select_where.append("chemical_name = 'hydroxyl'")
		
	# Red Shift preprocessing
	
	req_z = request.params['z']
	try:
		float(req_z)
	except:
		req_z = 0.0
		
	
	# Telescope Bands
	
	req_band = request.params['band']
	if (req_band !='any'):  
		if (req_band == 'alma3'):
			req_from =  84000 * (1 + req_z)
			req_to   = 116000 * (1 + req_z)
		
		elif (req_band == 'alma4'):
			req_from = 125000 * (1 + req_z)
			req_to   = 163000 * (1 + req_z)
		
		elif (req_band == 'alma5'):
			req_from = 163000 * (1 + req_z)
			req_to   = 211000 * (1 + req_z)
		
		elif (req_band == 'alma6'):
			req_from = 211000 * (1 + req_z)
			req_to   = 275000 * (1 + req_z)
		
		elif (req_band == 'alma7'):
			req_from = 275000 * (1 + req_z)
			req_to   = 373000 * (1 + req_z)
		
		elif (req_band == 'alma8'):
			req_from = 385000 * (1 + req_z)
			req_to   = 500000 * (1 + req_z)
		
		elif (req_band == 'alma9'):
			req_from = 602000 * (1 + req_z)
			req_to   = 720000 * (1 + req_z)
		
		elif (req_band == 'alma10'):
			req_from = 787000 * (1 + req_z)
			req_to   = 950000 * (1 + req_z)
		
		elif (req_band == 'pf1'):
			req_from = 290 * (1 + req_z)
			req_to   = 920 * (1 + req_z)
		
		elif (req_band == 'pf2'):
			req_from = 910 * (1 + req_z)
			req_to   = 1230 * (1 + req_z)
		
		elif (req_band == 'l'):
			req_from = 1000 * (1 + req_z)
			req_to   = 2000 * (1 + req_z)
		
		elif (req_band == 's'):
			req_from = 1700 * (1 + req_z)
			req_to   = 4000 * (1 + req_z)
		
		elif (req_band == 'c'):
			req_from = 3900 * (1 + req_z)
			req_to   = 8000 * (1 + req_z)
		
		elif (req_band == 'x'):
			req_from = 8000 * (1 + req_z)
			req_to   = 12000 * (1 + req_z)
		
		elif (req_band == 'ku'):
			req_from = 12000 * (1 + req_z)
			req_to   = 18000 * (1 + req_z)
		
		elif (req_band == 'kfpa'):
			req_from = 18000 * (1 + req_z)
			req_to   = 27500 * (1 + req_z)
		
		elif (req_band == 'k'):
			req_from = 18000 * (1 + req_z)
			req_to   = 26500 * (1 + req_z)
		
		elif (req_band == 'ka'):
			req_from = 26000 * (1 + req_z)
			req_to   = 40000 * (1 + req_z)
		
		elif (req_band == 'q'):
			req_from = 38000 * (1 + req_z)
			req_to   = 50000 * (1 + req_z)
		
		elif (req_band == 'w'):
			req_from = 67000 * (1 + req_z)
			req_to   = 93300 * (1 + req_z)
		
		elif (req_band == 'mustang'):
			req_from = 80000 * (1 + req_z)
			req_to   = 100000 * (1 + req_z)
		else:
			pass
	
	
	################################################
	# Energy range search
	################################################
	
	req_energy_range_from = request.params['energy_range_from']
	req_energy_range_to = request.params['energy_range_to']
	req_energy_range_type =request.params['energy_range_type']
	try:
		float(req_energy_range_from)
		try:
			float(req_energy_range_to)
			
			#	Swap the energy_range_from and energy_range_to values if energy_range_from is greater than energy_range_to
			if req_energy_range_from > req_energy_range_to:
				tmp = req_energy_range_from
				req_energy_range_from = eto
				req_energy_range_to = tmp
		except:
			pass
	except:
		pass
	
	if (req_energy_range_type == 'el_cm1'):
		try:
			float(req_energy_range_from)
			select_where.append("lower_state_energy >= '" + req_energy_range_from + "'")
		except:
			print 'energy range "from" non-numeric'
		
		try:
			float(req_energy_range_to)
			select_where.append("lower_state_energy <= '" + req_energy_range_to + "'")
		except:
			print 'energy range "to" non-numeric'

	if (req_energy_range_type == 'el_k'):
		try:
			float(req_energy_range_from)
			select_where.append("lower_state_energy_K >= '" + req_energy_range_from + "'")
		except:
			print 'energy range "from" non-numeric'
		
		try:
			float(req_energy_range_to)
			select_where.append("lower_state_energy_K <= '" + req_energy_range_to + "'")
		except:
			print 'energy range "to" non-numeric'
	
	

	#if (has_value(req_lill_cdms_jpl)):
	#	array_push(select_where, ('intintensity > %s' % mysql_real_escape_string(req_lill_cdms_jpl)))
	#	array_push(select_where, '(ll_id=10 OR ll_id=12)')
	#

	#if (has_value(req_lill_sijmu2)):
	#	array_push(select_where, ('sijmu2 > %s' % mysql_real_escape_string(req_lill_sijmu2)))
	#	array_push(select_where, 'll_id in (10, 12, 14)')
	

	#if (has_value(req_lill_aij)):
	#	array_push(select_where, ('aij > %s' % mysql_real_escape_string(req_lill_aij)))
	#	array_push(select_where, 'll_id in (10, 12, 14)')
	
	#req_lill_cdms_jpl = ''
	#req_lill_sijmu2 = ''
	#req_lill_aij = ''
	
	#if request.params['lill_cdms_jpl'] != '':
	#	req_lill_cdms_jpl = request.params['lill_cdms_jpl']
	
	#if request.params['lill_sijmu2'] != '':
	#	req_lill_sijmu2 = request.params['lill_sijmu2']
	
	#if request.params['lill_aij'] != '':
	#	req_lill_aij = request.params['lill_aij']
	
	req_from	 = req_to	 = 0.0
	req_from2	 = req_to2	 = 0.0
	req_from3	 = req_to3	 = 0.0
	req_from4	 = req_to4	 = 0.0
	req_from5	 = req_to5	 = 0.0
	req_from6	 = req_to6	 = 0.0
	req_from7	 = req_to7	 = 0.0
	req_from8	 = req_to8	 = 0.0
	req_from9	 = req_to9	 = 0.0
	req_from10	 = req_to10	 = 0.0
	req_from11	 = req_to11	 = 0.0
	req_from12	 = req_to12	 = 0.0
	req_from13	 = req_to13	 = 0.0
	req_from14	 = req_to14	 = 0.0
	req_from15	 = req_to15	 = 0.0
	req_from16	 = req_to16	 = 0.0
	req_from17	 = req_to17	 = 0.0
	req_from18	 = req_to18  = 0.0
	req_from19	 = req_to19	 = 0.0
	req_from20	 = req_to20	 = 0.0
	
	if request.params['from'] == '':
		print 'asdf'
	
	exec "try:\n if request.params['req_from'] == '': pass\n else: req_from = request.params['req_from'] \nexcept: pass"
	
	req_from = request.params['from']
	req_to = request.params['to']
	req_frequency_units = request.params['frequency_units']	
	try:
		float(req_to)
		try:
			float(req_from)
			# Swap the from and to values if from is greater than to
			if (req_from > req_to):
				
		 		tmp = req_from
		 		req_from = req_to
		 		req_to = tmp
		 	
		except:
			pass
	except:
		pass

	req_from2 = request.params['from2']
	req_to2 = request.params['to2']
	try:
		float(req_to2)
		try:
			float(req_from2)
			# Swap the from and to values if from is greater than to
			if (req_from2 > req_to2):
				
		 		tmp = req_from2
		 		req_from2 = req_to
		 		req_to2 = tmp
		 	
		except:
			pass
	except:
		pass
	
#-- 2 to 20 from/to variables ------------------
	
	req_top20 = '' 	
	if request.params['top20'] != '': 
		req_top20 = request.params['top20'] 
		
	req_no_potential = ''
	if request.params['no_potential'] != '': 
		req_no_potential = request.params['no_potential']
		
	base = os.path.dirname(__file__)
	
	file_path = base + '/templates/query_submitted_basic.pt'
	mdate = time.ctime(os.path.getmtime(file_path))
	
	
	dict = {
		'err_status' : False,
		'err_message' : '',
		'modifieddate' : mdate
	}
	
	
	#if ((req_display_recomb == '' or req_display_recomb is None) and 
	#	(req_display_cdms == '' or req_display_cdms is None) and 
	#	(req_display_jpl == '' or req_display_jpl is None) and 
	#	(req_display_lovas == '' or req_display_lovas is None) and 
	#	(req_display_slaim == '' or req_display_slaim is None) and 
	#	(req_display_toyama == '' or req_display_toyama is None) and 
	#	(req_display_osu == '' or req_display_osu is None) and 
	#	(req_display_lisa == '' or req_display_lisa is None) and 
	#	(req_display_rfi == '' or req_display_rfi is None)):
	#	dict['err_status'] = True
	#	dict['err_message'] = 'Please select a linelist catalogue'
	#	return {'retval' : dict}
	
	req_fromz = req_from / (1.0 + float(req_z))
	req_toz = req_to / (1.0 + float(req_z))
	req_from = req_from * (1.0 + float(req_z))
	req_to = req_to * (1.0 + float(req_z))
	req_from2z = req_from2 / (1.0 + float(req_z))
	req_to2z = req_to2 / (1.0 + float(req_z))
	req_from2 = req_from2 * (1.0 + float(req_z))
	req_to2 = req_to2 * (1.0 + float(req_z))
	req_from3z = req_from3 / (1.0 + float(req_z))
	req_to3z = req_to3 / (1.0 + float(req_z))
	req_from3 = req_from3 * (1.0 + float(req_z))
	req_to3 = req_to3 * (1.0 + float(req_z))
	#req_from4z = unicodedata.numeric(req_from4) / (1.0 + float(req_z))
	#req_to4z = unicodedata.numeric(req_to4) / (1.0 + float(req_z))
	#req_from4 = unicodedata.numeric(req_from4) * (1.0 + float(req_z))
	#req_to4 = unicodedata.numeric(req_to4) * (1.0 + float(req_z))
	#req_from5z = unicodedata.numeric(req_from5) / (1.0 + float(req_z))
	#req_to5z = unicodedata.numeric(req_to5) / (1.0 + float(req_z))
	#req_from5 = unicodedata.numeric(req_from5) * (1.0 + float(req_z))
	#req_to5 = unicodedata.numeric(req_to5) * (1.0 + float(req_z))
	#req_from6z = unicodedata.numeric(req_from6) / (1.0 + float(req_z))
	#req_to6z = unicodedata.numeric(req_to6) / (1.0 + float(req_z))
	#req_from6 = unicodedata.numeric(req_from6) * (1.0 + float(req_z))
	#req_to6 = unicodedata.numeric(req_to6) * (1.0 + float(req_z))
	#req_from7z = unicodedata.numeric(req_from7) / (1.0 + float(req_z))
	#req_to7z = unicodedata.numeric(req_to7) / (1.0 + float(req_z))
	#req_from7 = unicodedata.numeric(req_from7) * (1.0 + float(req_z))
	#req_to7 = unicodedata.numeric(req_to7) * (1.0 + float(req_z))
	#req_from8z = unicodedata.numeric(req_from8) / (1.0 + float(req_z))
	#req_to8z = unicodedata.numeric(req_to8) / (1.0 + float(req_z))
	#req_to8 = unicodedata.numeric(req_to8) * (1.0 + float(req_z))
	#req_from9z = unicodedata.numeric(req_from9) / (1.0 + float(req_z))
	#req_to9z = unicodedata.numeric(req_to9) / (1.0 + float(req_z))
	#req_from9 = unicodedata.numeric(req_from9) * (1.0 + float(req_z))
	#req_to9 = unicodedata.numeric(req_to9) * (1.0 + float(req_z))
	#req_from10z = unicodedata.numeric(req_from10) / (1.0 + float(req_z))
	#req_from10 = unicodedata.numeric(req_from10) * (1.0 + float(req_z))
	#req_to10 = unicodedata.numeric(req_to10) * (1.0 + float(req_z))
	#req_from11z = unicodedata.numeric(req_from11) / (1.0 + float(req_z))
	#req_from12z = float(req_from12) / (1.0 + float(req_z))
	#req_to12z = float(req_to12) / (1.0 + float(req_z))
	#req_to12 = float(req_to12) * (1.0 + float(req_z))
	#req_from13z = float(req_from13) / (1.0 + float(req_z))
	#req_to13z = float(req_to13) / (1.0 + float(req_z))
	#req_from13 = float(req_from13) * (1.0 + float(req_z))
	#req_to13 = float(req_to13) * (1.0 + float(req_z))
	#req_from14z = float(req_from14) / (1.0 + float(req_z))
	#req_to14z = float(req_to14) / (1.0 + float(req_z))
	#req_from14 = float(req_from14) * (1.0 + float(req_z))
	#req_to14 = float(req_to14) * (1.0 + float(req_z))
	#req_from15z = float(req_from15) / (1.0 + float(req_z))
	#req_to15z = float(req_to15) / (1.0 + float(req_z))
	#req_from15 = float(req_from15) * (1.0 + float(req_z))
	##req_to16z = float(req_to16) / (1.0 + float(req_z))
	#req_from16 = float(req_from16) * (1.0 + float(req_z))
	#req_to16 = float(req_to16) * (1.0 + float(req_z))
	#req_from17z = float(req_from17) / (1.0 + float(req_z))
	#req_to17z = float(req_to17) / (1.0 + float(req_z))
	#req_from17 = float(req_from17) * (1.0 + float(req_z))
	#req_to17 = float(req_to17) * (1.0 + float(req_z))
	#req_from18z = float(req_from18) / (1.0 + float(req_z))
	#req_to18z = float(req_to18) / (1.0 + float(req_z))
	#req_from18 = float(req_from18) * (1.0 + float(req_z))
	#req_to18 = float(req_to18) * (1.0 + float(req_z))
	#req_from19z = float(req_from19) / (1.0 + float(req_z))
	#req_to19z = float(req_to19) / (1.0 + float(req_z))
	##req_from20z = float(req_from20) / (1.0 + float(req_z))
	#req_to20z = float(req_to20) / (1.0 + float(req_z))
	#req_from20 = float(req_from20) * (1.0 + float(req_z))
	#req_to20 = float(req_to20) * (1.0 + float(req_z))
	
	#array_push(select_where, "m.species_id = s.species_id")
	#array_push(select_where, "s.SPLAT_ID > 100")

	
	################################################
	# Search top20s
	################################################

	select_where = array_push_if(select_where, "s.%s=1" % req_top20, has_value(req_top20))
	select_where = array_push_if(select_where, "potential != 1", has_value(req_no_potential))
	select_where = array_push_if(select_where, "probable != 1", has_value(req_no_probable))
	select_where = array_push_if(select_where, "known_ast_molecules != 1", has_value(req_known))

	#select_where = array_push_if(select_where, "Lovas_NRAO = 1", has_value(req_include_only_nrao']))
	select_where = array_push_if(select_where, "((frequency > 0 and uncertainty <= 50) or (measfreq > 0 and measerrfreq <= 50))", has_value(req_fel))
	select_where = array_push_if(select_where, "(resolved_QNs NOT LIKE '%F=%')", has_value(req_noHFS))
	
	select_where = array_push_if(select_where, "intintensity>=%s" % mysql_real_escape_string(req_il), has_value(req_intl))	
	  
	select_where = array_push_if(select_where, "quantum_numbers like '%s'" % mysql_real_escape_string(tran), has_value(req_trans))
    
	if (has_value(req_data_version)):
		select_where = array_push_if(select_where, "m.`v1.0` = 1", req_data_version == "v1.0")
		select_where = array_push_if(select_where, "m.`v2.0` = 2", req_data_version == "v2.0")
    
	lines = array_push_if(lines, "10", has_value(req_display_cdms))
	lines = array_push_if(lines, "11", has_value(req_display_lovas))
	lines = array_push_if(lines, "12", has_value(req_display_jpl))
	lines = array_push_if(lines, "14", has_value(req_display_slaim))
	lines = array_push_if(lines, "15", has_value(req_display_recomb))
	lines = array_push_if(lines, "16", has_value(req_display_toyama))
	lines = array_push_if(lines, "17", has_value(req_display_osu))
	lines = array_push_if(lines, "18", has_value(req_display_osu))
	lines = array_push_if(lines, "19", has_value(req_display_rfi))


	lines_clean = lines
	array_map("mysql_real_escape_string", lines_clean)
	select_where = array_push(select_where, "ll_id in (" + ", ".join(lines_clean) + ")")


	if (req_from != '' and req_to != ''):
		if (req_frequency_units == 'Hz'):
			req_from = req_from / 1000000
			req_to = req_to / 1000000
		
		elif (req_frequency_units == 'KHz'):
			req_from = req_from / 1000
			req_to = req_to / 1000
		
		elif (req_frequency_units == 'MHz'):
			req_from = req_from * 1
			req_to = req_to * 1
		
		elif (req_frequency_units == 'GHz'):
			req_from = req_from * 1000
			req_to = req_to * 1000
		
		elif (req_frequency_units == 'THz'):
			req_from = req_from * 1000000
			req_to = req_to * 1000000
		
		elif (req_frequency_units == 'a'):
			req_from = 2.99792458 * pow(10,12) / req_fromz
			req_to = 2.99792458 * pow(10,12) / req_toz
		
		elif (req_frequency_units == 'nm'):
			req_from = 2.99792458 * pow(10,11) / req_fromz
			req_to = 2.99792458 * pow(10,11) / req_toz
		
		elif (req_frequency_units == 'mum'):
			req_from = 2.99792458 * pow(10,8) / req_fromz
			req_to = 2.99792458 * pow(10,8) / req_toz
		
		elif (req_frequency_units == 'mm'):
			req_from = 2.99792458 * pow(10,5) / req_fromz
			req_to = 2.99792458 * pow(10,5) / req_toz
		
		elif (req_frequency_units == 'cm'):
			req_from = 2.99792458 * pow(10,4) / req_fromz
			req_to = 2.99792458 * pow(10,4) / req_toz
		
		else:
			req_from = 2.99792458 * pow(10,2) / req_fromz
			req_to = 2.99792458 * pow(10,2) / req_toz
		
	
	elif (req_from != '' and req_to == ''):
		if (req_frequency_units == 'Hz'):
			req_from = req_from / 1000000
			req_to = 1 * pow(10,50)
		
		elif (req_frequency_units == 'KHz'):
			req_from = req_from / 1000
			req_to = 1 * pow(10,50)
		
		elif (req_frequency_units == 'MHz'):
			req_from = req_from * 1
			req_to = 1 * pow(10,50)
		
		elif (req_frequency_units == 'GHz'):
			req_from = req_from * 1000
			req_to = 1 * pow(10,50)
		
		elif (req_frequency_units == 'THz'):
			req_from = req_from * 1000000
			req_to = 1 * pow(10,50)
		
		elif (req_frequency_units == 'a'):
			req_from = 0.0
#			req_to = 2.99792458 * pow(10,12) / req_toz
			req_to = 2.99792458 * pow(10,12)
		
		elif (req_frequency_units == 'nm'):
			req_from = 0.0
			req_to = 2.99792458 * pow(10,11) / req_toz
		
		elif (req_frequency_units == 'mum'):
			req_from = 0.0
			req_to = 2.99792458 * pow(10,8) / req_toz
		
		elif (req_frequency_units == 'mm'):
			req_from = 0.0
			req_to = 2.99792458 * pow(10,5) / req_toz
		
		elif (req_frequency_units == 'cm'):
			req_from = 0.0
			req_to = 2.99792458 * pow(10,4) / req_toz
		
		else:
			req_from = 0.0
			req_to = 2.99792458 * pow(10,2) / req_toz
		
	
	elif (req_from == '' and req_to != ''):
		if (req_frequency_units == 'Hz'):
			req_from = 0.0
			req_to = req_to / 1000000
		
		elif (req_frequency_units == 'KHz'):
			req_from = 0.0
			req_to = req_to / 1000
		
		elif (req_frequency_units == 'MHz'):
			req_from = 0.0
			req_to = req_to * 1
		
		elif (req_frequency_units == 'GHz'):
			req_from = 0.0
			req_to = req_to * 1000
		
		elif (req_frequency_units == 'THz'):
			req_from = 0.0
			req_to = req_to * 1000000
		
		elif (req_frequency_units == 'a'):
			req_from = 2.99792458 * pow(10,12) / req_fromz
			req_to = 1 * pow(10,50)
		
		elif (req_frequency_units == 'nm'):
			req_from = 2.99792458 * pow(10,11) / req_fromz
			req_to = 1 * pow(10,50)
		
		elif (req_frequency_units == 'mum'):
			req_from = 2.99792458 * pow(10,8) / req_fromz
			req_to = 1 * pow(10,50)
		
		elif (req_frequency_units == 'mm'):
			req_from = 2.99792458 * pow(10,5) / req_fromz
			req_to = 1 * pow(10,50)
		
		elif (req_frequency_units == 'cm'):
			req_from = 2.99792458 * pow(10,4) / req_fromz
			req_to = 1 * pow(10,50)
		
		else:
			req_from = 2.99792458 * pow(10,2) / req_fromz
			req_to = 1 * pow(10,50)
		
	
	else:
		req_from = req_from * 1
		req_to = req_to * 1
	
	

	if (req_from2 != '' or req_to2 != ''):
		if (req_frequency_units == 'Hz'):
			req_from2 = req_from2 / 1000000
			req_to2 = req_to2 / 1000000
		
		elif (req_frequency_units == 'KHz'):
			req_from2 = req_from2 / 1000
			req_to2 = req_to2 / 1000
		
		elif (req_frequency_units == 'MHz'):
			req_from2 = req_from2 * 1
			req_to2 = req_to2 * 1 
		
		elif (req_frequency_units == 'GHz'):
			req_from2 = req_from2 * 1000
			req_to2 = req_to2 * 1000
		
		elif (req_frequency_units == 'THz'):
			req_from2 = req_from2 * 1000000
			req_to2 = req_to2 * 1000000
		
		elif (req_frequency_units == 'a'):
			req_from2 = 2.99792458 * pow(10,12) / req_from2z
			req_to2 = 2.99792458 * pow(10,12) / req_to2z
		
		elif (req_frequency_units == 'nm'):
			req_from2 = 2.99792458 * pow(10,11) / req_from2z
			req_to2 = 2.99792458 * pow(10,11) / req_to2z
		
		elif (req_frequency_units == 'mum'):
			req_from2 = 2.99792458 * pow(10,8) / req_from2z
			req_to2 = 2.99792458 * pow(10,8) / req_to2z
		
		elif (req_frequency_units == 'mm'):
			req_from2 = 2.99792458 * pow(10,5) / req_from2z
			req_to2 = 2.99792458 * pow(10,5) / req_to2z
		
		elif (req_frequency_units == 'cm'):
			req_from2 = 2.99792458 * pow(10,4) / req_from2z
			req_to2 = 2.99792458 * pow(10,4) / req_to2z
		
		else:
			req_from2 = 2.99792458 * pow(10,2) / req_from2z
			req_to2 = 2.99792458 * pow(10,2) / req_to2z
		
	

	if (req_from3 != '' or req_to3 != ''):
		if (req_frequency_units == 'Hz'):
			req_from3 = req_from3 / 1000000
			req_to3 = req_to3 / 1000000
		
		elif (req_frequency_units == 'KHz'):
			req_from3 = req_from3 / 1000
			req_to3 = req_to3 / 1000
		
		elif (req_frequency_units == 'MHz'):
			req_from3 = req_from3 * 1
			req_to3 = req_to3 * 1 
		
		elif (req_frequency_units == 'GHz'):
			req_from3 = req_from3 * 1000
			req_to3 = req_to3 * 1000
		
		elif (req_frequency_units == 'THz'):
			req_from3 = req_from3 * 1000000
			req_to3 = req_to3 * 1000000
		
		elif (req_frequency_units == 'a'):
			req_from3 = 2.99792458 * pow(10,12) / req_from3z
			req_to3 = 2.99792458 * pow(10,12) / req_to3z
		
		elif (req_frequency_units == 'nm'):
			req_from3 = 2.99792458 * pow(10,11) / req_from3z
			req_to3 = 2.99792458 * pow(10,11) / req_to3z
		
		elif (req_frequency_units == 'mum'):
			req_from3 = 2.99792458 * pow(10,8) / req_from3z
			req_to3 = 2.99792458 * pow(10,8) / req_to3z
		
		elif (req_frequency_units == 'mm'):
			req_from3 = 2.99792458 * pow(10,5) / req_from3z
			req_to3 = 2.99792458 * pow(10,5) / req_to3z
		
		elif (req_frequency_units == 'cm'):
			req_from3 = 2.99792458 * pow(10,4) / req_from3z
			req_to3 = 2.99792458 * pow(10,4) / req_to3z
		
		else:
			req_from3 = 2.99792458 * pow(10,2) / req_from3z
			req_to3 = 2.99792458 * pow(10,2) / req_to3z
		
	

	if (req_from4 != '' or req_to4 != ''):
		if (req_frequency_units == 'Hz'):
			req_from4 = req_from4 / 1000000
			req_to4 = req_to4 / 1000000
		
		elif (req_frequency_units == 'KHz'):
			req_from4 = req_from4 / 1000
			req_to4 = req_to4 / 1000
		
		elif (req_frequency_units == 'MHz'):
			req_from4 = req_from4 * 1
			req_to4 = req_to4 * 1 
		
		elif (req_frequency_units == 'GHz'):
			req_from4 = req_from4 * 1000
			req_to4 = req_to4 * 1000
		
		elif (req_frequency_units == 'THz'):
			req_from4 = req_from4 * 1000000
			req_to4 = req_to4 * 1000000
		
		elif (req_frequency_units == 'a'):
			req_from4 = 2.99792458 * pow(10,12) / req_from4z
			req_to4 = 2.99792458 * pow(10,12) / req_to4z
		
		elif (req_frequency_units == 'nm'):
			req_from4 = 2.99792458 * pow(10,11) / req_from4z
			req_to4 = 2.99792458 * pow(10,11) / req_to4z
		
		elif (req_frequency_units == 'mum'):
			req_from4 = 2.99792458 * pow(10,8) / req_from4z
			req_to4 = 2.99792458 * pow(10,8) / req_to4z
		
		elif (req_frequency_units == 'mm'):
			req_from4 = 2.99792458 * pow(10,5) / req_from4z
			req_to4 = 2.99792458 * pow(10,5) / req_to4z
		
		elif (req_frequency_units == 'cm'):
			req_from4 = 2.99792458 * pow(10,4) / req_from4z
			req_to4 = 2.99792458 * pow(10,4) / req_to4z
		
		else:
			req_from4 = 2.99792458 * pow(10,2) / req_from4z
			req_to4 = 2.99792458 * pow(10,2) / req_to4z
		
	

	if (req_from5 != '' or req_to5 != ''):
		if (req_frequency_units == 'Hz'):
			req_from5 = req_from5 / 1000000
			req_to5 = req_to5 / 1000000
		
		elif (req_frequency_units == 'KHz'):
			req_from5 = req_from5 / 1000
			req_to5 = req_to5 / 1000
		
		elif (req_frequency_units == 'MHz'):
			req_from5 = req_from5 * 1
			req_to5 = req_to5 * 1 
		
		elif (req_frequency_units == 'GHz'):
			req_from5 = req_from5 * 1000
			req_to5 = req_to5 * 1000
		
		elif (req_frequency_units == 'THz'):
			req_from5 = req_from5 * 1000000
			req_to5 = req_to5 * 1000000
		
		elif (req_frequency_units == 'a'):
			req_from5 = 2.99792458 * pow(10,12) / req_from5z
			req_to5 = 2.99792458 * pow(10,12) / req_to5z
		
		elif (req_frequency_units == 'nm'):
			req_from5 = 2.99792458 * pow(10,11) / req_from5z
			req_to5 = 2.99792458 * pow(10,11) / req_to5z
		
		elif (req_frequency_units == 'mum'):
			req_from5 = 2.99792458 * pow(10,8) / req_from5z
			req_to5 = 2.99792458 * pow(10,8) / req_to5z
		
		elif (req_frequency_units == 'mm'):
			req_from5 = 2.99792458 * pow(10,5) / req_from5z
			req_to5 = 2.99792458 * pow(10,5) / req_to5z
		
		elif (req_frequency_units == 'cm'):
			req_from5 = 2.99792458 * pow(10,4) / req_from5z
			req_to5 = 2.99792458 * pow(10,4) / req_to5z
		
		else:
			req_from5 = 2.99792458 * pow(10,2) / req_from5z
			req_to5 = 2.99792458 * pow(10,2) / req_to5z
		
	

	if (req_from6 != '' or req_to6 != ''):
		if (req_frequency_units == 'Hz'):
			req_from6 = req_from6 / 1000000
			req_to6 = req_to6 / 1000000
		
		elif (req_frequency_units == 'KHz'):
			req_from6 = req_from6 / 1000
			req_to6 = req_to6 / 1000
		
		elif (req_frequency_units == 'MHz'):
			req_from6 = req_from6 * 1
			req_to6 = req_to6 * 1 
		
		elif (req_frequency_units == 'GHz'):
			req_from6 = req_from6 * 1000
			req_to6 = req_to6 * 1000
		
		elif (req_frequency_units == 'THz'):
			req_from6 = req_from6 * 1000000
			req_to6 = req_to6 * 1000000
		
		elif (req_frequency_units == 'a'):
			req_from6 = 2.99792458 * pow(10,12) / req_from6z
			req_to6 = 2.99792458 * pow(10,12) / req_to6z
		
		elif (req_frequency_units == 'nm'):
			req_from6 = 2.99792458 * pow(10,11) / req_from6z
			req_to6 = 2.99792458 * pow(10,11) / req_to6z
		
		elif (req_frequency_units == 'mum'):
			req_from6 = 2.99792458 * pow(10,8) / req_from6z
			req_to6 = 2.99792458 * pow(10,8) / req_to6z
		
		elif (req_frequency_units == 'mm'):
			req_from6 = 2.99792458 * pow(10,5) / req_from6z
			req_to6 = 2.99792458 * pow(10,5) / req_to6z
		
		elif (req_frequency_units == 'cm'):
			req_from6 = 2.99792458 * pow(10,4) / req_from6z
			req_to6 = 2.99792458 * pow(10,4) / req_to6z
		
		else:
			req_from6 = 2.99792458 * pow(10,2) / req_from6z
			req_to6 = 2.99792458 * pow(10,2) / req_to6z
		
	

	if (req_from7 != '' or req_to7 != ''):
		if (req_frequency_units == 'Hz'):
			req_from7 = req_from7 / 1000000
			req_to7 = req_to7 / 1000000
		
		elif (req_frequency_units == 'KHz'):
			req_from7 = req_from7 / 1000
			req_to7 = req_to7 / 1000
		
		elif (req_frequency_units == 'MHz'):
			req_from7 = req_from7 * 1
			req_to7 = req_to7 * 1 
		
		elif (req_frequency_units == 'GHz'):
			req_from7 = req_from7 * 1000
			req_to7 = req_to7 * 1000
		
		elif (req_frequency_units == 'THz'):
			req_from7 = req_from7 * 1000000
			req_to7 = req_to7 * 1000000
		
		elif (req_frequency_units == 'a'):
			req_from7 = 2.99792458 * pow(10,12) / req_from7z
			req_to7 = 2.99792458 * pow(10,12) / req_to7z
		
		elif (req_frequency_units == 'nm'):
			req_from7 = 2.99792458 * pow(10,11) / req_from7z
			req_to7 = 2.99792458 * pow(10,11) / req_to7z
		
		elif (req_frequency_units == 'mum'):
			req_from7 = 2.99792458 * pow(10,8) / req_from7z
			req_to7 = 2.99792458 * pow(10,8) / req_to7z
		
		elif (req_frequency_units == 'mm'):
			req_from7 = 2.99792458 * pow(10,5) / req_from7z
			req_to7 = 2.99792458 * pow(10,5) / req_to7z
		
		elif (req_frequency_units == 'cm'):
			req_from7 = 2.99792458 * pow(10,4) / req_from7z
			req_to7 = 2.99792458 * pow(10,4) / req_to7z
		
		else:
			req_from7 = 2.99792458 * pow(10,2) / req_from7z
			req_to7 = 2.99792458 * pow(10,2) / req_to7z
		
	

	if (req_from8 != '' or req_to8 != ''):
		if (req_frequency_units == 'Hz'):
			req_from8 = req_from8 / 1000000
			req_to8 = req_to8 / 1000000
		
		elif (req_frequency_units == 'KHz'):
			req_from8 = req_from8 / 1000
			req_to8 = req_to8 / 1000
		
		elif (req_frequency_units == 'MHz'):
			req_from8 = req_from8 * 1
			req_to8 = req_to8 * 1 
		
		elif (req_frequency_units == 'GHz'):
			req_from8 = req_from8 * 1000
			req_to8 = req_to8 * 1000
		
		elif (req_frequency_units == 'THz'):
			req_from8 = req_from8 * 1000000
			req_to8 = req_to8 * 1000000
		
		elif (req_frequency_units == 'a'):
			req_from8 = 2.99792458 * pow(10,12) / req_from8z
			req_to8 = 2.99792458 * pow(10,12) / req_to8z
		
		elif (req_frequency_units == 'nm'):
			req_from8 = 2.99792458 * pow(10,11) / req_from8z
			req_to8 = 2.99792458 * pow(10,11) / req_to8z
		
		elif (req_frequency_units == 'mum'):
			req_from8 = 2.99792458 * pow(10,8) / req_from8z
			req_to8 = 2.99792458 * pow(10,8) / req_to8z
		
		elif (req_frequency_units == 'mm'):
			req_from8 = 2.99792458 * pow(10,5) / req_from8z
			req_to8 = 2.99792458 * pow(10,5) / req_to8z
		
		elif (req_frequency_units == 'cm'):
			req_from8 = 2.99792458 * pow(10,4) / req_from8z
			req_to8 = 2.99792458 * pow(10,4) / req_to8z
		
		else:
			req_from8 = 2.99792458 * pow(10,2) / req_from8z
			req_to8 = 2.99792458 * pow(10,2) / req_to8z
		
	

	if (req_from9 != '' or req_to9 != ''):
		if (req_frequency_units == 'Hz'):
			req_from9 = req_from9 / 1000000
			req_to9 = req_to9 / 1000000
		
		elif (req_frequency_units == 'KHz'):
			req_from9 = req_from9 / 1000
			req_to9 = req_to9 / 1000
		
		elif (req_frequency_units == 'MHz'):
			req_from9 = req_from9 * 1
			req_to9 = req_to9 * 1 
		
		elif (req_frequency_units == 'GHz'):
			req_from9 = req_from9 * 1000
			req_to9 = req_to9 * 1000
		
		elif (req_frequency_units == 'THz'):
			req_from9 = req_from9 * 1000000
			req_to9 = req_to9 * 1000000
		
		elif (req_frequency_units == 'a'):
			req_from9 = 2.99792458 * pow(10,12) / req_from9z
			req_to9 = 2.99792458 * pow(10,12) / req_to9z
		
		elif (req_frequency_units == 'nm'):
			req_from9 = 2.99792458 * pow(10,11) / req_from9z
			req_to9 = 2.99792458 * pow(10,11) / req_to9z
		
		elif (req_frequency_units == 'mum'):
			req_from9 = 2.99792458 * pow(10,8) / req_from9z
			req_to9 = 2.99792458 * pow(10,8) / req_to9z
		
		elif (req_frequency_units == 'mm'):
			req_from9 = 2.99792458 * pow(10,5) / req_from9z
			req_to9 = 2.99792458 * pow(10,5) / req_to9z
		
		elif (req_frequency_units == 'cm'):
			req_from9 = 2.99792458 * pow(10,4) / req_from9z
			req_to9 = 2.99792458 * pow(10,4) / req_to9z
		
		else:
			req_from9 = 2.99792458 * pow(10,2) / req_from9z
			req_to9 = 2.99792458 * pow(10,2) / req_to9z
		
	

	if (req_from10 != '' or req_to10 != ''):
		if (req_frequency_units == 'Hz'):
			req_from10 = req_from10 / 1000000
			req_to10 = req_to10 / 1000000
		
		elif (req_frequency_units == 'KHz'):
			req_from10 = req_from10 / 1000
			req_to10 = req_to10 / 1000
		
		elif (req_frequency_units == 'MHz'):
			req_from10 = req_from10 * 1
			req_to10 = req_to10 * 1 
		
		elif (req_frequency_units == 'GHz'):
			req_from10 = req_from10 * 1000
			req_to10 = req_to10 * 1000
		
		elif (req_frequency_units == 'THz'):
			req_from10 = req_from10 * 1000000
			req_to10 = req_to10 * 1000000
		
		elif (req_frequency_units == 'a'):
			req_from10 = 2.99792458 * pow(10,12) / req_from10z
			req_to10 = 2.99792458 * pow(10,12) / req_to10z
		
		elif (req_frequency_units == 'nm'):
			req_from10 = 2.99792458 * pow(10,11) / req_from10z
			req_to10 = 2.99792458 * pow(10,11) / req_to10z
		
		elif (req_frequency_units == 'mum'):
			req_from10 = 2.99792458 * pow(10,8) / req_from10z
			req_to10 = 2.99792458 * pow(10,8) / req_to10z
		
		elif (req_frequency_units == 'mm'):
			req_from10 = 2.99792458 * pow(10,5) / req_from10z
			req_to10 = 2.99792458 * pow(10,5) / req_to10z
		
		elif (req_frequency_units == 'cm'):
			req_from10 = 2.99792458 * pow(10,4) / req_from10z
			req_to10 = 2.99792458 * pow(10,4) / req_to10z
		
		else:
			req_from10 = 2.99792458 * pow(10,2) / req_from10z
			req_to10 = 2.99792458 * pow(10,2) / req_to10z
		
	

	if (req_from11 != '' or req_to11 != ''):
		if (req_frequency_units == 'Hz'):
			req_from11 = req_from11 / 1000000
			req_to11 = req_to11 / 1000000
		
		elif (req_frequency_units == 'KHz'):
			req_from11 = req_from11 / 1000
			req_to11 = req_to11 / 1000
		
		elif (req_frequency_units == 'MHz'):
			req_from11 = req_from11 * 1
			req_to11 = req_to11 * 1 
		
		elif (req_frequency_units == 'GHz'):
			req_from11 = req_from11 * 1000
			req_to11 = req_to11 * 1000
		
		elif (req_frequency_units == 'THz'):
			req_from11 = req_from11 * 1000000
			req_to11 = req_to11 * 1000000
		
		elif (req_frequency_units == 'a'):
			req_from11 = 2.99792458 * pow(10,12) / req_from11z
			req_to11 = 2.99792458 * pow(10,12) / req_to11z
		
		elif (req_frequency_units == 'nm'):
			req_from11 = 2.99792458 * pow(10,11) / req_from11z
			req_to11 = 2.99792458 * pow(10,11) / req_to11z
		
		elif (req_frequency_units == 'mum'):
			req_from11 = 2.99792458 * pow(10,8) / req_from11z
			req_to11 = 2.99792458 * pow(10,8) / req_to11z
		
		elif (req_frequency_units == 'mm'):
			req_from11 = 2.99792458 * pow(10,5) / req_from11z
			req_to11 = 2.99792458 * pow(10,5) / req_to11z
		
		elif (req_frequency_units == 'cm'):
			req_from11 = 2.99792458 * pow(10,4) / req_from11z
			req_to11 = 2.99792458 * pow(10,4) / req_to11z
		
		else:
			req_from11 = 2.99792458 * pow(10,2) / req_from11z
			req_to11 = 2.99792458 * pow(10,2) / req_to11z
		
	

	if (req_from12 != '' or req_to12 != ''):
		if (req_frequency_units == 'Hz'):
			req_from12 = req_from12 / 1000000
			req_to12 = req_to12 / 1000000
		
		elif (req_frequency_units == 'KHz'):
			req_from12 = req_from12 / 1000
			req_to12 = req_to12 / 1000
		
		elif (req_frequency_units == 'MHz'):
			req_from12 = req_from12 * 1
			req_to12 = req_to12 * 1 
		
		elif (req_frequency_units == 'GHz'):
			req_from12 = req_from12 * 1000
			req_to12 = req_to12 * 1000
		
		elif (req_frequency_units == 'THz'):
			req_from12 = req_from12 * 1000000
			req_to12 = req_to12 * 1000000
		
		elif (req_frequency_units == 'a'):
			req_from12 = 2.99792458 * pow(10,12) / req_from12z
			req_to12 = 2.99792458 * pow(10,12) / req_to12z
		
		elif (req_frequency_units == 'nm'):
			req_from12 = 2.99792458 * pow(10,11) / req_from12z
			req_to12 = 2.99792458 * pow(10,11) / req_to12z
		
		elif (req_frequency_units == 'mum'):
			req_from12 = 2.99792458 * pow(10,8) / req_from12z
			req_to12 = 2.99792458 * pow(10,8) / req_to12z
		
		elif (req_frequency_units == 'mm'):
			req_from12 = 2.99792458 * pow(10,5) / req_from12z
			req_to12 = 2.99792458 * pow(10,5) / req_to12z
		
		elif (req_frequency_units == 'cm'):
			req_from12 = 2.99792458 * pow(10,4) / req_from12z
			req_to12 = 2.99792458 * pow(10,4) / req_to12z
		
		else:
			req_from12 = 2.99792458 * pow(10,2) / req_from12z
			req_to12 = 2.99792458 * pow(10,2) / req_to12z
		
	

	if (req_from13 != '' or req_to13 != ''):
		if (req_frequency_units == 'Hz'):
			req_from13 = req_from13 / 1000000
			req_to13 = req_to13 / 1000000
		
		elif (req_frequency_units == 'KHz'):
			req_from13 = req_from13 / 1000
			req_to13 = req_to13 / 1000
		
		elif (req_frequency_units == 'MHz'):
			req_from13 = req_from13 * 1
			req_to13 = req_to13 * 1 
		
		elif (req_frequency_units == 'GHz'):
			req_from13 = req_from13 * 1000
			req_to13 = req_to13 * 1000
		
		elif (req_frequency_units == 'THz'):
			req_from13 = req_from13 * 1000000
			req_to13 = req_to13 * 1000000
		
		elif (req_frequency_units == 'a'):
			req_from13 = 2.99792458 * pow(10,12) / req_from13z
			req_to13 = 2.99792458 * pow(10,12) / req_to13z
		
		elif (req_frequency_units == 'nm'):
			req_from13 = 2.99792458 * pow(10,11) / req_from13z
			req_to13 = 2.99792458 * pow(10,11) / req_to13z
		
		elif (req_frequency_units == 'mum'):
			req_from13 = 2.99792458 * pow(10,8) / req_from13z
			req_to13 = 2.99792458 * pow(10,8) / req_to13z
		
		elif (req_frequency_units == 'mm'):
			req_from13 = 2.99792458 * pow(10,5) / req_from13z
			req_to13 = 2.99792458 * pow(10,5) / req_to13z
		
		elif (req_frequency_units == 'cm'):
			req_from13 = 2.99792458 * pow(10,4) / req_from13z
			req_to13 = 2.99792458 * pow(10,4) / req_to13z
		
		else:
			req_from13 = 2.99792458 * pow(10,2) / req_from13z
			req_to13 = 2.99792458 * pow(10,2) / req_to13z
		
	

	if (req_from14 != '' or req_to14 != ''):
		if (req_frequency_units == 'Hz'):
			req_from14 = req_from14 / 1000000
			req_to14 = req_to14 / 1000000
		
		elif (req_frequency_units == 'KHz'):
			req_from14 = req_from14 / 1000
			req_to14 = req_to14 / 1000
		
		elif (req_frequency_units == 'MHz'):
			req_from14 = req_from14 * 1
			req_to14 = req_to14 * 1 
		
		elif (req_frequency_units == 'GHz'):
			req_from14 = req_from14 * 1000
			req_to14 = req_to14 * 1000
		
		elif (req_frequency_units == 'THz'):
			req_from14 = req_from14 * 1000000
			req_to14 = req_to14 * 1000000
		
		elif (req_frequency_units == 'a'):
			req_from14 = 2.99792458 * pow(10,12) / req_from14z
			req_to14 = 2.99792458 * pow(10,12) / req_to14z
		
		elif (req_frequency_units == 'nm'):
			req_from14 = 2.99792458 * pow(10,11) / req_from14z
			req_to14 = 2.99792458 * pow(10,11) / req_to14z
		
		elif (req_frequency_units == 'mum'):
			req_from14 = 2.99792458 * pow(10,8) / req_from14z
			req_to14 = 2.99792458 * pow(10,8) / req_to14z
		
		elif (req_frequency_units == 'mm'):
			req_from14 = 2.99792458 * pow(10,5) / req_from14z
			req_to14 = 2.99792458 * pow(10,5) / req_to14z
		
		elif (req_frequency_units == 'cm'):
			req_from14 = 2.99792458 * pow(10,4) / req_from14z
			req_to14 = 2.99792458 * pow(10,4) / req_to14z
		
		else:
			req_from14 = 2.99792458 * pow(10,2) / req_from14z
			req_to14 = 2.99792458 * pow(10,2) / req_to14z
		
	

	if (req_from15 != '' or req_to15 != ''):
		if (req_frequency_units == 'Hz'):
			req_from15 = req_from15 / 1000000
			req_to15 = req_to15 / 1000000
		
		elif (req_frequency_units == 'KHz'):
			req_from15 = req_from15 / 1000
			req_to15 = req_to15 / 1000
		
		elif (req_frequency_units == 'MHz'):
			req_from15 = req_from15 * 1
			req_to15 = req_to15 * 1 
		
		elif (req_frequency_units == 'GHz'):
			req_from15 = req_from15 * 1000
			req_to15 = req_to15 * 1000
		
		elif (req_frequency_units == 'THz'):
			req_from15 = req_from15 * 1000000
			req_to15 = req_to15 * 1000000
		
		elif (req_frequency_units == 'a'):
			req_from15 = 2.99792458 * pow(10,12) / req_from15z
			req_to15 = 2.99792458 * pow(10,12) / req_to15z
		
		elif (req_frequency_units == 'nm'):
			req_from15 = 2.99792458 * pow(10,11) / req_from15z
			req_to15 = 2.99792458 * pow(10,11) / req_to15z
		
		elif (req_frequency_units == 'mum'):
			req_from15 = 2.99792458 * pow(10,8) / req_from15z
			req_to15 = 2.99792458 * pow(10,8) / req_to15z
		
		elif (req_frequency_units == 'mm'):
			req_from15 = 2.99792458 * pow(10,5) / req_from15z
			req_to15 = 2.99792458 * pow(10,5) / req_to15z
		
		elif (req_frequency_units == 'cm'):
			req_from15 = 2.99792458 * pow(10,4) / req_from15z
			req_to15 = 2.99792458 * pow(10,4) / req_to15z
		
		else:
			req_from15 = 2.99792458 * pow(10,2) / req_from15z
			req_to15 = 2.99792458 * pow(10,2) / req_to15z
		
	

	if (req_from16 != '' or req_to16 != ''):
		if (req_frequency_units == 'Hz'):
			req_from16 = req_from16 / 1000000
			req_to16 = req_to16 / 1000000
		
		elif (req_frequency_units == 'KHz'):
			req_from16 = req_from16 / 1000
			req_to16 = req_to16 / 1000
		
		elif (req_frequency_units == 'MHz'):
			req_from16 = req_from16 * 1
			req_to16 = req_to16 * 1 
		
		elif (req_frequency_units == 'GHz'):
			req_from16 = req_from16 * 1000
			req_to16 = req_to16 * 1000
		
		elif (req_frequency_units == 'THz'):
			req_from16 = req_from16 * 1000000
			req_to16 = req_to16 * 1000000
		
		elif (req_frequency_units == 'a'):
			req_from16 = 2.99792458 * pow(10,12) / req_from16z
			req_to16 = 2.99792458 * pow(10,12) / req_to16z
		
		elif (req_frequency_units == 'nm'):
			req_from16 = 2.99792458 * pow(10,11) / req_from16z
			req_to16 = 2.99792458 * pow(10,11) / req_to16z
		
		elif (req_frequency_units == 'mum'):
			req_from16 = 2.99792458 * pow(10,8) / req_from16z
			req_to16 = 2.99792458 * pow(10,8) / req_to16z
		
		elif (req_frequency_units == 'mm'):
			req_from16 = 2.99792458 * pow(10,5) / req_from16z
			req_to16 = 2.99792458 * pow(10,5) / req_to16z
		
		elif (req_frequency_units == 'cm'):
			req_from16 = 2.99792458 * pow(10,4) / req_from16z
			req_to16 = 2.99792458 * pow(10,4) / req_to16z
		
		else:
			req_from16 = 2.99792458 * pow(10,2) / req_from16z
			req_to16 = 2.99792458 * pow(10,2) / req_to16z
		
	

	if (req_from17 != '' or req_to17 != ''):
		if (req_frequency_units == 'Hz'):
			req_from17 = req_from17 / 1000000
			req_to17 = req_to17 / 1000000
		
		elif (req_frequency_units == 'KHz'):
			req_from17 = req_from17 / 1000
			req_to17 = req_to17 / 1000
		
		elif (req_frequency_units == 'MHz'):
			req_from17 = req_from17 * 1
			req_to17 = req_to17 * 1 
		
		elif (req_frequency_units == 'GHz'):
			req_from17 = req_from17 * 1000
			req_to17 = req_to17 * 1000
		
		elif (req_frequency_units == 'THz'):
			req_from17 = req_from17 * 1000000
			req_to17 = req_to17 * 1000000
		
		elif (req_frequency_units == 'a'):
			req_from17 = 2.99792458 * pow(10,12) / req_from17z
			req_to17 = 2.99792458 * pow(10,12) / req_to17z
		
		elif (req_frequency_units == 'nm'):
			req_from17 = 2.99792458 * pow(10,11) / req_from17z
			req_to17 = 2.99792458 * pow(10,11) / req_to17z
		
		elif (req_frequency_units == 'mum'):
			req_from17 = 2.99792458 * pow(10,8) / req_from17z
			req_to17 = 2.99792458 * pow(10,8) / req_to17z
		
		elif (req_frequency_units == 'mm'):
			req_from17 = 2.99792458 * pow(10,5) / req_from17z
			req_to17 = 2.99792458 * pow(10,5) / req_to17z
		
		elif (req_frequency_units == 'cm'):
			req_from17 = 2.99792458 * pow(10,4) / req_from17z
			req_to17 = 2.99792458 * pow(10,4) / req_to17z
		
		else:
			req_from17 = 2.99792458 * pow(10,2) / req_from17z
			req_to17 = 2.99792458 * pow(10,2) / req_to17z
		
	

	if (req_from18 != '' or req_to18 != ''):
		if (req_frequency_units == 'Hz'):
			req_from18 = req_from18 / 1000000
			req_to18 = req_to18 / 1000000
		
		elif (req_frequency_units == 'KHz'):
			req_from18 = req_from18 / 1000
			req_to18 = req_to18 / 1000
		
		elif (req_frequency_units == 'MHz'):
			req_from18 = req_from18 * 1
			req_to18 = req_to18 * 1 
		
		elif (req_frequency_units == 'GHz'):
			req_from18 = req_from18 * 1000
			req_to18 = req_to18 * 1000
		
		elif (req_frequency_units == 'THz'):
			req_from18 = req_from18 * 1000000
			req_to18 = req_to18 * 1000000
		
		elif (req_frequency_units == 'a'):
			req_from18 = 2.99792458 * pow(10,12) / req_from18z
			req_to18 = 2.99792458 * pow(10,12) / req_to18z
		
		elif (req_frequency_units == 'nm'):
			req_from18 = 2.99792458 * pow(10,11) / req_from18z
			req_to18 = 2.99792458 * pow(10,11) / req_to18z
		
		elif (req_frequency_units == 'mum'):
			req_from18 = 2.99792458 * pow(10,8) / req_from18z
			req_to18 = 2.99792458 * pow(10,8) / req_to18z
		
		elif (req_frequency_units == 'mm'):
			req_from18 = 2.99792458 * pow(10,5) / req_from18z
			req_to18 = 2.99792458 * pow(10,5) / req_to18z
		
		elif (req_frequency_units == 'cm'):
			req_from18 = 2.99792458 * pow(10,4) / req_from18z
			req_to18 = 2.99792458 * pow(10,4) / req_to18z
		
		else:
			req_from18 = 2.99792458 * pow(10,2) / req_from18z
			req_to18 = 2.99792458 * pow(10,2) / req_to18z
		
	

	if (req_from19 != '' or req_to19 != ''):
		if (req_frequency_units == 'Hz'):
			req_from19 = req_from19 / 1000000
			req_to19 = req_to19 / 1000000
		
		elif (req_frequency_units == 'KHz'):
			req_from19 = req_from19 / 1000
			req_to19 = req_to19 / 1000
		
		elif (req_frequency_units == 'MHz'):
			req_from19 = req_from19 * 1
			req_to19 = req_to19 * 1 
		
		elif (req_frequency_units == 'GHz'):
			req_from19 = req_from19 * 1000
			req_to19 = req_to19 * 1000
		
		elif (req_frequency_units == 'THz'):
			req_from19 = req_from19 * 1000000
			req_to19 = req_to19 * 1000000
		
		elif (req_frequency_units == 'a'):
			req_from19 = 2.99792458 * pow(10,12) / req_from19z
			req_to19 = 2.99792458 * pow(10,12) / req_to19z
		
		elif (req_frequency_units == 'nm'):
			req_from19 = 2.99792458 * pow(10,11) / req_from19z
			req_to19 = 2.99792458 * pow(10,11) / req_to19z
		
		elif (req_frequency_units == 'mum'):
			req_from19 = 2.99792458 * pow(10,8) / req_from19z
			req_to19 = 2.99792458 * pow(10,8) / req_to19z
		
		elif (req_frequency_units == 'mm'):
			req_from19 = 2.99792458 * pow(10,5) / req_from19z
			req_to19 = 2.99792458 * pow(10,5) / req_to19z
		
		elif (req_frequency_units == 'cm'):
			req_from19 = 2.99792458 * pow(10,4) / req_from19z
			req_to19 = 2.99792458 * pow(10,4) / req_to19z
		
		else:
			req_from19 = 2.99792458 * pow(10,2) / req_from19z
			req_to19 = 2.99792458 * pow(10,2) / req_to19z
		
	

	if (req_from20 != '' or req_to20 != ''):
		if (req_frequency_units == 'Hz'):
			req_from20 = req_from20 / 1000000
			req_to20 = req_to20 / 1000000
		
		elif (req_frequency_units == 'KHz'):
			req_from20 = req_from20 / 1000
			req_to20 = req_to20 / 1000
		
		elif (req_frequency_units == 'MHz'):
			req_from20 = req_from20 * 1
			req_to20 = req_to20 * 1 
		
		elif (req_frequency_units == 'GHz'):
			req_from20 = req_from20 * 1000
			req_to20 = req_to20 * 1000
		
		elif (req_frequency_units == 'THz'):
			req_from20 = req_from20 * 1000000
			req_to20 = req_to20 * 1000000
		
		elif (req_frequency_units == 'a'):
			req_from20 = 2.99792458 * pow(10,12) / req_from20z
			req_to20 = 2.99792458 * pow(10,12) / req_to20z
		
		elif (req_frequency_units == 'nm'):
			req_from20 = 2.99792458 * pow(10,11) / req_from20z
			req_to20 = 2.99792458 * pow(10,11) / req_to20z
		
		elif (req_frequency_units == 'mum'):
			req_from20 = 2.99792458 * pow(10,8) / req_from20z
			req_to20 = 2.99792458 * pow(10,8) / req_to20z
		
		elif (req_frequency_units == 'mm'):
			req_from20 = 2.99792458 * pow(10,5) / req_from20z
			req_to20 = 2.99792458 * pow(10,5) / req_to20z
		
		elif (req_frequency_units == 'cm'):
			req_from20 = 2.99792458 * pow(10,4) / req_from20z
			req_to20 = 2.99792458 * pow(10,4) / req_to20z
		
		else:
			req_from20 = 2.99792458 * pow(10,2) / req_from20z
			req_to20 = 2.99792458 * pow(10,2) / req_to20z

	

	if (req_from == 0.0 or req_to == 0.0):
		a = mysql_real_escape_string(req_from)
		array_push_if(select_where, ('orderedfreq>=%s' % (a)), has_number(req_from))	
		a = mysql_real_escape_string(req_to)
		array_push_if(select_where, ('orderedfreq<=%s' % (a)), has_number(req_to))	
	
	elif ((req_from != 0.0 or req_to != 0.0) and req_from2 == 0.0):
		a = mysql_real_escape_string(req_from)
		array_push_if(select_where, ('orderedfreq>=%s' % (a)), has_number(req_from))	
		a = mysql_real_escape_string(req_to)
		array_push_if(select_where, ('orderedfreq<=%s' % (a)), has_number(req_to))	
	
	elif ((req_from2!= 0.0 or req_to2!= 0.0) and (req_from3== 0.0 or req_to3== 0.0)):
		array_push_if(select_where, ('((orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s))' % (mysql_real_escape_string(req_from), mysql_real_escape_string(req_to), mysql_real_escape_string(req_from2), mysql_real_escape_string(req_to2))), has_number(req_from2))	
	
	elif (req_from3!= 0.0 and req_from4== 0.0):
		array_push_if(select_where, ('((orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s))' % (mysql_real_escape_string(req_from), mysql_real_escape_string(req_to), mysql_real_escape_string(req_from2), mysql_real_escape_string(req_to2), mysql_real_escape_string(req_from3), mysql_real_escape_string(req_to3))), has_number(req_from2))	
	
	elif (req_from4!= 0.0 and req_from5== 0.0):
		array_push_if(select_where, ('((orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s))' % (mysql_real_escape_string(req_from), mysql_real_escape_string(req_to), mysql_real_escape_string(req_from2), mysql_real_escape_string(req_to2), mysql_real_escape_string(req_from3), mysql_real_escape_string(req_to3), mysql_real_escape_string(req_from4), mysql_real_escape_string(req_to4))), has_number(req_from2))	
	
	elif (req_from5!= 0.0 and req_from6== 0.0):
		array_push_if(select_where, ('((orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s))' % (mysql_real_escape_string(req_from), mysql_real_escape_string(req_to), mysql_real_escape_string(req_from2), mysql_real_escape_string(req_to2), mysql_real_escape_string(req_from3), mysql_real_escape_string(req_to3), mysql_real_escape_string(req_from4), mysql_real_escape_string(req_to4), mysql_real_escape_string(req_from5), mysql_real_escape_string(req_to5))), has_number(req_from2))	
	
	elif (req_from6!= 0.0 and req_from7== 0.0):
		array_push_if(select_where, ('((orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s))' % (mysql_real_escape_string(req_from), mysql_real_escape_string(req_to), mysql_real_escape_string(req_from2), mysql_real_escape_string(req_to2), mysql_real_escape_string(req_from3), mysql_real_escape_string(req_to3), mysql_real_escape_string(req_from4), mysql_real_escape_string(req_to4), mysql_real_escape_string(req_from5), mysql_real_escape_string(req_to5), mysql_real_escape_string(req_from6), mysql_real_escape_string(req_to6))), has_number(req_from2))	
	
	elif (req_from7!= 0.0 and req_from8== 0.0):
		array_push_if(select_where, ('((orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s))' % (mysql_real_escape_string(req_from), mysql_real_escape_string(req_to), mysql_real_escape_string(req_from2), mysql_real_escape_string(req_to2), mysql_real_escape_string(req_from3), mysql_real_escape_string(req_to3), mysql_real_escape_string(req_from4), mysql_real_escape_string(req_to4), mysql_real_escape_string(req_from5), mysql_real_escape_string(req_to5), mysql_real_escape_string(req_from6), mysql_real_escape_string(req_to6), mysql_real_escape_string(req_from7), mysql_real_escape_string(req_to7))), has_number(req_from2))	
	
	elif (req_from8!= 0.0 and req_from9== 0.0):
		array_push_if(select_where, ('((orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s))' % (mysql_real_escape_string(req_from), mysql_real_escape_string(req_to), mysql_real_escape_string(req_from2), mysql_real_escape_string(req_to2), mysql_real_escape_string(req_from3), mysql_real_escape_string(req_to3), mysql_real_escape_string(req_from4), mysql_real_escape_string(req_to4), mysql_real_escape_string(req_from5), mysql_real_escape_string(req_to5), mysql_real_escape_string(req_from6), mysql_real_escape_string(req_to6), mysql_real_escape_string(req_from7), mysql_real_escape_string(req_to7), mysql_real_escape_string(req_from8), mysql_real_escape_string(req_to8))), has_number(req_from2))	
	
	elif (req_from9!= 0.0 and req_from10== 0.0):
		array_push_if(select_where, ('((orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s))' % (mysql_real_escape_string(req_from), mysql_real_escape_string(req_to), mysql_real_escape_string(req_from2), mysql_real_escape_string(req_to2), mysql_real_escape_string(req_from3), mysql_real_escape_string(req_to3), mysql_real_escape_string(req_from4), mysql_real_escape_string(req_to4), mysql_real_escape_string(req_from5), mysql_real_escape_string(req_to5), mysql_real_escape_string(req_from6), mysql_real_escape_string(req_to6), mysql_real_escape_string(req_from7), mysql_real_escape_string(req_to7), mysql_real_escape_string(req_from8), mysql_real_escape_string(req_to8), mysql_real_escape_string(req_from9), mysql_real_escape_string(req_to9))), has_number(req_from2))	
	
	elif (req_from10!= 0.0 and req_from11== 0.0):
		array_push_if(select_where, ('((orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s))' % (mysql_real_escape_string(req_from), mysql_real_escape_string(req_to), mysql_real_escape_string(req_from2), mysql_real_escape_string(req_to2), mysql_real_escape_string(req_from3), mysql_real_escape_string(req_to3), mysql_real_escape_string(req_from4), mysql_real_escape_string(req_to4), mysql_real_escape_string(req_from5), mysql_real_escape_string(req_to5), mysql_real_escape_string(req_from6), mysql_real_escape_string(req_to6), mysql_real_escape_string(req_from7), mysql_real_escape_string(req_to7), mysql_real_escape_string(req_from8), mysql_real_escape_string(req_to8), mysql_real_escape_string(req_from9), mysql_real_escape_string(req_to9), mysql_real_escape_string(req_from10), mysql_real_escape_string(req_to10))), has_number(req_from2))	
	
	elif (req_from11!= 0.0 and req_from12== 0.0):
		array_push_if(select_where, ('((orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s))' % (mysql_real_escape_string(req_from), mysql_real_escape_string(req_to), mysql_real_escape_string(req_from2), mysql_real_escape_string(req_to2), mysql_real_escape_string(req_from3), mysql_real_escape_string(req_to3), mysql_real_escape_string(req_from4), mysql_real_escape_string(req_to4), mysql_real_escape_string(req_from5), mysql_real_escape_string(req_to5), mysql_real_escape_string(req_from6), mysql_real_escape_string(req_to6), mysql_real_escape_string(req_from7), mysql_real_escape_string(req_to7), mysql_real_escape_string(req_from8), mysql_real_escape_string(req_to8), mysql_real_escape_string(req_from9), mysql_real_escape_string(req_to9), mysql_real_escape_string(req_from10), mysql_real_escape_string(req_to10), mysql_real_escape_string(req_from11), mysql_real_escape_string(req_to11))), has_number(req_from2))	
	
	elif (req_from12!= 0.0 and req_from13== 0.0):
		array_push_if(select_where, ('((orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s))' % (mysql_real_escape_string(req_from), mysql_real_escape_string(req_to), mysql_real_escape_string(req_from2), mysql_real_escape_string(req_to2), mysql_real_escape_string(req_from3), mysql_real_escape_string(req_to3), mysql_real_escape_string(req_from4), mysql_real_escape_string(req_to4), mysql_real_escape_string(req_from5), mysql_real_escape_string(req_to5), mysql_real_escape_string(req_from6), mysql_real_escape_string(req_to6), mysql_real_escape_string(req_from7), mysql_real_escape_string(req_to7), mysql_real_escape_string(req_from8), mysql_real_escape_string(req_to8), mysql_real_escape_string(req_from9), mysql_real_escape_string(req_to9), mysql_real_escape_string(req_from10), mysql_real_escape_string(req_to10), mysql_real_escape_string(req_from11), mysql_real_escape_string(req_to11), mysql_real_escape_string(req_from12), mysql_real_escape_string(req_to12))), has_number(req_from2))	
	
	elif (req_from13!= 0.0 and req_from14== 0.0):
		array_push_if(select_where, ('((orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s))' % (mysql_real_escape_string(req_from), mysql_real_escape_string(req_to), mysql_real_escape_string(req_from2), mysql_real_escape_string(req_to2), mysql_real_escape_string(req_from3), mysql_real_escape_string(req_to3), mysql_real_escape_string(req_from4), mysql_real_escape_string(req_to4), mysql_real_escape_string(req_from5), mysql_real_escape_string(req_to5), mysql_real_escape_string(req_from6), mysql_real_escape_string(req_to6), mysql_real_escape_string(req_from7), mysql_real_escape_string(req_to7), mysql_real_escape_string(req_from8), mysql_real_escape_string(req_to8), mysql_real_escape_string(req_from9), mysql_real_escape_string(req_to9), mysql_real_escape_string(req_from10), mysql_real_escape_string(req_to10), mysql_real_escape_string(req_from11), mysql_real_escape_string(req_to11), mysql_real_escape_string(req_from12), mysql_real_escape_string(req_to12), mysql_real_escape_string(req_from13), mysql_real_escape_string(req_to13))), has_number(req_from2))	
	
	elif (req_from14!= 0.0 and req_from15== 0.0):
		array_push_if(select_where, ('((orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s))' % (mysql_real_escape_string(req_from), mysql_real_escape_string(req_to), mysql_real_escape_string(req_from2), mysql_real_escape_string(req_to2), mysql_real_escape_string(req_from3), mysql_real_escape_string(req_to3), mysql_real_escape_string(req_from4), mysql_real_escape_string(req_to4), mysql_real_escape_string(req_from5), mysql_real_escape_string(req_to5), mysql_real_escape_string(req_from6), mysql_real_escape_string(req_to6), mysql_real_escape_string(req_from7), mysql_real_escape_string(req_to7), mysql_real_escape_string(req_from8), mysql_real_escape_string(req_to8), mysql_real_escape_string(req_from9), mysql_real_escape_string(req_to9), mysql_real_escape_string(req_from10), mysql_real_escape_string(req_to10), mysql_real_escape_string(req_from11), mysql_real_escape_string(req_to11), mysql_real_escape_string(req_from12), mysql_real_escape_string(req_to12), mysql_real_escape_string(req_from13), mysql_real_escape_string(req_to13), mysql_real_escape_string(req_from14), mysql_real_escape_string(req_to14))), has_number(req_from2))	
	
	elif (req_from15!= 0.0 and req_from16== 0.0):
		array_push_if(select_where, ('((orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s))' % (mysql_real_escape_string(req_from), mysql_real_escape_string(req_to), mysql_real_escape_string(req_from2), mysql_real_escape_string(req_to2), mysql_real_escape_string(req_from3), mysql_real_escape_string(req_to3), mysql_real_escape_string(req_from4), mysql_real_escape_string(req_to4), mysql_real_escape_string(req_from5), mysql_real_escape_string(req_to5), mysql_real_escape_string(req_from6), mysql_real_escape_string(req_to6), mysql_real_escape_string(req_from7), mysql_real_escape_string(req_to7), mysql_real_escape_string(req_from8), mysql_real_escape_string(req_to8), mysql_real_escape_string(req_from9), mysql_real_escape_string(req_to9), mysql_real_escape_string(req_from10), mysql_real_escape_string(req_to10), mysql_real_escape_string(req_from11), mysql_real_escape_string(req_to11), mysql_real_escape_string(req_from12), mysql_real_escape_string(req_to12), mysql_real_escape_string(req_from13), mysql_real_escape_string(req_to13), mysql_real_escape_string(req_from14), mysql_real_escape_string(req_to14), mysql_real_escape_string(req_from15), mysql_real_escape_string(req_to15))), has_number(req_from2))	
	
	elif (req_from16!= 0.0 and req_from17== 0.0):
		array_push_if(select_where, ('((orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s))' % (mysql_real_escape_string(req_from), mysql_real_escape_string(req_to), mysql_real_escape_string(req_from2), mysql_real_escape_string(req_to2), mysql_real_escape_string(req_from3), mysql_real_escape_string(req_to3), mysql_real_escape_string(req_from4), mysql_real_escape_string(req_to4), mysql_real_escape_string(req_from5), mysql_real_escape_string(req_to5), mysql_real_escape_string(req_from6), mysql_real_escape_string(req_to6), mysql_real_escape_string(req_from7), mysql_real_escape_string(req_to7), mysql_real_escape_string(req_from8), mysql_real_escape_string(req_to8), mysql_real_escape_string(req_from9), mysql_real_escape_string(req_to9), mysql_real_escape_string(req_from10), mysql_real_escape_string(req_to10), mysql_real_escape_string(req_from11), mysql_real_escape_string(req_to11), mysql_real_escape_string(req_from12), mysql_real_escape_string(req_to12), mysql_real_escape_string(req_from13), mysql_real_escape_string(req_to13), mysql_real_escape_string(req_from14), mysql_real_escape_string(req_to14), mysql_real_escape_string(req_from15), mysql_real_escape_string(req_to15), mysql_real_escape_string(req_from16), mysql_real_escape_string(req_to16))), has_number(req_from2))	
	
	elif (req_from17!= 0.0 and req_from18== 0.0):
		array_push_if(select_where, ('((orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s))' % (mysql_real_escape_string(req_from), mysql_real_escape_string(req_to), mysql_real_escape_string(req_from2), mysql_real_escape_string(req_to2), mysql_real_escape_string(req_from3), mysql_real_escape_string(req_to3), mysql_real_escape_string(req_from4), mysql_real_escape_string(req_to4), mysql_real_escape_string(req_from5), mysql_real_escape_string(req_to5), mysql_real_escape_string(req_from6), mysql_real_escape_string(req_to6), mysql_real_escape_string(req_from7), mysql_real_escape_string(req_to7), mysql_real_escape_string(req_from8), mysql_real_escape_string(req_to8), mysql_real_escape_string(req_from9), mysql_real_escape_string(req_to9), mysql_real_escape_string(req_from10), mysql_real_escape_string(req_to10), mysql_real_escape_string(req_from11), mysql_real_escape_string(req_to11), mysql_real_escape_string(req_from12), mysql_real_escape_string(req_to12), mysql_real_escape_string(req_from13), mysql_real_escape_string(req_to13), mysql_real_escape_string(req_from14), mysql_real_escape_string(req_to14), mysql_real_escape_string(req_from15), mysql_real_escape_string(req_to15), mysql_real_escape_string(req_from16), mysql_real_escape_string(req_to16), mysql_real_escape_string(req_from17), mysql_real_escape_string(req_to17))), has_number(req_from2))	
	
	elif (req_from18!= 0.0 and req_from19== 0.0):
		array_push_if(select_where, ('((orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s))' % (mysql_real_escape_string(req_from), mysql_real_escape_string(req_to), mysql_real_escape_string(req_from2), mysql_real_escape_string(req_to2), mysql_real_escape_string(req_from3), mysql_real_escape_string(req_to3), mysql_real_escape_string(req_from4), mysql_real_escape_string(req_to4), mysql_real_escape_string(req_from5), mysql_real_escape_string(req_to5), mysql_real_escape_string(req_from6), mysql_real_escape_string(req_to6), mysql_real_escape_string(req_from7), mysql_real_escape_string(req_to7), mysql_real_escape_string(req_from8), mysql_real_escape_string(req_to8), mysql_real_escape_string(req_from9), mysql_real_escape_string(req_to9), mysql_real_escape_string(req_from10), mysql_real_escape_string(req_to10), mysql_real_escape_string(req_from11), mysql_real_escape_string(req_to11), mysql_real_escape_string(req_from12), mysql_real_escape_string(req_to12), mysql_real_escape_string(req_from13), mysql_real_escape_string(req_to13), mysql_real_escape_string(req_from14), mysql_real_escape_string(req_to14), mysql_real_escape_string(req_from15), mysql_real_escape_string(req_to15), mysql_real_escape_string(req_from16), mysql_real_escape_string(req_to16), mysql_real_escape_string(req_from17), mysql_real_escape_string(req_to17), mysql_real_escape_string(req_from18), mysql_real_escape_string(req_to18))), has_number(req_from2))	
	
	elif (req_from19!= 0.0 and req_from20== 0.0):
		array_push_if(select_where, ('((orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s))' % (mysql_real_escape_string(req_from), mysql_real_escape_string(req_to), mysql_real_escape_string(req_from2), mysql_real_escape_string(req_to2), mysql_real_escape_string(req_from3), mysql_real_escape_string(req_to3), mysql_real_escape_string(req_from4), mysql_real_escape_string(req_to4), mysql_real_escape_string(req_from5), mysql_real_escape_string(req_to5), mysql_real_escape_string(req_from6), mysql_real_escape_string(req_to6), mysql_real_escape_string(req_from7), mysql_real_escape_string(req_to7), mysql_real_escape_string(req_from8), mysql_real_escape_string(req_to8), mysql_real_escape_string(req_from9), mysql_real_escape_string(req_to9), mysql_real_escape_string(req_from10), mysql_real_escape_string(req_to10), mysql_real_escape_string(req_from11), mysql_real_escape_string(req_to11), mysql_real_escape_string(req_from12), mysql_real_escape_string(req_to12), mysql_real_escape_string(req_from13), mysql_real_escape_string(req_to13), mysql_real_escape_string(req_from14), mysql_real_escape_string(req_to14), mysql_real_escape_string(req_from15), mysql_real_escape_string(req_to15), mysql_real_escape_string(req_from16), mysql_real_escape_string(req_to16), mysql_real_escape_string(req_from17), mysql_real_escape_string(req_to17), mysql_real_escape_string(req_from18), mysql_real_escape_string(req_to18), mysql_real_escape_string(req_from19), mysql_real_escape_string(req_to19))), has_number(req_from2))	
	
	elif (req_from20!= 0.0):
		array_push_if(select_where, ('((orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s))' % (mysql_real_escape_string(req_from), mysql_real_escape_string(req_to), mysql_real_escape_string(req_from2), mysql_real_escape_string(req_to2), mysql_real_escape_string(req_from3), mysql_real_escape_string(req_to3), mysql_real_escape_string(req_from4), mysql_real_escape_string(req_to4), mysql_real_escape_string(req_from5), mysql_real_escape_string(req_to5), mysql_real_escape_string(req_from6), mysql_real_escape_string(req_to6), mysql_real_escape_string(req_from7), mysql_real_escape_string(req_to7), mysql_real_escape_string(req_from8), mysql_real_escape_string(req_to8), mysql_real_escape_string(req_from9), mysql_real_escape_string(req_to9), mysql_real_escape_string(req_from10), mysql_real_escape_string(req_to10), mysql_real_escape_string(req_from11), mysql_real_escape_string(req_to11), mysql_real_escape_string(req_from12), mysql_real_escape_string(req_to12), mysql_real_escape_string(req_from13), mysql_real_escape_string(req_to13), mysql_real_escape_string(req_from14), mysql_real_escape_string(req_to14), mysql_real_escape_string(req_from15), mysql_real_escape_string(req_to15), mysql_real_escape_string(req_from16), mysql_real_escape_string(req_to16), mysql_real_escape_string(req_from17), mysql_real_escape_string(req_to17), mysql_real_escape_string(req_from18), mysql_real_escape_string(req_to18), mysql_real_escape_string(req_from19), mysql_real_escape_string(req_to19), mysql_real_escape_string(req_from20), mysql_real_escape_string(req_to20))), has_number(req_from2))	
	
	else:
#		echo 'Frequency ranges were not selected!'	
		req_from20== 0.0	

	
	

	array_push(select_fields, 'line_id')
	array_push(select_fields, 'frequency*1.0 as frequency')
	array_push(select_fields, 'uncertainty')
	array_push(select_fields, 'orderedfreq')
	array_push(select_fields, 'measfreq*1.0 as measfreq')
	array_push(select_fields, 'measerrfreq')
	array_push(select_fields, 'rel_int_HFS_Lovas')
	array_push(select_fields, 'll_id')
	array_push(select_fields, 'resolved_QNs')
	array_push(select_fields, 'Sij')
	array_push(select_fields, 'Sijmu2')
	array_push(select_fields, 'Aij')
	array_push(select_fields, 'intintensity')
	array_push(select_fields, 'obsintensity_Lovas_NIST')
	array_push(select_fields, 'lower_state_energy')
	array_push(select_fields, 'lower_state_energy_K')
	array_push(select_fields, 'upper_state_energy')
	array_push(select_fields, 'upper_state_energy_K')
	array_push(select_fields, 'rel_int_HFS_Lovas')
	array_push(select_fields, 'obsref_Lovas_NIST')
	array_push(select_fields, 'labref_Lovas_NIST')
	array_push(select_fields, 'm.species_id')
	array_push(select_fields, 'name')
	array_push(select_fields, 's_name')
	array_push(select_fields, 'chemical_name')
	array_push(select_fields, 'Lovas_NRAO')
	array_push(select_fields, '`v1.0` as v1_0')
	array_push(select_fields, '`v2.0` as v2_0')

	array_push_if(select_fields, 'quantum_numbers', has_value(req_show_unres_qn))
	array_push_if(select_fields, 'upper_state_degeneracy' , has_value(req_show_upper_degeneracy))
	array_push_if(select_fields, 'molecule_tag' , has_value(req_show_molecule_tag))
	array_push_if(select_fields, 'qn_code' , has_value(req_show_qn_code))

	
	where = '1'
	fields = ''
	if select_fields:	
		fields = ', '.join(select_fields)
	if select_where: 	
		where = ' AND '.join(select_where)

	#	db.engine.execute( <sql here> )
	sql = ('SELECT SQL_CALC_FOUND_ROWS %s FROM main m, species s WHERE %s ORDER BY orderedfreq LIMIT %d, %d' % (fields, where, offset, limit))	
	
	
	Base = declarative_base()

	#db = create_engine('sqlite:///tutorial.db')

	
	dbhost = '127.0.0.1'
	dbuser = 'root'
	dbpass = 'W6AuH9VU'
	dburi = 'mysql+mysqldb://' + \
		dbuser + ':' + dbpass + '@' + dbhost + \
		'/splat?charset=utf8&compress=true'
	db = create_engine(dburi)

	# Try changing this to True and see what happens
	db.echo = False  

	Session = sessionmaker()
	Session.configure(bind=db)
	session = Session()
	
	print sql
	linelist = db.engine.execute(sql)

	for line in linelist: logger.debug(line)

	dict = {
		'hits' : r,
		'err_status' : False,
		'err_message' : '',
		'modifieddate' : mdate
	}
    
	return {'retval': dict }
	
	


