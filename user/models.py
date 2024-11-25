from django.db import models


class SMSCode(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='sms_code')
    sms_code = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sms_code

    class Meta:
        verbose_name = 'Код подтверждения'
        verbose_name_plural = 'Коды подтверждения'