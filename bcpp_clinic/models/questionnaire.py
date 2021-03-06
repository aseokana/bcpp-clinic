from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from edc_base.model_fields.custom_fields import OtherCharField
from edc_constants.choices import YES_NO_DWTA

from ..choices import REGISTRATION_TYPES
from ..models.crf_model_mixin import CrfModelMixin


class Questionnaire(CrfModelMixin):
    """A model completed by the user that captures ARV and CD4 data."""

    registration_type = models.CharField(
        verbose_name="What type of Clinic Registration is this?",
        max_length=35,
        choices=REGISTRATION_TYPES,
        help_text="",
    )

    registration_type_other = OtherCharField()

    on_arv = models.CharField(
        verbose_name="Are you currently taking antiretroviral therapy (ARVs)?",
        max_length=25,
        choices=YES_NO_DWTA,
        help_text="",
    )

    knows_last_cd4 = models.CharField(
        verbose_name="Do you know the value of your last 'CD4' result?",
        max_length=25,
        choices=YES_NO_DWTA,
        help_text="",
    )

    cd4_count = models.DecimalField(
        verbose_name="What is the value of your last 'CD4' test?",
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(3000)],
        null=True,
        blank=True,
        help_text="",
    )

    class Meta(CrfModelMixin.Meta):
        app_label = 'bcpp_clinic'
        verbose_name = "Questionnaire"
        verbose_name_plural = "Questionnaire"
