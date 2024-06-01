from django import forms


class adminform(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

class studentregister(forms.Form):
    firstname=forms.CharField(max_length=50)
    lastname=forms.CharField(max_length=50)
    email=forms.EmailField()
    phone=forms.IntegerField()
    department=forms.CharField(max_length=20)
    password=forms.CharField(max_length=20)
    confirmpassword=forms.CharField(max_length=20)


class regform(forms.Form):
    name=forms.CharField(max_length=20)
    email=forms.EmailField()
    phone=forms.IntegerField()

class stud_login(forms.Form):
    regno=forms.CharField(max_length=20)
    psw=forms.CharField(max_length=20)

class adminsort(forms.Form):
    department1=forms.CharField(max_length=20)

class first_sem(forms.Form):
    arabic=forms.IntegerField()
    english=forms.IntegerField()
    C=forms.IntegerField()
    DE=forms.IntegerField()
    DM=forms.IntegerField()
    c_programming_Lab=forms.IntegerField()
    DE_Lab=forms.IntegerField()
    environment=forms.IntegerField()

class second_sem(forms.Form):
    arabic=forms.IntegerField()
    english=forms.IntegerField()
    DS=forms.IntegerField()
    DBMS=forms.IntegerField()
    NSM=forms.IntegerField()
    DS_Lab=forms.IntegerField()
    DBMS_Lab=forms.IntegerField()
    ICHR=forms.IntegerField()

class third_sem(forms.Form):
    arabic=forms.IntegerField()
    english=forms.IntegerField()
    Cpp=forms.IntegerField()
    Accounting=forms.IntegerField()
    OperatingSystem=forms.IntegerField()
    Cpp_Lab=forms.IntegerField()
    Accounting_Lab=forms.IntegerField()
    CDS=forms.IntegerField()

class fourth_sem(forms.Form):
    arabic=forms.IntegerField()
    english=forms.IntegerField()
    Vprogramming=forms.IntegerField()
    USprogramming=forms.IntegerField()
    oR=forms.IntegerField()
    Vp_Lab=forms.IntegerField()
    UNIX_Lab=forms.IntegerField()
    PD=forms.IntegerField()

class fifth_sem(forms.Form):
    DCN=forms.IntegerField()
    SE=forms.IntegerField()
    CA=forms.IntegerField()
    JP=forms.IntegerField()
    MP=forms.IntegerField()
    Project=forms.IntegerField()
    BF=forms.IntegerField()

class sixth_sem(forms.Form):
    TOC=forms.IntegerField()
    SP=forms.IntegerField()
    CNS=forms.IntegerField()
    WP=forms.IntegerField()
    WPL=forms.IntegerField()
    Project=forms.IntegerField()
    CAIT=forms.IntegerField()