# Generated by Django 4.2.1 on 2023-07-10 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0003_rename_comments_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="image",
            field=models.ImageField(
                blank=True,
                upload_to="product/product_cover",
                verbose_name="Product Image",
            ),
        ),
        migrations.AlterField(
            model_name="comment",
            name="body",
            field=models.TextField(verbose_name="Comment's text"),
        ),
        migrations.AlterField(
            model_name="comment",
            name="stars",
            field=models.CharField(
                choices=[
                    ("1", "Very Bad"),
                    ("2", "Bad"),
                    ("3", "Good"),
                    ("4", "Very Good"),
                    ("5", "Amazing"),
                ],
                max_length=10,
                verbose_name="Your Rate",
            ),
        ),
    ]
