# -*- coding: utf-8 -*-
{
    'name': "fpinformatica",
    'summary': "Gestión de prácticas FCT (Alumnos y Empresas)",
    'description': "Módulo para gestionar la asignación de alumnos de FP a empresas.",
    'author': "Grupo DAM2",
    'website': "https://www.tusitio.com",
    'category': 'Education',
    'version': '0.1',

    # Módulos necesarios para que este funcione
    'depends': ['base'],

    # Lista de archivos a cargar (EL ORDEN IMPORTA)
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/alumno_views.xml',   # <--- 1º Define las vistas de Alumnos (y su search view)
        'views/empresa_views.xml',  # <--- 2º Define las vistas de Empresa
        'views/menus.xml',          # <--- 3º AHORA sí puedes cargar los menús y acciones que usan lo anterior
        'reports/report_fct.xml',
    ],
    
    'application': True,
    'installable': True,
}