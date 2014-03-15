uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ";
lowercase="abcdefghijklmnopqrstuvwxyz";
number="0123456789.";

function loadContent(url,target) {
	var content = '';
	var value = false;		
	if (window.XMLHttpRequest) {
	    request = new XMLHttpRequest();
	} else if (window.ActiveXObject)	{
	    request = new ActiveXObject("Microsoft.XMLHTTP");
	}	

	if (request) {
		request.open("GET", url, false);		
		request.send(null);
		if (request.status == 200) {
			content = request.responseText;
			value = true;
		}
	}
    
	document.getElementById(target).innerHTML = content;
    
	return value;
}

function calculate(formula) {
    precision=0;
    value = "";

    try {
        weight = masscalc.parse(formula);
        weight = rounded(weight,precision);

        if(weight < 10)
            paddedWeight = "00" + weight;
        if(weight > 9 && weight < 100)
            paddedWeight = "0" + weight;
        if(weight >= 100)
            paddedWeight = weight;

        value = "Species ID like \"" + paddedWeight + "\"";
    } catch (ex) {
        value = "Unable to parse formula: " + ex.message;
    }

    document.getElementById('calcLabel').innerHTML = value;

    return false;
}

function rounded(number,init_precision) {
   var rounded=Math.round(number*Math.pow(10,init_precision))/Math.pow(10,init_precision);
   var numStr=rounded+"";
   var precis=(numStr.substring(numStr.indexOf(".")+1,numStr.length)).length;
   
   if (numStr.indexOf(".")!=-1){
      var extrazeros=(init_precision-precis<0)?0:init_precision-precis;
      
      for (var i=0;i<extrazeros;i++){
         rounded=rounded+"0";
      }
   }
   
   return rounded;
}

function toggle_display(element_id) {
	element = document.getElementById(element_id);
	if (element.style.display != "none") {
		element.style.display = "none";
	} else {
		element.style.display = "block";
	}
	
	return false;
}

function info_window(url) {
	popWin = open(url,'','height=400,width=300,status=yes,toolbar=no,menubar=no,location=no, scrollbars=1, resizable=1');
	popWin.focus();
	popWin.moveTo(screen.availWidth-310,50);
	
	return false;
}

function ref_window(foo) {
	popWin = open("refwindow.php?ref="+foo,foo,'height=200,width=300,status=yes,toolbar=no,menubar=no,location=no');
	popWin.focus();
	popWin.moveTo(screen.availWidth-310,50);
	
	return false;
}

function metadata_window(foo) {
	popWin = open("species_metadata_displayer.php?species_id="+foo,foo,'height=600,width=500,status=yes,toolbar=no,menubar=no,location=no,scrollbars=1,resizable=1');
	popWin.focus();
	popWin.moveTo(screen.availWidth-310,50);
	
	return false;
}

function save_window(foo) {
        document.execCommand("species_metadata_displayer.php?species_id="+foo);

        return false;
}

function toggleInput(check, id){
	var element = document.getElementById(id);
	element.disabled = !(check.checked);
}

function toggleOne(enabled, disabled1, disabled2, disabled3, disabled4) {
	var element = document.getElementById(enabled);
	if (null != element) element.disabled = false;
	
	element = document.getElementById(disabled1);
	if (null != element) element.disabled = true;
	
	element = document.getElementById(disabled2);
	if (null != element) element.disabled = true;
	
	element = document.getElementById(disabled3);
	if (null != element) element.disabled = true;
	
	element = document.getElementById(disabled4);
	if (null != element) element.disabled = true;
}
