from django.urls import path

from users.views import GetUser, RetrieveProfile, ListEducation, CreateEducation, ListJob, CreateJob, DeleteEducation, DeleteJob

urlpatterns = [
    path('get-user/', GetUser.as_view(), name="get_user"),
    path('profile/<str:profile_username>', RetrieveProfile.as_view(), name="get_profile"),
    path('education/<str:profile_username>', ListEducation.as_view(), name="get_education_list"),
    path('add-education/', CreateEducation.as_view(), name="add_education"),
    path('delete-education/<int:pk>/', DeleteEducation.as_view(), name="delete_education"),
    path('job/<str:profile_username>', ListJob.as_view(), name="get_job_list"),
    path('add-job/', CreateJob.as_view(), name="add_job"),
    path('delete-job/<int:pk>/', DeleteJob.as_view(), name="delete_job"),
]
