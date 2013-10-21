import sys
from math import log

class Converter:

	def __init__(self, number):
		number= float(number)						#In case number is type int, then I don't have to worry about a non-existent decimal point
		point = str(number).find('.')				#Position of the decimal point
		self.integer= str(number)[:point]
		if self.integer[0]=="-":					#If number is signed, first bit is eliminated and sign is equal to "1"
			self.integer = self.integer[1:]
			self.sign = "1"
		else:
			self.sign = "0"

		self.decimal = str(number)[point:]
		self.result = ""

	def integerConverter(self):

		array=[]
		n =  self.integer
		pows = int(log(n,2))
		x=range(pows+1)
		x.reverse()

		for i in x:
			if pow(2,i) > n:
				array.append(str(0))
			else:
				n= n - pow(2,i)
				array.append(str(1))

		x = ''.join(array)
		return x										#Returns string

	def fractionalConverter(self):						#Converts fractional part of the number to binary
		
		result = ""
		num =  float(self.decimal)
		for i in range(1, 101):							#Up to 100 units to the right

			if num - 1.0/pow(2,i) >= 0:					
				result = result + "1"
			else:
				result = result +"0"

		return result

	def scientificFormatting(self):

		integerB =  self.integerConverter()
		decimalB =  self.fractionalConverter()

		if int(integerB) != 0:
			
			exponent =  integerB.__len__()	#int

			result =  integerB[1:] + decimalB        #The mantissa of our scientific notation number

		else:
			exponent= decimalB.find('1')		#int
			result = decimalB[exponent:]				#Same as the result above

		return (result, exponent)

	def BtoHex(self):
		stack =  self.result
		i = 0
		Hex= ""
		hashes = {10 : "A", 11: "B", 12: "C", 13: "D", 14:"E", 15:"F"}		#Used a hash for simplicity...the program is still too lenghty for my taste
		while i < stack.__len__():
			part =  stack[i:i+3]
			j = 3
			accumulate = 0
			for i in part:
				if i == "1":
					accumulate = accumulate+ pow(2, j)
				j-=1
			if accumulate >=10:
				Hex = Hex + hashes[accumulate]
			else:
				Hex =  Hex + str(accumulate)
			i += 4
		return Hex
				
	def floatIt(self, expWidth, mantissa, bias):

		result, exponent =  self.scientificFormatting()
		exponent = Converter(exponent).integerConverter()

		self.result= self.sign + exponent + result[:mantissa]	#Type: string

		return self.BtoHex()

	
		

