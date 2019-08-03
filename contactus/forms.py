from django import forms
from .models import idea,join,startup


class ideaForm(forms.ModelForm):
	class Meta:
		model = idea
		fields = ('first_name','last_name','email','enrollment_no','idea','join_ciie','why_do_you_want_to_join_CIIE')

	def __init__(self, *args, **kwargs):
		super(ideaForm, self).__init__(*args, **kwargs)
		self.fields['first_name'].widget.attrs['placeholder'] = 'First name'
		self.fields['last_name'].widget.attrs['placeholder'] = 'Last name'
		self.fields['email'].widget.attrs['placeholder'] = 'Email'
		self.fields['enrollment_no'].widget.attrs['placeholder'] = 'Enrollment number'
		self.fields['idea'].widget.attrs['placeholder'] = 'Your idea'
		self.fields['why_do_you_want_to_join_CIIE'].widget.attrs['placeholder'] = 'Why do you want to join CIIE'




class joinForm(forms.ModelForm):
	class Meta:
		model = join
		fields = ('first_name','last_name','email','enrollment_no','why_do_you_want_to_join_CIIE')

	def __init__(self, *args, **kwargs):
		super(joinForm, self).__init__(*args, **kwargs)
		self.fields['first_name'].widget.attrs['placeholder'] = 'First name'
		self.fields['last_name'].widget.attrs['placeholder'] = 'Last name'
		self.fields['email'].widget.attrs['placeholder'] = 'Email'
		self.fields['enrollment_no'].widget.attrs['placeholder'] = 'Enrollment number'
		self.fields['why_do_you_want_to_join_CIIE'].widget.attrs['placeholder'] = 'Why do you want to join CIIE'


class incubationForm(forms.ModelForm):
	class Meta:
		model = startup
		fields = ('name_of_enterprise',
				  'name_of_enterpreneur',
				  'email',
				  'phone_number',
				  'nationality',
				  'dob',
				  'address',
				  'education',
				  'website',
				  'organization_type',
				  'is_your_enterprise',
				  'impact',
				  'nu_mentor',
				  'name_of_mentor',
				  'sector',
				  'mention',
				  'infra_resource',
				  'special_req',
				  'pro_req',
				  'employee_space',
				  'current_space',
				  'descr',
				  'descr_bplan',
				  'attachment_of_bplan',
				  'sourc_fund',
				  'benefic',
				  'stp_benefit',
				  'if_select',
				  'other_de',
				  'Signature',
				  )
	def __init__(self, *args, **kwargs):
		super(incubationForm, self).__init__(*args, **kwargs)
		self.fields['name_of_enterprise'].widget.attrs['placeholder'] = 'Name of enterprise'
		self.fields['name_of_enterpreneur'].widget.attrs['placeholder'] = 'Name of enterpreneur'
		self.fields['email'].widget.attrs['placeholder'] = 'Email'
		self.fields['phone_number'].widget.attrs['placeholder'] = 'Phone number'
		self.fields['nationality'].widget.attrs['placeholder'] = 'Nationality'
		self.fields['dob'].widget.attrs['placeholder'] = 'Date of birth'
		self.fields['address'].widget.attrs['placeholder'] = 'Permanent Address'
		self.fields['education'].widget.attrs['placeholder'] = 'Education'
		self.fields['website'].widget.attrs['placeholder'] = 'Website'
		self.fields['organization_type'].widget.attrs['placeholder'] = 'Organization type'
		self.fields['is_your_enterprise'].widget.attrs['placeholder'] = 'Is your enterprise'
		self.fields['impact'].widget.attrs['placeholder'] = 'Type of impact on social sector'
		self.fields['nu_mentor'].widget.attrs['placeholder'] = 'Nu mentor'
		self.fields['name_of_mentor'].widget.attrs['placeholder'] = 'Have a mentor from NU ?'
		self.fields['sector'].widget.attrs['placeholder'] = 'Sector for your enterprise'
		self.fields['mention'].widget.attrs['placeholder'] = 'Mention your sector if not mentioned above'
		self.fields['infra_resource'].widget.attrs['placeholder'] = 'What all infrastructural resources you require ? Mention them clearly'
		self.fields['special_req'].widget.attrs['placeholder'] = 'Mention any special requirement'
		self.fields['pro_req'].widget.attrs['placeholder'] = 'Mention requirements of professional services/support if needed'
		self.fields['employee_space'].widget.attrs['placeholder'] = 'Mention number of employees occupying the space'
		self.fields['current_space'].widget.attrs['placeholder'] = 'Are you currently occupying a space ? If yes give details such as area, location and monthly cost'
		self.fields['descr'].widget.attrs['placeholder'] = 'Description of your business products/services'
		self.fields['descr_bplan'].widget.attrs['placeholder'] = 'Description of your b plan and attach a copy of the same'
		self.fields['attachment_of_bplan'].widget.attrs['placeholder'] = 'Attachment of bplan'
		self.fields['sourc_fund'].widget.attrs['placeholder'] = 'Specify sources of funds'
		self.fields['benefic'].widget.attrs['placeholder'] = 'Who will benefit from your product/Service'
		self.fields['stp_benefit'].widget.attrs['placeholder'] = 'How will your startup be benefitted from incubating at NU'
		self.fields['if_select'].widget.attrs['placeholder'] = 'If selected , when will you start the incubation facility ?'
		self.fields['other_de'].widget.attrs['placeholder'] = 'Any other details you want to give which will help evaluating your proposal?'
		self.fields['Signature'].widget.attrs['placeholder'] = 'Signature'