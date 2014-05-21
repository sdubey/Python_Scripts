import re
import sys

def mach_regular_expression_of_association(regular_expression,association):
	occurence = 0
	flag = False
	if regular_expression.search(' '.join(association)) is not None: 
		flag = True
	return flag

def generate_list_from_file(filename):
	associations = []
 	file_name = open(filename, 'r')
	for line in file_name.readlines():
  		association = eval(line.split(') ')[0].rstrip()+')')
  		associations.append(association)
  	# close the input file
  	file_name.close()
  	return associations

def main():
    
	if len(sys.argv) is not 3:
		print 'incorrect arguments\nneed: output_from_step5.txt outputdire'
		sys.exit(2)
	else:
		word_association_file = sys.argv[1]
		output_data_directory = sys.argv[2]

	familynames = re.compile(r'\b(mother|brother|grandfather|sister|grandmother|father|mom|dad|son|daughter|uncle|aunt|niece|nephew|cousin)(\'s|s)*\b', re.I)
	disease_names = re.compile(r'\b(breast|cancer|ADHD|HTN|Breast cancer|bipolar|hypertension|CA|bipolar disorder|brain aneurysm|cancer|depressed\
		|cerebral aneurysm|colon cancer|depression|cerebrovascular accident|gastric carcinoma|mental illness|stroke|lung cancer|mood disorder|\
		strokes|prostate cancer|mood disorder/bipolar|adult-onset diabetes|renal CA|nervous breakdowns|diabetes|throat cancer|Schizophrenia|\
		diabetes mellitus|CHF|suicide|DM|CAD|coronary heart disease|type 2 diabetes|acute myocardial infarction|heart attack|alcohol abuse|\
		congestive heart failure heart disease alcoholic|coronary artery disease|Heart disease|alcoholism|myocardial infarction|heart failure|\
		alcohol to excess|valvular heart disease|MI|alcohol use|vascular strokes|drug addict| deceased from alcohol|substance abuse|using substance)(\'s|s)*\b', re.I)
	
	associations = generate_list_from_file(word_association_file)

	count_family_member_only=0
	count_disease_only=0
	count_family_no_disease = 0	
	count_family_and_disease = 0
	count_no_family_no_disease = 0
	

	for association in associations:
		# part a how many of them contain at least one family member?	
		if mach_regular_expression_of_association(familynames,association):
			count_family_member_only+=1

		#part b	how many of them contain at least one of the following diseases?
		if mach_regular_expression_of_association(disease_names,association):
			count_disease_only+=1

		# part c how many of them contain one family member but no disease? 
		if (mach_regular_expression_of_association(disease_names,association) is False and mach_regular_expression_of_association(familynames,association)):
			count_family_no_disease+=1

		#(e)how many of them contain both a family member and a disease? 	
		if (mach_regular_expression_of_association(disease_names,association) and mach_regular_expression_of_association(familynames,association)):
			count_family_and_disease+=1
		
		#(f) how many of them contain neither a family nor a disease? 
		if (mach_regular_expression_of_association(disease_names,association) is False and mach_regular_expression_of_association(familynames,association) is False):
			count_no_family_no_disease+=1

	f = open(output_data_directory+"/step_six_output.txt", "w")
    	f.write("part a : how many of them contain at least one family member? " + str(count_family_member_only) +"\n")
    	f.write("part b	: how many of them contain at least one of the following diseases? " + str(count_disease_only) +"\n")
    	f.write("part c : how many of them contain one family member but no disease? " + str(count_family_no_disease) +"\n")
    	f.write("part e : how many of them contain both a family member and a disease?  " + str(count_family_and_disease )+"\n")
    	f.write("part f : how many of them contain neither a family nor a disease " + str(count_no_family_no_disease )+"\n")
  	f.close()
		
main()

