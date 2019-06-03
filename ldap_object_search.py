import ldap

l = ldap.open("127.0.0.1")
l.protocol_version = ldap.VERSION3	

cn = raw_input("type the desired cn >>> "
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
