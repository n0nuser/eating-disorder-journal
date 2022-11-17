from web.views.home import IndexView
from web.views.generate import generate_fake_data
from web.views.save import (
    SaveView,
    JournalCSV, JournalPDF,
    ThoughtCSV, ThoughtPDF,
    SportCSV, SportPDF,
    FoodCSV, FoodPDF,
    MeasurementsCSV, MeasurementsPDF,
    ForTheBetterLifeCSV, ForTheBetterLifePDF,
    HealReasonsCSV, HealReasonsPDF,
    ProsConsCSV, ProsConsPDF,
)
from web.views.statistics import StatisticsView

from web.views.journal import JournalListView, JournalCreateView, JournalUpdateView, JournalDeleteView
from web.views.thought import ThoughtListView, ThoughtCreateView, ThoughtUpdateView, ThoughtDeleteView
from web.views.food import FoodListView, FoodCreateView, FoodUpdateView, FoodDeleteView
from web.views.measurements import MeasurementsListView, MeasurementsCreateView, MeasurementsUpdateView, MeasurementsDeleteView
from web.views.sport import SportListView, SportCreateView, SportUpdateView, SportDeleteView
from web.views.sport_type import SportTypeListView, SportTypeCreateView, SportTypeUpdateView, SportTypeDeleteView
from web.views.forthebetterlife import ForTheBetterLifeListView, ForTheBetterLifeCreateView, ForTheBetterLifeUpdateView, ForTheBetterLifeDeleteView
from web.views.healreasons import HealReasonsListView, HealReasonsCreateView, HealReasonsUpdateView, HealReasonsDeleteView
from web.views.proscons import ProsConsListView, ProsConsCreateView, ProsConsUpdateView, ProsConsDeleteView
