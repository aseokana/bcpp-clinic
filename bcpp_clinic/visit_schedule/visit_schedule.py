import sys

from django.core.management.color import color_style

from edc_map.site_mappers import site_mappers
from edc_visit_schedule.visit_schedule import VisitSchedule

from bcpp_clinic.visit_schedule.clinic_schedule import clinic_schedule


style = color_style()

try:
    map_area = site_mappers.current_map_area
except AttributeError as e:
    sys.stdout.write(style.ERROR(
        '  * ERROR: visit schedule requires the current map area. '
        'Either the site mapper is not set or the current map area '
        'is not a valid \'community\'.\n    Got {} ({})\n'.format(
            site_mappers.current_map_area, str(e))))


clinic_visit_schedule = VisitSchedule(
    name='clinic_visit_schedule',
    verbose_name='BCPP Clinic Survey',
    app_label='bcpp_clinic',
    visit_model='bcpp_clinic.clinicvisit',
    offstudy_model='bcpp_clinic.clinicoffstudy',
    previous_visit_schedule=None,
)

clinic_visit_schedule.add_schedule(clinic_schedule)
