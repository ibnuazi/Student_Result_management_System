from django.urls import path
from .views import *

urlpatterns=[
   path('index/',index),
   path('student_login/',student_login),
   path('admin_login/',adminlogin),
   path('student_register/',Student_Register),
   path('admin view/',adminview),
   path('delete_student/<int:id>',deletedata),
   path('update student details/<int:id>',editdata),
   path('add result/<int:id>',addresult),
   path('first semester/<int:id>',firstsem),
   path('second semester/<int:id>',secondsem),
   path('third semester/<int:id>',thirdsem),
   path('fourth semester/<int:id>',fourthsem),
   path('fifth semester/<int:id>',fifthsem),
   path('sixth semester/<int:id>',sixthsem),
   path('marklist uploaded success/',marlistsuccess),
   path('student view page/',student_view_page),
   path('sixthsemester_mark/<int:id>',sixthsem_markcard),
   path('fifthsemester_mark/<int:id>',fifthsem_markcard),
   path('fourthsemester_mark/<int:id>',fourthsem_markcard),
   path('thirdsemester_mark/<int:id>',thirdsem_makcard),
   path('secondsemseter_mark/<int:id>',secondsem_markcard),
   path('firstsemester_mark/<int:id>',firstsem_markcard),
   path('show_result6/',show_result6),
   path('courses/',courses),
   path('ContactUs/',contact)
]