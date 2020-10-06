from django.contrib import admin
import nested_admin
from .models import Questions_teacher, Questions_student, Questions_answer
# Register your models here.

class AnswerInline(nested_admin.NestedTabularInline):
	model = Questions_answer
	extra = 4
	max_num = 4

class QuestionTeacherInline(nested_admin.NestedTabularInline):
	model = Questions_teacher
	inlines = [AnswerInline,]
	extra = 5

class QuestionAdmin(nested_admin.NestedModelAdmin):
	inlines = [AnswerInline,]


admin.site.register(Questions_answer)
admin.site.register(Questions_student,QuestionAdmin)
admin.site.register(Questions_teacher, QuestionAdmin)








# class UsersAnswerInline(admin.TabularInline):
# 	model = UsersAnswer


# class QuizTakerAdmin(admin.ModelAdmin):
# 	inlines = [UsersAnswerInline,]


# admin.site.register(Quiz, QuizAdmin)
# admin.site.register(Question)
# admin.site.register(Answer)
# admin.site.register(QuizTaker, QuizTakerAdmin)
# admin.site.register(UsersAnswer)


