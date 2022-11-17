from django.urls import path
import web.views as views

urlpatterns = [
    path("", views.IndexView.as_view(), name="home"),
    #
    path("statistics/", views.StatisticsView.as_view(), name="statistics"),
    #
    path("generate/", views.generate_fake_data, name="generate"),
    #
    path("save/", views.SaveView.as_view(), name="save"),
    path("save/journal/csv/", views.JournalCSV, name="journal_csv"),
    path("save/journal/pdf/", views.JournalPDF, name="journal_pdf"),
    path("save/thought/csv/", views.ThoughtCSV, name="thought_csv"),
    path("save/thought/pdf/", views.ThoughtPDF, name="thought_pdf"),
    path("save/sport/csv/", views.SportCSV, name="sport_csv"),
    path("save/sport/pdf/", views.SportPDF, name="sport_pdf"),
    path("save/measurements/csv/", views.MeasurementsCSV, name="measurements_csv"),
    path("save/measurements/pdf/", views.MeasurementsPDF, name="measurements_pdf"),
    path("save/food/csv/", views.FoodCSV, name="food_csv"),
    path("save/food/pdf/", views.FoodPDF, name="food_pdf"),
    path("save/heal-reasons/csv/", views.HealReasonsCSV, name="healreasons_csv"),
    path("save/heal-reasons/pdf/", views.HealReasonsPDF, name="healreasons_pdf"),
    path("save/pros-cons/csv/", views.ProsConsCSV, name="proscons_csv"),
    path("save/pros-cons/pdf/", views.ProsConsPDF, name="proscons_pdf"),
    path("save/for-the-better-life/csv/", views.ForTheBetterLifeCSV, name="forthebetterlife_csv"),
    path("save/for-the-better-life/pdf/", views.ForTheBetterLifePDF, name="forthebetterlife_pdf"),
    #
    path("journal/", views.JournalListView.as_view(), name="journal_list"),
    path("journal/add/", views.JournalCreateView.as_view(), name="journal_create"),
    path("journal/edit/<pk>", views.JournalUpdateView.as_view(), name="journal_update"),
    path("journal/del/<pk>", views.JournalDeleteView.as_view(), name="journal_delete"),
    # 
    path("thought/", views.ThoughtListView.as_view(), name="thought_list"),
    path("thought/add/", views.ThoughtCreateView.as_view(), name="thought_create"),
    path("thought/edit/<pk>", views.ThoughtUpdateView.as_view(), name="thought_update"),
    path("thought/del/<pk>", views.ThoughtDeleteView.as_view(), name="thought_delete"),
    #
    path("sport-type/", views.SportTypeListView.as_view(), name="sporttype_list"),
    path("sport-type/add/", views.SportTypeCreateView.as_view(), name="sporttype_create"),
    path("sport-type/edit/<pk>", views.SportTypeUpdateView.as_view(), name="sporttype_update"),
    path("sport-type/del/<pk>", views.SportTypeDeleteView.as_view(), name="sporttype_delete"),
    #
    path("sport/", views.SportListView.as_view(), name="sport_list"),
    path("sport/add/", views.SportCreateView.as_view(), name="sport_create"),
    path("sport/edit/<pk>", views.SportUpdateView.as_view(), name="sport_update"),
    path("sport/del/<pk>", views.SportDeleteView.as_view(), name="sport_delete"),
    #
    path("food/", views.FoodListView.as_view(), name="food_list"),
    path("food/add/", views.FoodCreateView.as_view(), name="food_create"),
    path("food/edit/<pk>", views.FoodUpdateView.as_view(), name="food_update"),
    path("food/del/<pk>", views.FoodDeleteView.as_view(), name="food_delete"),
    #
    path("heal-reasons/", views.HealReasonsListView.as_view(), name="healreasons_list"),
    path("heal-reasons/add/", views.HealReasonsCreateView.as_view(), name="healreasons_create"),
    path("heal-reasons/edit/<pk>", views.HealReasonsUpdateView.as_view(), name="healreasons_update"),
    path("heal-reasons/del/<pk>", views.HealReasonsDeleteView.as_view(), name="healreasons_delete"),
    #
    path("pros-cons/", views.ProsConsListView.as_view(), name="proscons_list"),
    path("pros-cons/add/", views.ProsConsCreateView.as_view(), name="proscons_create"),
    path("pros-cons/edit/<pk>", views.ProsConsUpdateView.as_view(), name="proscons_update"),
    path("pros-cons/del/<pk>", views.ProsConsDeleteView.as_view(), name="proscons_delete"),
    #
    path("for-the-better-life/", views.ForTheBetterLifeListView.as_view(), name="forthebetterlife_list"),
    path("for-the-better-life/add/", views.ForTheBetterLifeCreateView.as_view(), name="forthebetterlife_create"),
    path("for-the-better-life/edit/<pk>", views.ForTheBetterLifeUpdateView.as_view(), name="forthebetterlife_update"),
    path("for-the-better-life/del/<pk>", views.ForTheBetterLifeDeleteView.as_view(), name="forthebetterlife_delete"),
    #
    path("measurements/", views.MeasurementsListView.as_view(), name="measurements_list"),
    path("measurements/add/", views.MeasurementsCreateView.as_view(), name="measurements_create"),
    path("measurements/edit/<pk>", views.MeasurementsUpdateView.as_view(), name="measurements_update"),
    path("measurements/del/<pk>", views.MeasurementsDeleteView.as_view(), name="measurements_delete"),
]
