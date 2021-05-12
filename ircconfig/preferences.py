from typing  import Dict, Any
from os.path import isfile
import json

class Preferences(object):
	def __init__(self,
		file:     str,
		settings: Dict):

		self.file      = file
		self.defaults  = settings
		self.database  = {}
		self.preftypes = {}

		self._defaults()
		self._from_file()
		self._write()

	def _defaults(self):
		self.database = {
	        "global": {
	        	k: v.default for k, v in self.defaults.items()
	        }
	    }

	def _from_file(self):
	    if isfile(self.file):
	        with open(self.file) as db_file:
	            database = json.loads(db_file.read())

	            self.database.update({
	            	t: {
	            		k: self.defaults[k].deserialize(v) for k,v in database[t].items()
	            	} for t in database.keys()
	            })

	def _write(self):
	    database_serialized = {
	    	t: {
	        	k: self.defaults[k].serialize(v) for k,v in self.database[t].items()
	        } for t in self.database.keys()
	    }
	    data = json.dumps(database_serialized, indent=4, sort_keys=True)
	    with open(self.file, "w") as db_file:
	        db_file.write(data)

	def getPreference(self,
		key: str,
		default: Any = None,
		channel: str = None):

		if channel and channel in self.database.keys():
			target = channel
		else:
			target = "global"

		try:
			value = self.database[target][key]
		except KeyError:
			value = default

		return value

	def setPreference(self,
		key: str,
		value: str,
		channel: str = None):

		if not key in self.defaults.keys():
			raise KeyError(f"{key} is not a valid preference")

		if channel:
			target = channel
		else:
			target = "global"

		if not target in self.database.keys():
			self.database[target] = {}
		self.database[target][key] = value

		self._write()
