from django.conf.urls import url, patterns

urlpatterns = patterns('course_dashboard.problem_stats.views',
                       url(r'^index/$', 'index', name='index'),
                       url(r'^get_stats/(?P<problem_id>.*)$', 'get_stats', name='get-stats'),
)
