# Generated by Django 4.2.4 on 2023-11-23 01:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DepositProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_co_no', models.TextField()),
                ('kor_co_nm', models.TextField()),
                ('fin_prdt_cd', models.TextField(unique=True)),
                ('fin_prdt_nm', models.TextField()),
                ('join_way', models.TextField(blank=True, null=True)),
                ('join_member', models.TextField(blank=True, null=True)),
                ('join_deny', models.IntegerField(blank=True, null=True)),
                ('max_limit', models.TextField(blank=True, null=True)),
                ('spcl_cnd', models.TextField(blank=True, null=True)),
                ('mtrt_int', models.TextField(blank=True, null=True)),
                ('etc_note', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FinancialCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_co_no', models.TextField(unique=True)),
                ('kor_co_nm', models.TextField()),
                ('homp_url', models.TextField(blank=True, null=True)),
                ('cal_tel', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LoanForHome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_co_no', models.TextField()),
                ('kor_co_nm', models.TextField()),
                ('fin_prdt_cd', models.TextField(unique=True)),
                ('fin_prdt_nm', models.TextField()),
                ('loan_lmt', models.TextField(blank=True, null=True)),
                ('loan_inci_expn', models.TextField(blank=True, null=True)),
                ('erly_rpay_fee', models.TextField(blank=True, null=True)),
                ('dly_rate', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SavingProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_co_no', models.TextField()),
                ('kor_co_nm', models.TextField()),
                ('fin_prdt_cd', models.TextField(unique=True)),
                ('fin_prdt_nm', models.TextField()),
                ('join_way', models.TextField(blank=True, null=True)),
                ('join_member', models.TextField(blank=True, null=True)),
                ('join_deny', models.IntegerField(blank=True, null=True)),
                ('max_limit', models.TextField(blank=True, null=True)),
                ('spcl_cnd', models.TextField(blank=True, null=True)),
                ('mtrt_int', models.TextField(blank=True, null=True)),
                ('etc_note', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SavingProductOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intr_rate_type', models.TextField(blank=True, null=True)),
                ('intr_rate_type_nm', models.TextField(blank=True, null=True)),
                ('intr_rate', models.FloatField(blank=True, null=True)),
                ('intr_rate2', models.FloatField(blank=True, null=True)),
                ('save_trm', models.IntegerField(blank=True, null=True)),
                ('saving_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saving_product_option', to='financial_products.savingproduct', to_field='fin_prdt_cd')),
            ],
        ),
        migrations.CreateModel(
            name='LoanForHomeOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lend_rate_type', models.TextField(blank=True, null=True)),
                ('lend_rate_type_nm', models.TextField(blank=True, null=True)),
                ('lend_rate_avg', models.TextField(blank=True, null=True)),
                ('lend_rate_min', models.TextField(blank=True, null=True)),
                ('lend_rate_max', models.TextField(blank=True, null=True)),
                ('loan_home_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loan_home_product_option', to='financial_products.loanforhome', to_field='fin_prdt_cd')),
            ],
        ),
        migrations.CreateModel(
            name='DepositProductOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intr_rate_type', models.TextField(blank=True, null=True)),
                ('intr_rate_type_nm', models.TextField(blank=True, null=True)),
                ('intr_rate', models.FloatField(blank=True, null=True)),
                ('intr_rate2', models.FloatField(blank=True, null=True)),
                ('save_trm', models.IntegerField(blank=True, null=True)),
                ('deposit_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deposit_product_option', to='financial_products.depositproduct', to_field='fin_prdt_cd')),
            ],
        ),
    ]
