import ldap
import ldap.modlist as modlist

# open LDAP-server protoside [since we use unsecure ldap' we indicate 'ldap' instead 'ldaps']
l = ldap.initialize("ldap://ldapserver:389/") #the hosts file refers 'ldapserver' to the relevant IP

# Bind/authenticate with a user with apropriate rights to add objects
pass = raw_input("type user password here >>> ")
l.simple_bind_s("cn=manager,dc=test,dc=com",)

# difine the dn of our new entry/object
dn1="cn=user,dc=test,dc=com"
attrs = {}
attrs['objectclass'] = ['organizationalRole','simpleSecurityObject']
attrs['userPassword'] = "user" + "pass"
attrs['description'] = 'object named user'
dn2="cn=computer,dc=test,dc=com"
attrs = {}
attrs['objectclass'] = ['organizationalRole','simpleSecurityObject']
attrs['userPassword'] = "computer" + "pass"
attrs['description'] = 'object named computer'

objects = [dn1,dn2]

# adding the objects to ldapserver
for dn in objects:
	l.add_s(dn,ldif)

# close socket
l.unbind_s()
