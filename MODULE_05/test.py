

#from abc import ABC
import abc
import typing

#class Vehicle(abc.ABC):
#	@abc.abstractmethod
#	def go(self):
#		pass

class DataProcessor(abc.ABC):
	@abc.abstractmethod
	def validate(self, data: typing.Any) -> bool:
		pass

	@abc.abstractmethod
	def ingest(self, data: typing.Any) -> None:
		pass

	def output(self) -> tuple[int, str] :
		pass



class NumericProcessor(DataProcessor):
	def validate(self, data: typing.Any) -> bool:
		data = self.data_value
		self.validate_called = True
		if not isinstance(data, int | float | list):
			return False
		if isinstance(data, list):
			for item in data:
				if not isinstance(item, (int, float)):
					return False
		return True

	def ingest(self, data: int | float | list) -> None:
		if not self.validate_called:
			data_type = ""
			if type(data) == str:
				data_type = "string"
			elif type(data) == int:
				data_type = "int"
			elif type(data) == float:
				data_type = "float"
			elif type(data) == list:
				data_type = "list"

			print(f"Test invalid ingestion of {data_type} '{data}' without prior validation:")


class TextProcessor(DataProcessor):
	pass

class LogProcessor(DataProcessor):
	pass

testnum = NumericProcessor()
res = testnum.validate(25)

ing = testnum.ingest(8)


#print(res)




