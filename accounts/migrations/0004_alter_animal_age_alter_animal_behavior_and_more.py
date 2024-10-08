# Generated by Django 5.0.6 on 2024-09-07 15:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0003_animal_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="animal",
            name="age",
            field=models.CharField(
                blank=True, max_length=20, null=True, verbose_name="อายุเฉลี่ย"
            ),
        ),
        migrations.AlterField(
            model_name="animal",
            name="behavior",
            field=models.TextField(
                blank=True, max_length=500, null=True, verbose_name="พฤติกรรม"
            ),
        ),
        migrations.AlterField(
            model_name="animal",
            name="category",
            field=models.CharField(
                blank=True,
                choices=[
                    ("mammals", "สัตว์เลี้ยงลูกด้วยนม"),
                    ("reptiles", "สัตว์เลื้อยคลาน"),
                    ("birds", "สัตว์ปีก"),
                    ("fish", "สัตว์น้ำ"),
                    ("amphibians", "สะเทินน้ำสะเทินบก"),
                ],
                max_length=100,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="animal",
            name="food",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="อาหาร"
            ),
        ),
        migrations.AlterField(
            model_name="animal",
            name="habitat",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="ถิ่นอาศัย"
            ),
        ),
        migrations.AlterField(
            model_name="animal",
            name="interest",
            field=models.TextField(
                blank=True, max_length=1000, null=True, verbose_name="สิ่งที่น่าสนใจ"
            ),
        ),
        migrations.AlterField(
            model_name="animal",
            name="photo",
            field=models.ImageField(blank=True, null=True, upload_to="animals/photos/"),
        ),
        migrations.AlterField(
            model_name="animal",
            name="reproductive_age",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="วัยเจริญพันธุ์"
            ),
        ),
        migrations.AlterField(
            model_name="animal",
            name="scientific_name",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="ชื่อวิทยาศาสตร์"
            ),
        ),
        migrations.AlterField(
            model_name="animal",
            name="size_weight",
            field=models.CharField(
                blank=True, max_length=200, null=True, verbose_name="ขนาดและน้ำหนัก"
            ),
        ),
    ]
