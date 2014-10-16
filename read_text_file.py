import sys
import os

class date_string:
	def __init__(self, datetimestring):
		self.datetimestring = datetimestring

    # convert dates found in the file into a desirable format
	def date_convert(self):
		d = self.datetimestring
		d_converted = d[0:4] + '-' + d[4:6] + '-' + d[6:8]
		return d_converted
    
    # convert datetimes found in the file into a desirable format
	def datetime_convert(self):
		d = self.datetimestring
		d_converted = d[0:4] + '-' + d[4:6] + '-' + d[6:8] + ' ' + d[8:10] + ':' + d[10:12] + ':' + d[12:14]
		return d_converted

class text_file:
	def __init__(self, filename):
		self.filename = filename

	def read(self):

		def identifier_parse(line):

			if line[0] == '<':
				remove_first_bracket = line.split('<')[1]
				remove_last_bracket = remove_first_bracket.split('>')[0]
				return remove_last_bracket
			
			# otherwise, the identifier is of this format: IDENTIFIER:
			line = line.lstrip()
			return line.split(':')[0]

        # given the identifier, retrieve the desired information
		def get_content(identifier, line, entry):

			def extract_content(identifier, line):
				remove_id = line.split('\t')
				remove_id.reverse()
				remove_carriage = remove_id[0].split('\n')[0]
				content = remove_carriage
				return content

			if identifier == 'COMPANY CONFORMED NAME' and company_data == 1:
				content = extract_content(identifier, line)
				return ('company_name', content)

			if identifier == 'SEC-DOCUMENT':
				result = line.split('>')
				remove_id = line.split('>')[1]
				content = remove_id.split(' ')[0]
				return ('sec_document_name', content)

			if identifier == 'ACCEPTANCE-DATETIME':
				remove_id = line.split('>')[1]
				remove_carriage = remove_id.split('\n')[0]
				d = date_string(remove_carriage)
				datetime = d.datetime_convert()
				return ('acceptance_datetime', datetime)

			if identifier == 'TYPE':
				if '>' in line:
					remove_id = line.split('>')[1]
					remove_carriage = remove_id.split('\n')[0]
					return ('type', remove_carriage)

			if identifier == 'FILENAME':
				remove_id = line.split('>')[1]
				remove_carriage = remove_id.split('\n')[0]
				return ('filename', remove_carriage)

			if identifier == 'ACCESSION NUMBER':
				content = extract_content(identifier, line)
				return ('accession_num', content)

			if identifier == 'CONFORMED PERIOD OF REPORT':
				content = extract_content(identifier, line)
				return ('conformed_period_of_report', content)

			if identifier == 'FILED AS OF DATE':
				content = extract_content(identifier, line)
				d = date_string(content)
				date = d.date_convert()
				return ('filed_as_of_date', date)

			if identifier == 'DATE AS OF CHANGE':
				content = extract_content(identifier, line)
				d = date_string(content)
				date = d.date_convert()
				return ('date_as_of_change', date)

			if identifier == 'CONFORMED SUBMISSION TYPE':
				content = extract_content(identifier, line)
				return ('submission_type', content)

			# must remove white space at the front of the string
			if identifier == 'FISCAL YEAR END':
				line = line.lstrip()
				content = extract_content(identifier, line)
				return ('fiscal_year_end', content)

			if identifier == 'CENTRAL INDEX KEY':
				line = line.lstrip()
				content = extract_content(identifier, line)
				return ('CIK', content)

			if identifier == 'ITEM INFORMATION':
				content = extract_content(identifier, line)
				if content == 'Entry into a Material Definitive Agreement':
					return ('I101', '1')

				if content == 'Termination of a Material Definitive Agreement':
					return ('I102', '1')

				if content == 'Bankruptcy or Receivership':
					return ('I103', '1')

				if content == 'Mine Safety - Reporting of Shutdowns and Patterns of Violations':
					return ('I104', '1')

				if content == 'Completion of Acquisition or Disposition of Assets':
					return ('I201', '1')

				if content == 'Results of Operations and Financial Condition':
					return ('I202', '1')

				if content == 'Creation of a Direct Financial Obligation or an Obligation under an Off-Balance Sheet Arrangement of a Registrant':
					return ('I203', '1')

				if content == 'Triggering Events That Accelerate or Increase a Direct Financial Obligation or an Obligation under an Off-Balance Sheet Arrangement':
					return ('I204', '1')

				if content == 'Costs Associated with Exit or Disposal Activities':
					return ('I205', '1')

				if content == 'Material Impairments':
					return ('I206', '1')

				if content == 'Notice of Delisting or Failure to Satisfy a Continued Listing Rule or Standard; Transfer of Listing':
					return ('I301', '1')

				if content == 'Unregistered Sales of Equity Securities':
					return ('I302', '1')

				if content == 'Material Modification to Rights of Security Holders':
					return ('I303', '1')

				if content == "Changes in Registrant's Certifying Accountant":
					return ('I401', '1')

				if content == 'Non-Reliance on Previously Issued Financial Statements or a Related Audit Report or Completed Interim Review':
					return ('I402', '1')

				if content == 'Changes in Control of Registrant':
					return ('I501', '1')

				if content == 'Departure of Directors or Certain Officers; Election of Directors; Appointment of Certain Officers; Compensatory Arrangements of Certain Officerserial':
					return ('I502', '1')

				if content == 'Amendments to Articles of Incorporation or Bylaws; Change in Fiscal Year':
					return ('I503', '1')

				if content == 'Temporary Suspension of Trading Under Registrant\'s Employee Benefit Plans':
					return ('I504', '1')

				if content == 'Amendment to Registrant\'s Code of Ethics, or Waiver of a Provision of the Code of Ethics':
					return ('I505', '1')

				if content == 'Change in Shell Company Status':
					return ('I506', '1')

				if content == 'Submission of Matters to a Vote of Security Holders':
					return ('I507', '1')

				if content == 'Shareholder Director Nominations':
					return ('I508', '1')

				if content == 'ABS Informational and Computational Material':
					return ('I601', '1')

				if content == 'Change of Servicer or Trustee':
					return ('I602', '1')

				if content == 'Change in Credit Enhancement or Other External Support':
					return ('I603', '1')

				if content == 'Failure to Make a Required Distribution':
					return ('I604', '1')

				if content == 'Securities Act Updating Disclosure':
					return ('I605', '1')

				if content == 'Regulation FD Disclosure':
					return ('I701', '1')

				if content == 'Other Events':
					return ('I801', '1')

				if content == 'Financial Statements and Exhibits':
					return ('I901', '1')
    
		with open(self.filename) as f:
			entry = []
			columns = ['CIK', 'company_name', 'sec_document_name', 'acceptance_datetime', 'type', 
			'filename', 'accession_num', 'conformed_period_of_report', 'filed_as_of_date', 'date_as_of_change', 'submission_type', 
			'fiscal_year_end', 'I101', 'I102', 'I103', 'I104', 'I201', 'I202', 'I203', 'I204', 'I205', 'I206', 'I301', 
			'I302', 'I303', 'I401', 'I402', 'I501', 'I502', 'I503', 'I504', 'I505', 'I506', 'I507', 'I508',
			'I601', 'I602', 'I603', 'I604', 'I605', 'I701', 'I801', 'I901']

			company_data = 0

			for line in f:
				identifier = identifier_parse(line)
				if identifier == 'COMPANY DATA':
					company_data = 1

				if identifier == '/SEC-HEADER':
					continue
				item = get_content(identifier, line, entry)

				if item:
					entry.append(item)

			entry_dict = dict(entry)

			# get file size
			filesize = os.path.getsize(self.filename)
			fs_string = str(filesize)
			sys.stdout.write(fs_string)
			sys.stdout.write('\t')

			for key in columns:

				if key in entry_dict.keys():
					sys.stdout.write(entry_dict[key])

				else:
					sys.stdout.write('\N')

				sys.stdout.write('\t')

			sys.stdout.write('\r\n')	


with open('names.txt') as f:
	for line in f:
		line = line.split('\n')[0]
		read_file = text_file(line)
		read_file.read()

# testing 
"""
first_file = text_file('540.txt')
first_file.read()
"""


