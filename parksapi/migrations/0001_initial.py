# Generated by Django 4.1.6 on 2023-02-16 15:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('post_body', models.CharField(max_length=1000)),
                ('date_created', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Campground',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('available_sites', models.IntegerField()),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=255)),
                ('start_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='NaturalAttraction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Park',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('history', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=800)),
                ('park', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='park_photos', to='parksapi.park')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_photos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WildlifeGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Wildlife',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('information', models.CharField(max_length=255)),
                ('image', models.CharField(max_length=5000)),
                ('wildlife_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_wildlife', to='parksapi.wildlifegroup')),
            ],
        ),
        migrations.CreateModel(
            name='PhotoFavorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_photo', to='parksapi.photo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_photo_favorites', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ParkWildlife',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('park', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wildlife_at_park', to='parksapi.park')),
                ('wildlife', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wildlife', to='parksapi.wildlife')),
            ],
        ),
        migrations.CreateModel(
            name='ParkNaturalAttraction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=255)),
                ('attraction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attraction_types', to='parksapi.naturalattraction')),
                ('park', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attractions_by_park', to='parksapi.park')),
            ],
        ),
        migrations.CreateModel(
            name='ParkFavorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('park', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_park', to='parksapi.park')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ParkAmenity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('amenity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='type_amenities', to='parksapi.amenity')),
                ('park', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='park_amenities', to='parksapi.park')),
            ],
        ),
        migrations.CreateModel(
            name='EventRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attending_events', to='parksapi.event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_events', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EventFavorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_event', to='parksapi.event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_favorite_events', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='park',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='park_events', to='parksapi.park'),
        ),
        migrations.CreateModel(
            name='CampingReservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('campground', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reserved_campgrounds', to='parksapi.campground')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_reservations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='campground',
            name='park',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='park_campgrounds', to='parksapi.park'),
        ),
        migrations.CreateModel(
            name='BlogFavorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_blog', to='parksapi.blog')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='park',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='park_blogs', to='parksapi.park'),
        ),
        migrations.AddField(
            model_name='blog',
            name='photo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog_photos', to='parksapi.photo'),
        ),
        migrations.AddField(
            model_name='blog',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_blogs', to=settings.AUTH_USER_MODEL),
        ),
    ]
