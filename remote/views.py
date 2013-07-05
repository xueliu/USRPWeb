from django.shortcuts import render, render_to_response;
from django.template.loader import render_to_string;
from django.http import HttpResponse, Http404;
import xmlrpclib;

def index(request):
	return render(request, 'remote/index.html', {});

def get_property(request, property_name):	
	
	usrp_ip_address = "192.168.160.105";
	
	s = xmlrpclib.ServerProxy("http://" + usrp_ip_address + ":65123");
	response = "";
	if property_name=="get_center_freq":
		response = s.get_center_freq();
	elif property_name=="get_start_freq":
		response = s.get_start_freq();
	elif property_name=="get_stop_freq":
		response = s.get_stop_freq();
	elif property_name=="get_samp_rate":
		response = s.get_samp_rate();
	# RPC		
	#set_center_freq(int)
	#set_start_freq(int)
	#set_stop_freq(int)
	#set_samp_rate(int )
	#get_center_freq()
	#get_start_freq()
	#get_stop_freq()
	#get_samp_rate()
	return HttpResponse(response);

def change_property(request, property_name, property_value):
	
	usrp_ip_address = "192.168.160.105";
	
	s = xmlrpclib.ServerProxy("http://" + usrp_ip_address + ":65123");
	value = int(property_value);
	if property_name=="set_center_freq":
		s.set_center_freq(value);
	elif property_name=="set_start_freq":
		s.set_start_freq(value);
	elif property_name=="set_stop_freq":
		s.set_stop_freq(value);
	elif property_name=="set_samp_rate":
		s.set_samp_rate(value);
	return HttpResponse(property_name + "(" + property_value + ")");
