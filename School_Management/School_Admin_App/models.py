from django.db import models
from School_Creating_Admin.models import MyUser
from School_Creating_Admin.models import school_details

class Teacher_Details(models.Model):
    teacher_subject=models.CharField(max_length=20)
    teacher_address=models.CharField( max_length=100)
    teacher_phone=models.CharField( max_length=10)
    empty='empty'
    first='1st'
    second='2nd'
    third='3rd'
    fourth='4th'
    fifth='5th'
    sixth='6th'
    seventh='7th'
    eighth='8th'
    nineth='9th'
    tenth='10th'
    eleventh='11th'
    twelveth='12th'

    class_choices=((empty,'empty'),(first, '1st'),(second, '2nd'),(third,'3rd'),(fourth,'4th'),(fifth,'5th'),(sixth,'6th'),(seventh,'7th'),(eighth,'8th'),(nineth,'9th'),(tenth,'10th'),(eleventh,'11th'),(twelveth,'12th'))          
    
    A='A'
    B='B'
    C='C'
    D='D'
    section_choices=((empty,'empty'),(A,'A'),(B,'B'),(C,'C'),(D,'D'))
   
    teacher_taking_class1=models.CharField(
       max_length=10,
       choices=class_choices, 
    )
    teacher_taking_class1_section=models.CharField(
       max_length=10,
       choices=section_choices,
      
    )
    teacher_taking_class2=models.CharField(
       max_length=10,
       choices=class_choices,
    )
    teacher_taking_class2_section=models.CharField(
       max_length=10,
       choices=section_choices,
       
    )
    teacher_taking_class3=models.CharField(
       max_length=10,
       choices=class_choices,
    )
    teacher_taking_class3_section=models.CharField(
       max_length=10,
       choices=section_choices,
       
    )
    teacher_taking_class4=models.CharField(
       max_length=10,
       choices=class_choices,
    )
    teacher_taking_class4_section=models.CharField(
       max_length=10,
       choices=section_choices,
       
    )
    teacher_taking_class5=models.CharField(
       max_length=10,
       choices=class_choices,
    )
    teacher_taking_class5_section=models.CharField(
       max_length=10,
       choices=section_choices,
       
    )

    user=models.ForeignKey(MyUser, on_delete=models.CASCADE)


class Student_Details(models.Model):
   

   empty='empty'
   first='1st'
   second='2nd'
   third='3rd'
   fourth='4th'
   fifth='5th'
   sixth='6th'
   seventh='7th'
   eighth='8th'
   nineth='9th'
   tenth='10th'
   eleventh='11th'
   twelveth='12th'

   class_choices=((empty,'empty'),(first, '1st'),(second, '2nd'),(third,'3rd'),(fourth,'4th'),(fifth,'5th'),(sixth,'6th'),(seventh,'7th'),(eighth,'8th'),(nineth,'9th'),(tenth,'10th'),(eleventh,'11th'),(twelveth,'12th'))          
    
   A='A'
   B='B'
   C='C'
   D='D'
   section_choices=((empty,'empty'),(A,'A'),(B,'B'),(C,'C'),(D,'D'))

   student_register_number=models.CharField( max_length=20)
   student_class=models.CharField(
      max_length=10,
      choices=class_choices,  
    )
   student_class_section=models.CharField(
      max_length=10,
      choices=section_choices,  
   )
   student_address=models.CharField( max_length=100)
   student_phone=models.CharField( max_length=10)
   school=models.ForeignKey(school_details, on_delete=models.CASCADE)


class Student_Subjects_Marks(models.Model):
   student=models.ForeignKey(Student_Details, on_delete=models.CASCADE)
   school=models.ForeignKey(school_details, on_delete=models.CASCADE)

   Exam_name=models.CharField(max_length=20)

   student_first_subject_marks=models.CharField(max_length=5)
   student_second_subject_marks=models.CharField(max_length=5)
   student_third_subject_marks=models.CharField(max_length=5)
   student_fourth_subject_marks=models.CharField(max_length=5)
   student_fifth_subject_marks=models.CharField(max_length=5)
   student_sixth_subject_marks=models.CharField(max_length=5)





    

class Class_Subjects(models.Model):
   school=models.ForeignKey(school_details, on_delete=models.CASCADE)

   first='1st'
   second='2nd'
   third='3rd'
   fourth='4th'
   fifth='5th'
   sixth='6th'
   seventh='7th'
   eighth='8th'
   nineth='9th'
   tenth='10th'
   eleventh='11th'
   twelveth='12th'

   class_choices=((first, '1st'),(second, '2nd'),(third,'3rd'),(fourth,'4th'),(fifth,'5th'),(sixth,'6th'),(seventh,'7th'),(eighth,'8th'),(nineth,'9th'),(tenth,'10th'),(eleventh,'11th'),(twelveth,'12th'))          
   class_is=models.CharField(
       max_length=10,
       choices=class_choices, 
    )


   NoSubject='NoSubject'
   Tamil='Tamil'
   English='English'
   Mathematics='Mathematics'
   Science='Science'
   SocialScience='SocialScience'
   Physics='Physics'
   Chemistry='Chemistry'
   Biology='Biology'
   Zoology='Zoology'
   ComputerScience='ComputerScience'

   subjects=((NoSubject,'NoSubject'),(Tamil,'Tamil'),(English,'English'),(Mathematics,'Mathematics'),(Science,'Science'),(SocialScience,'SocialScience'),(Physics,'Physics'),(Chemistry,'Chemistry'),(Biology,'Biology'),(Zoology,'Zoology'),(ComputerScience,'ComputerScience'))
   first_subject=models.CharField(
       max_length=20,
       choices=subjects,  
    )
   second_subject=models.CharField(
       max_length=20,
       choices=subjects,  
    )
   third_subject=models.CharField(
       max_length=20,
       choices=subjects,  
    )
   fourth_subject=models.CharField(
       max_length=20,
       choices=subjects,  
    )
   fifth_subject=models.CharField(
       max_length=20,
       choices=subjects,  
    )
   sixth_subject=models.CharField(
       max_length=20,
       choices=subjects,  
    )

   
