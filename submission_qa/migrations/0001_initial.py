# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'QualityReview'
        db.create_table('submission_qa_qualityreview', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('submission', self.gf('django.db.models.fields.related.ForeignKey')(related_name='quality_reviews', to=orm['parsed_xforms.ParsedInstance'])),
            ('reviewer', self.gf('django.db.models.fields.related.ForeignKey')(related_name='quality_reviews', null=True, to=orm['auth.User'])),
            ('score', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('comment', self.gf('django.db.models.fields.TextField')(null=True)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('date_changed', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('hidden', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('submission_qa', ['QualityReview'])

        # Adding unique constraint on 'QualityReview', fields ['submission', 'reviewer']
        db.create_unique('submission_qa_qualityreview', ['submission_id', 'reviewer_id'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'QualityReview', fields ['submission', 'reviewer']
        db.delete_unique('submission_qa_qualityreview', ['submission_id', 'reviewer_id'])

        # Deleting model 'QualityReview'
        db.delete_table('submission_qa_qualityreview')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'locations.district': {
            'Meta': {'object_name': 'District'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'depth': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kml_present': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'latlng_string': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'numchild': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'path': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'parsed_xforms.parsedinstance': {
            'Meta': {'object_name': 'ParsedInstance'},
            'district': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['locations.District']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instance': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'parsed_instance'", 'unique': 'True', 'to': "orm['xform_manager.Instance']"}),
            'phone': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['phone_manager.Phone']"}),
            'surveyor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['surveyor_manager.Surveyor']", 'null': 'True'})
        },
        'phone_manager.phone': {
            'Meta': {'object_name': 'Phone'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imei': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'note': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'search_field': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'functional'", 'max_length': '16'}),
            'surveyor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['surveyor_manager.Surveyor']", 'null': 'True'}),
            'visible_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'})
        },
        'submission_qa.qualityreview': {
            'Meta': {'unique_together': "(('submission', 'reviewer'),)", 'object_name': 'QualityReview'},
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'hidden': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reviewer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'quality_reviews'", 'null': 'True', 'to': "orm['auth.User']"}),
            'score': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'submission': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'quality_reviews'", 'to': "orm['parsed_xforms.ParsedInstance']"})
        },
        'surveyor_manager.surveyor': {
            'Meta': {'object_name': 'Surveyor', '_ormbases': ['auth.User']},
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        'xform_manager.instance': {
            'Meta': {'object_name': 'Instance'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {}),
            'survey_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['xform_manager.SurveyType']"}),
            'xform': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'surveys'", 'to': "orm['xform_manager.XForm']"}),
            'xml': ('django.db.models.fields.TextField', [], {})
        },
        'xform_manager.surveytype': {
            'Meta': {'object_name': 'SurveyType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'xform_manager.xform': {
            'Meta': {'ordering': "('id_string',)", 'object_name': 'XForm'},
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'downloadable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_string': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'web_title': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'xml': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['submission_qa']