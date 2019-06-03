import ldap

#create a connection to the ldap server
l = ldap.open("127.0.0.1")
l.protocol_version = ldap.VERSION3	

#indicate the object & retrieve its attributes
cn = raw_input("type the desired cn (user/computer) >>> "
baseDN = "o=test.com"
searchScope = ldap.SCOPE_SUBTREE
retrieveAttributes = None 
searchFilter = "cn=" + cn

ldap_result_id = l.search(baseDN, searchScope, searchFilter, retrieveAttributes)
result_set = []
while 1:
	result_type, result_data = l.result(ldap_result_id, 0)
	if (result_data == []):
		break
print result_set
