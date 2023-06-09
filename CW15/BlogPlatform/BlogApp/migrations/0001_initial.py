# Generated by Django 4.2.3 on 2023-07-14 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
        ('Author', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.CharField(max_length=500)),
                ('publication_date', models.DateTimeField(auto_now_add=True)),
                ('auther', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Author.author')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='BlogApp.post')),
                ('content', models.CharField(max_length=500)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('auther', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Author.author')),
            ],
        ),
    ]
