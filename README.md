# Hospital-Patient-Management-System

A hospital wants to implement a Patient Management System to efficiently manage patient records, doctor appointments, treatment history, and hospital performance metrics. The system should allow for the storage of electronic health records (EHR), patient demographics, medical diagnoses, treatment history, and doctor information. Additionally, it should support the analysis of patient demographics, disease prevalence, treatment outcomes, and hospital performance metrics.

## Solution Overview

A relational database system will be designed and implemented to store patient and doctor information, medical records, and treatment details. SQL queries will be utilized to perform various analyses such as patient demographics, disease prevalence, treatment outcomes, and hospital performance metrics.

## Database schema:

1. Patients: Stores patient demographics
2. Doctors: Stores doctor information and specialization
3. Medical Records: Stores medical records, including admission dates, discharge dates, diagnoses, treatments, and associated doctor IDs

## Detailed Data Schema:

**Patient's Table**
```
patient_id (Primary Key)
patient_name
date_of_birth
gender
address
phone_number
```

**Doctors Table**

```
doctor_id (Primary Key)
doctor_name
specialization
department
```

**Medical Records Table**

```
record_id (Primary Key)
patient_id (Foreign Key referencing Patients)
admission_date
discharge_date
diagnosis
treatment
doctor_id
```
**Dataset link to download** [Link](https://drive.google.com/drive/folders/1ObzTi2AGI5gdHjzVug44Bqrkl8yKY4cn?usp=drive_link)



















