from django import forms
import re
from django.core.exceptions import ValidationError

class TeacherRegistrationForm(forms.Form):
 
    teacher_subject=forms.CharField(max_length=20,label=" teacher_subject")
    teacher_address=forms.CharField( max_length=100,label=" teacher_address")
    teacher_phone=forms.CharField( max_length=10,label="teacher_phone")
    teacher_classes = (('empty','empty'),('1st', '1st'),('2nd', '2nd'),('3rd','3rd'),('4th','4th'),('5th','5th'),('6th','6th'),('7th','7th'),('8th','8th'),('9th','9th'),('10th','10th'),('11th','11th'),('12th','12th'))
    teacher_taking_class1 = forms.ChoiceField(choices=teacher_classes,label="teacher_taking_class1")
    teacher_taking_class2 = forms.ChoiceField(choices=teacher_classes,label="teacher_taking_class2")
    teacher_taking_class3 = forms.ChoiceField(choices=teacher_classes,label="teacher_taking_class3")
    teacher_taking_class4 = forms.ChoiceField(choices=teacher_classes,label="teacher_taking_class4")
    teacher_taking_class5 = forms.ChoiceField(choices=teacher_classes,label="teacher_taking_class5")

    teacher_classes_section = (('empty','empty'),('A','A'),('B','B'),('C','C'),('D','D'))
    teacher_taking_class1_section = forms.ChoiceField(choices=teacher_classes_section,label="teacher_taking_class1_section")
    teacher_taking_class2_section = forms.ChoiceField(choices=teacher_classes_section,label="teacher_taking_class2_section")
    teacher_taking_class3_section = forms.ChoiceField(choices=teacher_classes_section,label="teacher_taking_class3_section")
    teacher_taking_class4_section = forms.ChoiceField(choices=teacher_classes_section,label="teacher_taking_class4_section")
    teacher_taking_class5_section = forms.ChoiceField(choices=teacher_classes_section,label="teacher_taking_class5_section")
   

class ClassSubjectsForm(forms.Form):
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
   class_is=forms.ChoiceField(choices=class_choices,label="class_is")


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
   first_subject=forms.ChoiceField(choices=subjects,label="first_subject"  )
   second_subject=forms.ChoiceField(choices=subjects,label="second_subject"   )
   third_subject=forms.ChoiceField(choices=subjects,label="third_subject"   )
   fourth_subject=forms.ChoiceField(choices=subjects,label="fourth_subject"   )
   fifth_subject=forms.ChoiceField(choices=subjects, label="fifth_subject"  )
   sixth_subject=forms.ChoiceField(choices=subjects, label="sixth_subject"  )
