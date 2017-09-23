import re

DOMAIN_REGEX = "([a-z0-9-]+\.)+[a-z]+"

class Parser :
	def __init (self):
		pass

	def parse (self, file):
		domains = []
		for line in file:
			search = re.search(DOMAIN_REGEX, line)
			if search is not None:
				domain = search.group(0)
				if domain not in domains:
					domains.append(domain)

		return domains