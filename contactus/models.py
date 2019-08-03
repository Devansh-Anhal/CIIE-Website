from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import URLValidator

# Create your models here.
class idea(models.Model):
	first_name = models.CharField(max_length=50)
	last_name  = models.CharField(max_length=50)
	email      = models.EmailField()
	enrollment_no = models.CharField(max_length=30)
	idea   = models.TextField(max_length = 4095, null=True)
	why_do_you_want_to_join_CIIE   = models.TextField(max_length = 4095, null = True, blank=True)
	join_ciie = models.BooleanField(default=True )

	def __str__(self):
		return self.first_name+' '+self.last_name

class join(models.Model):
	first_name = models.CharField(max_length=50)
	last_name  = models.CharField(max_length=50)
	email      = models.EmailField()
	enrollment_no  = models.CharField(max_length=30)
	why_do_you_want_to_join_CIIE   = models.TextField(max_length = 4095)

	def __str__(self):
		return self.first_name+' '+self.last_name

class startup(models.Model):
	org_choice = (
					('n', 'Not for Profit Organization'),
					('p', 'For Profit Organization'),
				)

	enterprise = (
					('r', 'Registered'),
					('n', 'Not Registered'),
				)

	type_impact = (
					('d', 'Direct'),
					('i', 'Indirect'),

				)

	sector_d = (
					('ai', 'Information, Communication and Entertainment'),
					('bi', 'Food, Agriculture and allied sectors'),
					('ci', 'Augmented Reality , Big data and analytics , Image Processing and Recognition ,Cloud computing, Cyber Security'),
					('di', 'Renewable energy sources , Green Technology'),
					('ei', 'Bio Informatics'),
					('fi', 'Financial Technology, NPD , Services'),
					('gi', 'Other Contemporary area'),


				)

	name_of_enterprise = models.CharField(max_length=50)
	name_of_enterpreneur  = models.CharField(max_length=50)
	email      = models.EmailField()
	phone_number  = models.CharField(primary_key=True, max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
	nationality  = models.CharField(max_length=50,default="")
	dob = models.CharField(max_length=50,default="")
	address = models.TextField("permanent address", default="")
	education = models.CharField(max_length=20, default="")
	website  = models.CharField(max_length=300, blank=True, validators=[URLValidator()],default="")
	organization_type = models.CharField(max_length=30, choices = org_choice,default="")
	is_your_enterprise = models.CharField(max_length=30, choices = enterprise,default="")
	impact = models.CharField("type of impact on social sector", max_length=30 , choices = type_impact,default="")
	nu_mentor = models.BooleanField("Have a mentor from NU ?" , default = False)
	name_of_mentor = models.CharField(blank =True , max_length = 50,default="")
	sector = models.CharField("sector for your enterprise" , max_length=300 , choices = sector_d,default="")
	mention = models.CharField("Mention your sector if not mentioned above" , blank = True, max_length= 40,default="")

	infra_resource = models.TextField("What all infrastructural resources you require ? Mention them clearly" , default="")
	special_req    = models.TextField("Mention any special requirement", default="", blank = True)
	pro_req        = models.TextField("Mention requirements of professional services/support if needed", blank = True)
	employee_space = models.TextField("Mention number of employees occupying the space", default="")
	current_space  = models.TextField("Are you currently occupying a space ? If yes give details such as area, location and monthly cost", default="" , blank = True)
	descr          = models.TextField("Description of your business products/services", default ="")
	descr_bplan    = models.TextField("Description of your b plan and attach a copy of the same" , default="")
	attachment_of_bplan = models.FileField(blank =True)
	sourc_fund  = models.TextField("Specify sources of funds",default ="", blank = True)
	benefic = models.TextField("Who will benefit from your product/Service",default ="")
	stp_benefit = models.TextField("How will your startup be benefitted from incubating at NU", default="")
	if_select = models.TextField("If selected , when will you start the incubation facility ?"  , default ="")
	other_de  = models.TextField("Any other details you want to give which will help evaluating your proposal ? " , default="", blank = True)
	Signature = models.FileField(default="#")

	def __str__(self):
		return self.name_of_enterprise
