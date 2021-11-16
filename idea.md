Use model-view-controller approach to design our program. 

Vaccination information -> M

Translator -> C

Administrator -> V

Information of students:

| student ID | secret | department | vaccination record (from earliest to latest) | Student Name |
| ---------- | ------ | ---------- | -------------------------------------------- | ------------ |
|            |        |            |                                              |              |



Model:

- Local file system store the vaccination information

Controller:

- Process user input, and translate it into Model 

View:

- Command Line
- GUI
- Before administrator and general users:
- Intput ID and secrete
- Choose method
  - If administrator:
    - List all: 
      - student and staff in a specific department with indentation
      - and their vaccination information

    - Find students
    - Find teaching staff
    - List an information of a specific department
    - 

  - If students and teaching staff:
    - 


