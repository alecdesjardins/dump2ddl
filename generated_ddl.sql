CREATE SCHEMA IF NOT EXISTS carrier_integration;

CREATE TABLE IF NOT EXISTS carrier_integration.mcp_carrier (
    id SERIAL NOT NULL,
   dot_number INTEGER,
   legal_name TEXT,
   dba_name TEXT,
   address1 TEXT,
   address2 TEXT,
   city TEXT,
   zip_code TEXT,
   state TEXT,
   country TEXT,
   cell_phone TEXT,
   phone TEXT,
   fax TEXT,
   free_phone TEXT,
   emergency_phone TEXT,
   email TEXT,
   fraud_identity_theft_status TEXT,
   mc_number TEXT,
   scac TEXT,
   mailing_address1 TEXT,
   mailing_address2 TEXT,
   mailing_city TEXT,
   mailing_state TEXT,
   mailing_zipcode TEXT,
   mailing_country TEXT,
   after_hrs_wkday_support_name TEXT,
   after_hrs_wkday_support_phone TEXT,
   after_hrs_wkday_support_fax TEXT,
   after_hrs_wkday_support_from TIME,
   after_hrs_wkday_support_to TIME,
   after_hrs_wkend_support_name TEXT,
   after_hrs_wkend_support_phone TEXT,
   after_hrs_wkend_support_fax TEXT,
   after_hrs_wkend_support_from TIME,
   after_hrs_wkend_support_to TIME,
   website TEXT,
   operation_manager_name TEXT,
   online_access_to_available_loads BOOLEAN,
   available_loads_email TEXT,
   driver_logs_safety_dept_manager_name TEXT,
   driver_logs_safety_dept_manager_phone TEXT,
   dispatchers TEXT,
   claims_contact_name TEXT,
   claims_contact_phone TEXT,
   claims_contact_email TEXT,
   dispatch_service_used BOOLEAN,
   dispatch_service_name TEXT,
   dispatch_service_phone TEXT,
   broker_out_extra_freight BOOLEAN,
   created_datetime TIMESTAMP,
   modified_datetime TIMESTAMP,
   owner_contact_name TEXT,
   owner_contact_phone TEXT,
   owner_contact_email TEXT
);
