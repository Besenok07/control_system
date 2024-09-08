
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='in_class',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='subject',
        ),
        migrations.AddField(
            model_name='student',
            name='in_class',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='students', to='school.class'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='subject',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='teachers', to='school.subject'),
            preserve_default=False,
        ),
    ]
