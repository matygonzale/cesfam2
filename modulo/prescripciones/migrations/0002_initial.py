# Generated by Django 4.0.5 on 2022-06-02 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('medicamentos', '0001_initial'),
        ('prescripciones', '0001_initial'),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='idCarnet_Paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.carnet_paciente'),
        ),
        migrations.AddField(
            model_name='reserva',
            name='idPrescripcion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prescripciones.prescripcion'),
        ),
        migrations.AddField(
            model_name='reg_entregas',
            name='idCarnet_Paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.carnet_paciente'),
        ),
        migrations.AddField(
            model_name='reg_entregas',
            name='idFarmaceuta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.farmaceuta'),
        ),
        migrations.AddField(
            model_name='reg_entregas',
            name='idMedicamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='medicamentos.medicamento'),
        ),
        migrations.AddField(
            model_name='prescripcion',
            name='idCarnet_Paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.carnet_paciente', verbose_name='Sector Paciente '),
        ),
        migrations.AddField(
            model_name='prescripcion',
            name='idDoctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.doctor'),
        ),
        migrations.AddField(
            model_name='cita_medica',
            name='idDoctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.doctor'),
        ),
        migrations.AddField(
            model_name='cita_medica',
            name='idPaciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.paciente'),
        ),
        migrations.AddField(
            model_name='cita_medica',
            name='idPrescripcion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='prescripciones.prescripcion'),
        ),
    ]