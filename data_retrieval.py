from ftplib import FTP
import xml.etree.ElementTree as ET

class file_info:
	def __init__(self, foldername, filename):
		self.foldername = foldername;
		self.filename = filename;
    
    # given FTP connection, download files
    # name them chronologically using a counter
	def download_file(self, counter, connection):
		connection.cwd('edgar/data/' + self.foldername)
		connection.retrbinary('RETR %s' % self.filename, open(str(counter) + '.txt', 'wb').write)
		connection.cwd('/')

class xml_file:
	def __init__(self, xml_name):
		self.xml_name = xml_name;

    # using the list of URLs that contain the file locations,
    # find and download the files
	def download_files(self, num):
		tree = ET.parse(self.xml_name)
		root = tree.getroot()
		counter = 100000 * num

		ftp = FTP('ftp.sec.gov', 'anonymous', 'allisonhwang@yahoo.com')

		for url in root:
			raw_url = url[0].text

			url_splitted = raw_url.split('data/')
			url2 = url_splitted[1]

			url_splitted2 = url2.split('/')
			url3 = url_splitted2[1]
			foldername = url_splitted2[0]

			url_splitted3 = url3.split('-index')
			filename = url_splitted3[0]

			filename = filename + '.txt'
			url_file_info = file_info(foldername, filename)

			url_file_info.download_file(counter, ftp)
			counter = counter + 1

# choose the index file that has desired file locations
print "Enter index file name number: "
xml_file_input = raw_input()

xml_file_name = 'sitemap.quarterlyindex' + xml_file_input + '.xml'
xml_file_num = int(xml_file_input)

# download the files
file1 = xml_file(xml_file_name)
file1.download_files(xml_file_num)
