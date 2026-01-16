class CookTime:
   def __init__(self, minute=0, second=0):
       self.minute = minute
       self.second = second
  
   @property
   def minute(self):
       return self._minute
  
   @minute.setter
   def minute(self, new_value):
       if new_value >= 0:
           self._minute = new_value
       else:
           print("Error: Minute must be 0 or over.")


      
   @property
   def second(self):
       return self._second
  
   @second.setter
   def second(self, new_value):
       if new_value in range(0,60):
           self._second = new_value
       else:
           print("Error: Second must be in between 0 - 59.")
           self._second = 0




   def get_total_seconds(self):
       return (self.minute * 60 + self.second)