from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from ..models import (DBSession,)

import re, os.path, time, math, sys


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
		return
	
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
	string = string + 'eblu sok'
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