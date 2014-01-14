import re
import math

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

def has_number(value):
	if (value == '' or value is None):
		return False

	if math.isnan(value):
		return False

	return True
	
def set_if_has_value(original, yes, no=""):
	if original is None or original == "":
		original = no
	else:
		original = yes

def array_push_if(array, value, condition):
	if condition == True:
		array.append(value)
		return array
	return array
		
def mysql_real_escape_string(string):
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

	print req['energy_range_type'] == "eu_k"
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
		
		print req['energy_range_type'] == "eu_k"
		return found
		
#def extract(request, 'req'):
#	for i in request.params:
#		print i
#	globals().update({foo : '3'})
	
	
def build_query(req, offset = 0, limit = 4294967296):
	extracted = extract(_REQUEST, EXTR_PREFIX_ALL, "req")

	select_where = []
	select_fields = []
	lines = []
	lower_limits = []
	
	if (req_displayRecomb == '' and 
		req_displayCDMS == '' and 
		req_displayJPL == '' and 
		req_displayLovas == '' and 
		req_displaySLAIM == '' and 
		req_displayToyaMA == '' and 
		req_displayOSU == '' and 
		req_displayLisa == '' and 
		req_displayRFI == ''):
		print "Please select a linelist catalogue"
		return
	
	if (req_z == ""):
		req_z=0.0
	
	req_fromz = req_from / (1 + req_z)
	req_toz = req_to / (1 + req_z)
	req_from = req_from * (1 + req_z)
	req_to = req_to * (1 + req_z)
	req_from2z = req_from2 / (1 + req_z)
	req_to2z = req_to2 / (1 + req_z)
	req_from2 = req_from2 * (1 + req_z)
	req_to2 = req_to2 * (1 + req_z)
	req_from3z = req_from3 / (1 + req_z)
	req_to3z = req_to3 / (1 + req_z)
	req_from3 = req_from3 * (1 + req_z)
	req_to3 = req_to3 * (1 + req_z)
	req_from4z = req_from4 / (1 + req_z)
	req_to4z = req_to4 / (1 + req_z)
	req_from4 = req_from4 * (1 + req_z)
	req_to4 = req_to4 * (1 + req_z)
	req_from5z = req_from5 / (1 + req_z)
	req_to5z = req_to5 / (1 + req_z)
	req_from5 = req_from5 * (1 + req_z)
	req_to5 = req_to5 * (1 + req_z)
	req_from6z = req_from6 / (1 + req_z)
	req_to6z = req_to6 / (1 + req_z)
	req_from6 = req_from6 * (1 + req_z)
	req_to6 = req_to6 * (1 + req_z)
	req_from7z = req_from7 / (1 + req_z)
	req_to7z = req_to7 / (1 + req_z)
	req_from7 = req_from7 * (1 + req_z)
	req_to7 = req_to7 * (1 + req_z)
	req_from8z = req_from8 / (1 + req_z)
	req_to8z = req_to8 / (1 + req_z)
	req_from8 = req_from8 * (1 + req_z)
	req_to8 = req_to8 * (1 + req_z)
	req_from9z = req_from9 / (1 + req_z)
	req_to9z = req_to9 / (1 + req_z)
	req_from9 = req_from9 * (1 + req_z)
	req_to9 = req_to9 * (1 + req_z)
	req_from10z = req_from10 / (1 + req_z)
	req_to10z = req_to10 / (1 + req_z)
	req_from10 = req_from10 * (1 + req_z)
	req_to10 = req_to10 * (1 + req_z)
	req_from11z = req_from11 / (1 + req_z)
	req_to11z = req_to11 / (1 + req_z)
	req_from11 = req_from11 * (1 + req_z)
	req_to11 = req_to11 * (1 + req_z)
	req_from12z = req_from12 / (1 + req_z)
	req_to12z = req_to12 / (1 + req_z)
	req_from12 = req_from12 * (1 + req_z)
	req_to12 = req_to12 * (1 + req_z)
	req_from13z = req_from13 / (1 + req_z)
	req_to13z = req_to13 / (1 + req_z)
	req_from13 = req_from13 * (1 + req_z)
	req_to13 = req_to13 * (1 + req_z)
	req_from14z = req_from14 / (1 + req_z)
	req_to14z = req_to14 / (1 + req_z)
	req_from14 = req_from14 * (1 + req_z)
	req_to14 = req_to14 * (1 + req_z)
	req_from15z = req_from15 / (1 + req_z)
	req_to15z = req_to15 / (1 + req_z)
	req_from15 = req_from15 * (1 + req_z)
	req_to15 = req_to15 * (1 + req_z)
	req_from16z = req_from16 / (1 + req_z)
	req_to16z = req_to16 / (1 + req_z)
	req_from16 = req_from16 * (1 + req_z)
	req_to16 = req_to16 * (1 + req_z)
	req_from17z = req_from17 / (1 + req_z)
	req_to17z = req_to17 / (1 + req_z)
	req_from17 = req_from17 * (1 + req_z)
	req_to17 = req_to17 * (1 + req_z)
	req_from18z = req_from18 / (1 + req_z)
	req_to18z = req_to18 / (1 + req_z)
	req_from18 = req_from18 * (1 + req_z)
	req_to18 = req_to18 * (1 + req_z)
	req_from19z = req_from19 / (1 + req_z)
	req_to19z = req_to19 / (1 + req_z)
	req_from19 = req_from19 * (1 + req_z)
	req_to19 = req_to19 * (1 + req_z)
	req_from20z = req_from20 / (1 + req_z)
	req_to20z = req_to20 / (1 + req_z)
	req_from20 = req_from20 * (1 + req_z)
	req_to20 = req_to20 * (1 + req_z)
	
	#array_push(select_where, "m.species_id = s.species_id")
	#array_push(select_where, "s.SPLAT_ID > 100")

	#chemical_name conversion
	
	if req['chemical_name'] == "Cyanobutadiyne (HC5N v11 = 1)": req_chemical_name = "1"
	if req['chemical_name'] == "Formic Acid (t-H(13)COOH)": req_chemical_name = "3"
	if req['chemical_name'] == "Carbon Monoxide ((13)CO v=0)": req_chemical_name = "4"
	if req['chemical_name'] == "Carbon Monosulfide ((13)C(34)S v=0)": req_chemical_name = "5"
	if req['chemical_name'] == "Carbon Monosulfide (CS v=0)": req_chemical_name = "6"
	if req['chemical_name'] == "Formylium (D(13)CO+)": req_chemical_name = "7"
	if req['chemical_name'] == "Atomic Carbon ((13)C)": req_chemical_name = "10" #species_id=10
	if req['chemical_name'] == "Silicon tetracarbide (SiC4)": req_chemical_name = "12"
	if req['chemical_name'] == "Carbon Monoxide ((13)C(18)O)": req_chemical_name = "14"
	if req['chemical_name'] == "Ketenimine (H2CCNH)": req_chemical_name = "17"
	if req['chemical_name'] == "Silicon Monoxide (SiO v=0)": req_chemical_name = "20"
	if req['chemical_name'] == "Ethylene Oxide (c-H2COCH2)": req_chemical_name = "21"
	if req['chemical_name'] == "Carbon Monophosphide (CP)": req_chemical_name = "22"
	if req['chemical_name'] == "Hydrogen Cyanide (DCN v=0)": req_chemical_name = "23"
	if req['chemical_name'] == "Sulfur Monoxide ((34)SO)": req_chemical_name = "24"
	if req['chemical_name'] == "Cyanobutadiyne (HCC(13)CCCN)": req_chemical_name = "27"
	if req['chemical_name'] == "Carbon Monosulfide (C(36)S v = 0)": req_chemical_name = "30"
	if req['chemical_name'] == "Silicon Mononitride (SiN)": req_chemical_name = "33"
	if req['chemical_name'] == "Cyanoacetylene (HC3N v7=1)": req_chemical_name = "36"
	if req['chemical_name'] == "Formylium (H(13)CO+)": req_chemical_name = "38"
	if req['chemical_name'] == "Cyanide Radical (CN v=0)": req_chemical_name = "40"
	if req['chemical_name'] == "Ammonia (ND3)": req_chemical_name = "41"
	if req['chemical_name'] == "Ketene (H2CCO)": req_chemical_name = "44"
	if req['chemical_name'] == "Propadienylidene (l-H2CCC)": req_chemical_name = "45"
	if req['chemical_name'] == "Cyanoacetylene (HC3N v6=1,v7=1)": req_chemical_name = "46"
	if req['chemical_name'] == "Trihydrogen ion (H2D+)": req_chemical_name = "47"
	if req['chemical_name'] == "Sodium Chloride (NaCl v=0)": req_chemical_name = "51"
	if req['chemical_name'] == "Propynylidyne (l-C3H v=0)": req_chemical_name = "52"
	if req['chemical_name'] == "Methanol (CH3OH vt=0)": req_chemical_name = "55"
	if req['chemical_name'] == "2,4,6-Heptatriynenitrile (HC7N v=0)": req_chemical_name = "58"
	if req['chemical_name'] == "Diazenylium (N2D+)": req_chemical_name = "59"
	if req['chemical_name'] == "Sulfur Dioxide ((33)SO2)": req_chemical_name = "60"
	if req['chemical_name'] == "Silicon Isocyanide (SiNC 2P1/2)": req_chemical_name = "61"
	if req['chemical_name'] == "1,3-Butadiynyl radical (C(13)CCCH)": req_chemical_name = "63"
	if req['chemical_name'] == "1,3,5-Hexatriynyl (C6H)": req_chemical_name = "64"
	if req['chemical_name'] == "Cyanide Radical ((13)CN)": req_chemical_name = "65"
	if req['chemical_name'] == "Thioformaldehyde (D2CS)": req_chemical_name = "68"
	if req['chemical_name'] == "Nitrosyl cyanide (ONCN)": req_chemical_name = "75"
	if req['chemical_name'] == "Ammonia (NH2D)": req_chemical_name = "77"
	if req['chemical_name'] == "Sulfur Dioxide ((34)SO2 v=0)": req_chemical_name = "78"
	if req['chemical_name'] == "Iminomethylium (HCNH+)": req_chemical_name = "79"
	if req['chemical_name'] == "Sulfur dioxide (SO2 v=0)": req_chemical_name = "80"
	if req['chemical_name'] == "Hydrogen Isocyanide (HNC v=0)": req_chemical_name = "82"
	if req['chemical_name'] == "Cyanoethynyl (CC(13)CN)": req_chemical_name = "85"
	if req['chemical_name'] == "2,4-Pentadiynylidyne (l-C5H)": req_chemical_name = "92"
	if req['chemical_name'] == "Formaldehyde (D2CO)": req_chemical_name = "94"
	if req['chemical_name'] == "1,3-Butadiynyl radical (C4H v=0)": req_chemical_name = "96"
	if req['chemical_name'] == "Magnesium Isocyanide (MgNC v = 0)": req_chemical_name = "100"
	if req['chemical_name'] == "Silicon Monoxide ((29)SiO v=0)": req_chemical_name = "103"
	if req['chemical_name'] == "Aluminum Isocyanitrile (AlNC)": req_chemical_name = "107"
	if req['chemical_name'] == "1,3,5-Hexatriynyl anion (C6H-)": req_chemical_name = "108"
	if req['chemical_name'] == "Formaldehyde (HDCO)": req_chemical_name = "109"
	if req['chemical_name'] == "2,4,6,8,10-Undecapentaynenitrile (HC11N)": req_chemical_name = "110"
	if req['chemical_name'] == "Fluoromethyliumylidene (CF+ v=0)": req_chemical_name = "115"
	if req['chemical_name'] == "Silicon Monoxide (Si(18)O v = 0)": req_chemical_name = "116"
	if req['chemical_name'] == "Carbon Monosulfide (C(34)S v=0)": req_chemical_name = "117"
	if req['chemical_name'] == "Carbon monosulfide (CS v=1-0)": req_chemical_name = "1249"
	if req['chemical_name'] == "Ethylene Glycol (g'Ga-(CH2OH)2)": req_chemical_name = "121"
	if req['chemical_name'] == "Atomic Carbon (C)": req_chemical_name = "125"
	if req['chemical_name'] == "Silicon Cyanide (SiCN 2P1/2)": req_chemical_name = "127"
	if req['chemical_name'] == "2,4,6-Heptatriynylidyne (C7H)": req_chemical_name = "129"
	if req['chemical_name'] == "Cyanoacetylene (HC(13)CCN v6=1)": req_chemical_name = "130"
	if req['chemical_name'] == "4-Cyano-1,3-Butadiynyl (C5N)": req_chemical_name = "133"
	if req['chemical_name'] == "Cyclopropenone (c-H2C3O)": req_chemical_name = "136"
	if req['chemical_name'] == "Hydrogen Cyanide (H(13)CN v=0)": req_chemical_name = "137"
	if req['chemical_name'] == "Isothiocyanic acid (HNCS a-type)": req_chemical_name = "138"
	if req['chemical_name'] == "Thioformaldehyde (HDCS)": req_chemical_name = "139"
	if req['chemical_name'] == "Formylium (HC(17)O+)": req_chemical_name = "141"
	if req['chemical_name'] == "Carbon Monosulfide ((13)CS v=0)": req_chemical_name = "142"
	if req['chemical_name'] == "Methyl diacetylene (CH3C4H)": req_chemical_name = "146"
	if req['chemical_name'] == "Cyanoacetylene (HC3N v6=1)": req_chemical_name = "147"
	if req['chemical_name'] == "Diazenylium (N2H+ v=0)": req_chemical_name = "148"
	if req['chemical_name'] == "Sulfur Dioxide (OS(18)O)": req_chemical_name = "149"
	if req['chemical_name'] == "Potassium chloride (K(37)Cl v = 0)": req_chemical_name = "150"
	if req['chemical_name'] == "Formaldehyde (H2C(18)O)": req_chemical_name = "155"
	if req['chemical_name'] == "Glycolaldehyde (cis-CH2OHCHO v=0)": req_chemical_name = "156"
	if req['chemical_name'] == "2-Butynenitrile (CH3C3N)": req_chemical_name = "158"
	if req['chemical_name'] == "Hydroxymethylidyne (HOC+ v = 0)": req_chemical_name = "160"
	if req['chemical_name'] == "Formic Acid (t-HCOOH)": req_chemical_name = "163"
	if req['chemical_name'] == "Protonate 2-proynenitrile (HC3NH+)": req_chemical_name = "170"
	if req['chemical_name'] == "Trihydrogen ion (HD2+)": req_chemical_name = "172"
	if req['chemical_name'] == "2,4,6,8-Nonatetraynenitrile (HC9N)": req_chemical_name = "173"
	if req['chemical_name'] == "Carbonyl Sulfide ((18)OCS)": req_chemical_name = "174"
	if req['chemical_name'] == "1,3-Butadiynyl radical (C4D)": req_chemical_name = "175"
	if req['chemical_name'] == "Molecular Hydrogen (HD v=0)": req_chemical_name = "178"
	if req['chemical_name'] == "Carbonyl Sulfide (O(13)CS)": req_chemical_name = "179"
	if req['chemical_name'] == "Ethynyl (CCD)": req_chemical_name = "182"
	if req['chemical_name'] == "Methylene (CH2)": req_chemical_name = "185"
	if req['chemical_name'] == "Methylidyne (CH 2P1/2)": req_chemical_name = "189"
	if req['chemical_name'] == "Potassium chloride (KCl v = 0)": req_chemical_name = "193"
	if req['chemical_name'] == "Formaldehyde (H2CO)": req_chemical_name = "194"
	if req['chemical_name'] == "Hydrogen Cyanide (DCN v2=1)": req_chemical_name = "196"
	if req['chemical_name'] == "3-Cyano-1,2-propadienylidene (l-HC4N)": req_chemical_name = "198"
	if req['chemical_name'] == "Cyanoacetylene (HCCC(15)N)": req_chemical_name = "203"
	if req['chemical_name'] == "Carbon Monoxide (CO v=0)": req_chemical_name = "204"
	if req['chemical_name'] == "Methyl Acetylene (CH3CCD)": req_chemical_name = "209"
	if req['chemical_name'] == "Thioformaldehyde (H2CS)": req_chemical_name = "210"
	if req['chemical_name'] == "Cyanoethynyl (CCCN v=0)": req_chemical_name = "212"
	if req['chemical_name'] == "Vinyl Alcohol (a-H2CCHOH)": req_chemical_name = "214"
	if req['chemical_name'] == "Cyanobutadiyne (HCCCC(13)CN)": req_chemical_name = "215"
	if req['chemical_name'] == "Methylcyanodiacetylene (CH3C5N)": req_chemical_name = "220"
	if req['chemical_name'] == "Phosphaethyne (HCP v=0)": req_chemical_name = "221"
	if req['chemical_name'] == "Cyanoacetylene (HC(13)CCN v7 = 1)": req_chemical_name = "222"
	if req['chemical_name'] == "Cyanoformaldehyde (CNCHO)": req_chemical_name = "223"
	if req['chemical_name'] == "Hydroxymethylium ion (H2COH+)": req_chemical_name = "224"
	if req['chemical_name'] == "Cyanoacetylene (HCC(13)CN)": req_chemical_name = "225"
	if req['chemical_name'] == "Carbon Monoxide (C(17)O)": req_chemical_name = "226"
	if req['chemical_name'] == "Formylium (HC(18)O+)": req_chemical_name = "227"
	if req['chemical_name'] == "Thioformaldehyde (H2(13)CS)": req_chemical_name = "228"
	if req['chemical_name'] == "Sulfur Monoxide ((33)SO)": req_chemical_name = "232"
	if req['chemical_name'] == "Diazenylium ((15)NNH+)": req_chemical_name = "234"
	if req['chemical_name'] == "Cyanoacetylene (HC3N v4=1,v7=1)": req_chemical_name = "242"
	if req['chemical_name'] == "Cyanoacetylene (H(13)CCCN)": req_chemical_name = "244"
	if req['chemical_name'] == "Carbon Monoxide (C(18)O)": req_chemical_name = "245"
	if req['chemical_name'] == "Thioformylium (HCS+)": req_chemical_name = "247"
	if req['chemical_name'] == "Thioxoethenylidene (CCS)": req_chemical_name = "251"
	if req['chemical_name'] == "Cyanoacetylene (HC(13)CCN v7=2)": req_chemical_name = "252"
	if req['chemical_name'] == "Hydrogen Cyanide (HC(15)N v=0)": req_chemical_name = "255"
	if req['chemical_name'] == "Formylium (DCO+ v=0)": req_chemical_name = "256"
	if req['chemical_name'] == "Hydrogen Cyanide (HCN v=0)": req_chemical_name = "258"
	if req['chemical_name'] == "Cyanobutadiyne (HCCC(13)CCN)": req_chemical_name = "260"
	if req['chemical_name'] == "Silicon Monocarbide (SiC v=0)": req_chemical_name = "261"
	if req['chemical_name'] == "Carbon Monoxide ((13)C(17)O)": req_chemical_name = "264"
	if req['chemical_name'] == "Ethynyl ((13)CCH)": req_chemical_name = "268"
	if req['chemical_name'] == "Carbonyl Sulfide (OC(34)S)": req_chemical_name = "270"
	if req['chemical_name'] == "Cyanobutadiyne (H(13)CCCCCN)": req_chemical_name = "272"
	if req['chemical_name'] == "Cyanoacetylene (DC3N)": req_chemical_name = "273"
	if req['chemical_name'] == "1,3-Butadiynyl radical (CCC(13)CH)": req_chemical_name = "275"
	if req['chemical_name'] == "Sulfur Monoxide (SO 3Sigma v=0)": req_chemical_name = "279"
	if req['chemical_name'] == "1,3-Butadiynyl radical ((13)CCCCH)": req_chemical_name = "280"
	if req['chemical_name'] == "Ethynyl (CCH v=0)": req_chemical_name = "282"
	if req['chemical_name'] == "Ammonia (NHD2)": req_chemical_name = "285"
	if req['chemical_name'] == "1,3,5,7-Octatetraynyl (C8H)": req_chemical_name = "286"
	if req['chemical_name'] == "1,3-Butadiynyl radical (C4H v7 = 2 l=0)": req_chemical_name = "289"
	if req['chemical_name'] == "Sulfur Monoxide (S(18)O)": req_chemical_name = "291"
	if req['chemical_name'] == "Silicon Monoxide ((30)SiO v=0)": req_chemical_name = "293"
	if req['chemical_name'] == "Cyanoacetylene (HC3N v=0)": req_chemical_name = "294"
	if req['chemical_name'] == "Hydrogen Isocyanide (DNC)": req_chemical_name = "296"
	if req['chemical_name'] == "Cyanoethynyl ((13)CCCN)": req_chemical_name = "299"
	if req['chemical_name'] == "Carbon Monosulfide   (C(33)S v=0)": req_chemical_name = "300"
	if req['chemical_name'] == "Cyanoacetylene (HC(13)CCN)": req_chemical_name = "304"
	if req['chemical_name'] == "Copper hydride ((65)CuH)": req_chemical_name = "305"
	if req['chemical_name'] == "Methyl Acetylene (CH2DCCH)": req_chemical_name = "308"
	if req['chemical_name'] == "Hydrogen Cyanide (HCN v2=1)": req_chemical_name = "309"
	if req['chemical_name'] == "Methyl Acetylene (CH3CCH v=0)": req_chemical_name = "311"
	if req['chemical_name'] == "Cyanobutadiyne (DCCCCCN)": req_chemical_name = "312"
	if req['chemical_name'] == "Cyanoacetylene (H(13)CCCN v7=2)": req_chemical_name = "316"
	if req['chemical_name'] == "Carbonyl Sulfide (OCS v=0)": req_chemical_name = "317"
	if req['chemical_name'] == "Methanol ((13)CH3OH vt=0)": req_chemical_name = "319"
	if req['chemical_name'] == "Cyanoacetylene (H(13)CCCN v7 = 1)": req_chemical_name = "321"
	if req['chemical_name'] == "Cyanoallene (H2CCCHCN)": req_chemical_name = "323"
	if req['chemical_name'] == "Formaldehyde (H2(13)CO)": req_chemical_name = "324"
	if req['chemical_name'] == "Cyanoacetylene (HC3N v7=2)": req_chemical_name = "326"
	if req['chemical_name'] == "Carbon trimer (C3)": req_chemical_name = "330"
	if req['chemical_name'] == "Hydrogen Cyanide (H(13)CN v2=1)": req_chemical_name = "332"
	if req['chemical_name'] == "Cyanobutadiyne (HC5N)": req_chemical_name = "337"
	if req['chemical_name'] == "1,3-Butadiynyl radical (CC(13)CCH)": req_chemical_name = "339"
	if req['chemical_name'] == "Methylene amidogen (H2CN)": req_chemical_name = "341"
	if req['chemical_name'] == "Amidogen (NH2)": req_chemical_name = "351"
	if req['chemical_name'] == "3-Oxo-1,2-Propadienylidene (CCCO)": req_chemical_name = "352"
	if req['chemical_name'] == "3-Thioxo-1,2-Propadieylidene (CCCS)": req_chemical_name = "353"
	if req['chemical_name'] == "Ethynyl (C(13)CH)": req_chemical_name = "355"
	if req['chemical_name'] == "Sulfur Dioxide (OS(17)O)": req_chemical_name = "356"
	if req['chemical_name'] == "Diazenylium (N(15)NH+)": req_chemical_name = "360"
	if req['chemical_name'] == "Cyanoacetylene (HC3N v4=1)": req_chemical_name = "368"
	if req['chemical_name'] == "1,3-Butadiynyl radical (C4H v7 = 1)": req_chemical_name = "369"
	if req['chemical_name'] == "Cyanide Radical (C(15)N)": req_chemical_name = "371"
	if req['chemical_name'] == "Cyanoethynyl (C(13)CCN)": req_chemical_name = "372"
	if req['chemical_name'] == "3-Silanetetrayl-1,2-Propadienylidene  (c-SiC3)": req_chemical_name = "374"
	if req['chemical_name'] == "Hexatrienyl (l-C6H2)": req_chemical_name = "375"
	if req['chemical_name'] == "Vinyl Alcohol (s-H2CCHOH)": req_chemical_name = "379"
	if req['chemical_name'] == "Butatrienylidene (l-C4H2)": req_chemical_name = "385"
	if req['chemical_name'] == "Thioformaldehyde (H2C(34)S)": req_chemical_name = "387"
	if req['chemical_name'] == "Methyltriacetylene (CH3C6H)": req_chemical_name = "388"
	if req['chemical_name'] == "Hydrochloric acid (H(37)Cl)": req_chemical_name = "392"
	if req['chemical_name'] == "Methyl Formate (CH3OCHO v=0)": req_chemical_name = "393"
	if req['chemical_name'] == "Formic Acid (t-HCOOD)": req_chemical_name = "400"
	if req['chemical_name'] == "Methyl Cyanide (CH3(13)CN)": req_chemical_name = "401"
	if req['chemical_name'] == "Hydrogen sulfide (HDS)": req_chemical_name = "402"
	if req['chemical_name'] == "Aluminum Monofluoride (AlF v=0)": req_chemical_name = "403"
	if req['chemical_name'] == "Cyclopropenylidene (c-HCC(13)CH)": req_chemical_name = "410"
	if req['chemical_name'] == "Water (H2O v=0)": req_chemical_name = "418"
	if req['chemical_name'] == "Protonated Carbon Dioxide (HOCO+)": req_chemical_name = "430"
	if req['chemical_name'] == "Aluminum Monochloride (Al(37)Cl v=0)": req_chemical_name = "431"
	if req['chemical_name'] == "trans-Ethanol (t-CH3CH2OH)": req_chemical_name = "436"
	if req['chemical_name'] == "Methyl isocyanide (CH3NC)": req_chemical_name = "445"
	if req['chemical_name'] == "Cyanamide (NH2CN)": req_chemical_name = "449"
	if req['chemical_name'] == "Magnesium Cyanide (MgCN)": req_chemical_name = "451"
	if req['chemical_name'] == "Nitrous Oxide (N2O v=0)": req_chemical_name = "453"
	if req['chemical_name'] == "Oxoethenylidene (CCO)": req_chemical_name = "454"
	if req['chemical_name'] == "Lithium Hydride (LiH v=0)": req_chemical_name = "463"
	if req['chemical_name'] == "Isocyanic Acid (DNCO)": req_chemical_name = "468"
	if req['chemical_name'] == "Methyliumylidene (CH+)": req_chemical_name = "469"
	if req['chemical_name'] == "Water (HDO)": req_chemical_name = "472"
	if req['chemical_name'] == "Hydrogen Isocyanide (HN(13)C)": req_chemical_name = "473"
	if req['chemical_name'] == "Phosphorous nitride (PN v=0)": req_chemical_name = "482"
	if req['chemical_name'] == "Methyl Acetylene (CH3C(13)CH)": req_chemical_name = "484"
	if req['chemical_name'] == "Ammonia ((15)NH3)": req_chemical_name = "485"
	if req['chemical_name'] == "Methyl Acetylene ((13)CH3CCH)": req_chemical_name = "486"
	if req['chemical_name'] == "Hydrogen Isocyanide (H(15)NC)": req_chemical_name = "489"
	if req['chemical_name'] == "Molecular oxygen (O2 v=0)": req_chemical_name = "490"
	if req['chemical_name'] == "Ammonia (NH3 v2=1)": req_chemical_name = "491"
	if req['chemical_name'] == "Silicon Carbide (SiC2 v=0)": req_chemical_name = "492"
	if req['chemical_name'] == "Cyclopropenylidene (c-HCCCH v=0)": req_chemical_name = "493"
	if req['chemical_name'] == "Dimethyl ether (CH3OCH3)": req_chemical_name = "495"
	if req['chemical_name'] == "Silicon monosulfide (Si(34)S v=0)": req_chemical_name = "497"
	if req['chemical_name'] == "Sulfur Monoxide ion (SO+)": req_chemical_name = "504"
	if req['chemical_name'] == "Cyclopropenylidene (c-HCCCD)": req_chemical_name = "507"
	if req['chemical_name'] == "Aluminum Monochloride (AlCl v=0)": req_chemical_name = "521"
	if req['chemical_name'] == "Hydroxyl (OH v=0)": req_chemical_name = "523"
	if req['chemical_name'] == "3-Imino-1,2 Propadienylidene (HNCCC)": req_chemical_name = "528"
	if req['chemical_name'] == "Acetaldehyde (CH3CHO vt=0)": req_chemical_name = "529"
	if req['chemical_name'] == "Hydrogen fluoride (HF)": req_chemical_name = "535"
	if req['chemical_name'] == "Phosphorus Monoxide (PO)": req_chemical_name = "541"
	if req['chemical_name'] == "Sulfur dioxide (SO2 v2=1)": req_chemical_name = "546"
	if req['chemical_name'] == "Ethyl Cyanide (CH3CH2CN v=0)": req_chemical_name = "547"
	if req['chemical_name'] == "Ethyl Cyanide ((13)CH3CH2CN)": req_chemical_name = "549"
	if req['chemical_name'] == "Vinyl Cyanide  ((13)CH2CHCN)": req_chemical_name = "551"
	if req['chemical_name'] == "Thioxoethenylidene (C(13)CS)": req_chemical_name = "558"
	if req['chemical_name'] == "Ethyne Isocyanide (HCCNC v=0)": req_chemical_name = "564"
	if req['chemical_name'] == "Formamide (NH2CHO)": req_chemical_name = "573"
	if req['chemical_name'] == "Cyanobutadiyne (HC(13)CCCCN)": req_chemical_name = "578"
	if req['chemical_name'] == "Hydrogen sulfide (H2S)": req_chemical_name = "582"
	if req['chemical_name'] == "Silicon monosulfide   ((29)SiS v=0)": req_chemical_name = "586"
	if req['chemical_name'] == "2,4-Pentadiynylidyne (l-C5D)": req_chemical_name = "589"
	if req['chemical_name'] == "Nitric sulfide (NS, v=0)": req_chemical_name = "595"
	if req['chemical_name'] == "Silicon monosulfide ((30)SiS v=0)": req_chemical_name = "598"
	if req['chemical_name'] == "Methyl Cyanide (CH3CN v=0)": req_chemical_name = "606"
	if req['chemical_name'] == "Nitric sulfide (N(34)S)": req_chemical_name = "607"
	if req['chemical_name'] == "Nitrosyl hydride (HNO)": req_chemical_name = "618"
	if req['chemical_name'] == "Methyl Cyanide (CH3C(15)N)": req_chemical_name = "619"
	if req['chemical_name'] == "Water (H2(18)O v=0)": req_chemical_name = "620"
	if req['chemical_name'] == "Thioxoethenylidene ((13)CCS)": req_chemical_name = "624"
	if req['chemical_name'] == "Ethyl Cyanide (CH3CH2(13)CN)": req_chemical_name = "631"
	if req['chemical_name'] == "Water (H2O v2=1)": req_chemical_name = "637"
	if req['chemical_name'] == "Ammonia (NH3 v=0)": req_chemical_name = "638"
	if req['chemical_name'] == "Vinyl Cyanide  (CH2(13)CHCN)": req_chemical_name = "646"
	if req['chemical_name'] == "Methyl Cyanide ((13)CH3CN)": req_chemical_name = "651"
	if req['chemical_name'] == "Silicon monosulfide   (SiS v=0)": req_chemical_name = "652"
	if req['chemical_name'] == "Hydrochloric acid (HCl)": req_chemical_name = "655"
	if req['chemical_name'] == "Methanimine (CH2NH)": req_chemical_name = "664"
	if req['chemical_name'] == "Hydroxyl (18OH)": req_chemical_name = "665"
	if req['chemical_name'] == "Isocyanic Acid (HNCO v=0)": req_chemical_name = "673"
	if req['chemical_name'] == "Cyclopropenylidene (c-H(13)CCCH)": req_chemical_name = "682"
	if req['chemical_name'] == "Thioxoethenylidene (CC(34)S)": req_chemical_name = "685"
	if req['chemical_name'] == "Atomic Deuterium (D)": req_chemical_name = "697"
	if req['chemical_name'] == "Atomic Hydrogen (H)": req_chemical_name = "699"
	if req['chemical_name'] == "Formic Acid (t-DCOOH)": req_chemical_name = "706"
	if req['chemical_name'] == "Vinyl Cyanide  (CH2CH(13)CN)": req_chemical_name = "707"
	if req['chemical_name'] == "Carbon Monoxide Ion (CO+)": req_chemical_name = "709"
	if req['chemical_name'] == "Nitric oxide (NO)": req_chemical_name = "713"
	if req['chemical_name'] == "Ethyl Cyanide (CH3(13)CH2CN)": req_chemical_name = "717"
	if req['chemical_name'] == "Formyl Radical (HCO)": req_chemical_name = "727"
	if req['chemical_name'] == "2-Propynal (HCCCHO)": req_chemical_name = "729"
	if req['chemical_name'] == "Sodium Cyanide (NaCN/NaNC)": req_chemical_name = "736"
	if req['chemical_name'] == "Cyanomethyl (CH2CN)": req_chemical_name = "748"
	if req['chemical_name'] == "Vinyl Cyanide (CH2CHCN v=0)": req_chemical_name = "758"
	if req['chemical_name'] == "Hydrogen sulfide (H2(34)S)": req_chemical_name = "776"
	if req['chemical_name'] == "Silicon Carbide (Si(13)CC)": req_chemical_name = "791"
	if req['chemical_name'] == "Hydroxyl ((17)OH)": req_chemical_name = "801"
	if req['chemical_name'] == "Hydrogen Isocyanide (D(15)NC)": req_chemical_name = "808"
	if req['chemical_name'] == "Methanol (CH3OD)": req_chemical_name = "813"
	if req['chemical_name'] == "Acetone ((CH3)2CO v=0)": req_chemical_name = "819"
	if req['chemical_name'] == "Methylamine (CH3NH2)": req_chemical_name = "828"
	if req['chemical_name'] == "Silicon monosulfide (Si(33)S v=0)": req_chemical_name = "833"
	if req['chemical_name'] == "Methyl Mercaptan (CH3SH v=0)": req_chemical_name = "841"
	if req['chemical_name'] == "Silicon Carbide ((30)SiC2)": req_chemical_name = "849"
	if req['chemical_name'] == "Propenal (t-CH2CHCHO)": req_chemical_name = "853"
	if req['chemical_name'] == "Silicon Carbide ((29)SiC2)": req_chemical_name = "872"
	if req['chemical_name'] == "Methanol (CH2DOH)": req_chemical_name = "874"
	if req['chemical_name'] == "Formamide (NH2(13)CHO)": req_chemical_name = "875"
	if req['chemical_name'] == "Magnesium Isocyanide ((26)MgNC)": req_chemical_name = "885"
	if req['chemical_name'] == "Methanol (CH3(18)OH)": req_chemical_name = "892"
	if req['chemical_name'] == "Methyl Cyanide (CH3CN v8=1)": req_chemical_name = "1041"
	if req['chemical_name'] == "Methanol (CHD2OH)": req_chemical_name = "906"
	if req['chemical_name'] == "Silicon monosulfide   ((30)Si(34)S v=0)": req_chemical_name = "934"
	if req['chemical_name'] == "Acetic Acid (CH3COOH v=0)": req_chemical_name = "941"
	if req['chemical_name'] == "Methylidyne (CH 2P3/2)": req_chemical_name = "963"
	if req['chemical_name'] == "Carbon Monosulfide (CS v=1)": req_chemical_name = "994"
	if req['chemical_name'] == "Hydrogen Cyanide (HCN v2=2)": req_chemical_name = "964"
	if req['chemical_name'] == "Hydrogen Cyanide (HCN v3=1)": req_chemical_name = "966"
	if req['chemical_name'] == "Hydrogen Cyanide (HCN v1=1)": req_chemical_name = "967"
	if req['chemical_name'] == "Hydrogen Isocyanide (HNC v2=1)": req_chemical_name = "971"
	if req['chemical_name'] == "Hydrogen Recombination Line (H(alpha))": req_chemical_name = "1154"
	if req['chemical_name'] == "Methanol (CH3OH vt=1)": req_chemical_name = "984"
	if req['chemical_name'] == "Methanol ((13)CH3OH vt=1)": req_chemical_name = "985"
	if req['chemical_name'] == "Methanol (CD3OH)": req_chemical_name = "986"
	if req['chemical_name'] == "Carbon Monoxide (CO v=1)": req_chemical_name = "990"
	if req['chemical_name'] == "Carbon Monosulfide (C(34)S v=1)": req_chemical_name = "1001"
	if req['chemical_name'] == "Acetaldehyde (CH3CHO vt=1)": req_chemical_name = "1042"
	if req['chemical_name'] == "Acetaldehyde (CH3CHO vt=2)": req_chemical_name = "1043"
	if req['chemical_name'] == "gauche-Ethanol (g-CH3CH2OH)": req_chemical_name = "1044"
	if req['chemical_name'] == "Cyanoacetylene (HC3N v7=3)": req_chemical_name = "1045"
	if req['chemical_name'] == "Cyanoacetylene (HC3N v5=1)": req_chemical_name = "1046"
	if req['chemical_name'] == "Vinyl Cyanide (CH2CHCN v11=1)": req_chemical_name = "1048"
	if req['chemical_name'] == "Vinyl Cyanide (CH2CHCN v11=2)": req_chemical_name = "1049"
	if req['chemical_name'] == "Vinyl Cyanide (CH2CHCN v15=1)": req_chemical_name = "1050"
	if req['chemical_name'] == "Ethyl Cyanide (CH3CH2CN v=1)": req_chemical_name = "1052"
	if req['chemical_name'] == "Propanal (CH3CH2CHO)": req_chemical_name = "1053"
	if req['chemical_name'] == "1,3-Butadiynyl anion (C4H-)": req_chemical_name = "1055"
	if req['chemical_name'] == "1,3,5,7-Octatetraynyl anion (C8H-)": req_chemical_name = "1057"
	if req['chemical_name'] == "Hydrogen sulfide (D2S)": req_chemical_name = "1076"
	if req['chemical_name'] == "Silicon Monoxide (SiO v=1)": req_chemical_name = "1089"
	if req['chemical_name'] == "Silicon Monoxide (SiO v=2)": req_chemical_name = "1090"
	if req['chemical_name'] == "Silicon Monoxide (SiO v=3)": req_chemical_name = "1091"
	if req['chemical_name'] == "Silicon Monoxide (SiO v=4)": req_chemical_name = "1092"
	if req['chemical_name'] == "Silicon Monoxide (SiO v=5)": req_chemical_name = "1093"
	if req['chemical_name'] == "Silicon Monoxide (SiO v=6)": req_chemical_name = "1094"
	if req['chemical_name'] == "Silicon Monoxide ((29)SiO v=1)": req_chemical_name = "1095"
	if req['chemical_name'] == "Silicon Monoxide ((29)SiO v=2)": req_chemical_name = "1096"
	if req['chemical_name'] == "Silicon Monoxide ((30)SiO v=1)": req_chemical_name = "1100"
	if req['chemical_name'] == "Silicon Monoxide ((30)SiO v=2)": req_chemical_name = "1101"
	if req['chemical_name'] == "Silicon monosulfide (SiS v=1)": req_chemical_name = "1112"
	if req['chemical_name'] == "Silicon monosulfide (SiS v=2)": req_chemical_name = "1113"
	if req['chemical_name'] == "Silicon monosulfide (SiS v=3)": req_chemical_name = "1114"
	if req['chemical_name'] == "Acetamide (CH3CONH2)": req_chemical_name = "1173"
	if req['chemical_name'] == "Hydrogen Recombination Line (H(beta))": req_chemical_name = "1155"
	if req['chemical_name'] == "Hydrogen Recombination Line (H(gamma))": req_chemical_name = "1156"
	if req['chemical_name'] == "Hydrogen Recombination Line (H(delta))": req_chemical_name = "1157"
	if req['chemical_name'] == "Hydrogen Recombination Line (H(epsilon))": req_chemical_name = "1158"
	if req['chemical_name'] == "Hydrogen Recombination Line (H(zeta))": req_chemical_name = "1159"
	if req['chemical_name'] == "Helium Recombination Line (He(alpha))": req_chemical_name = "1160"
	if req['chemical_name'] == "Helium Recombination Line (He(beta))": req_chemical_name = "1161"
	if req['chemical_name'] == "Helium Recombination Line (He(gamma))": req_chemical_name = "1162"
	if req['chemical_name'] == "Helium Recombination Line (He(delta))": req_chemical_name = "1163"
	if req['chemical_name'] == "Carbon Recombination Line (C(alpha))": req_chemical_name = "1164"
	if req['chemical_name'] == "Carbon Recombination Line (C(beta))": req_chemical_name = "1165"
	if req['chemical_name'] == "Carbon Recombination Line (C(gamma))": req_chemical_name = "1166"
	if req['chemical_name'] == "Hydrogen Cyanide (HCN v2=4)": req_chemical_name = "1179"
	if req['chemical_name'] == "Hydrogen Cyanide (HCN v2=1^1-v2=4^0)": req_chemical_name = "1180"
	if req['chemical_name'] == "Formylium (HCO+ v=0)": req_chemical_name = "15"
	if req['chemical_name'] == "Cyanoacetylene (HC3N v5=1,v7=1)": req_chemical_name = "1198"
	if req['chemical_name'] == "Cyanoacetylene (HC3N v6=1, v7=2)": req_chemical_name = "1199"
	if req['chemical_name'] == "Cyanoacetylene (HC3N v6=2)": req_chemical_name = "1201"
	if req['chemical_name'] == "Cyanoacetylene (HC3N v7=4)": req_chemical_name = "1202"
	if req['chemical_name'] == "Isocyanic Acid (HNCO v4=1)": req_chemical_name = "1244"
	if req['chemical_name'] == "Isocyanic Acid (HNCO v5=1)": req_chemical_name = "1245"
	if req['chemical_name'] == "Isocyanic Acid (HNCO v6=1)": req_chemical_name = "1246"
	if req['chemical_name'] == "Cyanoethynylide ion (C3N-)": req_chemical_name = "1264"
	if req['chemical_name'] == "Silicon Carbide (SiC2 v3=1)": req_chemical_name = "1268"
	if req['chemical_name'] == "Phosphapropynylidyne (CCP)": req_chemical_name = "1274"
	if req['chemical_name'] == "Aminoacetonitrile (H2NCH2CN)": req_chemical_name = "1277"
	if req['chemical_name'] == "Acetone ((CH3)2CO vt=1)": req_chemical_name = "1281"
	if req['chemical_name'] == "Cyanobutadiynylide anion (C5N-)": req_chemical_name = "1308"
	if req['chemical_name'] == "Methyl Formate (CH3OCHO v=1)": req_chemical_name = "1333"
	if req['chemical_name'] == "Fulminic acid (HCNO)": req_chemical_name = "1352"
	if req['chemical_name'] == "Cyanic acid (HOCN)": req_chemical_name = "1353"
	if req['chemical_name'] == "Atomic Carbon (CII)": req_chemical_name = "1364"
	if req['chemical_name'] == "Atomic Helium (3He+)": req_chemical_name = "1365"
	if req['chemical_name'] == "Atomic Nitrogen (NII)": req_chemical_name = "1366"
	if req['chemical_name'] == "Atomic Oxygen (OI)": req_chemical_name = "1367"
	if req['chemical_name'] == "Atomic Oxygen (OIII)": req_chemical_name = "1368"
	if req['chemical_name'] == "Atomic Carbon (13CII(13))": req_chemical_name = "1378"
	if req['chemical_name'] == "ortho-Oxidaniumyl (o-H2O+)": req_chemical_name = "1397"
	if req['chemical_name'] == "para-Oxidaniumyl (p-H3O+)": req_chemical_name = "1398"
	if req['chemical_name'] == "Propynylidynium (C3H+)": req_chemical_name = "1413"
	if req['chemical_name'] == "Cyanomethanimine (E-HNCHCN)": req_chemical_name = "1416"
	
	req['chemical_name'] = req['chemical_name'].lower()

	if req['chemical_name'] == "h2o": 
		req_chemical_name = "Water"
	
	if req['chemical_name'] == "carbon": 
		req_chemical_name = "atomic carbon"
	
	if req['chemical_name'] == "nitrogen": 
		req_chemical_name = "atomic nitrogen"
	
	if req['chemical_name'] == "oxygen": 
		req_chemical_name = "atomic oxygen"
	
	if req['chemical_name'] == "co": 
		req_chemical_name = "carbon monoxide"
	
	if req['chemical_name'] == "nh3": 
		req_chemical_name = "ammonia"
	
	if req['chemical_name'] == "ch3oh": 
		req_chemical_name = "methanol"
	
	if req['chemical_name'] == "o2": 
		req_chemical_name = "molecular oxygen"
	
	if req['chemical_name'] == "h": 
		req_chemical_name = "hydrogen recombination line"
	
	if req['chemical_name'] == "hcn" or req['chemical_name'] == "dcn": 
		req_chemical_name = "hydrogen cyanide"
	
	if req['chemical_name'] == "hco+" or req['chemical_name'] == "dco+": 
		req_chemical_name = "formylium"
	
	if req['chemical_name'] == "cs": 
		req_chemical_name = "carbon monosulfide"
	
	if req['chemical_name'] == "oh": 
		req_chemical_name = "hydroxyl"
	
	################################################
	# Search top20s
	################################################

	select_where = array_push_if(select_where, "s.%s=1" % req_top20, has_value(req_top20))
	select_where = array_push_if(select_where, "potential != 1", has_value(req_no_potential))
	select_where = array_push_if(select_where, "probable != 1", has_value(req_no_probable))
	select_where = array_push_if(select_where, "known_ast_molecules != 1", has_value(req_known))

	select_where = array_push_if(select_where, "Lovas_NRAO = 1", has_value(req['include_only_nrao']))
	select_where = array_push_if(select_where, "((frequency > 0 and uncertainty <= 50) or (measfreq > 0 and measerrfreq <= 50))", has_value(req_fel))
	select_where = array_push_if(select_where, "(resolved_QNs NOT LIKE '%F=%')", has_value(req_noHFS))
	
	select_where = array_push_if(select_where, "intintensity>=%s" % mysql_real_escape_string(req_il), has_value(req_intl))	
	if (req_chemical_name > 0):
		select_where = array_push_if(select_where, "m.species_id = '%s'" % req_chemical_name, has_value(req_chemical_name))
	else:
		select_where = array_push_if(select_where, "chemical_name = '%s'" % req_chemical_name, has_value(req_chemical_name))
	  
	select_where = array_push_if(select_where, "quantum_numbers like '%%s%'" % mysql_real_escape_string(tran), has_value(req_trans))
	
	if (count(req["sid"]) == 1):
        select_where = array_push_if(select_where, "m.species_id=%s", mysql_real_escape_string(req_sid[0]), has_value(req_sid[0]))
     
    elseif (count(req["sid"]) > 1): 
        sids = req["sid"]
        array_map("mysql_real_escape_string", sids)
        sids = join(",", sids)
        select_where = array_push(select_where, "m.species_id in (%s)", sids)
    

    if (has_value(req_data_version)):
        select_where = array_push_if(select_where, "m.`v1.0` = 1", req_data_version == "v1.0")
        select_where = array_push_if(select_where, "m.`v2.0` = 2", req_data_version == "v2.0")
    
    lines = array_push_if(lines, "10", has_value(req_displayCDMS))
    lines = array_push_if(lines, "11", has_value(req_displayLovas))
    lines = array_push_if(lines, "12", has_value(req_displayJPL))
    lines = array_push_if(lines, "14", has_value(req_displaySLAIM))
    lines = array_push_if(lines, "15", has_value(req_displayRecomb))
    lines = array_push_if(lines, "16", has_value(req_displayToyaMA))
    lines = array_push_if(lines, "17", has_value(req_displayOSU))
    lines = array_push_if(lines, "18", has_value(req_displayLisa))
    lines = array_push_if(lines, "19", has_value(req_displayRFI))

    lines_clean = lines
    array_map("mysql_real_escape_string", lines_clean)
    select_where = array_push(select_where, "ll_id in (" + ", ".join(lines_clean) + ")")
    
def array_push(array, string):
	return array.append(string)
	
def array_map(fun, array):
	method_list = dir(sys.modules[__name__])
	for m in method_list:
		if m == fun:
			print 'yomknKSNI'
	
	
line = 
	'sid' : 1,
	
req = 
	'from' : '',
	'to' : '',
	'frequency_units' : 'MHz',
	'band' : 'alma5',
	'energy_range_type' : "eu_k",
	'energy_range_from' : '',
	'energy_range_to' : ''
	
	
name = ''
amount = ''
start = 1
end = 500
fre =  describe_results(req, name, amount, start, end)
print fre