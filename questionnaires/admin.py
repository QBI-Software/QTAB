from django.contrib import admin
#from suit.widgets import HTML5Input
from .models import Questionnaire, Question, Choice, SubjectVisit, Category


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('questionnaire','question','choice_text','choice_image','choice_value')
    #list_filter =['choice_type']

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3



class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('qid','question_text', 'question_image','order','num_choices','question_type')
    list_filter = ['group','question_type']
    search_fields = ['question_text']
    actions = ['create_true','create_true1','create_true2','create_true3',
               'create_interpersonal',
               'create_agree','create_agree1',
               'create_yesnosometimes',
               'create_never_always',
               'create_never_often',
               'create_never_most',
               'create_good_bad',
               'create_little_much',
               'create_5number',
               'create_7number',
               'create_9number',
               'create_yesno',
               'create_days',
               'create_languages',
               'create_education',
               'create_aboriginal']


    def create_radiobuttons(self,request,queryset,labels):
        for obj in queryset:
            #Clear previous choices
            print(obj)
            for c in obj.choice_set.all():
                c.delete()
            num = 1
            for label in labels:
                ch = Choice(question=obj, choice_text=label, choice_value=num)
                ch.save()
                num += 1
        msg = 'Questions have been CREATED for selected questionnaires'
        self.message_user(request, msg)

    def create_true(self, request, queryset):
        labels = ["Not True", "Somewhat True", "Certainly True"]
        self.create_radiobuttons(request,queryset,labels)

    def create_true1(self, request, queryset):
        labels = ["Not True", "Sometimes", "True"]
        self.create_radiobuttons(request,queryset,labels)

    def create_true2(self, request, queryset):
        labels = ["Almost always untrue of you", "Usually untrue of you",
                  "Sometimes true, sometimes untrue of you",
                  "Usually true of you",
                  "Almost always true of you"]
        self.create_radiobuttons(request,queryset,labels)

    def create_true3(self, request, queryset):
        labels = ["Not true at all", "Slightly true",
                  "Moderately true",
                  "Extremely true"]
        self.create_radiobuttons(request,queryset,labels)

    def create_interpersonal(self, request, queryset):
        labels = ["A (Does not describe me well)", "B", "C", "D", "E (Describes me very well"]
        self.create_radiobuttons(request,queryset,labels)

    def create_yesnosometimes(self, request, queryset):
        labels = ["Yes", "No", "Sometimes","Don't know"]
        self.create_radiobuttons(request, queryset, labels)

    def create_never_always(self, request, queryset):
        labels = ["Never", "Sometimes", "Often","Always"]
        self.create_radiobuttons(request, queryset, labels)

    def create_never_often(self, request, queryset):
        labels = ["Never", "Rarely", "Occasionally","Often","Very Often","Not Applicable"]
        self.create_radiobuttons(request, queryset, labels)

    def create_never_most(self, request, queryset):
        labels = ["Never", "Sometimes", "Often","Most of the time"]
        self.create_radiobuttons(request, queryset, labels)

    def create_agree(self, request, queryset):
        labels = ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"]
        self.create_radiobuttons(request, queryset, labels)
    #Social Support
    def create_agree1(self, request, queryset):
        labels = ["Very Strongly Disagree","Strongly Disagree", "Mildly Disagree", "Neutral",
                  "Mildly Agree", "Strongly Agree", "Very Strongly Agree"]
        self.create_radiobuttons(request, queryset, labels)

    def create_good_bad(self, request, queryset):
        labels = ["Extremely bad", "Very bad", "Somewhat bad", "Slightly bad",
                  "Neither good or bad", "Slightly good", "Somewhat good", "Very good",
                  "Extremely good"]
        self.create_radiobuttons(request, queryset, labels)

    def create_little_much(self, request, queryset):
        labels = ["Not at all", "A little", "Some","A lot", "Very much"]
        self.create_radiobuttons(request, queryset, labels)


    def create_5number(self, request, queryset):
        labels = ["1", "2", "3", "4", "5","NA"]
        self.create_radiobuttons(request, queryset, labels)

    def create_7number(self, request, queryset):
        labels = ["1", "2", "3", "4", "5","6","7"]
        self.create_radiobuttons(request, queryset, labels)

    def create_9number(self, request, queryset):
        labels = ["1", "2", "3", "4", "5", "6", "7","8","9"]
        self.create_radiobuttons(request, queryset, labels)

    def create_yesno(self, request, queryset):
        labels = ["Yes", "No"]
        self.create_radiobuttons(request, queryset, labels)

    def create_aboriginal(self, request, queryset):
        labels = ["No", "Yes, Aboriginal","Yes, Torres Strait Islander",
                  "Yes, both Aboriginal and Torres Strait Islander",
                  "Don't know"]
        self.create_radiobuttons(request, queryset, labels)

    def create_languages(self, request, queryset):
        labels = ["Afrikaans","Arabic","Cantonese","Croatian","French","German","Greek",
                  "Hindi","Italian","Japanese","Malaysian","Mandarin","Macedonian","Polish",
                  "Serbian","Spanish","Tagalog/ Filipino","Turkish","Vietnamese","Other (specify)","Don’t know"]
        self.create_radiobuttons(request, queryset, labels)

    def create_education(self, request, queryset):
        labels = ["No formal education","Up to year 7 or equivalent (Primary School)",
                  "Year 8 or equivalent (Junior High School)","Year 9 or equivalent (Junior High School)",
                  "Year 10 or equivalent (Junior High School)","Year 11 or equivalent (Senior High School)",
                  "Year 12 or equivalent (Senior High School)","Don’t know"]
        self.create_radiobuttons(request, queryset, labels)

    #Substance Use
    def create_days(self, request, queryset):
        labels = ["Never", "Less often than 1 day a month",
                  "About 1 day a month", "2 to 3 days a month",
                  "Once a week", "2 to 3 days a week",
                  "4 to 6 days a week", "Every day"]
        self.create_radiobuttons(request, queryset, labels)


    create_true.short_description = "Create 'Not-Somewhat-Certainly True' Options"
    create_true1.short_description = "Create 'Not true-Sometimes-True' Options"
    create_true2.short_description = "Create verbose 'True of you' Options"
    create_true3.short_description = "Create verbose 'True' Options"
    create_interpersonal.short_description = "Create 'A to E' describes me well Options"
    create_yesnosometimes.short_description = "Create 'Yes-No-Sometimes-Don\'t know' Options"
    create_never_always.short_description = "Create 'Never...Always' Options"
    create_never_often.short_description = "Create 'Never...Often, NA' Options"
    create_never_most.short_description = "Create 'Never...Most of the time' Options"
    create_agree.short_description = "Create 'Disagree-Agree' Options"
    create_agree1.short_description = "Create 'Strongly Disagree-Agree' Options"
    create_good_bad.short_description = "Create 'Good-Bad' Options"
    create_little_much.short_description = "Create 'A little-Very much' Options"
    create_5number.short_description ="Create range '1 to 5' with NA options"
    create_7number.short_description = "Create range '1 to 7' options"
    create_9number.short_description = "Create range '1 to 9' options"
    create_yesno.short_description = "Create 'Yes No' Options"
    create_days.short_description = "Create 'Days, weeks, months' Options"
    create_aboriginal.short_description = "Create 'Aboriginal' Options"
    create_languages.short_description = "Create 'Language' Options"
    create_education.short_description = "Create 'Education' Options"

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 3



class QuestionnaireAdmin(admin.ModelAdmin):

    fieldsets = [
        (None, {'fields': ['title','active','description', 'intropage','code','type','category','group']}),
    ]
    inlines = [QuestionInline]
    list_display = ('title','description','code','type','active','categorylist','num_questions')
    list_filter = ['type','active']
    search_fields = ['title']
    actions=['sequence_questions','remove_questionnaire_results']

    def sequence_questions(self,request,queryset):
        """ Generate order sequences for questions in set of questionnaires - will reset existing """

        for obj in queryset:
            qnlist = obj.question_set.order_by('pk')
            #total = qnlist.count()
            num = 1
            for q in qnlist:
                q.order=num
                q.save()
                num += 1
        msg = 'Questions have been ordered for selected questionnaires'
        self.message_user(request, msg)

    def remove_questionnaire_results(self, request,queryset):
        """ Delete all result sets for selected questionnaires """
        n = 0
        for obj in queryset:
            print("DEBUG: Questionnaire ", obj, " results to delete=", obj.testresult_set.count())
            n0 = 0
            for t in obj.testresult_set.all():
                t.delete()
                n0 += 1
            for s in obj.subjectquestionnaire_set.all():
                s.delete()
            n = n+ n0
        msg = "%d result sets successfully REMOVED from selected questionnaires." % n
        self.message_user(request, msg)


    sequence_questions.short_description = 'Number all questions'
    remove_questionnaire_results.short_description = 'Remove questionnaire results'

class SubjectVisitAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['date_visit', 'subject', 'category', 'xnatid','parent1','parent2','twin','icon']}),
    ]
    list_display = ( 'subject','category', 'date_visit', 'xnatid','parent1','parent2','twin','icon')
    list_filter = ['category']
    search_fields = ['subject__username']

admin.site.register(Questionnaire, QuestionnaireAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(SubjectVisit,SubjectVisitAdmin)
#admin.site.register(Category)