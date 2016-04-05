# -*- coding:  utf-8 -*-
# класс для хранения записей
import datetime

class myStorage():
	
	#storageName = "C:\Users\Григорий\Google Диск\Python\RPGWorld\data.txt"
	#with open(storageName, 'a') as f:
	
	def __init__(self, Name):
		self.storageName = Name
	
	def addOne(self, text):
		now_time = datetime.datetime.now()
		with open(self.storageName, 'a') as f:
			f.write("#>" + now_time.__str__().encode('utf-8') + '\n' + text.encode('utf-8')+ '\n')
			#print text.encode('cp1251') 
			return True
		return False

		
	def deleteOne():
		pass
		
	def loadLast(self, Last):
		with open(self.storageName, 'r') as f:
			F = f.read().decode('utf-8').split('#>')
			if Last > len(F):
				return F[-len(F):][::-1]
			return F[-Last:][::-1] #первый элемент пустой
		return False
		
	#def loadLast(self):
		#with open(self.storageName, 'r') as f:
			#F = f.read().decode('utf-8').split('#>')
			#return F[::-1] #первый элемент пустой
		#return False
		
		
if __name__ == '__main__':
	Stor = myStorage('test.txt')
	#Stor.addOne(datetime.datetime.now().__str__())
	Stor.addOne("Проверка".decode('utf-8') )
	print Stor.loadLast(1)[0]#.decode(' utf-8')	
    
