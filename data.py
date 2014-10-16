from ftplib import FTP
import xml.etree.ElementTree as ET
from parse import *

class file_info:
	def __init__(self, foldername, filename):
		self.foldername = foldername;
		self.filename = filename;

	def download_file(self):
		ftp = FTP('ftp.sec.gov', 'anonymous', 'allisonhwang@yahoo.com')
		ftp.cwd('edgar/data/' + self.foldername)
		ftp.retrbinary('RETR %s' % self.filename, open(self.filename, 'wb').write)

class xml_file:
	def __init__(self, xml_name):
		self.xml_name = xml_name;
		self.address_count = address_list.count()

	def download_files():
		tree = ET.parse(xml_name)
		root = tree.getroot()
		file_info_list = [];

		for url in root:
			raw_url = url[0].text

			search_foldername = search('/data/{}/', raw_url) # <Result ('910832',) {}>
			foldername = search_foldername[0] # '910832'
			search_filename = parse('http://www.sec.gov/Archives/edgar/data/' + foldername + '/{}-index.htm', raw_url)
			filename = result[0]
			filename = search_filename + '.txt'
			url_file_info = file_info(foldername, filename)

			url_file_info.download_file()


