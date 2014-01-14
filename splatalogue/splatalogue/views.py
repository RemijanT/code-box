from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    )

import re, os.path, time



@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
	
	#print str(os.path.dirname(__file__))
	base = os.path.dirname(__file__)
	
	file_path = base + '/templates/mytemplate.pt'
	mdate = time.strftime("%B %d, %Y", time.localtime(os.path.getmtime(file_path)));
	
	dict = {
		'modifieddate' : mdate
	}
    
	return {'retval': dict }


