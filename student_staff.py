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
    
    @property
    def id(self):
        return self.id

    @id.setter
    def id(self, value):
        self.id = value
        

    @property
    def pswrd(self):
        return self.pswrd

    @pswrd.setter
    def pswrd(self, value):
        self.pswrd = value

   
    @property
    def last_n(self):
        return self.last_n

    @last_n.setter
    def last_n(self, value):
        self.last_n = value


    @property
    def first_n(self):
        return self.first_n

    @first_n.setter
    def first_n(self, value):
        self.first_n = value


    @property
    def dpt(self):
        return self.dpt

    @dpt.setter
    def dpt(self, value):
        self.dpt = value

    
    @property
    def num_inj(self):
        return self.num_inj

    @num_inj.setter
    def num_inj(self, value):
        self.num_inj = value
    

    @property
    def inj_info(self):
        return self.inj_info

    @inj_info.setter
    def inj_info(self, value):
        self.inj_info = value
        

    @property
    def is_stu(self):
        return self.is_stu

    @is_stu.setter
    def is_stu(self, value):
        self.is_stu = value


    def full_n(self):
        return self.last_n + " " + self.first_n
    """
    returns the full name of this student or staff
    """
   

    

    
        
