from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Table, Float, DateTime, TEXT, DECIMAL, VARCHAR
from sqlalchemy.dialects.mysql import LONGTEXT, BIT
from sqlalchemy.orm import sessionmaker
import pyodbc

import config as cfg

engine = create_engine("mssql+pyodbc://%s:%s@%s:%s/%s?driver=ODBC+Driver+17+for+SQL+Server" % (cfg.dbuser, cfg.dbpass, cfg.dbhost, cfg.dbport, cfg.dbname))
Base = declarative_base()


class CellData(Base):
    __tablename__ = "CellData"
    ID = Column(Integer, primary_key=True)
    LogDate = Column(DateTime)
    Charger_ip1 = Column(Integer)
    Charger_ip2 = Column(Integer)
    Charger_ip3 = Column(Integer)
    Charger_ip4 = Column(Integer)
    cell_id = Column(Integer)
    voltage = Column(DECIMAL(4, 3))
    amps = Column(DECIMAL(10, 3))
    capacity = Column(DECIMAL(10, 3))
    status = Column(VARCHAR(50))
    esr = Column(DECIMAL(10, 5))
    action_length = Column(DECIMAL(10, 1))
    discharge_cycles = Column(Integer)
    complete_cycles = Column(Integer)
    temperature = Column(DECIMAL(10, 3))
    ChargerCell_id = Column(Integer)


class CellDataHistoryData(Base):
    __tablename__ = "CellDataHistoryData"
    ID = Column(Integer, primary_key=True)
    LogDate = Column(DateTime)
    Charger_ip1 = Column(Integer)
    Charger_ip2 = Column(Integer)
    Charger_ip3 = Column(Integer)
    Charger_ip4 = Column(Integer)
    cell_id = Column(Integer)
    voltage = Column(DECIMAL(4, 3))
    amps = Column(DECIMAL(10, 3))
    capacity = Column(DECIMAL(10, 3))
    status = Column(VARCHAR(50))
    esr = Column(DECIMAL(10, 5))
    action_length = Column(DECIMAL(10, 1))
    discharge_cycles = Column(Integer)
    complete_cycles = Column(Integer)
    temperature = Column(DECIMAL(10, 3))
    ChargerCell_id = Column(Integer)
    CellSerialNumber = Column(Integer)
    test_cycle = Column(Integer)


class CellLibrary(Base):
    __tablename__ = "CellLibrary"
    ID = Column(Integer, primary_key=True)
    LogDate = Column(DateTime)
    voltage = Column(DECIMAL(4, 3))
    amps = Column(DECIMAL(10, 3))
    capacity = Column(DECIMAL(10, 3))
    esr = Column(DECIMAL(10, 5))
    action_length = Column(DECIMAL(10, 1))
    discharge_cycles = Column(Integer)
    temperature = Column(DECIMAL(10, 3))
    CellSerialNumber = Column(Integer)
    Available = Column(BIT)
    Reservation = Column(BIT)
    BadCell = Column(BIT)
    Process_id = Column(Integer)
    min_voltage = Column(DECIMAL(4, 3))
    max_voltage = Column(DECIMAL(4, 3))
    ProjectName = Column(VARCHAR(50))
    store_voltage = Column(DECIMAL(4, 3))
    rest_voltage = Column(DECIMAL(10, 3))
    rest_volt_logDate = Column(DateTime)
    test_cycle = Column(Integer)


class CellTypes(Base):
    __tablename__ = "CellTypes"
    ID = Column(Integer, primary_key=True)
    Model = Column(VARCHAR(50))
    spec_no = Column(VARCHAR(50))
    nominal_capacity = Column(Integer)
    typical_capacity = Column(Integer)
    minimum_capacity = Column(Integer)
    charging_voltage = Column(DECIMAL(3, 2))
    nominal_voltage  = Column(DECIMAL(3, 2))
    charging_current = Column(Integer)
    max_charging_current = Column(Integer)
    max_discharge_current = Column(Integer)
    internal_impedance = Column(Integer)


class EAH(Base):
    __tablename__ = "EAH"
    ID = Column(Integer, primary_key=True)
    LogDate = Column(DateTime)
    Charger_ip1 = Column(Integer)
    Charger_ip2 = Column(Integer)
    Charger_ip3 = Column(Integer)
    Charger_ip4 = Column(Integer)
    cell_id = Column(Integer)
    status = Column(VARCHAR(50))
    voltage = Column(DECIMAL(4, 3))
    amps = Column(DECIMAL(10, 3))
    capacity = Column(DECIMAL(10, 3))
    esr = Column(DECIMAL(10, 5))
    action_length = Column(DECIMAL(10, 1))
    discharge_cycles = Column(Integer)
    complete_cycles = Column(Integer)
    temperature = Column(DECIMAL(10, 3))
    ChargerCell_id = Column(Integer)


class RealtimeCellData(Base):
    __tablename__ = "RealtimeCellData"
    ID = Column(Integer, primary_key=True)
    LogDate = Column(DateTime)
    Charger_ip1 = Column(Integer)
    Charger_ip2 = Column(Integer)
    Charger_ip3 = Column(Integer)
    Charger_ip4 = Column(Integer)
    cell_id = Column(Integer)
    voltage = Column(DECIMAL(4, 3))
    amps = Column(DECIMAL(10, 3))
    capacity = Column(DECIMAL(10, 3))
    status = Column(VARCHAR(50))
    esr = Column(DECIMAL(10, 5))
    action_length = Column(DECIMAL(10, 1))
    discharge_cycles = Column(Integer)
    complete_cycles = Column(Integer)
    temperature = Column(DECIMAL(10, 3))
    ChargerCell_id = Column(Integer)


Base.metadata.create_all(engine)