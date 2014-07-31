from ftplib import FTP
import xml.etree.ElementTree as ET

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

	def get_file_info_list():
		tree = ET.parse(xml_name)
		root = tree.getroot()
		file_info_list = [];

		for url in root:
			raw_url = url[0].text
			foldername = search('/data/{}/', raw_url)
			filename = parse('http://www.sec.gov/Archives/edgar/data/' + foldername + '/{}-index.htm', raw_url)
			filename = filename + '.txt'
			url_file_info = file_info(foldername, filename)
			file_list.append(url_file_info)

