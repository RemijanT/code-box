from zope.sqlalchemy import ZopeTransactionExtension
from sqlalchemy import Table, Column, Integer, String, \
	MetaData, ForeignKey, DateTime, Float, Boolean, orm,Text
from sqlalchemy.dialects.mysql import BIT, DOUBLE,DATETIME
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
	aij = Column('aij', DOUBLE)                 
	asr = Column('asr', BIT)                     
	created = Column('created', DateTime)                 
	degree_freedom = Column('degree_freedom', Integer)          
	error = Column('error', DOUBLE)                   
	frequency = Column('frequency', DOUBLE)               
	html_name = Column('html_name', String)               
	intensity = Column('intintensity', String)            
	labref = Column('labref_Lovas_NIST', String)       
	extras = Column('lextras', String)                               
	wavelength = Column('line_wavelength', DOUBLE)         
	ll_id = Column('ll_id', Integer)                   
	lovas = Column('Lovas_NRAO', Integer)              
	lower_state_energy = Column('lower_state_energy', DOUBLE)      
	lower_state_energy_k = Column('lower_state_energy_K', DOUBLE)    
	lunc = Column('lunc', DOUBLE)                    
	measerrfreq = Column('measerrfreq', DOUBLE)             
	measfreq = Column('measfreq', DOUBLE)            
	molecule_name = Column('molecule_name', String)           
	molecule_tag = Column('molecule_tag', Integer)            
	obsintensity = Column('obsintensity_Lovas_NIST', String) 
	obsref = Column('obsref_Lovas_NIST', String)       
	ordered_freq = Column('orderedfreq', DOUBLE)             
	qn_code = Column('qn_code', Integer)                 
	quantum_numbers = Column('quantum_numbers', String)         
	rel_int_hfs_lovas = Column('rel_int_HFS_Lovas', String)       
	resolved_qns = Column('resolved_QNs', String)            
	rounded_freq = Column('roundedfreq', DOUBLE)             
	sij = Column('sij', DOUBLE)                     
	sijmu2 = Column('sijmu2', DOUBLE)                  
	source_lovas_nist = Column('source_Lovas_NIST', String)       
	species_id = Column('species_id', Integer, ForeignKey('species.species_id'))              
	telescope_lovas_nist = Column('telescope_Lovas_NIST', String)    
	tr_id = Column('tr_id', Integer)                   
	transition_in_space = Column('transition_in_space', Integer)     
	uncertainty = Column('uncertainty', DOUBLE)             
	upper_state_degeneracy = Column('upper_state_degeneracy', DOUBLE)   
	upper_state_energy = Column('upper_state_energy', DOUBLE)   
	upper_state_energy_k = Column('upper_state_energy_K', DOUBLE) 
	v1 = Column('v1.0', BIT)                 
	v2 = Column('v2.0', BIT)

class Receivers(Base):
	__tablename__='receivers'
	__table_args__=  {'extend_existing':True}
	rcv_id = Column("rcv_id", Integer,primary_key=True)
	telescope = Column("telescope", String)
	receiver = Column("receiver", String)
	min_freq = Column("min_freq", DOUBLE)
	max_freq = Column("max_freq", DOUBLE)
	created = Column("created", DATETIME)
	colour = Column("colour", String)
	colour_alt = Column("colour_alt", String)
	t_id = Column("t_id", Integer)

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
	
class SpeciesMetadata(Base):
	__tablename__='species_metadata'
	__table_args__=  {'extend_existing':True}
	species_id = Column('species_id', String, primary_key=True)
	species_id_noparens = Column('species_id_noparens', String)
	name = Column('Name', String)
	date = Column('Date', String)
	contributor = Column('Contributor', String)
	q_2000_ = Column('Q_2000_', String)
	q_1000_ = Column('Q_1000_', String)
	q_500_0 = Column('Q_500_0', String)
	q_300_0 = Column('Q_300_0', String)
	q_225_0 = Column('Q_225_0', String)
	q_150_0 = Column('Q_150_0', String)
	q_75_00 = Column('Q_75_00', String)
	q_37_50 = Column('Q_37_50', String)
	q_18_75 = Column('Q_18_75', String)
	q_9_375 = Column('Q_9_375', String)
	q_c = Column('Q_c', Integer)
	q_e = Column('Q_e', Integer)
	mu_a = Column('MU_A', String)
	mu_b = Column('MU_B', String)
	mu_c = Column('MU_C', String)
	a = Column('A', String)
	b = Column('B', String)
	c = Column('C', String)
	ref1 = Column('Ref1', String)
	ref2 = Column('Ref2', String)
	ref3 = Column('Ref3', String)
	ref4 = Column('Ref4', String)
	ref5 = Column('Ref5', String)
	ref6 = Column('Ref6', String)
	ref7 = Column('Ref7', String)
	ref8 = Column('Ref8', String)
	ref9 = Column('Ref9', String)
	ref10 = Column('Ref10', String)
	ref11 = Column('Ref11', String)
	ref12 = Column('Ref12', String)
	ref13 = Column('Ref13', String)
	ref14 = Column('Ref14', String)
	ref15 = Column('Ref15', String)
	ref16 = Column('Ref16', String)
	ref17 = Column('Ref17', String)
	ref18 = Column('Ref18', String)
	ref19 = Column('Ref19', String)
	ref20 = Column('Ref20', String)
	pdr_lau = Column('pdr_lau', String)
	pdr_ism = Column('pdr_ism', String)
	planet = Column('planet', Integer)
	ism_hotcore = Column('ism_hotcore', Integer)
	ism_diffuse = Column('ism_diffuse', Integer)
	ism_darkcloud = Column('ism_darkcloud', Integer)
	comet = Column('comet', Integer)
	extragalactic = Column('extragalactic', Integer)
	agb_ppn_pn = Column('AGB_PPN_PN', Integer)
	linelist = Column('LineList', String)
	v1_0 = Column('v1_0', BIT)
	v2_0 = Column('v2_0', BIT)
	ism = Column('ism', String)
	
class Linelists(Base):
	__tablename__='linelists'
	__table_args__=  {'extend_existing':True}	
	ll_id = Column("ll_id", Integer, primary_key=True)
	linelist = Column("linelist", String)
	reference = Column("reference", String)
	url = Column("url", String)
	notes = Column("notes", String)
	
class LovasReferences(Base):
	__tablename__='Lovas_References'
	__table_args__=  {'extend_existing':True}
	ref_index = Column("ref_index", Integer, primary_key=True)
	ll_id = Column("ll_id", String)
	lovas_shortref = Column("Lovas_shortref", String)
	lovas_fullref = Column("Lovas_fullref", String)

class SpeciesDb(Base):
	__tablename__='species_db'
	__table_args__=  {'extend_existing':True}
	sd_id = Column("sd_id", Integer, primary_key=True)
	ll_id = Column("ll_id", Integer)
	species_id = Column("species_id", Integer)
	database_key = Column("database_key", String)
	db_key = Column("db_key", Integer)
	created = Column("created", DATETIME)

class Transition(Base):
	__tablename__='transition'
	__table_args__=  {'extend_existing':True}
	tr_id = Column("tr_id", Integer, primary_key=True)
	species_id = Column("species_id", Integer)
	description = Column("description", String)
	created = Column("created", DATETIME)

class Telescopes(Base):
	__tablename__='telescopes'
	__table_args__=  {'extend_existing':True}
	t_id = Column("t_id", Integer, primary_key=True)
	telescope = Column("telescope", String)
	created = Column("created", DATETIME)
	
#class SlapViewTable(Base):
#	__tablename__='slapviewtable'
#	__table_args__=  {'extend_existing':True}
#	catname = Column("catname", String)
#	molformula = Column("molformula", String)
#	moltype = Column("moltype", Integer)
#	chemicalname = Column("chemicalname", String)
#	sname = Column("sname", String)
#	obsintensity = Column("obsintensity", String)
#	sijmu2 = Column("sijmu2", DOUBLE)
#	aij = Column("aij", DOUBLE)
#	lowerstateenergy = Column("lowerstateenergy", DOUBLE)
#	upperstateenergy = Column("upperstateenergy", DOUBLE)
#	lowerstateenergyk = Column("lowerstateenergyK", DOUBLE)
#	upperstateenergyk = Column("upperstateenergyK", DOUBLE)
#	frequency = Column("frequency", DOUBLE)
#	qns = Column("QNs", String)
#	recommended = Column("recommended", Integer)
#	known_interstellar = Column("known_interstellar", Integer)
	
class Stats(Base):
	__tablename__='stats'
	__table_args__=  {'extend_existing':True}
	id = Column("id", Integer, primary_key=True)
	browser = Column("browser", String)
	ip = Column("ip", String)
	received = Column("received", DATETIME)
	refer = Column("refer", String)
	query_string = Column("query_string", String)
	
class SQLQueries(Base):
	__tablename__='sql_queries'
	__table_args__=  {'extend_existing':True}
	sql_id = Column("sql_id", Integer, primary_key=True)
	client = Column("client", String)
	received = Column("received", DATETIME)
	sql_query = Column("sql_query", String)
	browser = Column("browser", String)
	ip = Column("ip", String)
	query_string = Column("query_string", String)
	results = Column("results", Integer)
	status = Column("status", Integer)
	
class Spx(Base):
	__tablename__='spx'
	__table_args__=  {'extend_existing':True}
	species_id = Column("species_id", Integer,primary_key=True)
	name = Column("name", String)
	nlines = Column("nlines", Integer)
	version = Column("version", String)
	created = Column("created", DATETIME)
	s_name = Column("s_name", String)