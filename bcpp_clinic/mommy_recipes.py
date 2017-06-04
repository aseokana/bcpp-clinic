# coding=utf-8

from dateutil.relativedelta import relativedelta
from faker import Faker
from model_mommy.recipe import Recipe, seq

from edc_base_test.utils import get_utcnow
from edc_constants.constants import NOT_APPLICABLE, YES, FEMALE, ALIVE, NO
from member.choices import REASONS_REFUSED
from bcpp_clinic.choices import REGISTRATION_TYPES

from .constants import ABLE_TO_PARTICIPATE
from .models import ClinicEligibility, ClinicHouseholdMember, ClinicConsent, ClinicRefusedMember, ClinicSubjectLocator, ClinicVisit, DailyLog, Questionnaire, ViralLoadTracking
from bcpp_clinic.models.clinic_enrollment_loss import ClinicEnrollmentLoss
from bcpp_clinic import choices
from edc_base.utils import get_utcnow


fake = Faker()

cliniceligibility = Recipe(
    ClinicEligibility,
    report_datetime=get_utcnow,
    dob=(get_utcnow() - relativedelta(years=25)).date(),
    part_time_resident=YES,
    initials='EW',
    gender=FEMALE,
    household_residency=YES,
    has_identity=YES,
    identity=seq('12315678'),
    confirm_identity=seq('12315678'),
    identity_type='OMANG',
    citizen=YES,
    literacy=YES,
    guardian=NOT_APPLICABLE,
    confirm_participation=NOT_APPLICABLE,
)

clinichouseholdmember = Recipe(
    ClinicHouseholdMember,
    report_datetime=get_utcnow,
    first_name=fake.first_name,
    initials='XX',
    inability_to_participate=ABLE_TO_PARTICIPATE,
    survival_status=ALIVE,
    age_in_years=25,
    study_resident=YES,
    gender=FEMALE,
    relation='cousin',
    subject_identifier=None,
    subject_identifier_as_pk=None,
    subject_identifier_aka=None,
    internal_identifier=None,
)

clinicenrollmentloss = Recipe(
    ClinicEnrollmentLoss,
    created=get_utcnow(),
    reason='reason for clinic enrollment loss',
)

clinicrefusedmember = Recipe(
    ClinicRefusedMember,
    refusal_date=get_utcnow(),
    reason=REASONS_REFUSED,
    comment=None
)

clinicsubjectlocator = Recipe(
    ClinicSubjectLocator,
    mail_address=None,
    home_visit_permission=YES,
    physical_address=None,
    may_follow_up=YES,
    may_sms_follow_up=YES,
    subject_cell=None,
    subject_cell_alt=None,
    subject_phone=None,
    subject_phone_alt=None,
    may_contact_someone=NO,
    contact_name=None,
    contact_rel=None,
    contact_physical_address=None,
    contact_cell=None,
    contact_phone=None,
    has_alt_contact=NO,
    alt_contact_name=None,
    alt_contact_rel=None,
    alt_contact_tel=None,
    other_alt_contact_cell=None,
    may_call_work=NO,
    subject_work_place=None,
    subject_work_phone=None
)

dailylog = Recipe(
    DailyLog,
    report_date=get_utcnow(),
    from_pharma=3,
    from_ssc=3,
    from_other=3,
    idcc_scheduled=3,
    idcc_newly_registered=5,
    idcc_no_shows=4,
    approached=3,
    refused=2
)

questionnaire = Recipe(
    Questionnaire,
    clinic_visit=None,
    report_datetime=get_utcnow(),
    registration_type=REGISTRATION_TYPES,
    on_arv=YES,
    knows_last_cd4=YES,
    cd4_count=1.3
)

viralloadtracking = Recipe(
    ViralLoadTracking,
    clinic_visit=None,
    report_datetime=get_utcnow(),
    is_drawn=YES,
    reason_not_drawn=None,
    drawn_datetime=get_utcnow(),
    clinician_initials='XX'
)
