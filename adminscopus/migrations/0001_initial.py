# Generated by Django 2.2 on 2019-09-11 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=45, null=True)),
                ('primer_nombre', models.CharField(blank=True, max_length=45, null=True)),
                ('segundo_nombre', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'autores',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='GenderApi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_base', models.CharField(blank=True, max_length=45, null=True)),
                ('name_sanitized', models.CharField(blank=True, max_length=45, null=True)),
                ('gender', models.CharField(blank=True, max_length=45, null=True)),
                ('samples', models.CharField(blank=True, max_length=45, null=True)),
                ('accuracy', models.CharField(blank=True, max_length=45, null=True)),
                ('source', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'gender_api',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='GenderApiV2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_base', models.CharField(blank=True, max_length=45, null=True)),
                ('name_sanitized', models.CharField(blank=True, max_length=45, null=True)),
                ('gender', models.CharField(blank=True, max_length=45, null=True)),
                ('samples', models.CharField(blank=True, max_length=45, null=True)),
                ('accuracy', models.CharField(blank=True, max_length=45, null=True)),
                ('source', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'gender_api_v2',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='GsAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('citedby', models.IntegerField(blank=True, null=True)),
                ('workplace', models.CharField(blank=True, max_length=1000, null=True)),
                ('authid_scopus', models.CharField(blank=True, max_length=45, null=True)),
                ('url_perfil', models.CharField(blank=True, max_length=500, null=True)),
                ('html_perfil', models.TextField(blank=True, null=True)),
                ('auth_kw', models.CharField(blank=True, max_length=1000, null=True)),
                ('url_image', models.CharField(blank=True, max_length=1000, null=True)),
                ('name_search', models.CharField(blank=True, max_length=100, null=True)),
                ('register', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'gs_author',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='GsPublication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True)),
                ('abstract', models.TextField(blank=True, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('doi', models.CharField(blank=True, max_length=200, null=True)),
                ('magazine', models.CharField(blank=True, max_length=1000, null=True)),
                ('article_link', models.CharField(blank=True, max_length=1000, null=True)),
                ('publication_date', models.CharField(blank=True, max_length=45, null=True)),
                ('volume', models.CharField(blank=True, max_length=45, null=True)),
                ('number', models.CharField(blank=True, max_length=45, null=True)),
                ('pages', models.CharField(blank=True, max_length=45, null=True)),
                ('publisher', models.CharField(blank=True, max_length=1000, null=True)),
                ('total_citation', models.IntegerField(blank=True, null=True)),
                ('medio', models.CharField(blank=True, max_length=45, null=True)),
                ('authors', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'gs_publication',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Hub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=255)),
                ('label', models.TextField(db_column='LABEL')),
                ('description', models.TextField(blank=True, db_column='DESCRIPTION', null=True)),
                ('type', models.CharField(blank=True, db_column='TYPE', max_length=50, null=True)),
                ('subtype', models.CharField(blank=True, db_column='SUBTYPE', max_length=50, null=True)),
                ('subjectarea', models.CharField(blank=True, db_column='SUBJECTAREA', max_length=50, null=True)),
                ('year', models.IntegerField(db_column='YEAR')),
                ('language', models.CharField(db_column='LANGUAGE', max_length=50)),
                ('organization', models.CharField(db_column='ORGANIZATION', max_length=255)),
                ('source', models.CharField(db_column='SOURCE', max_length=50)),
                ('link', models.CharField(blank=True, db_column='LINK', max_length=200, null=True)),
            ],
            options={
                'db_table': '_hub',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ProvidersOai',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baseurl', models.CharField(db_column='baseURL', max_length=255, unique=True)),
                ('informationurl', models.CharField(blank=True, db_column='informationURL', max_length=255, null=True)),
                ('statushttp', models.IntegerField(db_column='statusHTTP')),
                ('repositoryname', models.TextField(blank=True, db_column='repositoryName', null=True)),
                ('repositorysoftware', models.CharField(blank=True, db_column='repositorySoftware', max_length=255, null=True)),
                ('repositoryidentifier', models.CharField(blank=True, db_column='repositoryIdentifier', max_length=255, null=True)),
                ('sampleidentifier', models.CharField(blank=True, db_column='sampleIdentifier', max_length=255, null=True)),
                ('adminemail', models.CharField(blank=True, db_column='adminEmail', max_length=255, null=True)),
                ('protocolversion', models.CharField(blank=True, db_column='protocolVersion', max_length=25, null=True)),
                ('comment', models.CharField(blank=True, max_length=255, null=True)),
                ('harvestsets', models.IntegerField(db_column='harvestSets')),
                ('processsets', models.IntegerField(db_column='processSets')),
                ('harvestxml', models.IntegerField(db_column='harvestXML')),
                ('processxml', models.IntegerField(db_column='processXML')),
                ('organization', models.TextField(blank=True, null=True)),
                ('website', models.CharField(blank=True, max_length=255, null=True)),
                ('country_name', models.CharField(blank=True, max_length=100, null=True)),
                ('region_name', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('latitude', models.CharField(blank=True, max_length=100, null=True)),
                ('longitude', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('team', models.CharField(blank=True, max_length=255, null=True)),
                ('lastresumptiontoken', models.CharField(blank=True, db_column='lastResumptionToken', max_length=255, null=True)),
                ('lastresumptiontokensets', models.CharField(blank=True, db_column='lastResumptionTokenSets', max_length=255, null=True)),
                ('siglas', models.CharField(blank=True, max_length=255, null=True)),
                ('identifier', models.CharField(blank=True, db_column='Identifier', max_length=255, null=True)),
                ('scopus_identifier', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'providers_OAI',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ScpAffiliation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('affiliation_url', models.CharField(blank=True, max_length=500, null=True)),
                ('afid', models.BigIntegerField()),
                ('affilname', models.CharField(blank=True, max_length=500, null=True)),
                ('affiliation_city', models.CharField(blank=True, max_length=200, null=True)),
                ('affiliation_country', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'scp_affiliation',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ScpAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_url', models.CharField(blank=True, max_length=500, null=True)),
                ('authid', models.BigIntegerField()),
                ('authname', models.CharField(blank=True, max_length=200, null=True)),
                ('given_name', models.CharField(blank=True, max_length=45, null=True)),
                ('surname', models.CharField(blank=True, max_length=500, null=True)),
                ('initials', models.CharField(blank=True, max_length=45, null=True)),
                ('document_count', models.IntegerField(blank=True, null=True)),
                ('eid', models.CharField(blank=True, max_length=50, null=True)),
                ('orcid', models.CharField(blank=True, max_length=50, null=True)),
                ('download', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=100, null=True)),
                ('samples', models.IntegerField(blank=True, null=True)),
                ('accuracy', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'scp_author',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ScpConsulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=500, null=True)),
                ('total_resultados', models.IntegerField(blank=True, null=True)),
                ('register', models.DateTimeField(blank=True, null=True)),
                ('estado', models.IntegerField(blank=True, null=True)),
                ('link', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 'scp_consulta',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ScpFuncionalidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('padre', models.CharField(blank=True, max_length=45, null=True)),
                ('nombre', models.CharField(blank=True, max_length=45, null=True)),
                ('url', models.CharField(blank=True, max_length=45, null=True)),
                ('estado', models.IntegerField(blank=True, null=True)),
                ('icono', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'scp_funcionalidad',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ScpJson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('json', models.TextField(blank=True, null=True)),
                ('register', models.DateTimeField(blank=True, null=True)),
                ('total_resultados', models.IntegerField(blank=True, null=True)),
                ('desde', models.IntegerField(blank=True, null=True)),
                ('hasta', models.IntegerField(blank=True, null=True)),
                ('link', models.CharField(blank=True, max_length=1000, null=True)),
                ('procesado', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'scp_json',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ScpPublication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dc_title', models.CharField(blank=True, max_length=2000, null=True)),
                ('prism_url', models.CharField(blank=True, max_length=500, null=True)),
                ('dc_identifier', models.BigIntegerField()),
                ('eid', models.CharField(blank=True, max_length=50, null=True)),
                ('dc_creator', models.CharField(blank=True, max_length=50, null=True)),
                ('prism_publicationname', models.CharField(blank=True, db_column='prism_publicationName', max_length=500, null=True)),
                ('prism_issn', models.CharField(blank=True, max_length=50, null=True)),
                ('prism_eissn', models.CharField(blank=True, max_length=50, null=True)),
                ('prism_volume', models.CharField(blank=True, max_length=200, null=True)),
                ('prism_pagerange', models.CharField(blank=True, db_column='prism_pageRange', max_length=45, null=True)),
                ('prism_coverdate', models.CharField(blank=True, db_column='prism_coverDate', max_length=45, null=True)),
                ('prism_coverdisplaydate', models.CharField(blank=True, db_column='prism_coverDisplayDate', max_length=45, null=True)),
                ('prism_doi', models.CharField(blank=True, max_length=100, null=True)),
                ('dc_description', models.CharField(blank=True, max_length=10000, null=True)),
                ('citedby_count', models.IntegerField(blank=True, null=True)),
                ('prism_aggregationtype', models.CharField(blank=True, db_column='prism_aggregationType', max_length=45, null=True)),
                ('subtype', models.CharField(blank=True, max_length=45, null=True)),
                ('subtypedescription', models.CharField(blank=True, db_column='subtypeDescription', max_length=45, null=True)),
                ('authkeywords', models.CharField(blank=True, max_length=5000, null=True)),
                ('intid', models.IntegerField(blank=True, db_column='intId', null=True)),
                ('source_id', models.CharField(blank=True, max_length=45, null=True)),
                ('article_number', models.CharField(blank=True, max_length=100, null=True)),
                ('found_acr', models.CharField(blank=True, max_length=500, null=True)),
                ('found_sponsor', models.CharField(blank=True, max_length=500, null=True)),
                ('found_no', models.CharField(blank=True, max_length=500, null=True)),
                ('pii', models.CharField(blank=True, max_length=100, null=True)),
                ('author_count', models.IntegerField(blank=True, null=True)),
                ('prism_issueidentifier', models.CharField(blank=True, db_column='prism_issueIdentifier', max_length=100, null=True)),
                ('pubmed_id', models.IntegerField(blank=True, null=True)),
                ('pos_json', models.IntegerField(blank=True, null=True)),
                ('scp_json', models.ForeignKey(db_column='scp_json', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='adminscopus.ScpJson')),
            ],
            options={
                'db_table': 'scp_publication',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ScpRol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=45, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'scp_rol',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ScpUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=45, null=True)),
                ('correo', models.CharField(blank=True, max_length=45, null=True)),
                ('usuario', models.CharField(blank=True, max_length=45, null=True)),
                ('register', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'scp_usuario',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ScpSubconsulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=500, null=True)),
                ('total_resultados', models.IntegerField(blank=True, null=True)),
                ('cosechado', models.IntegerField(blank=True, null=True)),
                ('register', models.DateTimeField(blank=True, null=True)),
                ('link', models.CharField(blank=True, max_length=1500, null=True)),
                ('scp_consulta', models.ForeignKey(db_column='scp_consulta', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='adminscopus.ScpConsulta')),
            ],
            options={
                'db_table': 'scp_subconsulta',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ScpRolUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scp_rol', models.ForeignKey(db_column='scp_rol', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='adminscopus.ScpRol')),
                ('scp_usuario', models.ForeignKey(db_column='scp_usuario', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='adminscopus.ScpUsuario')),
            ],
            options={
                'db_table': 'scp_rol_usuario',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ScpRolFuncionalidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scp_funcionalidad', models.ForeignKey(db_column='scp_funcionalidad', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='adminscopus.ScpFuncionalidad')),
                ('scp_usuario', models.ForeignKey(db_column='scp_usuario', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='adminscopus.ScpUsuario')),
            ],
            options={
                'db_table': 'scp_rol_funcionalidad',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ScpPublicationAuthkw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dc_identifier', models.BigIntegerField(blank=True, null=True)),
                ('keyword', models.CharField(blank=True, max_length=1000, null=True)),
                ('scp_publication', models.ForeignKey(db_column='scp_publication', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='adminscopus.ScpPublication')),
            ],
            options={
                'db_table': 'scp_publication_authkw',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ScpPublicationAffiliation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dc_identifier', models.BigIntegerField()),
                ('afid', models.BigIntegerField(blank=True, null=True)),
                ('scp_affiliation', models.ForeignKey(blank=True, db_column='scp_affiliation', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='adminscopus.ScpAffiliation')),
                ('scp_publication', models.ForeignKey(db_column='scp_publication', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='adminscopus.ScpPublication')),
            ],
            options={
                'db_table': 'scp_publication_affiliation',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ScpProyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=200, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=1000, null=True)),
                ('register', models.DateTimeField(blank=True, null=True)),
                ('apikey', models.CharField(blank=True, max_length=45, null=True)),
                ('tipo', models.CharField(blank=True, max_length=45, null=True)),
                ('scp_usuario', models.ForeignKey(db_column='scp_usuario', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='adminscopus.ScpUsuario')),
            ],
            options={
                'db_table': 'scp_proyecto',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='scpjson',
            name='scp_subconsulta',
            field=models.ForeignKey(db_column='scp_subconsulta', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='adminscopus.ScpSubconsulta'),
        ),
        migrations.AddField(
            model_name='scpconsulta',
            name='proyecto',
            field=models.ForeignKey(db_column='proyecto', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='adminscopus.ScpProyecto'),
        ),
        migrations.CreateModel(
            name='ScpAuthorAffiliation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dc_identifier', models.BigIntegerField()),
                ('authid', models.BigIntegerField(blank=True, null=True)),
                ('afid', models.BigIntegerField(blank=True, null=True)),
                ('orden', models.IntegerField(blank=True, null=True)),
                ('scp_affiliation', models.ForeignKey(blank=True, db_column='scp_affiliation', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='adminscopus.ScpAffiliation')),
                ('scp_author', models.ForeignKey(blank=True, db_column='scp_author', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='adminscopus.ScpAuthor')),
                ('scp_publication', models.ForeignKey(db_column='scp_publication', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='adminscopus.ScpPublication')),
            ],
            options={
                'db_table': 'scp_author_affiliation',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ScpAuth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, max_length=45, null=True)),
                ('clave', models.CharField(blank=True, max_length=45, null=True)),
                ('ultimo_ingreso', models.DateTimeField(blank=True, null=True)),
                ('scp_usuario', models.ForeignKey(db_column='scp_usuario', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='adminscopus.ScpUsuario')),
            ],
            options={
                'db_table': 'scp_auth',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ScpAffiliationVariant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_variant', models.CharField(blank=True, max_length=1000, null=True)),
                ('afid', models.BigIntegerField(blank=True, null=True)),
                ('scp_affiliation', models.ForeignKey(db_column='scp_affiliation', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='adminscopus.ScpAffiliation')),
            ],
            options={
                'db_table': 'scp_affiliation_variant',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ProvidersEquiv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.BigIntegerField(blank=True, null=True, unique=True)),
                ('name_variant', models.CharField(blank=True, max_length=1000, null=True)),
                ('siglas', models.CharField(blank=True, max_length=45, null=True)),
                ('fuente', models.CharField(blank=True, max_length=45, null=True)),
                ('provider_oai', models.ForeignKey(blank=True, db_column='provider_oai', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='adminscopus.ProvidersOai')),
            ],
            options={
                'db_table': 'providers_equiv',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='GsPerfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('citedby', models.IntegerField(blank=True, null=True)),
                ('workplace', models.CharField(blank=True, max_length=1000, null=True)),
                ('url_perfil', models.CharField(blank=True, max_length=500, null=True)),
                ('auth_kw', models.CharField(blank=True, max_length=1000, null=True)),
                ('url_image', models.CharField(blank=True, max_length=1000, null=True)),
                ('name_search', models.CharField(blank=True, max_length=100, null=True)),
                ('register', models.DateTimeField(blank=True, null=True)),
                ('gs_author', models.ForeignKey(blank=True, db_column='gs_author', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='adminscopus.GsAuthor')),
            ],
            options={
                'db_table': 'gs_perfil',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='GsHtml',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_publications_page', models.CharField(blank=True, max_length=1000, null=True)),
                ('html_publications', models.TextField(blank=True, null=True)),
                ('register', models.DateTimeField(blank=True, null=True)),
                ('gs_perfil', models.ForeignKey(db_column='gs_perfil', default='1', on_delete=django.db.models.deletion.DO_NOTHING, to='adminscopus.GsPerfil')),
            ],
            options={
                'db_table': 'gs_html',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='GsAuthorPublication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gs_perfil', models.ForeignKey(db_column='gs_perfil', default='1', on_delete=django.db.models.deletion.DO_NOTHING, to='adminscopus.GsPerfil')),
                ('gs_publication', models.ForeignKey(db_column='gs_publication', default='1', on_delete=django.db.models.deletion.DO_NOTHING, to='adminscopus.GsPublication')),
            ],
            options={
                'db_table': 'gs_author_publication',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='GsAuthorKw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kw', models.CharField(blank=True, max_length=500, null=True)),
                ('url_auth_similar', models.CharField(blank=True, max_length=1000, null=True)),
                ('register', models.DateTimeField(blank=True, null=True)),
                ('gs_perfil', models.ForeignKey(db_column='gs_perfil', default='1', on_delete=django.db.models.deletion.DO_NOTHING, to='adminscopus.GsPerfil')),
            ],
            options={
                'db_table': 'gs_author_kw',
                'managed': True,
            },
        ),
    ]
