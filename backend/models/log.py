class Log:
  def __init__(self, description: str, date: str, hour: str, id: str = None) -> None:
    self.id = id
    self.date = date
    self.hour = hour    
    self.description = description