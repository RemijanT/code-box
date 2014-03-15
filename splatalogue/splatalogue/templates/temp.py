	if (req_display_recomb == '' or req_display_recomb is None)  and 
		(req_display_cdms == '' or req_display_cdms is None) and 
		(req_display_jpl == '' or req_display_jpl is None) and 
		(req_display_lovas == '' or req_display_lovas is None) and 
		(req_display_slaim == '' or req_display_slaim is None) and 
		(req_display_toyama == '' or req_display_toyama is None) and 
		(req_display_osu == '' or req_display_osu is None) and 
		(req_display_lisa == '' or req_display_lisa is None) and 
		(req_display_rfi == '' or req_display_rfi is None):
		print "Please select a linelist catalogue"
		return
	
	if (req_z == "" or req_z is None):
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
     
	elif (count(req["sid"]) > 1): 
		sids = req['sid']
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
	

	# Swap the from and to values if from is greater than to
	if (has_number(req_from) and has_number(req_to) and req_from > req_to):
		 tmp = req_from
		 req_from = req_to
		 req_to = tmp
	

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

	if (req['from'] == '' or req['to'] == ''):
		a = mysql_real_escape_string(req_from)
		array_push_if(select_where, ('orderedfreq>=%s' % (a)), has_number(req_from))	
		a = mysql_real_escape_string(req_to)
		array_push_if(select_where, ('orderedfreq<=%s' % (a)), has_number(req_to))	
	
	elif ((req['from'] != '' or req['to'] != '') and req['from2'] == ''):
		a = mysql_real_escape_string(req_from)
		array_push_if(select_where, ('orderedfreq>=%s' % (a)), has_number(req_from))	
		a = mysql_real_escape_string(req_to)
		array_push_if(select_where, ('orderedfreq<=%s' % (a)), has_number(req_to))	
	
	elif ((req['from2'] != '' or req['to2'] != '') and (req['from3'] == '' or req['to3'] == '')):
		array_push_if(select_where, ('((orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s))' % (mysql_real_escape_string(req_from), mysql_real_escape_string(req_to), mysql_real_escape_string(req_from2), mysql_real_escape_string(req_to2))), has_number(req_from2))	
	
	elif (req['from3'] != '' and req['from4'] == ''):
		array_push_if(select_where, ('((orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s))' % (mysql_real_escape_string(req_from), mysql_real_escape_string(req_to), mysql_real_escape_string(req_from2), mysql_real_escape_string(req_to2), mysql_real_escape_string(req_from3), mysql_real_escape_string(req_to3))), has_number(req_from2))	
	
	elif (req['from4'] != '' and req['from5'] == ''):
		array_push_if(select_where, ('((orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s))' % (mysql_real_escape_string(req_from), mysql_real_escape_string(req_to), mysql_real_escape_string(req_from2), mysql_real_escape_string(req_to2), mysql_real_escape_string(req_from3), mysql_real_escape_string(req_to3), mysql_real_escape_string(req_from4), mysql_real_escape_string(req_to4))), has_number(req_from2))	
	
	elif (req['from5'] != '' and req['from6'] == ''):
		array_push_if(select_where, ('((orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s))' % (mysql_real_escape_string(req_from), mysql_real_escape_string(req_to), mysql_real_escape_string(req_from2), mysql_real_escape_string(req_to2), mysql_real_escape_string(req_from3), mysql_real_escape_string(req_to3), mysql_real_escape_string(req_from4), mysql_real_escape_string(req_to4), mysql_real_escape_string(req_from5), mysql_real_escape_string(req_to5))), has_number(req_from2))	
	
	elif (req['from6'] != '' and req['from7'] == ''):
		array_push_if(select_where, ('((orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s))' % (mysql_real_escape_string(req_from), mysql_real_escape_string(req_to), mysql_real_escape_string(req_from2), mysql_real_escape_string(req_to2), mysql_real_escape_string(req_from3), mysql_real_escape_string(req_to3), mysql_real_escape_string(req_from4), mysql_real_escape_string(req_to4), mysql_real_escape_string(req_from5), mysql_real_escape_string(req_to5), mysql_real_escape_string(req_from6), mysql_real_escape_string(req_to6))), has_number(req_from2))	
	
	elif (req['from7'] != '' and req['from8'] == ''):
		array_push_if(select_where, ('((orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s))' % (mysql_real_escape_string(req_from), mysql_real_escape_string(req_to), mysql_real_escape_string(req_from2), mysql_real_escape_string(req_to2), mysql_real_escape_string(req_from3), mysql_real_escape_string(req_to3), mysql_real_escape_string(req_from4), mysql_real_escape_string(req_to4), mysql_real_escape_string(req_from5), mysql_real_escape_string(req_to5), mysql_real_escape_string(req_from6), mysql_real_escape_string(req_to6), mysql_real_escape_string(req_from7), mysql_real_escape_string(req_to7))), has_number(req_from2))	
	
	elif (req['from8'] != '' and req['from9'] == ''):
		array_push_if(select_where, ('((orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s))' % (mysql_real_escape_string(req_from), mysql_real_escape_string(req_to), mysql_real_escape_string(req_from2), mysql_real_escape_string(req_to2), mysql_real_escape_string(req_from3), mysql_real_escape_string(req_to3), mysql_real_escape_string(req_from4), mysql_real_escape_string(req_to4), mysql_real_escape_string(req_from5), mysql_real_escape_string(req_to5), mysql_real_escape_string(req_from6), mysql_real_escape_string(req_to6), mysql_real_escape_string(req_from7), mysql_real_escape_string(req_to7), mysql_real_escape_string(req_from8), mysql_real_escape_string(req_to8))), has_number(req_from2))	
	
	elif (req['from9'] != '' and req['from10'] == ''):
		array_push_if(select_where, ('((orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s))' % (mysql_real_escape_string(req_from), mysql_real_escape_string(req_to), mysql_real_escape_string(req_from2), mysql_real_escape_string(req_to2), mysql_real_escape_string(req_from3), mysql_real_escape_string(req_to3), mysql_real_escape_string(req_from4), mysql_real_escape_string(req_to4), mysql_real_escape_string(req_from5), mysql_real_escape_string(req_to5), mysql_real_escape_string(req_from6), mysql_real_escape_string(req_to6), mysql_real_escape_string(req_from7), mysql_real_escape_string(req_to7), mysql_real_escape_string(req_from8), mysql_real_escape_string(req_to8), mysql_real_escape_string(req_from9), mysql_real_escape_string(req_to9))), has_number(req_from2))	
	
	elif (req['from10'] != '' and req['from11'] == ''):
		array_push_if(select_where, ('((orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s))' % (mysql_real_escape_string(req_from), mysql_real_escape_string(req_to), mysql_real_escape_string(req_from2), mysql_real_escape_string(req_to2), mysql_real_escape_string(req_from3), mysql_real_escape_string(req_to3), mysql_real_escape_string(req_from4), mysql_real_escape_string(req_to4), mysql_real_escape_string(req_from5), mysql_real_escape_string(req_to5), mysql_real_escape_string(req_from6), mysql_real_escape_string(req_to6), mysql_real_escape_string(req_from7), mysql_real_escape_string(req_to7), mysql_real_escape_string(req_from8), mysql_real_escape_string(req_to8), mysql_real_escape_string(req_from9), mysql_real_escape_string(req_to9), mysql_real_escape_string(req_from10), mysql_real_escape_string(req_to10))), has_number(req_from2))	
	
	elif (req['from11'] != '' and req['from12'] == ''):
		array_push_if(select_where, ('((orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s))' % (mysql_real_escape_string(req_from), mysql_real_escape_string(req_to), mysql_real_escape_string(req_from2), mysql_real_escape_string(req_to2), mysql_real_escape_string(req_from3), mysql_real_escape_string(req_to3), mysql_real_escape_string(req_from4), mysql_real_escape_string(req_to4), mysql_real_escape_string(req_from5), mysql_real_escape_string(req_to5), mysql_real_escape_string(req_from6), mysql_real_escape_string(req_to6), mysql_real_escape_string(req_from7), mysql_real_escape_string(req_to7), mysql_real_escape_string(req_from8), mysql_real_escape_string(req_to8), mysql_real_escape_string(req_from9), mysql_real_escape_string(req_to9), mysql_real_escape_string(req_from10), mysql_real_escape_string(req_to10), mysql_real_escape_string(req_from11), mysql_real_escape_string(req_to11))), has_number(req_from2))	
	
	elif (req['from12'] != '' and req['from13'] == ''):
		array_push_if(select_where, ('((orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s))' % (mysql_real_escape_string(req_from), mysql_real_escape_string(req_to), mysql_real_escape_string(req_from2), mysql_real_escape_string(req_to2), mysql_real_escape_string(req_from3), mysql_real_escape_string(req_to3), mysql_real_escape_string(req_from4), mysql_real_escape_string(req_to4), mysql_real_escape_string(req_from5), mysql_real_escape_string(req_to5), mysql_real_escape_string(req_from6), mysql_real_escape_string(req_to6), mysql_real_escape_string(req_from7), mysql_real_escape_string(req_to7), mysql_real_escape_string(req_from8), mysql_real_escape_string(req_to8), mysql_real_escape_string(req_from9), mysql_real_escape_string(req_to9), mysql_real_escape_string(req_from10), mysql_real_escape_string(req_to10), mysql_real_escape_string(req_from11), mysql_real_escape_string(req_to11), mysql_real_escape_string(req_from12), mysql_real_escape_string(req_to12))), has_number(req_from2))	
	
	elif (req['from13'] != '' and req['from14'] == ''):
		array_push_if(select_where, ('((orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s))' % (mysql_real_escape_string(req_from), mysql_real_escape_string(req_to), mysql_real_escape_string(req_from2), mysql_real_escape_string(req_to2), mysql_real_escape_string(req_from3), mysql_real_escape_string(req_to3), mysql_real_escape_string(req_from4), mysql_real_escape_string(req_to4), mysql_real_escape_string(req_from5), mysql_real_escape_string(req_to5), mysql_real_escape_string(req_from6), mysql_real_escape_string(req_to6), mysql_real_escape_string(req_from7), mysql_real_escape_string(req_to7), mysql_real_escape_string(req_from8), mysql_real_escape_string(req_to8), mysql_real_escape_string(req_from9), mysql_real_escape_string(req_to9), mysql_real_escape_string(req_from10), mysql_real_escape_string(req_to10), mysql_real_escape_string(req_from11), mysql_real_escape_string(req_to11), mysql_real_escape_string(req_from12), mysql_real_escape_string(req_to12), mysql_real_escape_string(req_from13), mysql_real_escape_string(req_to13))), has_number(req_from2))	
	
	elif (req['from14'] != '' and req['from15'] == ''):
		array_push_if(select_where, ('((orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s))' % (mysql_real_escape_string(req_from), mysql_real_escape_string(req_to), mysql_real_escape_string(req_from2), mysql_real_escape_string(req_to2), mysql_real_escape_string(req_from3), mysql_real_escape_string(req_to3), mysql_real_escape_string(req_from4), mysql_real_escape_string(req_to4), mysql_real_escape_string(req_from5), mysql_real_escape_string(req_to5), mysql_real_escape_string(req_from6), mysql_real_escape_string(req_to6), mysql_real_escape_string(req_from7), mysql_real_escape_string(req_to7), mysql_real_escape_string(req_from8), mysql_real_escape_string(req_to8), mysql_real_escape_string(req_from9), mysql_real_escape_string(req_to9), mysql_real_escape_string(req_from10), mysql_real_escape_string(req_to10), mysql_real_escape_string(req_from11), mysql_real_escape_string(req_to11), mysql_real_escape_string(req_from12), mysql_real_escape_string(req_to12), mysql_real_escape_string(req_from13), mysql_real_escape_string(req_to13), mysql_real_escape_string(req_from14), mysql_real_escape_string(req_to14))), has_number(req_from2))	
	
	elif (req['from15'] != '' and req['from16'] == ''):
		array_push_if(select_where, ('((orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s))' % (mysql_real_escape_string(req_from), mysql_real_escape_string(req_to), mysql_real_escape_string(req_from2), mysql_real_escape_string(req_to2), mysql_real_escape_string(req_from3), mysql_real_escape_string(req_to3), mysql_real_escape_string(req_from4), mysql_real_escape_string(req_to4), mysql_real_escape_string(req_from5), mysql_real_escape_string(req_to5), mysql_real_escape_string(req_from6), mysql_real_escape_string(req_to6), mysql_real_escape_string(req_from7), mysql_real_escape_string(req_to7), mysql_real_escape_string(req_from8), mysql_real_escape_string(req_to8), mysql_real_escape_string(req_from9), mysql_real_escape_string(req_to9), mysql_real_escape_string(req_from10), mysql_real_escape_string(req_to10), mysql_real_escape_string(req_from11), mysql_real_escape_string(req_to11), mysql_real_escape_string(req_from12), mysql_real_escape_string(req_to12), mysql_real_escape_string(req_from13), mysql_real_escape_string(req_to13), mysql_real_escape_string(req_from14), mysql_real_escape_string(req_to14), mysql_real_escape_string(req_from15), mysql_real_escape_string(req_to15))), has_number(req_from2))	
	
	elif (req['from16'] != '' and req['from17'] == ''):
		array_push_if(select_where, ('((orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s))' % (mysql_real_escape_string(req_from), mysql_real_escape_string(req_to), mysql_real_escape_string(req_from2), mysql_real_escape_string(req_to2), mysql_real_escape_string(req_from3), mysql_real_escape_string(req_to3), mysql_real_escape_string(req_from4), mysql_real_escape_string(req_to4), mysql_real_escape_string(req_from5), mysql_real_escape_string(req_to5), mysql_real_escape_string(req_from6), mysql_real_escape_string(req_to6), mysql_real_escape_string(req_from7), mysql_real_escape_string(req_to7), mysql_real_escape_string(req_from8), mysql_real_escape_string(req_to8), mysql_real_escape_string(req_from9), mysql_real_escape_string(req_to9), mysql_real_escape_string(req_from10), mysql_real_escape_string(req_to10), mysql_real_escape_string(req_from11), mysql_real_escape_string(req_to11), mysql_real_escape_string(req_from12), mysql_real_escape_string(req_to12), mysql_real_escape_string(req_from13), mysql_real_escape_string(req_to13), mysql_real_escape_string(req_from14), mysql_real_escape_string(req_to14), mysql_real_escape_string(req_from15), mysql_real_escape_string(req_to15), mysql_real_escape_string(req_from16), mysql_real_escape_string(req_to16))), has_number(req_from2))	
	
	elif (req['from17'] != '' and req['from18'] == ''):
		array_push_if(select_where, ('((orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s))' % (mysql_real_escape_string(req_from), mysql_real_escape_string(req_to), mysql_real_escape_string(req_from2), mysql_real_escape_string(req_to2), mysql_real_escape_string(req_from3), mysql_real_escape_string(req_to3), mysql_real_escape_string(req_from4), mysql_real_escape_string(req_to4), mysql_real_escape_string(req_from5), mysql_real_escape_string(req_to5), mysql_real_escape_string(req_from6), mysql_real_escape_string(req_to6), mysql_real_escape_string(req_from7), mysql_real_escape_string(req_to7), mysql_real_escape_string(req_from8), mysql_real_escape_string(req_to8), mysql_real_escape_string(req_from9), mysql_real_escape_string(req_to9), mysql_real_escape_string(req_from10), mysql_real_escape_string(req_to10), mysql_real_escape_string(req_from11), mysql_real_escape_string(req_to11), mysql_real_escape_string(req_from12), mysql_real_escape_string(req_to12), mysql_real_escape_string(req_from13), mysql_real_escape_string(req_to13), mysql_real_escape_string(req_from14), mysql_real_escape_string(req_to14), mysql_real_escape_string(req_from15), mysql_real_escape_string(req_to15), mysql_real_escape_string(req_from16), mysql_real_escape_string(req_to16), mysql_real_escape_string(req_from17), mysql_real_escape_string(req_to17))), has_number(req_from2))	
	
	elif (req['from18'] != '' and req['from19'] == ''):
		array_push_if(select_where, ('((orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s))' % (mysql_real_escape_string(req_from), mysql_real_escape_string(req_to), mysql_real_escape_string(req_from2), mysql_real_escape_string(req_to2), mysql_real_escape_string(req_from3), mysql_real_escape_string(req_to3), mysql_real_escape_string(req_from4), mysql_real_escape_string(req_to4), mysql_real_escape_string(req_from5), mysql_real_escape_string(req_to5), mysql_real_escape_string(req_from6), mysql_real_escape_string(req_to6), mysql_real_escape_string(req_from7), mysql_real_escape_string(req_to7), mysql_real_escape_string(req_from8), mysql_real_escape_string(req_to8), mysql_real_escape_string(req_from9), mysql_real_escape_string(req_to9), mysql_real_escape_string(req_from10), mysql_real_escape_string(req_to10), mysql_real_escape_string(req_from11), mysql_real_escape_string(req_to11), mysql_real_escape_string(req_from12), mysql_real_escape_string(req_to12), mysql_real_escape_string(req_from13), mysql_real_escape_string(req_to13), mysql_real_escape_string(req_from14), mysql_real_escape_string(req_to14), mysql_real_escape_string(req_from15), mysql_real_escape_string(req_to15), mysql_real_escape_string(req_from16), mysql_real_escape_string(req_to16), mysql_real_escape_string(req_from17), mysql_real_escape_string(req_to17), mysql_real_escape_string(req_from18), mysql_real_escape_string(req_to18))), has_number(req_from2))	
	
	elif (req['from19'] != '' and req['from20'] == ''):
		array_push_if(select_where, ('((orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s))' % (mysql_real_escape_string(req_from), mysql_real_escape_string(req_to), mysql_real_escape_string(req_from2), mysql_real_escape_string(req_to2), mysql_real_escape_string(req_from3), mysql_real_escape_string(req_to3), mysql_real_escape_string(req_from4), mysql_real_escape_string(req_to4), mysql_real_escape_string(req_from5), mysql_real_escape_string(req_to5), mysql_real_escape_string(req_from6), mysql_real_escape_string(req_to6), mysql_real_escape_string(req_from7), mysql_real_escape_string(req_to7), mysql_real_escape_string(req_from8), mysql_real_escape_string(req_to8), mysql_real_escape_string(req_from9), mysql_real_escape_string(req_to9), mysql_real_escape_string(req_from10), mysql_real_escape_string(req_to10), mysql_real_escape_string(req_from11), mysql_real_escape_string(req_to11), mysql_real_escape_string(req_from12), mysql_real_escape_string(req_to12), mysql_real_escape_string(req_from13), mysql_real_escape_string(req_to13), mysql_real_escape_string(req_from14), mysql_real_escape_string(req_to14), mysql_real_escape_string(req_from15), mysql_real_escape_string(req_to15), mysql_real_escape_string(req_from16), mysql_real_escape_string(req_to16), mysql_real_escape_string(req_from17), mysql_real_escape_string(req_to17), mysql_real_escape_string(req_from18), mysql_real_escape_string(req_to18), mysql_real_escape_string(req_from19), mysql_real_escape_string(req_to19))), has_number(req_from2))	
	
	elif (req['from20'] != ''):
		array_push_if(select_where, ('((orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s) or (orderedfreq>=%s and orderedfreq<=%s))' % (mysql_real_escape_string(req_from), mysql_real_escape_string(req_to), mysql_real_escape_string(req_from2), mysql_real_escape_string(req_to2), mysql_real_escape_string(req_from3), mysql_real_escape_string(req_to3), mysql_real_escape_string(req_from4), mysql_real_escape_string(req_to4), mysql_real_escape_string(req_from5), mysql_real_escape_string(req_to5), mysql_real_escape_string(req_from6), mysql_real_escape_string(req_to6), mysql_real_escape_string(req_from7), mysql_real_escape_string(req_to7), mysql_real_escape_string(req_from8), mysql_real_escape_string(req_to8), mysql_real_escape_string(req_from9), mysql_real_escape_string(req_to9), mysql_real_escape_string(req_from10), mysql_real_escape_string(req_to10), mysql_real_escape_string(req_from11), mysql_real_escape_string(req_to11), mysql_real_escape_string(req_from12), mysql_real_escape_string(req_to12), mysql_real_escape_string(req_from13), mysql_real_escape_string(req_to13), mysql_real_escape_string(req_from14), mysql_real_escape_string(req_to14), mysql_real_escape_string(req_from15), mysql_real_escape_string(req_to15), mysql_real_escape_string(req_from16), mysql_real_escape_string(req_to16), mysql_real_escape_string(req_from17), mysql_real_escape_string(req_to17), mysql_real_escape_string(req_from18), mysql_real_escape_string(req_to18), mysql_real_escape_string(req_from19), mysql_real_escape_string(req_to19), mysql_real_escape_string(req_from20), mysql_real_escape_string(req_to20))), has_number(req_from2))	
	
	else:
#		echo 'Frequency ranges were not selected!'	
		req['from20'] == ''	

	################################################
	# Energy range search
	################################################
	#	Swap the energy_range_from and energy_range_to values if energy_range_from is greater than energy_range_to
	if (has_number(req_energy_range_from) and has_number(req_energy_range_to) and req_energy_range_from > req_energy_range_to):
		tmp = req_energy_range_from
		req_energy_range_from = eto
		req_energy_range_to = tmp
	

	if (req_energy_range_type == 'el_cm1'):
		array_push_if(select_where, ('lower_state_energy>=%s' % mysql_real_escape_string(req_energy_range_from)), has_value(req_energy_range_from))
		array_push_if(select_where, ('lower_state_energy<=%s' % mysql_real_escape_string(req_energy_range_to)), has_value(req_energy_range_to))
	

	if (req_energy_range_type == 'eu_cm1'):
		array_push_if(select_where, ('upper_state_energy>=%s' % mysql_real_escape_string(req_energy_range_from)), has_value(req_energy_range_from))
		array_push_if(select_where, ('upper_state_energy<=%s' % mysql_real_escape_string(req_energy_range_to)), has_value(req_energy_range_to))
	

	if (req_energy_range_type == 'el_k'):
		array_push_if(select_where, ('lower_state_energy_K>=%s' % mysql_real_escape_string(req_energy_range_from)), has_value(req_energy_range_from))
		array_push_if(select_where, ('lower_state_energy_K<=%s' % mysql_real_escape_string(req_energy_range_to)), has_value(req_energy_range_to))
	

	if (req_energy_range_type == 'eu_k'):
		array_push_if(select_where, ('upper_state_energy_K>=%s' % mysql_real_escape_string(req_energy_range_from)), has_value(req_energy_range_from))
		array_push_if(select_where, ('upper_state_energy_K<=%s' % mysql_real_escape_string(req_energy_range_to)), has_value(req_energy_range_to))
	


	if (has_value(req_lill_cdms_jpl)):
		array_push(select_where, ('intintensity > %s' % mysql_real_escape_string(req_lill_cdms_jpl)))
		array_push(select_where, '(ll_id=10 OR ll_id=12)')
	

	if (has_value(req_lill_sijmu2)):
		array_push(select_where, ('sijmu2 > %s' % mysql_real_escape_string(req_lill_sijmu2)))
		array_push(select_where, 'll_id in (10, 12, 14)')
	

	if (has_value(req_lill_aij)):
		array_push(select_where, ('aij > %s' % mysql_real_escape_string(req_lill_aij)))
		array_push(select_where, 'll_id in (10, 12, 14)')
	

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

	fields = ' % '.join(select_fields)
	where = ' AND '.join(select_where)

	#	db.engine.execute( <sql here> )
	sql = ('SELECT SQL_CALC_FOUND_ROWS %s FROM main m, species s WHERE %s ORDER BY orderedfreq LIMIT %d, %d' % (fields, where, offset, limit))

	return sql
	
   
    

				
line = {
	'sid' : 1
	}	
req = {	
	'from' : '',
	'to' : '',
	'frequency_units' : 'MHz',
	'band' : 'alma5',
	'energy_range_type' : "eu_k",
	'energy_range_from' : '',
	'energy_range_to' : ''
	}
	
l = ['a','a','q']

name = ''
amount = ''
start = 1
end = 500
fre =  describe_results(req, name, amount, start, end)
e = array_map('mysql_real_escape_string', l)