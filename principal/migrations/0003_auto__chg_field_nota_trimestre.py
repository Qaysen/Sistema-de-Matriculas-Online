# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Nota.trimestre'
        db.alter_column('principal_nota', 'trimestre', self.gf('django.db.models.fields.CharField')(max_length=5))

    def backwards(self, orm):

        # Changing field 'Nota.trimestre'
        db.alter_column('principal_nota', 'trimestre', self.gf('django.db.models.fields.CharField')(max_length=1))

    models = {
        'principal.alumno': {
            'Meta': {'object_name': 'Alumno'},
            'correo': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'telefono': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '0'})
        },
        'principal.curso': {
            'Meta': {'object_name': 'Curso'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'num_creditos': ('django.db.models.fields.IntegerField', [], {})
        },
        'principal.dictar': {
            'Meta': {'object_name': 'Dictar'},
            'curso': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.Curso']"}),
            'fecha_ini': ('django.db.models.fields.DateField', [], {}),
            'fecha_ter': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profesor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.Profesor']"})
        },
        'principal.matricula': {
            'Meta': {'object_name': 'Matricula'},
            'alumno': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.Alumno']"}),
            'curso': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.Curso']"}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'principal.nota': {
            'Meta': {'object_name': 'Nota'},
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'matricula': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.Matricula']"}),
            'trimestre': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'valor': ('django.db.models.fields.IntegerField', [], {})
        },
        'principal.profesor': {
            'Meta': {'object_name': 'Profesor'},
            'correo': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'telefono': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '0'})
        }
    }

    complete_apps = ['principal']