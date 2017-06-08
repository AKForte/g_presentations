import ldap3

uri = "avworld"
user = "atma6951"
password = "sl^ntedl^ptop"

ldapClient = ldap3.initialize(uri)
ldapClient.set_option(ldap3.OPT_REFERRALS, 0)

ldapClient.bind(user, password)

results = ldapClient.search_s("cn=My-Group-1,ou=Groups,o=CUST", ldap3.SCOPE_BASE)

for result in results:
  result_dn = result[0]
  result_attrs = result[1]

  if "member" in result_attrs:
    for member in result_attrs["member"]:
      print(member)

ldapClient.unbind_s()