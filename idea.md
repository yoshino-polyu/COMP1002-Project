Use model-view-controller approach to design our program. 

Vaccination information -> M

Translator -> C

Administrator -> V

21096101d, 8 个数字 + 小写char



Information of students:

| student ID / stuff ID | secret | department | vaccination record (from earliest to latest)                 | Student Name / Staff Name | isStudent |
| --------------------- | ------ | ---------- | ------------------------------------------------------------ | ------------------------- | --------- |
|                       |        |            | Time to take vaccination, vaccination information (string), vaccinated or not. | Last name,                | 1, 0      |

users的权限:

1. Change password, at least 8 digits (alphabet and number)
2. See vaccination record
3. Input restriction, -> separated by comma. 
4. Input vaccination information (record)

查询关键字: 

1. Id, name, department
2. -1 -> 完全接种, 0, 1, 2, 3接种针数



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
  - If students and staff:
  - If administrator:
    - 
    - Add users
    - List all: 
      - student and staff in a specific department with indentation
      - and their vaccination information
    - Find students
    - Find teaching staff
    - List an information of a specific department
    - Information Analysis
  - If students and teaching staff:

- Only the administrator can open the txt file



