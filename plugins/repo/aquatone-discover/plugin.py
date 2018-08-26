#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

'''
Faraday Penetration Test IDE
Copyright (C) 2017  Infobyte LLC (http://www.infobytesec.com/)
See the file 'doc/LICENSE' for the license information
'''

from plugins import core
import re
import socket

__author__ = "Roberto Focke"
__copyright__ = "Copyright (c) 2017, Infobyte LLC"
__license__ = ""
__version__ = "1.0.0"


class Aquatonediscover (core.PluginBase):

	def __init__(self):

		core.PluginBase.__init__(self)
        	self.id = "aquatone-discover"
        	self.name = "aquatone-discover"
        	self.plugin_version = "0.0.1"
        	self.version = "1.0.0"
        	self.protocol='tcp'
        	self._command_regex = re.compile(r'^(sudo aquatone-discover|aquatone-discover|sudo aquatone-discover\.py|aquatone-discover\.py|python aquatone-discover\.py|\.\/aquatone-discover\.py).*?')

	def parseOutputString(self, output, debug=False):
		j=1
		asci_escape=re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
		output=asci_escape.sub('', output)
		ip=re.compile('(\d+.\d+.\d+.\d+.)(\s+\w+.\w+.\w?.\w?.)')
		ips = ip.findall(output)
                #import ipdb; ipdb.set_trace()
		print ips
		print len(ips)
		
		cantidadlist=len(ips)
		aux_ip=""
		host_id=None
		while cantidadlist !=1:
				
				if (aux_ip is not ips[j][0] and str(ips[j][0]).isalpha()==False): 
					host_id=self.createAndAddHost(ips[j][0])						
			        	interface_id=self.createAndAddInterface(host_id,ips[j][0],ipv4_address=ips[j][0], hostname_resolution=ips[j][1])
					aux_ip=ips[j][0]
					j=j+1
					cantidadlist=cantidadlist-1
				elif (aux_ip is not ips[j][0]) :
                                        interface_id=self.createAndAddInterface(host_id,ips[j][0],ipv4_address=ips[j][0], hostname_resolution=ips[j][1])
                                        aux_ip=ips[j][0]
                                        j=j+1
                                        cantidadlist=cantidadlist-1
					
	def processCommandString(self, username, current_path, command_string):
        	return None

def createPlugin():
    return Aquatonediscover()


if __name__ == '__main__':
    aquatone = Aquatonediscover()
    with open('aquatone', 'r') as output_file:
        aquatone.parseOutputString(output_file.read())
