# Generated by Django 2.1.7 on 2019-12-10 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('sent_at', models.DateTimeField(blank=True, null=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (2, 'Published')])),
            ],
        ),
        migrations.CreateModel(
            name='EmailSub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('status', models.IntegerField(choices=[(0, 'Subscribed'), (1, 'Unsubscribed')])),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('rank', models.FloatField(blank=True, default=0)),
                ('status', models.IntegerField(choices=[(0, 'Pending'), (1, 'Open'), (2, 'Closed'), (3, 'Deleted')], default=1)),
                ('type', models.IntegerField(choices=[(0, 'Question'), (1, 'Meta'), (2, 'Answer'), (3, 'Comment')], db_index=True)),
                ('vote_count', models.IntegerField(blank=True, db_index=True, default=0)),
                ('view_count', models.IntegerField(blank=True, default=0)),
                ('reply_count', models.IntegerField(blank=True, default=0)),
                ('comment_count', models.IntegerField(blank=True, default=0)),
                ('book_count', models.IntegerField(default=0)),
                ('changed', models.BooleanField(default=True)),
                ('subs_count', models.IntegerField(default=0)),
                ('thread_score', models.IntegerField(blank=True, db_index=True, default=0)),
                ('creation_date', models.DateTimeField(db_index=True)),
                ('lastedit_date', models.DateTimeField(db_index=True)),
                ('sticky', models.BooleanField(db_index=True, default=False)),
                ('has_accepted', models.BooleanField(blank=True, default=False)),
                ('content', models.TextField(default='')),
                ('html', models.TextField(default='')),
                ('tag_val', models.CharField(blank=True, default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PostPreview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('type', models.IntegerField(choices=[(0, 'Question'), (1, 'Meta'), (2, 'Answer'), (3, 'Comment')])),
                ('content', models.TextField(default='')),
                ('tag_val', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('memo', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReplyToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_created=True)),
                ('token', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(3, 'default'), (0, 'local messages'), (1, 'email'), (4, 'email for every new thread (mailing list mode)')], db_index=True, default=0)),
                ('date', models.DateTimeField(db_index=True, verbose_name='Date')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(db_index=True, max_length=50)),
                ('count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(0, 'Upvote'), (1, 'DownVote'), (2, 'Bookmark'), (3, 'Accept')], db_index=True)),
                ('date', models.DateTimeField(auto_now=True, db_index=True)),
            ],
        ),
    ]
