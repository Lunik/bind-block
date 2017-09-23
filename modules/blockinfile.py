import re

from .scraper import Scraper
import generator

DEFAULT_OPTIONS = {
	'mark': "# {mark} MANAGED BLOCK"
}

def parseOptions (options):
	for o in DEFAULT_OPTIONS:
		if o not in options:
			options[o] = DEFAULT_OPTIONS[o]
	return options

class Blockinfile:
	def __init__(self):
		pass

	def getMark (self, options):
		mark = {
			'begin': options['mark'].format(mark='BEGIN'),
			'end': options['mark'].format(mark='END')
		}
		mark['regex'] = "{begin}\\n(.*\\n)*{end}".format(
			begin=mark['begin'],
			end=mark['end'])
		return mark

	def exist (self, path, options):
		options = parseOptions(options)
		mark = self.getMark(options)

		file = open(path, 'r')
		fileContent = file.read()
		file.close()

		return re.search(mark['regex'], fileContent)

	def write (self, path, content, options):
		options = parseOptions(options)
		mark = self.getMark(options)

		file = open(path, 'r')
		fileContent = file.read()
		file.close()

		blockExist = self.exist(path, options)

		# Generate new block
		contentBlock = "{begin}\n{content}\n{end}".format(
			begin=mark['begin'],
			content=content,
			end=mark['end'])

		# Replace block
		if blockExist is not None:
			fileContent = fileContent.replace(blockExist.group(0), contentBlock)
		else :
			fileContent += "\n\n{contentBlock}".format(contentBlock=contentBlock)

		# Write file
		file = open(path, 'w')
		file.write(fileContent)
		file.close()










