# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Alumno'
        db.create_table('principal_alumno', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('telefono', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=0)),
            ('correo', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal('principal', ['Alumno'])

        # Adding model 'Profesor'
        db.create_table('principal_profesor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('telefono', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=0)),
            ('correo', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal('principal', ['Profesor'])

        # Adding model 'Curso'
        db.create_table('principal_curso', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('num_creditos', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('principal', ['Curso'])

        # Adding model 'Matricula'
        db.create_table('principal_matricula', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('alumno', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Alumno'])),
            ('curso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Curso'])),
        ))
        db.send_create_signal('principal', ['Matricula'])

        # Adding model 'Dictar'
        db.create_table('principal_dictar', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha_ini', self.gf('django.db.models.fields.DateField')()),
            ('fecha_ter', self.gf('django.db.models.fields.DateField')()),
            ('profesor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Profesor'])),
            ('curso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Curso'])),
        ))
        db.send_create_signal('principal', ['Dictar'])

        # Adding model 'Nota'
        db.create_table('principal_nota', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('valor', self.gf('django.db.models.fields.IntegerField')()),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('trimestre', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('matricula', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Matricula'])),
        ))
        db.send_create_signal('principal', ['Nota'])


    def backwards(self, orm):
        # Deleting model 'Alumno'
        db.delete_table('principal_alumno')

        # Deleting model 'Profesor'
        db.delete_table('principal_profesor')

        # Deleting model 'Curso'
        db.delete_table('principal_curso')

        # Deleting model 'Matricula'
        db.delete_table('principal_matricula')

        # Deleting model 'Dictar'
        db.delete_table('principal_dictar')

        # Deleting model 'Nota'
        db.delete_table('principal_nota')


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
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'principal.nota': {
            'Meta': {'object_name': 'Nota'},
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'matricula': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.Matricula']"}),
            'trimestre': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
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