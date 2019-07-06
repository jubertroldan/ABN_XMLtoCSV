# script to process ABN data
# https://data.gov.au/data/dataset/5bd7fcab-e315-42cb-8daf-50b7efc2027e
# Author: Jubert Roldan

# note that this reads the XML file and writes as a CSV.
# roughly process around 15mins each file

import xml.etree.ElementTree as ET
import csv
import time


starttime = time.asctime(time.localtime(time.time()))
print('starttime:',starttime)

recordLastUpdatedDate = None
replaced = None
ABNval = None
ABN_status = None
ABNStatusFromDate = None
EntityTypeInd = None
EntityTypeText = None
MainEnttype = None
NonIndividualNameText = None
LegalEntityType = None
NameTitle = None
GivenName = None
FamilyName = None
ASICNumber = None
GSTval = None
GSTStatusFromDate = None
GST_status = None
DGRStatusFromDate = None
DGRNonIndividualNameType = None
DGRNonIndividualNameText = None
OthrEnt_NonIndividualName = None
OthrEnt_NonIndividualNameText = None
State = None
Postcode = None

# modify line 41 and 45 for the file name
xml = 'C:\\Workfiles\\Projects\\ABN\\dinetpubwwwrootabnlookupwebadminbulkextractpublic_split_1_10\\20190703_Public02.xml'
tree = ET.parse(xml)
root = tree.getroot()

# write to file
with open('C:\\Workfiles\\Projects\\ABN\\dinetpubwwwrootabnlookupwebadminbulkextractpublic_split_1_10\\20190703_Public02.csv',mode='w', newline='') as file:
	file_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	# write header
	file_writer.writerow(['recordLastUpdatedDate','replaced','ABNval','ABN_status','ABNStatusFromDate','EntityTypeInd','EntityTypeText','MainEnttype','NonIndividualNameText','LegalEntityType','NameTitle','GivenName','FamilyName','ASICNumber','GSTval','GSTStatusFromDate','GST_status','DGRStatusFromDate','DGRNonIndividualNameType','DGRNonIndividualNameText','OthrEnt_NonIndividualName','OthrEnt_NonIndividualNameText','State','Postcode'])

	for ABR in root.iter('ABR'):
		recordLastUpdatedDate = ABR.get('recordLastUpdatedDate')
		replaced = ABR.get('replaced')

		for ABN in ABR.iter('ABN'):
			ABN_status = ABN.get('status')
			ABNStatusFromDate = ABN.get('ABNStatusFromDate')
			ABNval = ABN.text

		for Enttype in ABR.iter('EntityType'):
			if Enttype.find('EntityTypeInd') is not None:
				EntityTypeInd = Enttype.find('EntityTypeInd').text
			if Enttype.find('EntityTypeText') is not None:
				EntityTypeText = Enttype.find('EntityTypeText').text

		for MainEnt in ABR.iter('MainEntity'):
			for NonIndividualName in MainEnt.iter('NonIndividualName'):
					MainEnttype = NonIndividualName.get('type')
					if NonIndividualName.find('NonIndividualNameText') is not None:
						NonIndividualNameText = NonIndividualName.find('NonIndividualNameText').text
		

		for LegalEntity in ABR.iter('LegalEntity'):
			for IndividualName in LegalEntity.iter('IndividualName'):
					LegalEntityType = IndividualName.get('type')
					if IndividualName.find('NameTitle') is not None:
						NameTitle = IndividualName.find('NameTitle').text
					if IndividualName.find('GivenName') is not None:
						GivenName = IndividualName.find('GivenName').text
					if IndividualName.find('FamilyName') is not None:
						FamilyName = IndividualName.find('FamilyName').text

		for ASICNum in ABR.iter('ASICNumber'):
			if ASICNum.find('NameTitle') is not None:
				ASICNumber = ASICNum.find('ASICNumber').text

		for GST in ABR.iter('GST'):
			GST_status = GST.get('status')
			GSTStatusFromDate = GST.get('GSTStatusFromDate')
			GSTval = GST.text

		for DGR in ABR.iter('DGR'):
			DGRStatusFromDate = DGR.get('DGRStatusFromDate')
			for NonIndividualName in DGR.iter('NonIndividualName'):
				DGRNonIndividualNameType = NonIndividualName.get('type')
				if NonIndividualName.find('NonIndividualNameText') is not None:
						DGRNonIndividualNameText = NonIndividualName.find('NonIndividualNameText').text
				
		for OtherEntity in ABR.iter('OtherEntity'):
			for NonIndividualName in OtherEntity.iter('NonIndividualName'):
				OthrEnt_NonIndividualName = OtherEntity.get('type')
				if NonIndividualName.find('NonIndividualNameText') is not None:
					OthrEnt_NonIndividualNameText = NonIndividualName.find('NonIndividualNameText').text

		for BusinessAddress in ABR.iter('BusinessAddress'):
			for AddressDetails in BusinessAddress.iter('AddressDetails'):
				if AddressDetails.find('State') is not None:
					State = AddressDetails.find('State').text
				if AddressDetails.find('Postcode') is not None:
					Postcode = AddressDetails.find('Postcode').text

		
		# check data

		print(recordLastUpdatedDate,replaced,ABNval,ABN_status,ABNStatusFromDate,EntityTypeInd,EntityTypeText,
			MainEnttype,NonIndividualNameText,LegalEntityType,NameTitle,GivenName,FamilyName,ASICNumber,
			GSTval,GSTStatusFromDate,GST_status,DGRStatusFromDate,DGRNonIndividualNameType,DGRNonIndividualNameText,
			OthrEnt_NonIndividualName,OthrEnt_NonIndividualNameText,State,Postcode)


		# write as a CSV file
		file_writer.writerow([recordLastUpdatedDate,replaced,ABNval,ABN_status,ABNStatusFromDate,EntityTypeInd,EntityTypeText,
			MainEnttype,NonIndividualNameText,LegalEntityType,NameTitle,GivenName,FamilyName,ASICNumber,
			GSTval,GSTStatusFromDate,GST_status,DGRStatusFromDate,DGRNonIndividualNameType,DGRNonIndividualNameText,
			OthrEnt_NonIndividualName,OthrEnt_NonIndividualNameText,State,Postcode])


	# set all values back to None so that it will not overlay on the next iteration
	recordLastUpdatedDate = None
	replaced = None
	ABNval = None
	ABN_status = None
	ABNStatusFromDate = None
	EntityTypeInd = None
	EntityTypeText = None
	MainEnttype = None
	NonIndividualNameText = None
	LegalEntityType = None
	NameTitle = None
	GivenName = None
	FamilyName = None
	ASICNumber = None
	GSTval = None
	GSTStatusFromDate = None
	GST_status = None
	DGRStatusFromDate = None
	DGRNonIndividualNameType = None
	DGRNonIndividualNameText = None
	OthrEnt_NonIndividualName = None
	OthrEnt_NonIndividualNameText = None
	State = None
	Postcode = None	

endtime = time.asctime(time.localtime(time.time()))
print('starttime:',starttime)
print('endtime:',endtime)

# reference:
# https://docs.python.org/2/library/xml.etree.elementtree.html