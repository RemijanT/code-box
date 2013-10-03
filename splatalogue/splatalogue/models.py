from zope.sqlalchemy import ZopeTransactionExtension
from sqlalchemy import Table, Column, Integer, String, \
	MetaData, ForeignKey, DateTime, Float, Boolean, orm,Text
from sqlalchemy.dialects.mysql import BIT, DOUBLE
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    relation, 
    relationship, 
    backref
    )


DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()
metadata = Base.metadata
Session = orm.sessionmaker()


class Splatalogue(Base):
	__tablename__='main'
	__table_args__ = {'extend_existing':True}
 
 	id = Column('line_id', Integer, primary_key=True)
	aij = Column('aij', Double)                 
	asr = Column('asr', BIT)                     
	created = Column('created', DateTime)                 
	degree_freedom = Column('degree_freedom', Integer)          
	error = Column('error', Double)                   
	frequency = Column('frequency', Double)               
	html_name = Column('html_name', String)               
	intensity = Column('intintensity', String)            
	labref = Column('labref_Lovas_NIST', String)       
	extras = Column('lextras', String)                               
	wavelength = Column('line_wavelength', Double)         
	ll_id = Column('ll_id', Integer)                   
	lovas = Column('Lovas_NRAO', Integer)              
	lower_state_energy = Column('lower_state_energy', Double)      
	lower_state_energy_k = Column('lower_state_energy_K', Double)    
	lunc = Column('lunc', Double)                    
	measerrfreq = Column('measerrfreq', Double)             
	measfreq = Column('measfreq', Double)            
	molecule_name = Column('molecule_name', String)           
	molecule_tag = Column('molecule_tag', Integer)            
	obsintensity = Column('obsintensity_Lovas_NIST', String) 
	obsref = Column('obsref_Lovas_NIST', String)       
	ordered_freq = Column('orderedfreq', Double)             
	qn_code = Column('qn_code', Integer)                 
	quantum_numbers = Column('quantum_numbers', String)         
	rel_int_hfs_lovas = Column('rel_int_HFS_Lovas', String)       
	resolved_qns = Column('resolved_QNs', String)            
	rounded_freq = Column('roundedfreq', Double)             
	sij = Column('sij', Double)                     
	sijmu2 = Column('sijmu2', Double)                  
	source_lovas_nist = Column('source_Lovas_NIST', String)       
	species_id = Column('species_id', Integer, ForeignKey('species.id'))              
	telescope_lovas_nist = Column('telescope_Lovas_NIST', String)    
	tr_id = Column('tr_id', Integer)                   
	transition_in_space = Column('transition_in_space', Integer)     
	uncertainty = Column('uncertainty', Double)             
	upper_state_degeneracy = Column('upper_state_degeneracy', Double)   
	upper_state_energy = Column('upper_state_energy', Double)   
	upper_state_energy_k = Column('upper_state_energy_K', Double) 
	v1 = Column('v1.0', BIT)                 
	v2 = Column('v2.0', BIT)

class Species(Base):
	__tablename__='species'
	__table_args__=  {'extend_existing':True}
	id = Column('species_id', Integer, primary_key=True)
	splatalogues = relationship('Splatalogue',backref='main')
	name = Column('name', String)
	chemical_name = Column('chemical_name', String)
	s_name = Column('s_name', String)
	s_name_noparens = Column('s_name_noparens', String)
	splat_id = Column('SPLAT_ID', String)
	n_lines = Column('nlines', Integer)
	version = Column('version', String)
	created = Column('created', DateTime)
	resolved = Column('resolved', BIT)
	atmos = Column('atmos', Integer)
	potential = Column('potential', Integer)
	probable = Column('probable', Integer)
	known_ast_molecules = Column('known_ast_molecules', Integer)
	planet = Column('planet', Integer)
	ism_hotcore = Column('ism_hotcore', Integer)
	ism_diffusecloud = Column('ism_diffusecloud', Integer)
	ism_darkcloud = Column('ism_darkcloud', Integer)
	comet = Column('comet', Integer)
	extragalactic = Column('extragalactic', Integer)
	agb_ppn_pn = Column('AGB_PPN_PN', Integer)
	slise_it = Column('SLiSE_IT', Integer)
	top20 = Column('Top20', Integer)


