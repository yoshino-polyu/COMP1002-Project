class User:
    
    def __init__(self, id : str, last_n : str, first_n : str, dpt : str, num_inj : str, inj_info : str, is_stu : str, pswrd : str) -> None:
        self.id = id
        self.last_n = last_n
        self.first_n = first_n
        self.dpt = dpt
        self.num_inj = num_inj
        self.inj_info = inj_info
        self.is_stu = is_stu
        self.pswrd = pswrd
    """
    id, last 
    """
    
    @property
    def id(self):
        return self.id

    @property
    def pswrd(self):
        return self.pswrd
   
    @property
    def last_n(self):
        return self.last_n

    @property
    def first_n(self):
        return self.first_n

    @property
    def dpt(self):
        return self.dpt
    
    @property
    def num_inj(self):
        return self.num_inj
    
    @property
    def inj_info(self):
        return self.inj_info

    @property
    def is_stu(self):
        return self.is_stu

    def full_n(self):
        return self.last_n + " " + self.first_n
    """
    returns the full name of this student or staff
    """
    
    @id.setter
    def id(self, value):
        self.id = value
    
